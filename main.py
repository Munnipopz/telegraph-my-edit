import os
import uuid
import shutil
import logging
from pyrogram import Client, filters
from creds import Credentials
from telegraph import upload_file

logging.basicConfig(level=logging.INFO)

from pyrogram import Client, filters
from creds import Credentials
from telegraph import upload_file
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


TGraph = Client(
    "Image upload bot",
    bot_token=Credentials.BOT_TOKEN,
    api_id=Credentials.API_ID,
    api_hash=Credentials.API_HASH,
)


@TGraph.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text(
        f"Hello {message.from_user.first_name},\nIm telegram to telegra.ph image uploader bot by  @Munnipopz https://telegra.ph/file/6f8d9001de13b3f8e573a.jpg ",
        True,
        
    )
@Client.on_message(filters.command(["test"]))
async def test(client, message):
        await message.reply_text(
            text="{text}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Button 1", url="{link}"),
                        InlineKeyboardButton("Button 2", url="{link}"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Button 3", url="{link}")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )



@TGraph.on_message(filters.photo)
async def getimage(client, message):
    tmp = os.path.join("downloads", str(message.chat.id))
    if not os.path.isdir(tmp):
        os.makedirs(tmp)
    img_path = os.path.join(tmp, str(uuid.uuid4()) + ".jpg")
    dwn = await message.reply_text("Downloading...", True)
    img_path = await client.download_media(message=message, file_name=img_path)
    await dwn.edit_text("Uploading...")
    try:
        response = upload_file(img_path)
    except Exception as error:
        await dwn.edit_text(f"Oops something went wrong\n{error}")
        return
    await dwn.edit_text(f"https://telegra.ph{response[0]}")
    shutil.rmtree(tmp, ignore_errors=True)


TGraph.run()
