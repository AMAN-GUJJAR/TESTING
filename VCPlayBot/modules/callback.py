# (C) supun-maduraga my best friend for his project on call-music-plus

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from VCPlayBot.helpers.decorators import authorized_users_only
from VCPlayBot.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from VCPlayBot.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>β¨ **Welcome user, i'm {query.message.from_user.mention}** \n
β‘ **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) π°π»π»πΎπ ππΎπ ππΎ πΏπ»π°π πΌπππΈπ² πΎπ½ πΆππΎππΏπ ππ·ππΎππΆπ·π ππ·π΄ π½π΄π ππ΄π»π΄πΆππ°πΌ'π ππΎπΈπ²π΄ π²π·π°ππ !**

π±οΈ ** π΅πΎπ πΈπ½π΅πΎππΌπ°ππΈπΎπ½ π°π±πΎππ π°π»π» π΅π΄π°ππππ΄ πΎπ΅ ππ·π΄ π±πΎπ, πΉπππ πππΏπ΄ /help**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "π°π³π³ πΌπ΄ ππΎ ππΎππ πΆππΎππΏ", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "π·πΎπ ππΎ πππ΄ πΌπ΄", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "π²πΎπΌπΌπ°π½π³π", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                         "π²ππ΄π°ππ΄π", url=f"https://t.me/{OWNER_NAME}")
                ],[
                    InlineKeyboardButton(
                         "πππΏπΏπΎππ", url=f"https://t.me/{SUPPORT_GROUP}"
                    ),
                    InlineKeyboardButton(
                        "π²π·π°π½π½π΄π»", url=f"https://t.me/{UPDATES_CHANNEL}")
                ],[
                    InlineKeyboardButton(
                        "π°π»π΄ππ° ππΎπ±πΎπ", url="https://t.me/ALEXA_MANAGER_ROBOT"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b> hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°ππΈπ² π²πΌπ³", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "π°π³ππ°π½π²π΄π³ π²πΌπ³", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π°π³πΌπΈπ½ π²πΌπ³", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "πππ³πΎ π²πΌπ³", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πΎππ½π΄π π²πΌπ³", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π΅ππ½ π²πΌπ³", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ ", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the basic commands</b>

π§ [ GROUP VC CMD ]

- /play (song name) - play song from youtube
- /ytpplay (song name) - play song directly from youtube 
- /playlist - show the list song in queue
- /song (song name) - download song from youtube
- /search (video name)Β - search video from youtube detailed
- /video (video name)Β - download video from youtube detailed
- /lyrics - (song name) lyrics scrapper

π§ [ CHANNEL VC CMD ]

- /cplay - stream music on channel voice chat
- /cplayer - show the song in streaming
- /cpause - pause the streaming music
- /cresume - resume the streaming was paused
- /cskip - skip streaming to the next song
- /cend - end the streaming music
- /admincache - refresh the admin cache
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the advanced commands</b>

/start (in group) - see the bot alive status
/reload - reload bot and refresh the admin list
/admincache - refresh the admin cache
/ping - check the bot ping status
/uptime - check the bot uptime status

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the admin commands</b>

/player - show the music playing status
/pause - pause the music streaming
/resume - resume the music was paused
/skip - skip to the next song
/end - stop music streaming
/userbotjoin - invite assistant join to your group
/auth - authorized user for using music bot
/deauth - unauthorized for using music bot
/control - open the player settings panel
/delcmd (on | off) - enable / disable del cmd feature
/musicplayer (on / off) - disable / enable music player in your group
/b and /tb (ban / temporary ban) - banned permanently or temporarily banned user in group
/ub - to unbanned user you're banned from group
/m and /tm (mute / temporary mute) - mute permanently or temporarily muted user in group
/um - to unmute user you're muted in group

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the sudo commands</b>

/userbotleaveall - order the assistant to leave from all group
/gcast - send a broadcast message trought the assistant
/stats - show the bot statistic
/rmd - remove all downloaded files
/clean - Remove all raw files

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the owner commands</b>

/stats - show the bot statistic
/broadcast - send a broadcast message from bot
/block (user id - duration - reason) - block user for using your bot
/unblock (user id - reason) - unblock user you blocked for using your bot
/blocklist - show you the list of user was blocked for using your bot

π note: all commands owned by this bot can be executed by the owner of the bot without any exceptions.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π? here is the fun commands</b>

/chika - check it by yourself
/wibu - check it by yourself
/asupan - check it by yourself
/truth - check it by yourself
/dare - check it by yourself

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π²πΎπΌπΌπ°π½π³ π»πΈππ", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π π²π»πΎππ΄", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**π‘ here is the control menu of bot :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βΈ pause", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "βΆοΈ resume", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β© skip", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "βΉ end", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "β anti cmd", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π group tools", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π Close", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>

π‘ **Feature:** this feature contains functions that can ban, mute, unban, unmute users in your group.

and you can also set a time for the ban and mute penalties for members in your group so that they can be released from the punishment with the specified time.

β **usage:**

1οΈβ£ ban & temporarily ban user from your group:
   Β» type `/b username/reply to message` ban permanently
   Β» type `/tb username/reply to message/duration` temporarily ban user
   Β» type `/ub username/reply to message` to unban user

2οΈβ£ mute & temporarily mute user in your group:
   Β» type `/m username/reply to message` mute permanently
   Β» type `/tm username/reply to message/duration` temporarily mute user
   Β» type `/um username/reply to message` to unmute user

π note: cmd /b, /tb and /ub is the function to banned/unbanned user from your group, whereas /m, /tm and /um are commands to mute/unmute user in your group.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>this is the feature information :</b>
        
**π‘ Feature:** delete every commands sent by users to avoid spam in groups !

β usage:**

 1οΈβ£ to turn on feature:
     Β» type `/delcmd on`
    
 2οΈβ£ to turn off feature:
     Β» type `/delcmd off`
      
β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>π‘ Hello there, welcome to the help menu !</b>

**in this menu you can open several available command menus, in each command menu there is also a brief explanation of each command**

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°ππΈπ² π²πΌπ³", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "π°π³ππ°π½π²π΄π³ π²πΌπ³", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π°π³πΌπΈπ½ π²πΌπ³", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "πππ³πΎ π²πΌπ³", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "πΎππΌπ΄π π²πΌπ³", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π΅ππ½ π²πΌπ³", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""β HOW TO USE THIS BOT:

1.) first, add me to your group.
2.) then promote me as admin and give all permissions except anonymous admin.
3.) add @{ASSISTANT_NAME} to your group or type /userbotjoin to invite her.
4.) turn on the voice chat first before start to play music.

β‘ __Powered by {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "π±π°π²πΊ", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
