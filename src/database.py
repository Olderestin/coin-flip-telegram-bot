import sqlite3

DB_FILE = 'storage/coin_flip_bot.db'

def create_connection():
    return sqlite3.connect(DB_FILE)