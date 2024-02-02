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
    REDIS_PORT: int = 6379
    REDIS_DB: int = 0
    DATABASE_PATH: Path = project_dir / "storage"
    LOG_PATH: Path = project_dir / "storage"

    class Config:
        """
        Configuration class for settings.
        """

        env_file = ".env"
        case_sensitive = True


settings = Settings()  # type: ignore

USER_DB = UserDatabase(
    redis_host=settings.REDIS_HOST,
    redis_port=settings.REDIS_PORT,
    redis_db=settings.REDIS_DB,
)
