
███████╗██╗     ██╗   ██╗██╗  ██╗██╗  ██╗
██╔════╝██║     ██║   ██║╚██╗██╔╝╚██╗██╔╝
█████╗  ██║     ██║   ██║ ╚███╔╝  ╚███╔╝ 
██╔══╝  ██║     ██║   ██║ ██╔██╗  ██╔██╗ 
██║     ███████╗╚██████╔╝██╔╝ ██╗██╔╝ ██╗
╚═╝     ╚══════╝ ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝
**Welcome to the FLUXX Anti-Message Revocation Script**

# **Telegram Anti-Message Revocation Script**

This Python script monitors Telegram groups and private chats for deleted messages. When a message is deleted, the script logs the content of the deleted message and sends it to a predefined group for monitoring.

## **Features**
- Logs deleted messages.
- Sends deleted messages (including media) to a designated Telegram group.
- Caches incoming messages for tracking and detecting deletions.
- Supports retrying media downloads in case of failure.

## **Requirements**
- Python 3.7 or higher
- Telegram API credentials (API ID and API Hash)
- Required Python libraries

### **Libraries**
Install the necessary dependencies using `pip`:

```bash
pip install telethon
```

## **Setup**

### 1. **Create a Telegram App for API Access**

To use this script, you need to create a Telegram app to obtain an API ID and API Hash.

1. Visit [Telegram’s API Development Tools](https://my.telegram.org/auth).
2. Log in with your Telegram account.
3. Click on "API development tools" and fill out the required fields.
4. Once you have the API ID and Hash, you can use them in the script.

### 2. **Configure the Script**

Before running the script, you need to configure it with your Telegram API credentials and group link.

#### Configuration File (`config.json`)

The script will automatically save your API ID, API Hash, and the target group link to a `config.json` file after the first run. If the file does not exist, it will prompt you to input the details:

- **API ID**: The API ID you obtained from Telegram.
- **API Hash**: The API Hash you obtained from Telegram.
- **Group Link**: The link to the Telegram group where deleted messages will be sent (e.g., `https://t.me/your_group_name`).

#### Example of `config.json`:

```json
{
  "api_id": "your_api_id",
  "api_hash": "your_api_hash",
  "group": "https://t.me/your_group_name"
}
```

If you run the script and the `config.json` file is missing or incomplete, the script will prompt you to input these values.

### 3. **Running the Script**

To run the script, execute the following command in your terminal:

```bash
python revoke.py
```

The script will turn on start monitoring messages. When a message is deleted, it will log the message and send the details to the specified group.

### 4. **Permissions**

Ensure the bot or script has the necessary permissions in the group to send messages. If you're using the script to monitor a group chat, make sure that:

- The bot or user account is an admin in the group.
- The group allows the bot to post messages.

### 5. **Monitoring Process**

Once the script starts running, it will:

1. **Cache Messages**: The script caches incoming messages, so when a message is deleted, it can retrieve the content from the cache.
2. **Log Deleted Messages**: When a message is deleted, the script will log the message content, sender's name, and timestamp in a file called `deleted.txt`.
3. **Send Deleted Messages**: The script will send the deleted message (including media) to the designated group.

### 6. **Log File (`deleted.txt`)**

All deleted messages are logged in `deleted.txt`. Here's an example of how the log file will look:

```
Deleted Messages Log
==================================================
*New Deleted Message*

Sender: [John Doe](tg://user?id=123456789)
Group: Test Group
Time: 2024-11-27 12:34:56
Message Content: Some text content

--------------------------------------------------
```

### 7. **Stopping the Script**

To stop the script, press `Ctrl+C` in the terminal. The script will stop monitoring and gracefully disconnect from Telegram.

--------------------------------------------------------------------------------------------------------------------------------


---

## **Troubleshooting**

- **Script Doesn’t Start**: Make sure you’ve installed the required libraries and have valid API credentials.
- **No Deleted Messages**: Ensure the script has permission to access the group and that you're using an admin account or bot that can monitor message deletions.

---

## **License**

This script is open-source and free to use. Contributions are welcome!
If you find this script useful, please consider donating to support its development and maintenance.
## **BITCOIN DONATION**
```bash
bc1qswa3nxu40ckuvkqakg8g7v8hke6sx267mze9mk
```
## **USDT BEP20,ERC20 AND ETHEREUM DONATION**
```bash
0x79007BB1C0BC5082e4e959a6ba01322Af3555323
```
## ** TON DONATION**
```bash
UQC1IXbQa_DZ9sKGY2L9SrfPagBnfvGxw2pLhHHIjNm-nuVs
```
```bash
Ton tag: 100010570
```
Contact me on telegram for more scripts: https://t.me/echoFluxxx
