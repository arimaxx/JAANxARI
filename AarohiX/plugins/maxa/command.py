from AarohiX import app
from pyrogram import Client, filters
from config import *

# Initialize the Pyrogram client
bot = Client("BOT_TOKEN")

# Define a common function for sending the jaan photo reply
async def send_jaan_photo(client, message):
    photo_file_path = "https://telegra.ph/file/94cf72e3ae17f553c4f02.jpg"
    await message.reply_photo(
        photo=photo_file_path,
        caption="""🤍 afk ➪ sᴇᴛ ʏᴏᴜʀ ᴏғғʟɪɴᴇ ʀᴇᴀsᴏɴ 🌸\n
                   🤍 brb ➪ sʜᴏᴡ ʏᴏᴜʀ ᴏғғʟɪɴᴇ ʀᴇᴀsᴏɴ ɪɴsᴛᴀɴᴛ ✨🌸\n
                   🤍 alive ➪ ʙᴏᴛ ᴡɪʟʟ ᴀʟɪᴠᴇ ᴀɴᴅ sᴇɴᴅ ᴀ ᴀʟɪᴠᴇ ᴍᴀssᴀɢᴇ✨🌸\n
                   🤍 Welcome ➪ ɪᴛ's ᴀᴜᴛᴏ ᴅᴏɴ'ᴛ ɴᴇᴇᴅ ᴛᴏ sᴇᴛ ᴇᴠᴇʀʏᴛɪᴍᴇ ✨🌸\n
                   🤍 bt ➪ sʜᴏᴡ ᴛʜᴇ ᴀʟʟ ʙᴏᴛ ʟɪsᴛ ᴘᴇʀᴄᴇɴᴛ ɪɴ ᴛʜᴇ ɢʀᴏᴜᴘ✨🌸\n
                   🤍 tgraph ➪ [ᴛᴇxᴛ/ʀᴇᴘʟʏ ᴛᴏ ᴍᴇssᴀɢᴇ] - ᴘᴏsᴛ ᴛᴇxᴛ/ᴍᴇᴅɪᴀ ᴛᴏ ᴛᴇʟᴇɢʀᴀᴘʜ.🌸✨🌸\n
                   🤍 leavegroup ➪ ʙᴏᴛ ᴡɪʟʟ ʟᴇᴀᴠᴇ ᴛʜᴇ ɢʀᴏᴜᴘ ɪғ ᴏᴡɴᴇʀ sᴀʏs🌸✨🌸\n
                   🤍 calender ➪ ɢɪᴠᴇ ᴛʜᴇ ʏᴇᴀʀ ᴀɴᴅ ʙᴏᴛ ᴡɪʟʟ ɢɪᴇᴠᴇ ᴛʜᴇ ᴄᴀʟᴇɴᴅᴀʀ ᴏғ ᴛʜᴀᴛ ʏᴇᴀʀ .🌸✨🌸\n
                   🤍 figlet ➪ ɢɪᴠᴇ ᴀ ᴛᴇxᴛ ᴀɴᴅ ᴛᴏ ɢᴇᴛ ᴅᴇsɪɢɴᴇᴅ ᴛᴇxᴛ .🌸✨🌸\n
                   🤍 image ➪ ɢɪᴠᴇ sᴇᴀʀᴄʜ ǫᴜᴇʀʏ ʙᴏᴛ ᴡɪʟʟ ɢɪᴠᴇ ɪᴍᴀɢᴇ ғʀᴏᴍ ᴘɪɴᴛʀᴇsᴛ .🌸✨🌸\n
                   🤍 info ➪ ʀᴇᴘʟʏ ᴛᴏ ᴛᴇxᴛ ᴀɴᴅ ɢᴇᴛ ᴜsᴇʀ ɪɴғᴏ .🌸✨🌸\n
                   🤍 jaan ➪ sᴇᴇ ᴍʏ ʟᴏᴠᴇ 🙈\n
                   🤍 speedtest ➪ ʙᴏᴛ ᴡɪʟʟ ɢɪᴠᴇ sᴘᴇᴇᴅ ᴏғ ɴᴇᴛᴡᴏʀᴋ .🌸✨🌸\n
                   🤍 ᴡɪsʜᴘᴇʀ ➪[@ʙᴏᴛᴜsᴇʀɴᴀᴍᴇ] + [@ᴛᴀʀɢᴇᴛ ᴜsᴇʀɴᴀᴍᴇ] + [ᴛᴇxᴛ]❤️‍🔥♡゙""")

# Handle both /jaan and /jann commands
@app.on_message(filters.command(["command", "module", "extra"]))
async def handle_jaan_commands(client, message):
    await send_jaan_photo(client, message)
