# Copyright (C) @TheSmartBisnu
# Channel: https://t.me/itsSmartDev

import os
from time import time
from dotenv import load_dotenv

try:
    load_dotenv("config.env.local")
    load_dotenv("config.env")
except Exception:
    pass

# --- Configuration Variables ---
BOT_TOKEN = os.environ.get("BOT_TOKEN", "8657586410:AAFocrBpmheH7PDkCSsbudGIMVPczcfkmXE")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "27686895"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "0e996bd3891969ec5dfebf8bb3e39e94")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "1246987713"))

# Your Channel Id In Which Bot Upload Downloaded Video/File/Message etc.
# And Make Your Bot Admin In this channel with full rights.
# if you don't want to upload in channel then leave it blank don't fill anything.
CHANNEL_ID = os.environ.get("CHANNEL_ID", "-1003654284775")

# Session string for user client
SESSION_STRING = os.environ.get("SESSION_STRING")

# --- Validation ---
if not BOT_TOKEN or ":" not in BOT_TOKEN:
    print("Error: BOT_TOKEN must be in format '123456:abcdefghijklmnopqrstuvwxyz'")
    # exit(1) # Commented out to avoid crashing during setup if not needed immediately

if not SESSION_STRING or SESSION_STRING == "xxxxxxxxxxxxxxxxxxxxxxx":
    print("Warning: SESSION_STRING is not set. User client features will not work.")

# --- Pyrogram setup ---
class PyroConf(object):
    API_ID = API_ID
    API_HASH = API_HASH
    BOT_TOKEN = BOT_TOKEN
    SESSION_STRING = SESSION_STRING
    BOT_START_TIME = time()

    MAX_CONCURRENT_DOWNLOADS = int(os.environ.get("MAX_CONCURRENT_DOWNLOADS", "1"))
    BATCH_SIZE = int(os.environ.get("BATCH_SIZE", "1"))
    FLOOD_WAIT_DELAY = int(os.environ.get("FLOOD_WAIT_DELAY", "10"))

    # If FORWARD_CHAT_ID is not set in env, use CHANNEL_ID as default
    FORWARD_CHAT_ID = os.environ.get("FORWARD_CHAT_ID", CHANNEL_ID).strip() or None

