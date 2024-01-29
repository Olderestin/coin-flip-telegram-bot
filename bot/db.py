from __future__ import annotations
import random
import sqlite3
from pathlib import Path
from typing import Tuple
from typing_extensions import Self

class UserDatabase():
    """
    A class for interacting with a SQLite database to store user statistics.
    """
    
    def __init__(self, db_path: Path) -> None:
        """
        Initializes the UserDatabase instance.
        
        Args:
            param db_path: The path to sqlite3 database file.
        """
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path / "user.db")

    def __enter__(self) -> Self:
        """
        Called when entering a 'with' statement. Creates a cursor for database operations.

        Returns:
            self
        """

        self.cursor = self.conn.cursor()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb) -> None:
        """
        Called when exit a 'with' statement. Commits changes if no exceptions occurred and closes cursor.
        """

        try:
            if exc_type is None:
                self.conn.commit()
        finally:
            self.cursor.close()

    def create_user_table(self) -> None:
        """
        Creates the 'user' table in the database if it doesn't exist.
        """

        self.cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            flips_count INTEGER DEFAULT 0,
            heads_count INTEGER DEFAULT 0,
            tails_count INTEGER DEFAULT 0
        )
    ''')
        
    def add_user(self, user_id: int) -> None:
        """
        Adds a user to the 'user' table if they don't already exist.

        Args:
            param user_id: The ID of the user to be added.
        """

        self.cursor.execute('INSERT OR IGNORE INTO user (user_id) VALUES (?)', (user_id,))

    def make_flip(self, user_id: int) -> str:
        """
        Simulates a coin flip, updates user statistics, and returns the result.
        
        Args:
            param user_id: The ID of the user making the flip.
        Returns:
            str('heads' or 'tails').
        
        """

        self.cursor.execute('UPDATE user SET flips_count = flips_count + 1 WHERE user_id = ?', (user_id,))
        
        result = 'heads' if random.randint(0, 1) == 0 else 'tails'
        
        if result == 'heads':
            self.cursor.execute('UPDATE user SET heads_count = heads_count + 1 WHERE user_id = ?', (user_id,))
        else:
            self.cursor.execute('UPDATE user SET tails_count = tails_count + 1 WHERE user_id = ?', (user_id,))

        return result

    def get_stats(self, user_id: int) -> tuple[int, int, int]:
        """
        Retrieves user statistics from the database and returns it.
        
        Args:
            param user_id: The ID of the user.
        Returns:
            tuple(flips_count, heads_count, tails_count).
        """

        self.cursor.execute('SELECT flips_count, heads_count, tails_count FROM user WHERE user_id = ?', (user_id,))
        stats = self.cursor.fetchone()
        return stats
