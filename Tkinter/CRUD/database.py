# ----------------------------------------
# Banco De Dados
import sqlite3 as lite

con = lite.connect('database/database.db')

# ----------------------------------------
# Tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulário(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, email TEXT, telefone TEXT, dia_em DATE, estado TEXT, assunto TEXT)")