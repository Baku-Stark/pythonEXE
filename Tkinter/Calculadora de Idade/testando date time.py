from datetime import datetime

tempo = datetime.now()
dia = tempo.day
mes = tempo.month
ano = tempo.year

if mes < 10:
    print(f'Data atual: {dia}/0{mes}/{ano}')
else:
    print(f'Data atual: {dia}/0{mes}/{ano}')


idade = ano - 2000
meses = mes - 7
dias = dia - 7


print(f"Você tem {idade} anos {meses} meses {dias} dias")