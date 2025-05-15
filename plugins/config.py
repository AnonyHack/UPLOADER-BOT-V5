import os
from os import environ, getenv
import logging

logging.basicConfig(
    format='%(name)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log.txt'),
              logging.StreamHandler()],
    level=logging.INFO
)

class Config(object):
    # Required Configuration
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7990210328:AAFnFNvR5HuXOXHuYa5_iMujE-khn6nis7Y")
    API_ID = int(os.environ.get("API_ID", 25753873))  # Add your API_ID
    API_HASH = os.environ.get("API_HASH", "3a5cdc2079cd76af80586102bd9761e2")
    OWNER_ID = list(map(int, os.environ.get("OWNER_ID", "5962658076").split()))  # Your Telegram user ID
    
    # Database Configuration
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://ramybeginning:ALLAHAKBAr%40232956@cluster0.ja2zly9.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    
    # Channel Configuration
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", -100123456789))  # Channel ID where logs will be sent
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", "-1002380953539")  # Your updates channel
    
    # Bot Settings
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "Urluploader4GBbot")
    SESSION_NAME = "Urluploader4GBbot"
    
    # File Handling
    DOWNLOAD_LOCATION = "./DOWNLOADS"
    MAX_FILE_SIZE = 2194304000
    TG_MAX_FILE_SIZE = 2194304000
    CHUNK_SIZE = int(os.environ.get("CHUNK_SIZE", 128))
    
    # Thumbnail and Watermark
    DEF_THUMB_NAIL_VID_S = os.environ.get("DEF_THUMB_NAIL_VID_S", "https://placehold.it/90x90")
    DEF_WATER_MARK_FILE = "@Urluploader4GBbot"
    
    # Other Settings
    HTTP_PROXY = os.environ.get("HTTP_PROXY", "")
    OUO_IO_API_KEY = ""
    MAX_MESSAGE_LENGTH = 4096
    PROCESS_MAX_TIMEOUT = 3600
    BANNED_USERS = set(int(x) for x in os.environ.get("BANNED_USERS", "").split() if x)
    TRUE_OR_FALSE = os.environ.get("TRUE_OR_FALSE", "false").lower() == "true"
    
    # Shortlink settings
    SHORT_DOMAIN = environ.get("SHORT_DOMAIN", "")
    SHORT_API = environ.get("SHORT_API", "")
    
    # Verification
    VERIFICATION = os.environ.get("VERIFICATION", "")
    
    LOGGER = logging
