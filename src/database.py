import sqlite3
from pathlib import Path
from config import DATABASE_URL

DB_FILE = Path(DATABASE_URL).resolve()

def create_connection():
    return sqlite3.connect(DB_FILE)