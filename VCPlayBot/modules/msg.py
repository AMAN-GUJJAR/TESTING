import os
from VCPlayBot.config import SOURCE_CODE
from VCPlayBot.config import ASSISTANT_NAME
from VCPlayBot.config import PROJECT_NAME
from VCPlayBot.config import SUPPORT_GROUP
from VCPlayBot.config import UPDATES_CHANNEL
class Messages():
      START_MSG = "**𝙷𝙴𝙻𝙻𝙾 👋 [{}](tg://user?id={})!**\n\n🍁 𝙸 𝙰𝙼 𝙰𝙽 𝙰𝙳𝚅𝙰𝙽𝙲𝙴𝙳 𝙱𝙾𝚃 𝙲𝚁𝙴𝙰𝚃𝙴𝙳 𝙵𝙾𝚁 𝙿𝙻𝙰𝚈𝙸𝙽𝙶 𝙼𝚄𝚂𝙸𝙲 𝙸𝙽 𝚃𝙷𝙴 𝚅𝙾𝙸𝙲𝙴 𝙲𝙷𝙰𝚃𝚂 𝙾𝙵 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙶𝚁𝙾𝚄𝙿𝚂 & 𝙲𝙷𝙰𝙽𝙽𝙴𝙻𝚂.\n\n✅ 𝚂𝙴𝙽𝙳 𝙼𝙴 /help 𝙵𝙾𝙴 𝙼𝙾𝚁𝙴 𝙸𝙽𝙵𝙾.\n\n 𝙹𝙾𝙸𝙽 @DARKAMANCHANNEL"
      HELP_MSG = [
        ".",
f"""
**𝙷𝙴𝚈 👋 𝚆𝙴𝙻𝙲𝙾𝙼𝙴 𝙱𝙰𝙲𝙺 𝚃𝙾 {PROJECT_NAME}

⚪️ {PROJECT_NAME} can play music in your group's voice chat as well as channel voice chats

⚪️ Assistant name >> @{ASSISTANT_NAME}\n\nClick next for instructions**

Join @DARKAMANSUPPORT
""",

f"""
**Setting up**

1) Make bot admin (Group and in channel if use cplay)
2) Start a voice chat
3) Try /play [song name] for the first time by an admin
*) If userbot joined enjoy music, If not add @{ASSISTANT_NAME} to your group and retry

**For Channel Music Play**
1) Make me admin of your channel 
2) Send /userbotjoinchannel in linked group
3) Now send commands in linked group

Join @DARKAMANCHANNEL
""",
f"""
**Commands**

**=>> Song Playing 🎧**

- /play: Play the requestd song
- /play [yt url] : Play the given yt url
- /play [reply yo audio]: Play replied audio
- /splay: Play song via jio saavn
- /ytplay: Directly play song via Youtube Music

**=>> Playback ⏯**

- /player: Open Settings menu of player
- /skip: Skips the current track
- /pause: Pause track
- /resume: Resumes the paused track
- /end: Stops media playback
- /current: Shows the current Playing track
- /playlist: Shows playlist

*Player cmd and all other cmds except /play, /current  and /playlist  are only for admins of the group.
Join @DARKAMANCHANNEL
""",

f"""
**=>> Channel Music Play 🛠**

⚪️ For linked group admins only:

- /cplay [song name] - play song you requested
- /csplay [song name] - play song you requested via jio saavn
- /cplaylist - Show now playing list
- /cccurrent - Show now playing
- /cplayer - open music player settings panel
- /cpause - pause song play
- /cresume - resume song play
- /cskip - play next song
- /cend - stop music play
- /userbotjoinchannel - invite assistant to your chat

channel is also can be used instead of c ( /cplay = /channelplay )

⚪️ If you donlt like to play in linked group:

1) Get your channel ID.
2) Create a group with tittle: Channel Music: your_channel_id
3) Add bot as Channel admin with full perms
4) Add @{ASSISTANT_NAME} to the channel as an admin.
5) Simply send commands in your group. (remember to use /ytplay instead /play)
Join @DARKAMANSUPPORT
""",

f"""
**=>> More tools 🧑‍🔧**

- /musicplayer [on/off]: Enable/Disable Music player
- /admincache: Updates admin info of your group. Try if bot isn't recognize admin
- /userbotjoin: Invite @{ASSISTANT_NAME} Userbot to your chat
Join @DARKAMANSUPPORT
""",
f"""
**=>> Song Download 🎸**

- /video [song mame]: Download video song from youtube
- /song [song name]: Download audio song from youtube
- /saavn [song name]: Download song from saavn
- /deezer [song name]: Download song from deezer

**=>> Search Tools 📄**

- /search [song name]: Search youtube for songs
- /lyrics [song name]: Get song lyrics
Join @DARKAMANSUPPORT
""",

f"""
**=>> Commands for Sudo Users ⚔️**

 - /userbotleaveall - remove assistant from all chats
 - /broadcast <reply to message> - globally brodcast replied message to all chats
 - /pmpermit [on/off] - enable/disable pmpermit message
*Sudo Users can execute any command in any groups
Join @DARKAMANSUPPORT
"""
      ]
