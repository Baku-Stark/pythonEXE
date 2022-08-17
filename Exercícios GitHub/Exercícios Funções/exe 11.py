'''
Data com mês por extenso. Construa uma função que receba uma data no formato DD/MM/AAAA 
e devolva uma string no formato D de mesPorExtenso de AAAA. Opcionalmente, valide a data
e retorne NULL caso a data seja inválida. 
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
print('DATA DE NASCIMENTO:')
print('\a {}/{}/{}'.format(dia, mesExtenso(mes), ano))
