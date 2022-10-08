from cProfile import label
import streamlit as st

st.title("Formulário do cliente")

with st.form(key="include_cliente"):
    input_name = st.text_input(label="Insira o nome")
    input_ageU = st.number_input(label="Insira a idade", format="%d", step=1)
    input_ocuP = st.selectbox("Selecione a sua profissão", ("Professor", "Designer", "Desenvolvedor"))
    input_btnS = st.form_submit_button("Enviar")

if input_btnS:
    st.write(f"Nome: {input_name}")
    st.write(f"Idade: {input_ageU}")
    st.write(f"Ocupação: {input_ocuP}")