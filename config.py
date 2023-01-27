import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
class Config(object):
    log = True
    APP_ID = getenv("API_ID", "6296490")
    API_HASH = getenv("API_HASH", "24385183c93a98ae4155c25d9f5f64b2")
    TOKEN = getenv("TOKEN", "")
    OWNER_ID = getenv("OWNER_ID", "5467311248")
    ASSISTANT_ID = getenv("ASSISTANT_ID", "5763920115")
    STRING_SESSION = getenv("STRING_SESSION", "") #telethon
    OWNER_USERNAME = getenv("OWNER_USERNAME", "Sexsuxassist")
    DB_URI = getenv("DATABASE_URL", "")
    DB_URI = DB_URI.replace("postgres", "postgres://jrycfssc:fEZMYWiOcO9vB8cIq1_Z97GhW3TiTppJ@tiny.db.elephantsql.com/jrycfssc")
    MESSAGE_DUMP = getenv("MESSAGE_DUMP", "-1001647004968")
    GBAN_LOGS = getenv("GBAN_LOGS", "-1001647004968")
    SYS_ADMIN = getenv("SYS_ADMIN", "6296490")
    DEV_USERS = getenv("DEV_USERS", "844126468")
    LOAD = getenv("LOAD")
    WEBHOOK = False
    SPB_MODE = True
    DROP_UPDATES = False
    DEBUG = False
    URL = None
    INFOPIC = True
    CERT_PATH = None
    PORT = 5000
    DEL_CMDS = True
    STRICT_GBAN = True
    BAN_STICKER = getenv("BAN_STICKER", "https://te.legra.ph/file/7e5b79d224638c0d1a38f.jpg")
    ALLOW_EXCL = True
    CUSTOM_CMD = False
    CHANNEL = getenv("CHANNEL", "ALL_DEFENCE_Exams")
    SUPPORT = getenv("SUPPORT", "sexsuxassist")
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/35a7b5d9f1f2605c9c0d3.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/66518ed54301654f0b126.png")
    CASH_API_KEY = getenv("Y8SCX7ADDAYE1LER", "https://www.alphavantage.co/support/#api-key")
    TIME_API_KEY = getenv("IYRY6U4HY05H", "https://timezonedb.com/api")
    WALL_API = getenv("WALL_API", "https://wall.alphacoders.com/api.php")
    spamwatch_api = getenv("spamwatch_api", "https://t.me/SpamWatchBot")
    SPAMMERS = getenv("SPAMMERS", "")
    LASTFM_API_KEY = getenv("LASTFM_API_KEY", "https://www.last.fm/api/account/create")
    CF_API_KEY = getenv("CF_API_KEY", "coffehouse.intellivoid.net")
    BOT_API_URL = getenv("https://api.telegram.org/bot5802795983:AAFtocF-utPkBvF2d6ttMoxR8cu-26ZBhzo", "https://api.telegram.org/bot")
    BOT_API_FILE_URL = getenv("https://api.telegram.org/file/bot5802795983:AAFtocF-utPkBvF2d6ttMoxR8cu-26ZBhzo", "https://api.telegram.org/file/bot")
    SUDO_USERS = list(map(int, getenv("5763920115", "1669178360").split()))
    ZAID_USER = list(map(int, getenv("sexxyneo", "5467311248").split()))
    NO_LOAD = list(map(int, getenv("NO_LOAD", "").split()))
