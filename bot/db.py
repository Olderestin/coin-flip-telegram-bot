import random
import sqlite3
from pathlib import Path

from bot.config import settings


class UserDatabase():
    """
    A class for interacting with a SQLite database to store user statistics.

    param db_path: The path to sqlite3 database file.

    attribute db_path: The path to connect to sqlite3 database.
    """
    def __init__(self, db_path: Path = settings.DATABASE_URL):
        self.db_path = db_path

    def __enter__(self):
        """
        Called when entering a 'with' statement. Connects to the database.
        """

        self.conn = sqlite3.connect(self.db_path / "user.db")
        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """
        Called when exit a 'with' statement. Commits changes if no exceptions occurred.
        """

        try:
            if exc_type is None:
                self.conn.commit()
        finally:
            self.conn.close()
            del self.cursor

    def create_user_table(self):
        """
        Creates the 'user' table in the database if it doesn't exist.

        column user_id: Primary key representing the user.
        column flips_count: Count of coin flips for the user with a default value of 0.
        column heads_count: Count of 'heads' outcomes for the user with a default value of 0.
        column tails_count: Count of 'tails' outcomes for the user with a default value of 0.
        """

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            flips_count INTEGER DEFAULT 0,
            heads_count INTEGER DEFAULT 0,
            tails_count INTEGER DEFAULT 0
        )
    ''')
        
    def add_user(self, user_id: int):
        """
        Adds a user to the 'user' table if they don't already exist.

        param user_id: The ID of the user to be added.
        """

        self.cursor.execute('INSERT OR IGNORE INTO user (user_id) VALUES (?)', (user_id,))

    def make_flip(self, user_id: int):
        """
        Simulates a coin flip, updates user statistics, and returns the result.
        
        param user_id: The ID of the user making the flip.
        """

        self.cursor.execute('UPDATE user SET flips_count = flips_count + 1 WHERE user_id = ?', (user_id,))
        
        result = 'heads' if random.randint(0, 1) == 0 else 'tails'
        
        if result == 'heads':
            self.cursor.execute('UPDATE user SET heads_count = heads_count + 1 WHERE user_id = ?', (user_id,))
        else:
            self.cursor.execute('UPDATE user SET tails_count = tails_count + 1 WHERE user_id = ?', (user_id,))

        return result

    def get_stats(self, user_id: int):
        """
        Retrieves user statistics from the database and returns it.
        
        param user_id: The ID of the user.
        """

        self.cursor.execute('SELECT flips_count, heads_count, tails_count FROM user WHERE user_id = ?', (user_id,))
        stats = self.cursor.fetchone()
        return stats
