# ========================================================
# IMPORTAÇÕES
from flask import Flask, render_template, request, jsonify
# ===
from yaml import load, Loader

#   ---> Os [Operational System]
import os

#   ---> Criação do banco de dados
import sqlalchemy

# ========================================================
# ToDo List
def fetch_todo() -> dict:
    """
        Ler todas as taskas listadas em uma lista Todo

        Returns:
            Uma lista em dicionários
    """
    db = init_connection_engine()
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
# BANCO DE DADOS [lib: sqlalchemy]
def init_connection_engine():
    """
        Inicialização do banco de dados

        Returns:
            pool -- a connection to GCP MySQL
    """

    if os.environ.get("GAE_ENV") != 'standard':
        try:
            dic_local = r'{}\app\templates\app.yaml'.format(os.getcwd())
            variables = load(open(dic_local), Loader=Loader)
        
        except OSError:
            print(dic_local)
            print("Verifique se você tem a configuração do arquivo app.yaml")
            os._exit(os.X_OK)
        
        env_variables = variables['env_variables']
        for var in env_variables:
            os.environ[var] = env_variables[var]

    pool = sqlalchemy.create_engine(
        sqlalchemy.engine.url.URL(
            drivername="mysql+pymysql",
            username=os.environ.get('MYSQL_USER'),
            password=os.environ.get('MYSQL_PASSWORD'),
            database=os.environ.get('MYSQL_DB'),
            host=os.environ.get('MYSQL_HOST')
        )
    )
    return pool

# ========================================================
# [insert]
def insert_new_task(text: str) -> int:
    """
        Criar uma task e adicionar na Todo > Table

        Args:
            text(str) : Texto a ser inserido
        Return:
            O ID da task em INT
    """
    db = init_connection_engine()
    con = db.connect()
    query = f'INSERT INTO tasks(task, status) VALUES ("{text}", "{"Todo"}")'
    con.execute(query)
    query_result = con.execute("SELECT LAST_INSERT_ID()")
    query_result = [x for x in query_result]
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
    db = init_connection_engine()
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
    db = init_connection_engine()
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
    db = init_connection_engine()
    con = db.connect()
    query = f'DELETE FROM tasks WHERE id={task_id}'
    con.execute(query)
    con.close()

# ========================================================
# APLICAÇÃO FLASK
app = Flask(__name__)

# ========================================================
# Routes [@app.route]
@app.route("/")
def homepage():
    items = fetch_todo()
    return render_template("web_page.html", items=items)

@app.route("/delete/<int:task_id>", methods=['POST'])
def delete(task_id):
    """
        Pedidos de postagem recebidos para exclusão de entrada.
    """
    try:
        delete_task_by_id(task_id)
        result = {'success': True, 'response': 'Removed task'}
    except:
        result = {'success': False, 'response': 'Something went wrong'}

    return jsonify(result)

@app.route("/edit/<int:task_id>", methods=['POST'])
def update(task_id):
    """
        Pedidos de postagem recebidos para atualização.
    """
    data = request.get_json()
    try:
        if "status" in data:
            update_stauts_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Task Updated'}
        elif "description" in data:
            update_task_entry(task_id, data['description'])
        else:
            result = {'success': True, 'response': 'Nothing Updated'}
    except:
        result = {'success': True, 'response': 'Something went wrong'}
    return jsonify(result)

@app.route("/create", methods=['POST'])
def create():
    """
        Pedidos de postagem recebidos para adição de tasks.
    """
    data = request.get_json()
    insert_new_task(data['description'])
    result = {'success': True, 'response': 'Done'}
    return jsonify(result)


# ========================================================
# Ativação da aplicação
if __name__ == '__main__':
    app.run(debug=True)