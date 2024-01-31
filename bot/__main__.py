from loguru import logger
from telegram.ext import ApplicationBuilder
from telegram.ext import CommandHandler
from telegram.ext import filters
from telegram.ext import MessageHandler

from bot.config import settings
from bot.handlers import about
from bot.handlers import flip
from bot.handlers import start
from bot.handlers import stats

logger.add(settings.LOG_PATH / "app.log", rotation="500 MB", level="TRACE")


def main() -> None:
    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    logger.info("Start the app")

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

    application.run_polling()


if __name__ == "__main__":
    main()

logger.warning("App has been closed")
