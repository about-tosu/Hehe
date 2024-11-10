import logging  

from pyrogram import Client 

from telegram.ext import Application
from motor.motor_asyncio import AsyncIOMotorClient

logging.basicConfig(
    format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    handlers=[logging.FileHandler("log.txt"), logging.StreamHandler()],
    level=logging.INFO,
)

logging.getLogger("apscheduler").setLevel(logging.ERROR)
logging.getLogger('httpx').setLevel(logging.WARNING)
logging.getLogger("pyrate_limiter").setLevel(logging.ERROR)
LOGGER = logging.getLogger(__name__)

OWNER_ID = ["6965147961","6848223695"]
SUDO_USERS = ["6848223695","6965147961","5897492421","6745981296","1374057577","5458968679","6309921371"]
GROUP_ID = -1002332668271
TOKEN = "7749407611:AAEBsTIO6hRVNiD_tApKeOJVBYJAffGnMtc" 
mongo_url = "mongodb+srv://snatcherwaifu0925:snatcherwaifu0925@snatcher0.fft3j.mongodb.net/?retryWrites=true&w=majority&appName=Snatcher0"
PHOTO_URL = ["https://envs.sh/nJo.jpg", "https://envs.sh/nJs.jpg"]
SUPPORT_CHAT = "-1002332668271"
UPDATE_CHAT = "-1002332668271"
BOT_USERNAME = "SNATCH_YOURR_WAIFU_BOT"
CHARA_CHANNEL_ID = "-1002336624454"
api_id = "24835491"
api_hash = "04ee66f0079a9b11eefb33a89289899e" 

application = Application.builder().token(TOKEN).build()
Grabberu = Client("Grabber", api_id, api_hash, bot_token=TOKEN)
client = AsyncIOMotorClient(mongo_url)
db = client['Character_catcher']
collection = db['anime_characters']
user_totals_collection = db['user_totals']
user_collection = db["user_collection"]
group_user_totals_collection = db['group_user_total']
top_global_groups_collection = db['top_global_groups']
group_collection = db['group_collection']
pm_users = db['total_pm_users']
