import os, re
from os import getenv
from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN")
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "Raagini Music")
MONGO_DB_URI = getenv("MONGO_DB_URI", None)
DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 17000))
LOGGER_ID = int(getenv("LOGGER_ID", ""))
OWNER_ID = int(getenv("OWNER_ID", ""))
START_STICKER_ID = getenv("START_STICKER_ID", "CAACAgUAAxkBAAFLBQxqGpE3nyOVIe80zciOz-slTiti_wACsBMAAprIWFc2bbJCNGPswjsE")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("HEROKU_API_KEY")
YTPROXY_URL = getenv("YTPROXY_URL", 'https://tgapi.xbitcode.com') ## xBit Music Endpoint.
YT_API_KEY = getenv("YT_API_KEY" , 'xbit_FoPZuIwe2QtqAbVbc1Yc2YLWqk1Phhqe' )
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/icakofisuw242-droid/RUHIMUSIC",)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv("GIT_TOKEN", None)
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/MusicXUpdate")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/GUPTAJI_op")
AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", None)
AUTO_LEAVE_ASSISTANT_TIME = int(getenv("ASSISTANT_LEAVE_TIME", "9000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION", "9999999"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "9999999"))
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "1c21247d714244ddbb09925dac565aed")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "709e1a2969664491b58200860623ef19")
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "500"))
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "5242880000"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "5242880000"))
COOKIES = getenv("COOKIES", None)
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)
STRING6 = getenv("STRING_SESSION6", None)
STRING7 = getenv("STRING_SESSION7", None)
BANNED_USERS = filters.user()
TEMP_DB_FOLDER = "tempdb"
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/a6f2452e4409facd9231f-dd07dc43c453e1a94b.jpg")
PING_IMG_URL = getenv("PING_IMG_URL", "https://ibb.co/HfN4bRwH")
PLAYLIST_IMG_URL = "https://telegra.ph/file/7db32a17b15440fa88f91.jpg"
STATS_IMG_URL = "https://telegra.ph/file/02af26494524244cf83d0.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
STREAM_IMG_URL = "https://telegra.ph/file/03efec694e41e891b29dc.jpg"
SOUNCLOUD_IMG_URL = "https://telegra.ph/file/b00af14042edff8b71f2e.jpg"
YOUTUBE_IMG_URL = "https://telegra.ph/file/9f3720a8d4ec5ae50977f.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://telegra.ph/file/fa144f06d6d024877edda.jpg"
def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))
DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
