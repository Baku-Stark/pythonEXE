import sqlite3 as lite

# ----------------------------------------
# CRUD
con = lite.connect('database/database.db')


# ----------------------------------------
# Inserir Informações
def insert(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulário (nome, email, telefone, dia_em, estado, assunto) VALUES (?, ?, ?, ?, ?, ?)"
        cur.execute(query, i)

# ----------------------------------------
# Acessar Informações
def acess():
    lista = []

    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulário"
        cur.execute(query)
        info = cur.fetchall()
        
        for i in info:
            lista.append(i)
        
    return lista

# ----------------------------------------
# Atualizar Informações
def update(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulário SET nome=? , email=?, telefone=?, dia_em=?, estado=?, assunto=? WHERE id=?"
        cur.execute(query, i)

# ----------------------------------------
# Deletar Informações
def delete(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulário WHERE id=?"
        cur.execute(query, i)