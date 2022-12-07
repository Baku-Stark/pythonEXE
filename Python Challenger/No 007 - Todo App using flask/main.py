# ========================================================
# IMPORTAÇÕES
from flask import Flask, render_template, request, jsonify
# ===
from yaml import load, Loader

#   ---> Os [Operational System]
import os

#   ---> Criação do banco de dados
import sqlalchemy

#   ---> Banco de dados[database.py]
from app.database import *

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
# APLICAÇÃO FLASK
app = Flask(__name__)
db = init_connection_engine()

# ========================================================
# Routes [@app.route]
@app.route("/")
def homepage():
    items = fetch_todo()
    return render_template('index.html', items=items)

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
    try:
        if "status" in data:
            update_stauts_entry(task_id, data["status"])
            result = {'success': True, 'response': 'Status Updated'}
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

if __name__ == '__main__':
    app.run(debug=True)