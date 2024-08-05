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
        ''') # completed BOOLEAN NOT NULL DEFAULT 0 [0 = false, 1 = true]
        

def create_todo(todo : list):
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            query = "INSERT INTO todo_items (title, description, completed) VALUES (?, ?, ?)"
            cursor.execute(query, todo)
        
        except lite.OperationalError as error_sqlite3:
            print(error_sqlite3)
            
        else:
            print(f"** TAREFA '{todo[0]}' ADICIONADA **")
            conn.commit()
        
        finally:
            conn.close()

def read_all_todo() -> list[list]:
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            query = "SELECT * FROM todo_items"
            cursor.execute(query)

        except lite.ProgrammingError as error:
            print(error)
    
        else:
            cursor_list = cursor.fetchall()
        
        finally:
            conn.close()

    return cursor_list

def read_id_todo(_id : int) -> list:
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            cursor.row_factory = lite.Row
            query = "SELECT * FROM todo_items WHERE id=?"
            cursor.execute(query, (_id,))

        except lite.ProgrammingError as error:
            print(error)
    
        else:
            cursor_list = cursor.fetchone()

        finally:
            conn.close()

    return list(cursor_list)

def update_status_todo(_id : int) -> list:
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            todo_list= read_id_todo(_id)
            
            if todo_list[3] == 1:
                query = "UPDATE todo_items SET completed=0 WHERE id=?"

            else:
                query = "UPDATE todo_items SET completed=1 WHERE id=?"
            
            cursor.execute(query, (_id))

        except lite.ProgrammingError as error:
            print(error)
    
        else:
            conn.commit()
            print(f"** TAREFA '{todo_list[1]}' ATUALIZADA **")

        finally:
            conn.close()

    return read_id_todo(_id)

def update_body_todo(_id : int, todo : list) -> list:
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            todo_list= read_id_todo(_id)
            
            query = "UPDATE todo_items SET title=?, description=?, completed=? WHERE id=?"
            
            cursor.execute(query, (todo[0], todo[1], todo[2], _id))

        except lite.ProgrammingError as error:
            print(error)
    
        else:
            conn.commit()
            print(f"** TAREFA '{todo_list[1]}' ATUALIZADA PARA -> '{todo[0]}' **")

        finally:
            conn.close()

    return read_id_todo(_id)

def delete_status_todo(_id : int) -> list:
    with get_db() as conn:
        cursor = conn.cursor()
        try:
            todo_list = read_id_todo(_id)
            
            query = "DELETE FROM todo_items WHERE id=?"
            
        except lite.ProgrammingError as error:
            print(error)
    
        else:
            cursor.execute(query, (_id,))
            print(f"** TAREFA '{todo_list[1]}' APAGADA **")
            return read_id_todo(_id)
        
        finally:
            conn.commit()
            conn.close()