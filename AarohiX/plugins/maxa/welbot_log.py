from pyrogram import Client, filters
from pyrogram.types import Message
from AarohiX import app
from AarohiX.utils import get_served_chats
from config import LOGGER_ID


async def lul_message(chat_id: int, message: str):
    await app.send_message(chat_id=chat_id, text=message)


@app.on_message(filters.new_chat_members)
async def on_new_chat_members(client: Client, message: Message):
    if (await client.get_me()).id in [user.id for user in message.new_chat_members]:
        added_by = message.from_user.first_name if message.from_user else "ᴜɴᴋɴᴏᴡɴ ᴜsᴇʀ"
        matlabi_jhanto = message.chat.title
        served_chats = len(await get_served_chats())
        chat_id = message.chat.id
        if message.chat.username:
            chatusername = f"@{message.chat.username}"
        else:
            chatusername = "ᴩʀɪᴠᴀᴛᴇ ᴄʜᴀᴛ"
        lemda_text = f"❤️‍🔥 ʙᴏᴛ ᴀᴅᴅᴇᴅ ᴛᴏ ɴᴇᴡ ɢʀᴏᴜᴘ ..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ ❖ᴄʜᴀᴛ❖ › : {matlabi_jhanto}\n┣★ ❖ᴄʜᴀᴛ ɪᴅ❖ › : {chat_id}\n┣★ ❖ᴄʜᴀᴛ ᴜɴᴀᴍᴇ❖ › : {chatusername}\n┣★ ❖ᴛᴏᴛᴀʟ ᴄʜᴀᴛ❖ › : {served_chats}\n┣★ ❖ᴀᴅᴅᴇᴅ ʙʏ❖ › :\n┗━━━ {added_by}"
        await lul_message(LOGGER_ID, lemda_text)
