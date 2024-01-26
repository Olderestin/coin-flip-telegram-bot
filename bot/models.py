import random
import sqlite3
from pathlib import Path

from bot.config import settings


class UserDatabase():
    def __init__(self, db_path: Path = settings.DATABASE_URL):
        self.db_path = db_path

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_path / "user.db")
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        try:
            if exc_type is None:
                self.conn.commit()
        finally:
            self.conn.close()
            del self.cursor

    def create_user_table(self):
        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            flips_count INTEGER DEFAULT 0,
            heads_count INTEGER DEFAULT 0,
            tails_count INTEGER DEFAULT 0
        )
    ''')
        
    def add_user(self, user_id: int):
        self.cursor.execute('INSERT OR IGNORE INTO user (user_id) VALUES (?)', (user_id,))

    def make_flip(self, user_id: int):
        self.cursor.execute('UPDATE user SET flips_count = flips_count + 1 WHERE user_id = ?', (user_id,))
        
        result = 'heads' if random.randint(0, 1) == 0 else 'tails'
        
        if result == 'heads':
            self.cursor.execute('UPDATE user SET heads_count = heads_count + 1 WHERE user_id = ?', (user_id,))
        else:
            self.cursor.execute('UPDATE user SET tails_count = tails_count + 1 WHERE user_id = ?', (user_id,))

        return result

    def get_stats(self, user_id: int):
        self.cursor.execute('SELECT flips_count, heads_count, tails_count FROM user WHERE user_id = ?', (user_id,))
        stats = self.cursor.fetchone()
        return stats
