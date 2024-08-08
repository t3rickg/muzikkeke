from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = getenv("API_ID")
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = getenv("OWNER_ID")

PING_IMG = getenv("PING_IMG", "https://i.hizliresim.com/ebszw3y.jpg")
START_IMG = getenv("START_IMG", "https://i.hizliresim.com/ebszw3y.jpg")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/sohbetkiyicilar")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/kiyicitayfaa")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7490336041").split()))


FAILED = "https://i.hizliresim.com/ebszw3y.jpg"
