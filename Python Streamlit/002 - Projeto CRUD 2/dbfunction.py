import sqlite3 as lite

con = lite.connect("database/database.db", check_same_thread = False)


# ===============================================
# CRIAÇÃO DE TABELA
def create_table():
    conector = con.cursor()
    conector.execute('CREATE TABLE IF NOT EXISTS carslist(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, marca_do_carro TEXT, price TEXT)')

# ===============================================
# REGISTRAR NOVO MODELO
def insert(i):
    conector = con.cursor()
    query = ('INSERT INTO carslist(nome, marca_do_carro, price) VALUES (?, ?, ?)')
    
    conector.execute(query, i)
    con.commit()

# ===============================================
# LEITURA DOS DADOS
def readData():
    conector = con.cursor()
    query = "SELECT * FROM carslist"
    
    conector.execute(query)
    data = conector.fetchall()
    return data

def readDataNames():
    conector = con.cursor()
    query = "SELECT DISTINCT nome FROM carslist"
    
    conector.execute(query)
    data = conector.fetchall()
    return data

# ===============================================
# ATUALIZAÇÃO DOS DADOS
def selectData(i):
    conector = con.cursor()
    query = f'SELECT * FROM carslist WHERE nome="{i}"'

    conector.execute(query)
    data = conector.fetchall()
    return data

def editData(new_nome, new_marca_do_carro, new_price, nome, marca_do_carro, price):
    conector = con.cursor()
    query = f'UPDATE carslist SET nome="{new_nome}", marca_do_carro="{new_marca_do_carro}", price="{new_price}" WHERE nome="{nome}" and marca_do_carro="{marca_do_carro}" and price="{price}"'

    conector.execute(query)
    con.commit()
    data = conector.fetchall()
    return data

# ===============================================
# EXCLUSÃO DO DADO SELECIONADO
def deleteData(nome):
    conector = con.cursor()
    query = f'DELETE FROM carslist WHERE nome="{nome}"'

    conector.execute(query)
    con.commit()