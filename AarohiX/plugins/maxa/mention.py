from pyrogram import Client, filters
import asyncio
from config import API_ID, API_HASH, ARI_STRING

api_id = 'API_ID'
api_hash = 'API_HASH'
session_string = 'ARI_STRING'


app = Client(ARI_STRING, api_id=API_ID, api_hash=API_HASH)

# List to store chat_ids where tagging is ongoing
SPAM_CHATS = []

# Define your command handler for tagging
@app.on_message(filters.command(["maro", "ari"]) | filters.command("@ari", "") & filters.group)
async def tag_all_users(client, message):
    replied = message.reply_to_message  
    if len(message.command) < 2 and not replied:
        await message.reply_text("**Reply to a message or give some text to tag everyone.**") 
        return                  
    if replied:
        chat_id = message.chat.id
        SPAM_CHATS.append(chat_id)      
        usernum = 0
        usertxt = ""
        async for member in app.iter_chat_members(chat_id): 
            if chat_id not in SPAM_CHATS:
                break       
            usernum += 1
            usertxt += f"@{member.user.username} "
            if usernum == 5:
                await replied.reply_text(usertxt)
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""
        SPAM_CHATS.remove(chat_id)
    else:
        text = message.text.split(None, 1)[1]
        chat_id = message.chat.id
        SPAM_CHATS.append(chat_id)
        usernum = 0
        usertxt = ""
        async for member in app.iter_chat_members(chat_id):       
            if chat_id not in SPAM_CHATS:
                break 
            usernum += 1
            usertxt += f"@{member.user.username} "
            if usernum == 5:
                await app.send_message(chat_id, f'{text}\n{usertxt}')
                await asyncio.sleep(2)
                usernum = 0
                usertxt = ""                          
        SPAM_CHATS.remove(chat_id)

# Define your command handler for stopping tagging
@app.on_message(filters.command("mentionoff") & ~filters.private)
async def cancelcmd(client, message):
    chat_id = message.chat.id
    if chat_id in SPAM_CHATS:
        SPAM_CHATS.remove(chat_id)
        await message.reply_text("**Tagging all successfully stopped!**")     
    else:
        await message.reply_text("**No process ongoing!**")  
