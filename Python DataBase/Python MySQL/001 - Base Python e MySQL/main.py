import mysql.connector

con = mysql.connector.connect(
    host = 'localhost',
    user = '---',
    password = '---',
    database = 'bdyoutube'
)

cursor = con.cursor()


# =============================================
# CREATE
res_produto = str(input("Registre o nome do produto \nr: ")).capitalize()
print('')
res_valor = int(input("Registre o valor do produto \nr: "))
print('')

nome_produto = res_produto
valor = res_valor
comando = f'INSERT INTO vendas (nome_produto, valor) VALUES ("{nome_produto}", {valor})'
cursor.execute(comando)
con.commit() # EDITAR O BANCO DE DADOS

print('\033[36m(Commit Realizado!)\033[m')
print('=' *45)

# =============================================
# READ
comando = 'SELECT * FROM vendas'
cursor.execute(comando)
valores = cursor.fetchall()
for n in valores:
    print(f"{n}\n")

print('\033[32m(Leitura Realizada!)\033[m')
print('=' *45)

# =============================================
# UPDATE
set_update = str(input("Deseja atualizar algum valor? [S/N] \nr: ")).upper()
print('')
if set_update == "S":
    nome_produto = str(input("Registre o nome do produto \nr: ")).capitalize()
    print('')
    novo_valor = int(input("Registre o NOVO valor do produto \nr: "))

    comando = f'UPDATE vendas SET valor = {novo_valor} WHERE nome_produto = "{nome_produto}"'

    cursor.execute(comando)
    con.commit()

    print('\033[33m(Atualização Realizada!)\033[m')
else:
    print("\033[31m[AVISO!] - Nenhuma atualização foi solicitada pelo usuário.\033[m")
print('=' *45)

# =============================================
# DELETE
set_delete = str(input("Deseja deletar algum valor? [S/N] \nr: ")).upper()
print('')
if set_delete == "S":
    nome_produto = str(input("Registre o nome do produto \nr: ")).capitalize()

    comando = f'DELETE FROM vendas WHERE nome_produto = "{nome_produto}"'
    cursor.execute(comando)
    con.commit()
    print('\033[34m(Função Delete Realizada!)\033[m')
else:
    print("\033[31m[AVISO!] - Nenhum tópico foi excluído pelo usuário.\033[m")
print('=' *45)

cursor.close()
con.close()
