from dotenv import load_dotenv
import os

load_dotenv()

BOT_TOKEN = os.environ.get('BOT_TOKEN')
DATABASE_URL = 'storage/coin_flip_bot.db'