import sqlite3

def get_db():
    conn = sqlite3.connect("db.sqlite3")
    return conn

def create_table():
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            category TEXT,
            completed BOOLEAN
        )
    """)
    conn.commit()
    conn.close()
