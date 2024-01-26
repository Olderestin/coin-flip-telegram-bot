from pydantic_settings import BaseSettings
from pathlib import Path
import os

project_dir = Path(__file__).parent.parent

class Settings(BaseSettings):

    BOT_TOKEN: str
    DATABASE_URL: Path = project_dir / "storage"

    class Config():

        env_file = ".env"
        case_sensitive = True

settings = Settings()