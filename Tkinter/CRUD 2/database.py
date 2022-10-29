import sqlite3 as lite

# ===============================================
# CONEXÃO COM SQLITE3
con = lite.connect("data/cadastro.db")

# ===============================================
# CRIAÇÃO DA TABELA
try:
    cur = con.cursor()
    cur.execute("""
        CREATE TABLE cadastro(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            codigo TEXT,
            nome TEXT,
            telefone TEXT,
            cidade TEXT
        )
        """)
except Exception as e:
    print(f"Falha ao criar a tabela: {e}")
else:
    print("Tabela criada com sucesso!")