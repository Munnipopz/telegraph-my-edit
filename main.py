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


@Client.on_message(filters.command(["Start"])
        await message.reply_text(
            text="{പൊളി}",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("Button 1", url="{https://t.me/mpazaan


}"),
                        InlineKeyboardButton("Button 2", url="{https://t.me/mpazaan


}"),
                    ],
                    [
                        InlineKeyboardButton(
                            "Button 3", url="{https://t.me/mpazaan


}")
                    ]
                ]
            ),
            reply_to_message_id=message.message_id
        )
