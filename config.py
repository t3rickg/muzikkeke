from os import getenv

from dotenv import load_dotenv

load_dotenv()


API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")

BOT_TOKEN = getenv("BOT_TOKEN", None)
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "90"))

OWNER_ID = int(getenv("OWNER_ID"))

PING_IMG = getenv("PING_IMG", "https://c.tenor.com/_yFLs1OWgBAAAAAC/tenor.gif")
START_IMG = getenv("START_IMG", "https://c.tenor.com/_yFLs1OWgBAAAAAC/tenor.gif")

SESSION = getenv("SESSION", None)

SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/tilkicitayfa")
SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/tekornetwork")

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "7303086953").split()))


FAILED = "https://i.hizliresim.com/p9rb864.png"
