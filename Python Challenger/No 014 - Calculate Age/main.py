from datetime import datetime


def calcularIdade():
    data_atual = datetime.now()
    ano_atual = data_atual.year

    nome_usuario = str(input('Qual o seu nome?\nr : '))
    if nome_usuario == "":
        nome_usuario = "Nome não informado"
    print('')
    diaUser = int(input('   -> Dia do seu nascimento : '))
    mesUser = int(input('   -> Mês do seu nascimento : '))
    anoUser = int(input('   -> Ano do seu nascimento : '))
    print(f'   -> Data de nascimento : \033[36m{diaUser}/{mesUser}/{anoUser}\033[m')

    #Calculo positivo para a idade
    idadeUser = ano_atual - anoUser
    if idadeUser < 0:
        idadeUser *= -1

    diaVivid = idadeUser * 365
    mesVivid = idadeUser * 12

    print('-' *60)
    print(f'Dados de {nome_usuario}\nIdade: {idadeUser}anos\nMeses: {mesVivid} meses\nDias: {diaVivid} dias')
    print('-' *60)


# =====
if __name__ == '__main__':
    calcularIdade()