#https://t.me/ll_about_ari_ll
import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters
#from keep_alive import keep_alive

#keep_alive()

load_dotenv()


API_ID = int(getenv("API_ID", "21971830"))

API_HASH = getenv("API_HASH", "46389a1d51d331e5d30d4d6b8a101f3d")

BOT_TOKEN = getenv("BOT_TOKEN", "none")

BOT_USERNAME = ("ari_music_4u_bot")   

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://ariopp:ariopp@cluster0.fpdbynt.mongodb.net/?retryWrites=true&w=majority")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 54000))

SONG_DOWNLOAD_DURATION = int(
    getenv("SONG_DOWNLOAD_DURATION_LIMIT", "54000")
)

LOGGER_ID = int(getenv("LOGGER_ID", "-1002043787206"))

OWNER_ID = int(getenv("OWNER_ID", "6352061770"))

HEROKU_APP_NAME = getenv("arimusic")

HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/arimaxx/JAAnXARI",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "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", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/ll_about_ari_ll")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Three_stars_ki_duniya")

ARI_STRING = "BQG_NJ0AazT9C_HwTtBU5Wc9Sand4lDWmNYQPknCk_1_PTB378Zk7Fy9ehQo7U1VUX45s8yCdaewjjMhx3vvybUEpKDnXcKqjRFlV8M3N3cl48ZjCeAbqvGIdafFgcOVzeDjzIr6vCyRjGYmRKMEDUIWle1qXOghJFh_YMrTzKc-zlWQlAIA3y4-W15JfEEzfjgjzBBRICfmnBr8xLfrbwEGF4-hFH28Tr70HKWekjkU0enSWSCGZYyYS_ZTTe7cCgH8K8MDFhHkXOFtu3sPLOJBioIvXBpmSh0ihPfek1CBQ3UC_Owoj5q4OECU_QHhBD-g9n6iGRrGeKKP93lYeVLJ_olT6wAAAAEs_QHtAA"

AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))
AUTO_SUGGESTION_MODE = getenv("AUTO_SUGGESTION_MODE", "True")
AUTO_SUGGESTION_TIME = int(
    getenv("AUTO_SUGGESTION_TIME", "500"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", None)
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", None)



PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 25))

CLEANMODE_DELETE_MINS = int(
    getenv("CLEANMODE_MINS", "5"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))



# Get your pyrogram v2 session from @Shsusu_bot on Telegram
STRING1 = getenv("STRING_SESSION", "")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}
chatstats = {}
userstats = {}
clean = {}

autoclean = []
#https://telegra.ph/file/eee7b255edfc07c52959c.jpg
START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/645221f832dcf9661fde9.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/eee7b255edfc07c52959c.jpg"
)
PLAYLIST_IMG_URL = "https://telegra.ph/file/b609c4f51469c4778dfab.jpg"
STATS_IMG_URL = "https://telegra.ph/file/ba3411bd163e56c452f94.jpg"
TELEGRAM_AUDIO_URL = "https://telegra.ph/file/eee7b255edfc07c52959c.jpg"
TELEGRAM_VIDEO_URL = "https://telegra.ph/file/eee7b255edfc07c52959c.jpg"
STREAM_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"
SOUNCLOUD_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"
YOUTUBE_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/1d80c38ce328695547203.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00"))

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

YOUTUBE_IMG_URL = getenv(
    "YOUTUBE_IMG_URL",
    "https://te.legra.ph/file/389f11da55c1c1a60a215.jpg",
)
