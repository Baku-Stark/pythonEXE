import streamlit as st

st.write("""
# Olá, *mundo!*
# Minha primeira aplicação com o Streamlit!!!""")

# ================================================
# TEXTBOX
input_name = st.text_input(label="Insira o nome")
st.write(f"Seja bem-vindo ao Streamlit, {input_name}!")

# ================================================
# NUMBERBOX
input_ageU = st.number_input(label="Insira a idade", format="%d", step=1)
st.write(f"O usuário possui {input_ageU} anos!")

# ================================================
# CAIXA DE SELEÇÃO
input_ocuP = st.selectbox("Selecione a sua profissão", ("Professor", "Designer", "Desenvolvedor"))
st.write(f"A profissão do usuário é: {input_ageU}")

# ================================================
# SUBMIT BUTTON
input_btnS = st.button("Enviar")

# ================================================
# SLIDER DE NÚMERO (0 até 100)
num = st.slider("Escolha um número", 0, 100)
st.write(f"O número escolhi foi o: {num}")

# ================================================
# UPLOAD DE ARQUIVO
file = st.file_uploader("Envie o arquivo")

# ================================================
# SELEÇÃO DE CORES
cor = st.color_picker("Escolha uma cor", "#111111")
st.write(f"A cor escolhida foi: {cor}")

# ================================================
# RADIOBUTTON
pet = st.radio("Escolha um animal", ("Papagaio", "Leão", "Coruja"))
st.write(f"O pet escolhido foi: {pet}")

# ================================================
# CALENDÁRIO
date = st.date_input("Escolha uma data")
st.write(f"A data selecionada: {date}")