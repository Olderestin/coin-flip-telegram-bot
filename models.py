from database import create_connection

def create_user_table():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user (
            user_id INTEGER PRIMARY KEY,
            flips_count INTEGER DEFAULT 0,
            heads_count INTEGER DEFAULT 0,
            tails_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()