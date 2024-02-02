from loguru import logger
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import filters
from telegram.ext import MessageHandler

from bot.config import settings
from bot.handlers import about
from bot.handlers import error_handler
from bot.handlers import flip
from bot.handlers import start
from bot.handlers import stats

logger.add(settings.LOG_PATH / "app.log", rotation="500 MB", level="TRACE")


async def setup_bot(application) -> None:
    bot = application.bot
    logger.info(f"bot ID: {bot.id}")
    logger.info(f"bot username: {bot.username}")
    logger.info(f"bot link: {bot.link}")


def main() -> None:
    application = (
        ApplicationBuilder().token(settings.BOT_TOKEN).post_init(setup_bot).build()
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(
        MessageHandler(filters=filters.Regex(r"\bFlip\b"), callback=flip)
    )
    application.add_handler(
        MessageHandler(filters=filters.Regex(r"\bStats\b"), callback=stats)
    )
    application.add_handler(
        MessageHandler(filters=filters.Regex(r"\bAbout\b"), callback=about)
    )
    application.add_error_handler(error_handler)

    application.run_polling()


if __name__ == "__main__":
    main()

logger.warning("App has been closed")
