import sqlite3
import os

folder_path = 'storage'

if not os.path.exists(folder_path):
    os.makedirs(folder_path)

DB_FILE = 'storage/coin_flip_bot.db'

def create_connection():
    return sqlite3.connect(DB_FILE)