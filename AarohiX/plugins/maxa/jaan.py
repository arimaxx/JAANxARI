from AarohiX import app
from pyrogram import Client, filters
from config import *

# Initialize the Pyrogram client
bot = Client("BOT_TOKEN")

# Define a common function for sending the jaan photo reply
async def send_jaan_photo(client, message):
    photo_file_path = "https://telegra.ph/file/6bb70b1212c30e712b079.jpg"
    await message.reply_photo(photo=photo_file_path, caption="♡゙━━━━━ ❣️𝐌𝐘 𝐋𝐎𝐕𝐄❣️ ━━━━━━♡゙\n\n ♡゙━━🥺𝐓ᴜ 𝐇ɪ 𝐌ᴇʀᴀ 𝐏ʏᴀʀ 𝐇ᴀ𝐈💞━━♡゙\n\n ♡゙━━━❤️ 𝐓ᴜ 𝐇ɪ 𝐌ᴇʀ𝐈 𝐁ᴀ𝐍ᴅᴀɢ𝐈🌸━♡゙\n\n ♡゙━━💘𝐓ᴜ 𝐇ɪ 𝐌ᴇʀᴀ 𝐊ʜᴡᴀʙ 𝐇ᴀ𝐈 ━━♡゙\n\n ♡゙━━━🤍𝐓ᴜ 𝐇ɪ 𝐌ᴇʀ𝐈 𝐙ɪɴᴅᴀɢ𝐈❤️‍🔥━━♡゙")

# Handle both /jaan and /jann commands
@app.on_message(filters.command(["jaan", "jann", "gf", "pyar"]))
async def handle_jaan_commands(client, message):
    await send_jaan_photo(client, message)
