import logging
from telegram.ext import CommandHandler, ApplicationBuilder, MessageHandler, filters

from handlers import start, flip, stats, about
from config import BOT_TOKEN
from models import create_user_table

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def main() -> None:
    create_user_table()

    application = ApplicationBuilder().token(BOT_TOKEN).build()
    
    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bFlip\b'), callback=flip))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bStats\b'), callback=stats))
    application.add_handler(MessageHandler(filters=filters.Regex(r'\bAbout\b'), callback=about))

    
    application.run_polling()

if __name__ == '__main__':
    main()