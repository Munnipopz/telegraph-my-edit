import os
import uuid
import shutil
import logging
from pyrogram import Client, filters
from creds import Credentials
from telegraph import upload_file
from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
logging.basicConfig(level=logging.INFO)


TGraph = Client(
    "Image upload bot",
    bot_token=Credentials.BOT_TOKEN,
    api_id=Credentials.API_ID,
    api_hash=Credentials.API_HASH,
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
