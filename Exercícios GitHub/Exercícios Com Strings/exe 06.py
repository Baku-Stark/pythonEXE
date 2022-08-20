'''
Data por extenso. Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do 
usuário e imprima a data com o nome do mês por extenso.

    Data de Nascimento: 29/10/1973
    Você nasceu em  29 de Outubro de 1973.
'''

def mesExtenso(mes):
	lista_mes = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
	"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
	select = lista_mes[mes-1]
	return select


# ===
dia = int(input('Dia: '))
print('')
mes = int(input('Mês: '))
print('')
ano = int(input('Ano: '))
print('')
print('\a Data de nascimento: {}/{}/{}'.format(dia, mesExtenso(mes), ano))
