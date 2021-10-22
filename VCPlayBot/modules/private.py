
import logging
from time import time
from datetime import datetime
from VCPlayBot.config import BOT_USERNAME, BOT_NAME, ASSISTANT_NAME, OWNER_NAME, UPDATES_CHANNEL, SUPPORT_GROUP
from VCPlayBot.helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import sudo_users_only

logging.basicConfig(level=logging.INFO)


START_TIME = datetime.utcnow()
START_TIME_ISO = START_TIME.replace(microsecond=0).isoformat()
TIME_DURATION_UNITS = (
    ('week', 60 * 60 * 24 * 7),
    ('day', 60 * 60 * 24),
    ('hour', 60 * 60),
    ('min', 60),
    ('sec', 1)
)

async def _human_time_duration(seconds):
    if seconds == 0:
        return 'inf'
    parts = []
    for unit, div in TIME_DURATION_UNITS:
        amount, seconds = divmod(int(seconds), div)
        if amount > 0:
            parts.append('{} {}{}'
                         .format(amount, unit, "" if amount == 1 else "s"))
    return ', '.join(parts)


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def start_(client: Client, message: Message):
    await message.reply_photo("https://te.legra.ph/file/9ee01453fc404013fabf1.jpg")
    await message.reply_text(
        f"""<b>✨ **𝚆𝙴𝙻𝙲𝙾𝙼𝙴 {message.from_user.first_name}** \n
⚡ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) 𝙰𝙻𝙻𝙾𝚆 𝚈𝙾𝚄 𝚃𝙾 𝙿𝙻𝙰𝚈 𝙼𝚄𝚂𝙸𝙲 𝙾𝙽 𝙶𝚁𝙾𝚄𝙿𝚂 𝚃𝙷𝚁𝙾𝚄𝙶𝙷 𝚃𝙷𝙴 𝙽𝙴𝚆 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼'𝚂 𝚅𝙾𝙸𝙲𝙴 𝙲𝙷𝙰𝚃𝚂 !**

🖱️ **𝙵𝙾𝚁 𝙸𝙽𝙵𝙾𝚁𝙼𝙰𝚃𝙸𝙾𝙽 𝙰𝙱𝙾𝚄𝚃 𝙰𝙻𝙻 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝙾𝙵 𝚃𝙷𝙸𝚂 𝙱𝙾𝚃, 𝙹𝚄𝚂𝚃 𝚃𝚈𝙿𝙴 /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙳 𝙼𝙴 𝚃𝙾 𝚈𝙾𝚄𝚁 𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "𝙲𝙾𝙼𝙼𝙰𝙽𝙳𝚂", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                         "𝙲𝚁𝙴𝙰𝚃𝙴𝚁", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                        "𝚂𝚄𝙿𝙿𝙾𝚁𝚃", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "𝙰𝙻𝙴𝚇𝙰 𝚁𝙾𝙱𝙾𝚃", url="https://t.me/ALEXA_MANAGER_ROBOT"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def start(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        f"""⚡ **bot is running**\n<b>🖱️ **uptime:**</b> `{uptime}`""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙶𝚁𝙾𝚄𝙿", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "𝙲𝙷𝙰𝙽𝙽𝙴𝙻", url=f"https://t.me/{UPDATES_CHANNEL}"
                    )
                ]
            ]
        )
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 **Hello** {message.from_user.mention()}</b>

**Please press the button below to read the explanation and see the list of available commands !**

⚡ __Powered by {BOT_NAME} A.I""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="𝙷𝙾𝚆 𝚃𝙾 𝚄𝚂𝙴 𝙼𝙴", callback_data="cbguide"
                    )
                ]
            ]
        ),
    )

@Client.on_message(command(["help", f"help@{BOT_USERNAME}"]) & filters.private & ~filters.edited)
async def help_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>💡 Hello {message.from_user.mention} welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

⚡ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙱𝙰𝚂𝙸𝙲 𝙲𝙼𝙳", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝙲𝙼𝙳", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙰𝙳𝙼𝙸𝙽 𝙲𝙼𝙳", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "𝚂𝚄𝙳𝙾 𝙲𝙼𝙳", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙾𝚆𝙽𝙴𝚁 𝙲𝙼𝙳", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "𝙵𝚄𝙽 𝙲𝙼𝙳", callback_data="cbfun"
                    )
                ]
            ]
        )
    )


@Client.on_message(command(["ping", f"ping@{BOT_USERNAME}"]) & ~filters.edited)
async def ping_pong(client: Client, message: Message):
    start = time()
    m_reply = await message.reply_text("pinging...")
    delta_ping = time() - start
    await m_reply.edit_text(
        "🍁 `PONG!!`\n"
        f"⚡️ `{delta_ping * 1000:.3f} ms`"
    )


@Client.on_message(command(["uptime", f"uptime@{BOT_USERNAME}"]) & ~filters.edited)
@sudo_users_only
async def get_uptime(client: Client, message: Message):
    current_time = datetime.utcnow()
    uptime_sec = (current_time - START_TIME).total_seconds()
    uptime = await _human_time_duration(int(uptime_sec))
    await message.reply_text(
        "😇 bot status:\n"
        f"• **uptime:** `{uptime}`\n"
        f"• **start time:** `{START_TIME_ISO}`"
    )
