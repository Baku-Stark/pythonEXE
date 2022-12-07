# ========================================================
# Importação [__init__.py]
from main import db

def fetch_todo() -> dict:
    """
        Ler todas as taskas listadas em uma lista Todo

        Returns:
            Uma lista em dicionários
    """
    con = db.connect()
    query_results = con.execute("SELECT * FROM tasks").fetchall()
    con.close()

    todo_list = []
    for result in query_results:
        item ={
            "id": result[0],
            "task": result[1],
            "status": result[2]
        }
        todo_list.append(item)
    return todo_list

# ========================================================
# [insert -> creat]
def insert_new_task(text: str) -> int:
    """
        Criar uma task e adicionar na Todo > Table

        Args:
            text(str) : Texto a ser inserido
        Return:
            O ID da task em INT
    """
    con = db.connect()
    query = f'INSERT INTO tasks(task, status) VALUES ("{text}", "{"Todo"}")'
    con.execute(query)
    query_result = con.execute("SELECT LAST_INSERT_ID()")
    task_id = query_result[0][0]
    con.close()

    return task_id

# ========================================================
# [update]
def update_task_entry(task_id: int, text: str) -> None:
    """
        Função para atualizar as tasks `task`
        
        Args:
            task_id(int) : número de ID
            text(str) : Descrição atualizada
        
        Return:
            None
    """
    con = db.connect()
    query = f'UPDATE tasks SET task="{text}" WHERE id={task_id}'
    con.execute(query)
    con.close()

def update_stauts_entry(task_id: int, text: str) -> None:
    """
        Função para atualizar as tasks `status`
        
        Args:
            task_id(int) : número de ID
            text(str) : Descrição atualizada
        
        Return:
            None
    """
    con = db.connect()
    query = f'UPDATE tasks SET status="{text}" WHERE id={task_id}'
    con.execute(query)
    con.close()

# ========================================================
# [delete]
def delete_task_by_id(task_id: int) -> None:
    """
        Remover uma task pelo seu endereço de ID

        Args:
            task_id(int) : Número de endereço ID da task
        Return:
            None
    """
    con = db.connect()
    query = f'DELETE FROM tasks WHERE id={task_id}'
    con.execute(query)
    con.close()