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
# ----- INSERÇÃO
def inserirUser(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO client_users (users_name, users_age, users_profession) VALUES (?, ?, ?)"
        cur.execute(query, i)

def createUser(name, age, ocu):
    nome = name
    idade = age
    profissao = ocu

    lista = [nome, idade, profissao]

    inserirUser(lista)
    showTable()

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
    st.table(df)

# ----- DELETAR
def deleteUser(i):
    pass

# ----- ATUALIZAR
def updateUser(i):
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

    input_btnS = st.form_submit_button("Enviar Registro")
    btn_spaceDelete_function = st.form_submit_button("Excluir")
    btn_spaceUpdate_function = st.form_submit_button("Atualizar")
st.write("_"*30)
# =============================================
# TABELA [mySQL -> Pandas]
st.title("Cliente Cadastrados")
showTable()

# =============================================
# CHAMAR FUNÇÃO [button=TRUE]
if input_btnS:
    createUser(input_name, input_ageU, input_ocuP)

if btn_spaceDelete_function:
    btn_spaceDelete_function = st.button("Excluído")
    deleteUser(btn_spaceDelete_function)

if btn_spaceUpdate_function:
    btn_spaceUpdate_function = st.button("Atualizado")
    updateUser(btn_spaceUpdate_function)