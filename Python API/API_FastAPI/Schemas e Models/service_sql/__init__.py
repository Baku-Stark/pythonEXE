import sqlite3 as lite
from contextlib import contextmanager

DATABASE_URL = "./service_sql/db/todo.db"

@contextmanager
def get_db():
    conn = lite.connect(DATABASE_URL)
    try:
        print("Table created")
        yield conn
        
    finally:
        conn.close()

def init_db():
    with get_db() as conn:
        conn.execute('''
            CREATE TABLE IF NOT EXISTS todo_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                completed BOOLEAN NOT NULL DEFAULT 0
            )
        ''')
