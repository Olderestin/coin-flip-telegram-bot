from pydantic_settings import BaseSettings
from pathlib import Path
import os

from bot.db import UserDatabase

project_dir = Path(__file__).parent.parent

class Settings(BaseSettings):
    """
    Class for storing app settings.
    """

    BOT_TOKEN: str
    DATABASE_PATH: Path = project_dir / "storage"
    LOG_PATH: Path = project_dir / "storage"

    class Config():
        """
        Configuration class for settings.
        """

        env_file = ".env"
        case_sensitive = True

settings = Settings()

USER_DB = UserDatabase(settings.DATABASE_PATH)