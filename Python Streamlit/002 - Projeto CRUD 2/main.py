# ===============================================
# PANDAS
import pandas as pd

# ===============================================
# Data Viz Pkgs
import plotly.express as px

# ===============================================
# STREAMLIT
import streamlit as st
import streamlit.components.v1 as stc
# ----- CRUD FUNCTIONS
from dbfunction import *

with open("_css/style.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)

# ===============================================
# SITE
def main():
    st.title("Sistema De Cadastro (CRUD)")
    st.write("_" *30)
    
    menu = ["Novo Registro", "Visualizar", "Atualizar", "Deletar", "Sobre o projeto"]
    choice = st.sidebar.selectbox("Menu", menu)
    create_table()

    # ===============================================
    # CRIAÇÃO DE UM NOVO REGISTRO
    if choice == "Novo Registro":
        st.subheader("Adicionar um novo registro de veículo")
        st.info("Adicione as informações EXATAS de seu veículo.")
        col1, col2 = st.columns(2)

        with col1:
            input_name = st.text_input(label="Nome Do Veículo", placeholder="GTR, Palio...")

        with col2:
            ops = ("NISSAN", "BMW", "FIAT", "AUDI", "Chevrolet", "Outros")
            select_box = st.selectbox(label="Marca Do Veículo", options=ops)

            price = st.number_input(label="Insira o valor", format="%d", step=1)

        if st.button("Fazer Registro"):
            if input_name == "":
                st.warning("Você precisa inserir o nome do veículo!")
            
            elif price < 0:
                st.warning("O valor de PREÇO é inválido! Por favor, insira um valor aceitável...")
            
            else:
                lista = [input_name, select_box, price]
                insert(lista)
                st.success(f"O registro do novo veículo {input_name} foi adicionado com sucesso!")
    
    # ===============================================
    # LEITURA DO REGISTRO
    elif choice == "Visualizar":
        st.info("Acesse as informações:")
        with st.expander("Leitura De Dados"):
            result = readData()
            clean_df = pd.DataFrame(result, columns=["ID", "Nome Do Veículo", "Marca Do Veículo", "Preço"])
            st.dataframe(clean_df)

        with st.expander("Banco De Dados"):
            task_df = clean_df['Marca Do Veículo'].value_counts().to_frame()
            task_df = task_df.reset_index()
            st.dataframe(task_df)

            p1 = px.pie(task_df, names='index', values='Marca Do Veículo')
            st.plotly_chart(p1, use_container_width=True)

    # ===============================================
    # ATUALIZAÇÃO DE REGISTRO
    elif choice == "Atualizar":
        st.subheader("Atualizar Registro")
        st.info("Atualizar informações do seu registro.")

        with st.expander("Dados Atuais"):
            result = readData()
            clean_df = pd.DataFrame(result, columns=["ID", "Nome Do Veículo", "Marca Do Veículo", "Preço"])
            st.dataframe(clean_df)

        list_ops = [i[0] for i in readDataNames()]
        select_ops = st.selectbox(label="Selecione o modelo do carro", options=list_ops)
        result_ops = selectData(select_ops)

        if result_ops:
            nome = result_ops[0][1]
            marca_do_carro = result_ops[0][2]
            price = result_ops[0][3]

            col1, col2 = st.columns(2)

            with col1:
                new_nome = st.text_input(label="Nome do veículo", placeholder="GTR, Palio...", value=nome)

            with col2:
                ops = ("NISSAN", "BMW", "FIAT", "AUDI", "Chevrolet", "Outros")
                new_marca_do_carro = st.selectbox(label="Marca do veículo", options=ops)

                new_price = st.number_input(label=f'Novo valor do {marca_do_carro}-{nome}', format="%d", step=1, value=int(price))
            
            if st.button("Atualizar Registro"):
                editData(new_nome, new_marca_do_carro, new_price, nome, marca_do_carro, price)
                st.success(f"O registro do veículo {nome} foi atualizado com sucesso!")
            
            with st.expander("Dados Atualizados"):
                result = readData()
                clean_df = pd.DataFrame(result, columns=["ID", "Nome Do Veículo", "Marca Do Veículo", "Preço"])
                st.dataframe(clean_df)
    
    # ===============================================
    # DELETAR REGISTRO
    elif choice == "Deletar":
        st.subheader("Deletar")
        st.info("Deletar informações do seu registro.")

        with st.expander("Dados Atuais"):
            result = readData()
            clean_df = pd.DataFrame(result, columns=["ID", "Nome Do Veículo", "Marca Do Veículo", "Preço"])
            st.dataframe(clean_df)
        
        unique_list = [i[0] for i in readDataNames()]
        delete_select = st.selectbox(label="Escolha o veículo para excluir do banco de dados", options=unique_list)

        if st.button("Deletar"):
            deleteData(delete_select)
            st.warning(f"O {delete_select} foi excluído do banco de dados!")
        
        with st.expander("Dados Atualizados"):
                result = readData()
                clean_df = pd.DataFrame(result, columns=["ID", "Nome Do Veículo", "Marca Do Veículo", "Preço"])
                st.dataframe(clean_df)

                st.success(f"O registro do veículo {nome} foi excluido com sucesso!")

    # ===============================================
    # SOBRE A APLICAÇÃO
    elif choice == "Sobre o projeto":
        st.subheader("Sobre o Projeto")
        st.info("Criador: Baku-Stark")
        st.subheader("Redes Sociais")
        st.write("GitHub: https://github.com/Baku-Stark")
        st.write("Twitter: https://twitter.com/Walleemc2")
        st.write("Instagram: https://www.instagram.com/wallace_emc2/")

# ===============================================
# ATIVAR APLICAÇÃO
if __name__ == '__main__':
    main()