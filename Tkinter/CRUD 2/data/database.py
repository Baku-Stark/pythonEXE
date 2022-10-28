import sqlite3 as lite

# ===============================================
# CONEXÃO COM SQLITE3
con = lite.connect("data/database.db")

# ===============================================
# CRIAÇÃO DA TABELA
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE cadastro(id INTEGER PRIMARY KEY AUTOINCREMENT, codigo TEXT, nome TEXT, telefone TEXT, cidade TEXT)")