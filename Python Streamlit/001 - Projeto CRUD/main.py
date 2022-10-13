# =============================================
# GRÁFICOS E PÁGINA WEB
import pandas as pd
import streamlit as st

# =============================================
# IMPORTAÇÕES IMPORTANTES
import sqlite3 as lite

con = lite.connect('database/database.db')

# =============================================
# FUNÇÕES

# ----- MOSTRAR USUÁRIOS
def readTable():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM client_users"
        cur.execute(query)
        info = cur.fetchall()
        for i in info:
            lista.append(i)
    return lista

def showTable():
    columnsTable = ['ID', 'Nome', 'Idade', 'Profissão']
    
    df = pd.DataFrame(data=readTable(), columns=columnsTable)
    df

# ----- INSERÇÃO
def inserirUser(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO client_users (users_name, users_age, users_profession) VALUES  (?, ?, ?)"
        cur.execute(query, i)

def createUser(name, age, ocu):
    nome = name
    idade = age
    profissao = ocu

    lista = [nome, idade, profissao]

    inserirUser(lista)
    showTable()

# ----- ATUALIZAR
def updateUser(i):
    pass
# ----- DELETAR
def deleteUser(i):
    pass

# =============================================
# FORMULÁRIO PRINCIPAL
st.title("Formulário do cliente")
st.write("_"*30)
with st.form("FORM_USER"):
    input_name = st.text_input(label="Insira o nome")
    
    input_ageU = st.number_input(label="Insira a idade", format="%d", step=1)

    ops = ["Professor", "Designer", "Desenvolvedor"]
    input_ocuP = st.selectbox("Selecione a sua profissão", ops)

    input_btnS = st.form_submit_button("Enviar")
st.write("_"*30)
# =============================================
# TABELA [mySQL -> Pandas]
st.title("Cliente Cadastrados")
showTable()
with st.form("FUNCTION_USER"):
    input_delete = st.form_submit_button("Deletar")
    input_update = st.form_submit_button("Atualizar")

# =============================================
# CHAMAR FUNÇÃO [button=TRUE]
if input_btnS:
    createUser(input_name, input_ageU, input_ocuP)

if input_delete:
    pass

if input_update:
    pass