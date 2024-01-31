from pathlib import Path

from pydantic_settings import BaseSettings

from bot.db import UserDatabase

project_dir = Path(__file__).parent.parent


class Settings(BaseSettings):
    """
    Class for storing app settings.
    """

    BOT_TOKEN: str
    REDIS_HOST: str
    REDIS_PORT: int
    REDIS_DB: int
    DATABASE_PATH: Path = project_dir / "storage"
    LOG_PATH: Path = project_dir / "storage"

    class Config:
        """
        Configuration class for settings.
        """

        env_file = ".env"
        case_sensitive = True


settings = Settings()

USER_DB = UserDatabase(
    redis_host=settings.REDIS_HOST,
    redis_port=settings.REDIS_PORT,
    redis_db=settings.REDIS_DB,
)
