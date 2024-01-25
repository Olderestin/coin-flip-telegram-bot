from pydantic_settings import BaseSettings
from pathlib import Path
from dotenv import load_dotenv
import os

load_dotenv()

class Settings(BaseSettings):

    BOT_TOKEN: str = os.environ.get("BOT_TOKEN")
    DATABASE_URL: Path = Path('storage\coin_flip_bot.db').resolve()

# print(Settings().model_dump())

settings = Settings()