from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["test"])
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
