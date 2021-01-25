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
