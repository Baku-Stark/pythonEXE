import sqlite3 as lite
from contextlib import contextmanager

DATABASE_URL = "./service_sql/db/todo.db"

@contextmanager
def get_db():
    conn = lite.connect(DATABASE_URL)
    try:
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

        # completed BOOLEAN NOT NULL DEFAULT 0 [0 = false, 1 = true]

def create_todo(todo : list):
    with get_db() as conn:
        try:
            query = "INSERT INTO todo_items (title, description, completed) VALUES (?, ?, ?)"
            conn.execute(query, todo)
        
        except lite.OperationalError as error_sqlite3:
            print(error_sqlite3)
            
        finally:
            print(f"** TAREFA '{todo[0]}' ADICIONADA **")
            conn.commit()
            conn.close()
