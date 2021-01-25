from pyrogram import Client
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(filters.command(["start"])
        await message.reply_text(
            text="{start}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Button 1", url="{https://t.me/mpazaan}"),
                        InlineKeyboardButton("Button 2", url="{https://t.me/mpazaan}"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Button 3", url="{https://t.me/mpazaan}")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
