from loguru import logger
from telegram import ReplyKeyboardMarkup
from telegram import Update
from telegram.ext import CallbackContext

from bot.config import USER_DB

reply_keyboard = [
    ["Flip", "Stats"],
    ["About"],
]

MARKUP = ReplyKeyboardMarkup(
    reply_keyboard, one_time_keyboard=False, resize_keyboard=True
)


async def start(update: Update, context: CallbackContext) -> None:
    """
    Handles the /start command and initializes a new user.

    Args:
        param update: The incoming update.
        param context: The context for the callback.
    """

    user_id = update.effective_user.id

    logger.info(f"A new user: {user_id}")
    await update.message.reply_text(
        "Привет! Теперь вы можете использовать команды flip и stats.",
        reply_markup=MARKUP,
    )


async def flip(update: Update, context: CallbackContext) -> None:
    """
    Handles the «Flip» command and simulates a coin flip for the user and send the result.

    Args:
        param update: The incoming update.
        param context: The context for the callback.
    """

    user_id = update.effective_user.id

    result = USER_DB.make_flip(user_id)

    logger.info(f"User {user_id} make a flip with result: {result}")
    await update.message.reply_text(f"Результат подбрасывания монетки: {result}")


async def stats(update: Update, context: CallbackContext) -> None:
    """
    Handles the «Stats» command and displays the user's coin flip statistics.

    Args:
        param update: The incoming update.
        param context: The context for the callback.
    """

    user_id = update.effective_user.id

    flips_count, heads_count, tails_count = USER_DB.get_stats(user_id)
    if flips_count > 0:
        heads_percentage = heads_count * 100 / flips_count if flips_count > 0 else 0
        tails_percentage = tails_count * 100 / flips_count if flips_count > 0 else 0

        text = (
            "Статистика подбрасываний монетки:\n"
            f"Всего подбрасываний: {flips_count}\n"
            f"Орлов (heads): {heads_count} ({heads_percentage}%)\n"
            f"Решек (tails): {tails_count} ({tails_percentage}%)"
        )

        logger.info(f"User {update.effective_user.id} used «Stats» handler.")
        await update.message.reply_text(text)
    else:
        await update.message.reply_text(
            "Вы еще не подбрасывали монетку. Используйте Flip."
        )


async def about(update: Update, context: CallbackContext) -> None:
    """
    Handles the «About» command and provides information about the bot.

    Args:
        param update: The incoming update.
        param context: The context for the callback.
    """

    logger.info(f"User {update.effective_user.id} used «About» handler.")
    await update.message.reply_text(
        "Этот бот был создан в качестве тестового задания.\nОн выполняет функции подбрасывания монеты и запись статистики подбрасываний для каждого отдельного пользователя."
    )


def error_handler(update: Update, context: CallbackContext) -> None:
    """
    Log Errors caused by Updates.
    """
    logger.error(f"Update {update} caused error {context.error}")
