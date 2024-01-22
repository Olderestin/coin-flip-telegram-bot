import random
from telegram import ReplyKeyboardMarkup, Update
from telegram.ext import CallbackContext

from database import create_connection

reply_keyboard = [
    ["Flip", "Stats"],
    ["About"],
]

markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)

async def start(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('INSERT OR IGNORE INTO user (user_id) VALUES (?)', (user_id,))
    conn.commit()
    conn.close()

    
    await update.message.reply_text("Привет! Теперь вы можете использовать команды flip и stats.", reply_markup=markup)

async def flip(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('UPDATE user SET flips_count = flips_count + 1 WHERE user_id = ?', (user_id,))
    
    result = 'heads' if random.randint(0, 1) == 0 else 'tails'
    
    if result == 'heads':
        cursor.execute('UPDATE user SET heads_count = heads_count + 1 WHERE user_id = ?', (user_id,))
    else:
        cursor.execute('UPDATE user SET tails_count = tails_count + 1 WHERE user_id = ?', (user_id,))
    
    conn.commit()
    conn.close()
    await update.message.reply_text(f'Результат подбрасывания монетки: {result}')

async def stats(update: Update, context: CallbackContext) -> None:
    user_id = update.effective_user.id
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('SELECT flips_count, heads_count, tails_count FROM user WHERE user_id = ?', (user_id,))
    stats = cursor.fetchone()
    conn.close()

    if stats:
        flips_count, heads_count, tails_count = stats

        heads_percentage = heads_count * 100 / flips_count if flips_count > 0 else 0
        tails_percentage = tails_count * 100 / flips_count if flips_count > 0 else 0

        text = (
            'Статистика подбрасываний монетки:\n'
            f'Всего подбрасываний: {flips_count}\n'
            f'Орлов (heads): {heads_count} ({heads_percentage}%)\n'
            f'Решек (tails): {tails_count} ({tails_percentage}%)'
        )

        await update.message.reply_text(text)
    else:
        await update.message.reply_text('Вы еще не подбрасывали монетку. Используйте /flip.')

async def about(update: Update, context: CallbackContext) -> None:
    await update.message.reply_text('Этот бот был создан в качестве тестового задания.\nОн выполняет функции подбрасывания монеты и запись статистики подбрасываний для каждого отдельного пользователя.')