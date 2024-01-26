from loguru import logger
from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler, filters

from handlers import start, flip, stats, about
from config import settings
from models import UserDatabase

logger.add("app.log", rotation="500 MB", level="TRACE")

def main() -> None:
    
    with UserDatabase() as user_db:
        user_db.create_user_table()

    application = ApplicationBuilder().token(settings.BOT_TOKEN).build()

    logger.info("Start the app")


    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bFlip\b'), callback=flip))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bStats\b'), callback=stats))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bAbout\b'), callback=about))

    
    application.run_polling()

if __name__ == '__main__':
    main()

logger.warning("App has been closed")