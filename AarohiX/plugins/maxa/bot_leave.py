from AarohiX import app
from pyrogram.types import Chat, User

import pyrogram
from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
from pyrogram.enums import ParseMode
import asyncio
from PIL import Image, ImageDraw
from typing import Union, Optional

async def get_users(user_id):
    try:
        user = await app.get_users(user_id)
        profile_photo = user.photo
        user_id = user.id
        return profile_photo, user_id
    except Exception as e:
        print("Error occurred:", e)
        return None, None

# Placeholder function for get_font
def get_font(size, path):
    pass

async def get_userinfo_img(
    bg_path: str,
    font_path: str,
    user_id: Union[int, str],
    profile_path: Optional[str] = None
):
    bg = Image.open(bg_path)

    if profile_path:
        img = Image.open(profile_path)
        mask = Image.new("L", img.size, 0)
        draw = ImageDraw.Draw(mask)
        draw.pieslice([(0, 0), img.size], 0, 360, fill=255)

        circular_img = Image.new("RGBA", img.size, (0, 0, 0, 0))
        circular_img.paste(img, (0, 0), mask)
        resized = circular_img.resize((400, 400))
        bg.paste(resized, (440, 160), resized)

    img_draw = ImageDraw.Draw(bg)

    img_draw.text(
        (529, 627),
        text=str(user_id).upper(),
        font=get_font(100, font_path),
        fill=(255, 255, 255),
    )

    path = f"./userinfo_img_{user_id}.png"
    bg.save(path)
    return path

@app.on_chat_member_updated(filters.create(lambda _, __, event: event.new_chat_member is None))
async def bot_leave(client, event):
    left_member = event.old_chat_member.user
    left_member_name = left_member.first_name
    left_member_id = left_member.id

    left_message = f'»»————- ★ - ★ ————-««\n <a href="tg://user?id={left_member_id}">{left_member_name}</a> #LEFT ʜᴜᴍ ʜᴀɪ ʀᴀʜɪ ᴘʏᴀᴀʀ ᴋᴇ \nᴘʜɪʀ ᴍɪʟᴇɴɢᴇ ᴄʜᴀʟᴛᴇ ᴄʜᴀʟᴛᴇ. \n User ID: {left_member_id}\n »»————- ★ - ★ ————-««'

    profile_photo, _ = await get_users(left_member_id)
    profile_path = None
    if profile_photo:
        if profile_photo.big_file_id:
            # User has a profile photo, so we fetch it
            photos = client.get_chat_photos(left_member_id, limit=1)
            async for photo in aiter(photos):
                if photo:
                    profile_photo_path = await client.download_media(photo.file_id)
                    profile_path = profile_photo_path
                    break
                else:
                    # Handle the case when the user doesn't have any profile photos
                    pass
        else:
            # User doesn't have a profile photo, handle accordingly
            pass

    if profile_path:
        userinfo_img_path = await get_userinfo_img(
            bg_path="AarohiX/assets/userinfo.png",
            font_path="AarohiX/assets/hiroko.ttf",
            user_id=left_member_id,
            profile_path=profile_path
       )

        # Send the image along with the leave message
        await client.send_photo(
            chat_id=event.chat.id,
            photo=userinfo_img_path,
            caption=left_message,
            parse_mode=ParseMode.HTML
        )
    else:
        # Send the message without the image if profile photo is not available
        await client.send_message(
            chat_id=event.chat.id,
            text=left_message,
            parse_mode=ParseMode.HTML
        )
