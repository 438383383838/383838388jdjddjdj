lllllllllllllll, llllllllllllllI, lllllllllllllIl, lllllllllllllII, llllllllllllIll, llllllllllllIlI, llllllllllllIIl = input, __name__, Exception, open, KeyboardInterrupt, print, hasattr

from os.path import exists as IIIllIIIIIIIII
from json import dump as IIIllIlllIIIIl, load as IlIlIlIllIlIII
from telethon import TelegramClient as lIIIIIlllIllIl, events as IIllIlIIlIlIIl
from datetime import datetime as IllllllIIllIII
lIllIIlIIllllIIlIl = 'config.json'
llIlIlIIlllllIllIl = 'deleted.txt'
lIIlIIllIlIIlllIlI = '\n███████╗██╗     ██╗   ██╗██╗  ██╗██╗  ██╗\n██╔════╝██║     ██║   ██║╚██╗██╔╝╚██╗██╔╝\n█████╗  ██║     ██║   ██║ ╚███╔╝  ╚███╔╝ \n██╔══╝  ██║     ██║   ██║ ██╔██╗  ██╔██╗ \n██║     ███████╗╚██████╔╝██╔╝ ██╗██╔╝ ██╗\n╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝\nWelcome to DEV FLUXX ANTI-REVOKE SCRIPT\n'
IIllllIlIIIIlIIIIl = {}

def lllIIlIIllIIIIIIII():
    if not IIIllIIIIIIIII(llIlIlIIlllllIllIl):
        with lllllllllllllII(llIlIlIIlllllIllIl, 'w') as lIIIlIlIllIIllIIlI:
            lIIIlIlIllIIllIIlI.write('Deleted Messages Log\n')
            lIIIlIlIllIIllIIlI.write('=' * 50 + '\n')

def llllIllIIlIIIIllll(lIIlIIIlIIIIlIlllI, lIIllllIIlIIIlllll, IllIlIllIlIllIIIlI):
    lllIlIlIIllIIIlIIl = {'api_id': lIIlIIIlIIIIlIlllI, 'api_hash': lIIllllIIlIIIlllll, 'group': IllIlIllIlIllIIIlI}
    with lllllllllllllII(lIllIIlIIllllIIlIl, 'w') as lIIIlIlIllIIllIIlI:
        IIIllIlllIIIIl(lllIlIlIIllIIIlIIl, lIIIlIlIllIIllIIlI)

def llllIIIlllIIIlIllI():
    if IIIllIIIIIIIII(lIllIIlIIllllIIlIl):
        with lllllllllllllII(lIllIIlIIllllIIlIl, 'r') as lIIIlIlIllIIllIIlI:
            return IlIlIlIllIlIII(lIIIlIlIllIIllIIlI)
    return None

async def lIlIIlIIlllIlllIIl(IllIIIllIIIIlIlIII, lllllllIlIIIlIIIlI, IlIlIlIIIIIIIlllll, IIlIllIlIIIIIllIlI, llIIIllIlIllIlIlIl, lIIIlllIllIIlIllIl, IIlIIllIllIllIlllI=None):
    lIlllIllIIIlIIlIIl = f'[{IlIlIlIIIIIIIlllll}](tg://user?id={lllllllIlIIIlIIIlI})'
    with lllllllllllllII(llIlIlIIlllllIllIl, 'a', encoding='utf-8') as lIIIlIlIllIIllIIlI:
        lIIIlIlIllIIllIIlI.write(f'*New Deleted Message*\n\nSender: {lIlllIllIIIlIIlIIl}\nGroup: {IIlIllIlIIIIIllIlI}\nTime: {llIIIllIlIllIlIlIl}\n\n')
        if IIlIIllIllIllIlllI:
            lIIIlIlIllIIllIIlI.write('Message Content: Media/Non-text content\n\n')
        else:
            lIIIlIlIllIIllIIlI.write(f'Message Content: {lIIIlllIllIIlIllIl}\n\n')
        lIIIlIlIllIIllIIlI.write('-' * 50 + '\n')
    lllIlIlIIllIIIlIIl = llllIIIlllIIIlIllI()
    IIIIIlllIIIIlllIlI = lllIlIlIIllIIIlIIl.get('group')
    if IIIIIlllIIIIlllIlI:
        if IIlIIllIllIllIlllI:
            IIllIIIIlIlllIlIlI = f'🚫 **DELETED MESSAGE DETECTED**\n\n━━━━━━━━━━━━━━━━━━━━━\n👤 **From:** {lIlllIllIIIlIIlIIl}\n👥 **Group:** {IIlIllIlIIIIIllIlI}\n🕒 **Time:** {llIIIllIlIllIlIlIl}\n━━━━━━━━━━━━━━━━━━━━━\n📎 **Media Content Attached**'
            try:
                await IllIIIllIIIIlIlIII.send_file(IIIIIlllIIIIlllIlI, IIlIIllIllIllIlllI, caption=IIllIIIIlIlllIlIlI, parse_mode='markdown')
                llllllllllllIlI(f'✅ Deleted media message sent to group: {IIIIIlllIIIIlllIlI}')
            except lllllllllllllIl as lIIIllIlllIIllIIIl:
                llllllllllllIlI(f'❌ Failed to send media to group: {lIIIllIlllIIllIIIl}')
        else:
            lIlIIllIIIIIlllIII = f"🚫 **DELETED MESSAGE DETECTED**\n\n━━━━━━━━━━━━━━━━━━━━━\n👤 **From:** {lIlllIllIIIlIIlIIl}\n👥 **Group:** {IIlIllIlIIIIIllIlI}\n🕒 **Time:** {llIIIllIlIllIlIlIl}\n━━━━━━━━━━━━━━━━━━━━━\n📝 **Message Content:**\n\n{(lIIIlllIllIIlIllIl if lIIIlllIllIIlIllIl else 'No text content')}\n\n━━━━━━━━━━━━━━━━━━━━━"
            try:
                await IllIIIllIIIIlIlIII.send_message(IIIIIlllIIIIlllIlI, lIlIIllIIIIIlllIII, parse_mode='markdown')
                llllllllllllIlI(f'✅ Deleted message sent to group: {IIIIIlllIIIIlllIlI}')
            except lllllllllllllIl as lIIIllIlllIIllIIIl:
                llllllllllllIlI(f'❌ Failed to send message to group: {lIIIllIlllIIllIIIl}')

async def IlllllllIlllIllIlI(IllIIIllIIIIlIlIII):
    llllllllllllIlI('Monitoring started. Press Ctrl+C to stop.')

    @IllIIIllIIIIlIlIII.on(IIllIlIIlIlIIl.NewMessage)
    async def IIIIllIllIlIIllIll(IllIlIIIlIllIllIlI):
        IllIIlIIIIllIIIIIl = {'sender_id': IllIlIIIlIllIllIlI.lllllllIlIIIlIIIlI, 'sender': await IllIlIIIlIllIllIlI.get_sender(), 'text': IllIlIIIlIllIllIlI.lIlIIllIIIIIlllIII.lIlIIllIIIIIlllIII, 'date': IllIlIIIlIllIllIlI.lIlIIllIIIIIlllIII.date, 'media': IllIlIIIlIllIllIlI.lIlIIllIIIIIlllIII.IIlIIllIllIllIlllI}
        if IllIlIIIlIllIllIlI.chat_id:
            if IllIlIIIlIllIllIlI.chat_id not in IIllllIlIIIIlIIIIl:
                IIllllIlIIIIlIIIIl[IllIlIIIlIllIllIlI.chat_id] = {}
            IIllllIlIIIIlIIIIl[IllIlIIIlIllIllIlI.chat_id][IllIlIIIlIllIllIlI.id] = IllIIlIIIIllIIIIIl
            llllllllllllIlI(f'Cached group message: {IllIlIIIlIllIllIlI.chat_id}, {IllIlIIIlIllIllIlI.id}')
        else:
            lllllllIlIIIlIIIlI = IllIlIIIlIllIllIlI.lllllllIlIIIlIIIlI
            if lllllllIlIIIlIIIlI not in IIllllIlIIIIlIIIIl:
                IIllllIlIIIIlIIIIl[lllllllIlIIIlIIIlI] = {}
            IIllllIlIIIIlIIIIl[lllllllIlIIIlIIIlI][IllIlIIIlIllIllIlI.id] = IllIIlIIIIllIIIIIl
            llllllllllllIlI(f'Cached private message: {lllllllIlIIIlIIIlI}, {IllIlIIIlIllIllIlI.id}')

    @IllIIIllIIIIlIlIII.on(IIllIlIIlIlIIl.MessageDeleted)
    async def IlIIIIIlIlllIIlIII(IllIlIIIlIllIllIlI):
        llllllllllllIlI(f'Deleted event detected: Chat {IllIlIIIlIllIllIlI.chat_id}, Message IDs {IllIlIIIlIllIllIlI.deleted_ids}')
        for lllIIIlIlIIlllllll in IllIlIIIlIllIllIlI.deleted_ids:
            if IllIlIIIlIllIllIlI.chat_id:
                for lllIIIlIlIIlllllll in IllIlIIIlIllIllIlI.deleted_ids:
                    try:
                        if IllIlIIIlIllIllIlI.chat_id in IIllllIlIIIIlIIIIl and lllIIIlIlIIlllllll in IIllllIlIIIIlIIIIl[IllIlIIIlIllIllIlI.chat_id]:
                            IllIIlIIIIllIIIIIl = IIllllIlIIIIlIIIIl[IllIlIIIlIllIllIlI.chat_id].pop(lllIIIlIlIIlllllll, None)
                            if IllIIlIIIIllIIIIIl:
                                lllllllIlIIIlIIIlI = IllIIlIIIIllIIIIIl['sender_id']
                                IlIlIlIIIIIIIlllll = IllIIlIIIIllIIIIIl['sender'].first_name if IllIIlIIIIllIIIIIl['sender'] else 'Unknown'
                                llIIIllIlIllIlIlIl = IllIIlIIIIllIIIIIl['date'].strftime('%Y-%m-%d %H:%M:%S')
                                lIIIlllIllIIlIllIl = IllIIlIIIIllIIIIIl['text'] or 'Media/Non-text content'
                                IIlIIllIllIllIlllI = IllIIlIIIIllIIIIIl['media']
                                IIlIllIlIIIIIllIlI = ''
                                try:
                                    lIIlllIIllllIIIIlI = await IllIIIllIIIIlIlIII.get_entity(IllIlIIIlIllIllIlI.chat_id)
                                    IIlIllIlIIIIIllIlI = lIIlllIIllllIIIIlI.title if llllllllllllIIl(lIIlllIIllllIIIIlI, 'title') else 'Unknown Group'
                                except lllllllllllllIl as lIIIllIlllIIllIIIl:
                                    IIlIllIlIIIIIllIlI = 'Unknown Group'
                                    llllllllllllIlI(f'Failed to fetch group name: {lIIIllIlllIIllIIIl}')
                                await lIlIIlIIlllIlllIIl(IllIIIllIIIIlIlIII, lllllllIlIIIlIIIlI, IlIlIlIIIIIIIlllll, IIlIllIlIIIIIllIlI, llIIIllIlIllIlIlIl, lIIIlllIllIIlIllIl, IIlIIllIllIllIlllI)
                                llllllllllllIlI(f'Deleted group message logged from {IlIlIlIIIIIIIlllll} in group {IIlIllIlIIIIIllIlI}: {lIIIlllIllIIlIllIl}')
                    except lllllllllllllIl as lIIIllIlllIIllIIIl:
                        llllllllllllIlI(f'Failed to process group message: {lIIIllIlllIIllIIIl}')
            else:
                for lllIIIlIlIIlllllll in IllIlIIIlIllIllIlI.deleted_ids:
                    try:
                        for lllllllIlIIIlIIIlI in IIllllIlIIIIlIIIIl:
                            if lllIIIlIlIIlllllll in IIllllIlIIIIlIIIIl[lllllllIlIIIlIIIlI]:
                                IllIIlIIIIllIIIIIl = IIllllIlIIIIlIIIIl[lllllllIlIIIlIIIlI].pop(lllIIIlIlIIlllllll, None)
                                if IllIIlIIIIllIIIIIl:
                                    IlIlIlIIIIIIIlllll = IllIIlIIIIllIIIIIl['sender'].first_name if IllIIlIIIIllIIIIIl['sender'] else 'Unknown'
                                    lIIIlllIllIIlIllIl = IllIIlIIIIllIIIIIl['text'] or 'Media/Non-text content'
                                    llIIIllIlIllIlIlIl = IllIIlIIIIllIIIIIl['date'].strftime('%Y-%m-%d %H:%M:%S')
                                    IIlIIllIllIllIlllI = IllIIlIIIIllIIIIIl['media']
                                    await lIlIIlIIlllIlllIIl(IllIIIllIIIIlIlIII, lllllllIlIIIlIIIlI, IlIlIlIIIIIIIlllll, 'Private Chat', llIIIllIlIllIlIlIl, lIIIlllIllIIlIllIl, IIlIIllIllIllIlllI)
                                    llllllllllllIlI(f'Deleted DM message logged from {IlIlIlIIIIIIIlllll}: {lIIIlllIllIIlIllIl}')
                        else:
                            llllllllllllIlI(f'Message ID {lllIIIlIlIIlllllll} not found in cache for DM.')
                    except lllllllllllllIl as lIIIllIlllIIllIIIl:
                        llllllllllllIlI(f'Failed to process DM message: {lIIIllIlllIIllIIIl}')
    await IllIIIllIIIIlIlIII.run_until_disconnected()

def lIIIlllIlIlllllIlI():
    llllllllllllIlI(lIIlIIllIlIIlllIlI)
    lllIIlIIllIIIIIIII()
    lllIlIlIIllIIIlIIl = llllIIIlllIIIlIllI()
    if not lllIlIlIIllIIIlIIl:
        lIIlIIIlIIIIlIlllI = lllllllllllllll('Enter your Telegram API ID: ')
        lIIllllIIlIIIlllll = lllllllllllllll('Enter your Telegram API Hash: ')
        IllIlIllIlIllIIIlI = lllllllllllllll('Enter your Telegram group link: ')
        llllIllIIlIIIIllll(lIIlIIIlIIIIlIlllI, lIIllllIIlIIIlllll, IllIlIllIlIllIIIlI)
    else:
        lIIlIIIlIIIIlIlllI = lllIlIlIIllIIIlIIl.get('api_id')
        lIIllllIIlIIIlllll = lllIlIlIIllIIIlIIl.get('api_hash')
        IllIlIllIlIllIIIlI = lllIlIlIIllIIIlIIl.get('group')
    if not lIIlIIIlIIIIlIlllI or not lIIllllIIlIIIlllll or (not IllIlIllIlIllIIIlI):
        llllllllllllIlI('API ID, Hash, and Group Link are required. Exiting.')
        return
    IllIIIllIIIIlIlIII = lIIIIIlllIllIl('session', lIIlIIIlIIIIlIlllI, lIIllllIIlIIIlllll)
    try:
        IllIIIllIIIIlIlIII.start()
        IllIIIllIIIIlIlIII.loop.run_until_complete(IlllllllIlllIllIlI(IllIIIllIIIIlIlIII))
    except llllllllllllIll:
        llllllllllllIlI('\nMonitoring stopped.')
    except lllllllllllllIl as lIIIllIlllIIllIIIl:
        llllllllllllIlI(f'Error: {lIIIllIlllIIllIIIl}')
    finally:
        IllIIIllIIIIlIlIII.disconnect()
if llllllllllllllI == '__main__':
    lIIIlllIlIlllllIlI()