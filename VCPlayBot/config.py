import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "DARKAMANCHANNEL")
BG_IMAGE = getenv("BG_IMAGE", "https://te.legra.ph/file/798bd58d8ce671f5d4b6f.png")
THUMB_IMG = getenv("THUMB_IMG", "https://te.legra.ph/file/798bd58d8ce671f5d4b6f.png")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "ALEXA_MUSIC_1.0")
OWNER_NAME = getenv("OWNER_NAME", "DARKAMAN")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "DARKAMANSUPPORT")
PROJECT_NAME = getenv("PROJECT_NAME", "ALEXA_MUSIC_1.0")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/AMAN-GUJJAR/VCPlayBot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
ARQ_API_KEY = getenv("ARQ_API_KEY", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "1946450856").split()))
