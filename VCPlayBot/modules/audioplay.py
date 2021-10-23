#DARKAMAN 
#ALEXA_MUSIC
#COPY_RIGHT = DARKAMAN

from os import path

from pyrogram import Client
from pyrogram.types import Message, Voice

from VCPlayBot.callsmusic import callsmusic, queues

import VCPlayBot.converter
from VCPlayBot.downloaders import youtube

from VCPlayBot.config import BOT_NAME, DURATION_LIMIT, UPDATES_CHANNEL, BG_IMAGE, SUPPORT_GROUP,
from VCPlayBot.helpers.filters import command, other_filters
from VCPlayBot.helpers.decorators import errors
from VCPlayBot.helpers.errors import DurationLimitError
from VCPlayBot.helpers.gets import get_url, get_file_name
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(command("audio") & other_filters)
@errors
async def stream(_, message: Message):

    lel = await message.reply("🔁 **processing**")
    sender_id = message.from_user.id
    sender_name = message.from_user.first_name

    keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="🖱️𝚂𝚄𝙿𝙿𝙾𝚁𝚃🖱️",
                        url=f"https://t.me/{SUPPORT_GROUP}"),
                    InlineKeyboardButton(
                        text="🍁𝙲𝙷𝙰𝙽𝙽𝙴𝙻🍁",
                        url=f"https://t.me/{UPDATES_CHANNEL}")
                ]
            ]
        )

    audio = (message.reply_to_message.audio or message.reply_to_message.voice) if message.reply_to_message else None
    url = get_url(message)

    if audio:
        if round(audio.duration / 60) > DURATION_LIMIT:
            raise DurationLimitError(
                f"❌ Videos longer than {DURATION_LIMIT} minute(s) aren't allowed to play!"
            )

        file_name = get_file_name(audio)
        file_path = await converter.convert(
            (await message.reply_to_message.download(file_name))
            if not path.isfile(path.join("downloads", file_name)) else file_name
        )
    elif url:
        file_path = await converter.convert(youtube.download(url))
    else:
        return await lel.edit_text("❗ you did not give me audio file or yt link to stream!")

    if message.chat.id in callsmusic.pytgcalls.active_calls:
        position = await queues.put(message.chat.id, file=file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"⚡ Track added to the **queue**\n\n🔢 position: » `{position}` «\n🎧 request by: {costumer}\n\n⚡ __Powered by {bn} A.I__")
        return await lel.delete()
    else:
        callsmusic.pytgcalls.join_group_call(message.chat.id, file_path)
        costumer = message.from_user.mention
        await message.reply_photo(
        photo=f"{BG_IMAGE}",
        reply_markup=keyboard,
        caption=f"💡 **Status**: `Playing`\n🎧 Request by: {costumer}\n\n⚡ __Powered by {bn} A.I__"
        )
        return await lel.delete()
