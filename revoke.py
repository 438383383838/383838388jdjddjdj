from telethon import TelegramClient, events
import os
import json
from datetime import datetime, time, timedelta

CONFIG_FILE = "config.json"
DELETED_LOG_FILE = "deleted.txt"

ASCII_ART = """
███████╗██╗     ██╗   ██╗██╗  ██╗██╗  ██╗
██╔════╝██║     ██║   ██║╚██╗██╔╝╚██╗██╔╝
█████╗  ██║     ██║   ██║ ╚███╔╝  ╚███╔╝ 
██╔══╝  ██║     ██║   ██║ ██╔██╗  ██╔██╗ 
██║     ███████╗╚██████╔╝██╔╝ ██╗██╔╝ ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
Welcome to DEV FLUXX ANTI-REVOKE SCRIPT
"""
message_cache = {}
CACHE_EXPIRY = 86400
last_cache_clean = datetime.now()

def clean_expired_cache():
    current_time = time.time()
    for chat_id, messages in list(message_cache.items()):
        for msg_id, message_data in list(messages.items()):
            if (current_time - message_data["date"].timestamp()) > CACHE_EXPIRY:
                del message_cache[chat_id][msg_id]
        if not message_cache[chat_id]:
            del message_cache[chat_id]

def check_and_clean_cache():
    global last_cache_clean
    current_time = datetime.now()
    if (current_time - last_cache_clean).total_seconds() >= 86400:
        clean_expired_cache()
        last_cache_clean = current_time

def ensure_deleted_file_exists():
    if not os.path.exists(DELETED_LOG_FILE):
        with open(DELETED_LOG_FILE, "w") as file:
            file.write("Deleted Messages Log\n")
            file.write("=" * 50 + "\n")


def save_config(api_id, api_hash, group):
    config = {
        "api_id": api_id,
        "api_hash": api_hash,
        "group": group
    }
    with open(CONFIG_FILE, "w") as file:
        json.dump(config, file)


def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as file:
            return json.load(file)
    return None


async def log_deleted_message(client, sender_id, sender_name, group_name, time, content, media=None):
    sender_link = f"[{sender_name}](tg://user?id={sender_id})"  
    
    with open(DELETED_LOG_FILE, "a", encoding="utf-8") as file:
        file.write(f"*New Deleted Message*\n\nSender: {sender_link}\nGroup: {group_name}\nTime: {time}\n\n")
        if media:
            file.write("Message Content: Media/Non-text content\n\n")
        else:
            file.write(f"Message Content: {content}\n\n")
        file.write("-" * 50 + "\n")

    config = load_config()
    group_link = config.get("group")
    if group_link:
        if media:
            caption = (
                "🚫 **DELETED MESSAGE DETECTED**\n\n"
                "━━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 **From:** {sender_link}\n"
                f"👥 **Group:** {group_name}\n"
                f"🕒 **Time:** {time}\n"
                "━━━━━━━━━━━━━━━━━━━━━\n"
                "📎 **Media Content Attached**"
            )
            try:
                await client.send_file(group_link, media, caption=caption, parse_mode="markdown")
                print(f"✅ Deleted media message sent to group: {group_link}")
            except Exception as e:
                print(f"❌ Failed to send media to group: {e}")
        else:
            message = (
                "🚫 **DELETED MESSAGE DETECTED**\n\n"
                "━━━━━━━━━━━━━━━━━━━━━\n"
                f"👤 **From:** {sender_link}\n"
                f"👥 **Group:** {group_name}\n"
                f"🕒 **Time:** {time}\n"
                "━━━━━━━━━━━━━━━━━━━━━\n"
                "📝 **Message Content:**\n"
                f"\n{content if content else 'No text content'}\n\n"
                "━━━━━━━━━━━━━━━━━━━━━"
            )
            try:
                await client.send_message(group_link, message, parse_mode="markdown")
                print(f"✅ Deleted message sent to group: {group_link}")
            except Exception as e:
                print(f"❌ Failed to send message to group: {e}")


async def start_monitoring(client):
    print("Monitoring started. Press Ctrl+C to stop.")

    @client.on(events.NewMessage)
    async def cache_message(event):
        check_and_clean_cache()
        message_data = {
            "sender_id": event.sender_id,  
            "sender": await event.get_sender(),
            "text": event.message.message,
            "date": event.message.date,
            "media": event.message.media,  
        }


        if event.chat_id:
            if event.chat_id not in message_cache:
                message_cache[event.chat_id] = {}
            message_cache[event.chat_id][event.id] = message_data
            print(f"Cached group message: {event.chat_id}, {event.id}")
        else:
            sender_id = event.sender_id
            if sender_id not in message_cache:
                message_cache[sender_id] = {}
            message_cache[sender_id][event.id] = message_data
            print(f"Cached private message: {sender_id}, {event.id}")


    @client.on(events.MessageDeleted)
    async def on_message_deleted(event):
        check_and_clean_cache()
        print(f"Deleted event detected: Chat {event.chat_id}, Message IDs {event.deleted_ids}")

        for msg_id in event.deleted_ids:
            if event.chat_id:
                for msg_id in event.deleted_ids:
                    try:
                        if event.chat_id in message_cache and msg_id in message_cache[event.chat_id]:
                            message_data = message_cache[event.chat_id].pop(msg_id, None)
                            if message_data:
                                sender_id = message_data["sender_id"]
                                sender_name = message_data["sender"].first_name if message_data["sender"] else "Unknown"
                                time = message_data["date"].strftime("%Y-%m-%d %H:%M:%S")
                                content = message_data["text"] or "Media/Non-text content"
                                media = message_data["media"]
                                group_name = ""
                                try:
                                    entity = await client.get_entity(event.chat_id)
                                    group_name = entity.title if hasattr(entity, 'title') else 'Unknown Group'
                                except Exception as e:
                                    group_name = "Unknown Group"
                                    print(f"Failed to fetch group name: {e}")

                                await log_deleted_message(client, sender_id, sender_name, group_name, time, content, media)

                                print(f"Deleted group message logged from {sender_name} in group {group_name}: {content}")
                    except Exception as e:
                        print(f"Failed to process group message: {e}")

            else:
                for msg_id in event.deleted_ids:
                    try:
                        
                        for sender_id in message_cache:
                            if msg_id in message_cache[sender_id]:
                                message_data = message_cache[sender_id].pop(msg_id, None)
                                if message_data:
                                    sender_name = message_data["sender"].first_name if message_data["sender"] else "Unknown"
                                    content = message_data["text"] or "Media/Non-text content"
                                    time = message_data["date"].strftime("%Y-%m-%d %H:%M:%S")
                                    media = message_data["media"]

                                    await log_deleted_message(client, sender_id, sender_name, "Private Chat", time, content, media)
                                    print(f"Deleted DM message logged from {sender_name}: {content}")
                        else:
                            print(f"Message ID {msg_id} not found in cache for DM.")
                    except Exception as e:
                        print(f"Failed to process DM message: {e}")

    await client.run_until_disconnected()


def main():
    print(ASCII_ART)

    ensure_deleted_file_exists()

    config = load_config()
    if not config:
        api_id = input("Enter your Telegram API ID: ")
        api_hash = input("Enter your Telegram API Hash: ")
        group = input("Enter your Telegram group link: ")
        save_config(api_id, api_hash, group)
    else:
        api_id = config.get("api_id")
        api_hash = config.get("api_hash")
        group = config.get("group")

    if not api_id or not api_hash or not group:
        print("API ID, Hash, and Group Link are required. Exiting.")
        return

    client = TelegramClient("session", api_id, api_hash)

    try:
        client.start()
        client.loop.run_until_complete(start_monitoring(client))
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")  
    except Exception as e:
        print(f"Error: {e}")
    finally:
        client.disconnect()


if __name__ == "__main__":
    main()