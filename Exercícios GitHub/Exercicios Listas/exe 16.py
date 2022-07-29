'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores 
com base em comissões. O vendedor recebe $200 por semana mais 9 por cento de suas vendas 
brutas daquela semana. Por exemplo, um vendedor que teve vendas brutas de $3000 em uma 
semana recebe $200 mais 9 por cento de $3000, ou seja, um total de $470. Escreva um 
programa (usando um array de contadores) que determine quantos vendedores receberam 
salários nos seguintes intervalos de valores: 

	$200 - $299
	$300 - $399
	$400 - $499
	$500 - $599
	$600 - $699
	$700 - $799
	$800 - $899
	$900 - $999
	$1000 em diante


Desafio: Crie uma fórmula para chegar na posição da lista a partir do salário, 
sem fazer vários ifs aninhados. 
'''

# Fórmula
porcentagem = 3000 - (3000 * 9 / 100)
multi = 200 * 1
media = 3000 - porcentagem
res = 200 + media
print(res) #470


# ====== PROGRAMA COM IFs ANINHADOS ======
from time import sleep

# Dados
c = 1
count_duz = 0
count_tre = 0
count_qua = 0
count_qui = 0
count_sex = 0
count_set = 0
count_oct = 0
count_nin = 0
count_max = 0

while True:
	# ---
	print('{}° EMPREGADO'.format(c))
	c += 1
	venda_bruta = float(input('\a Registre o valor da venda bruta \nr: '))
	print('')
	semana = int(input('\a Registre a quantidade de semana de vendas \nr: '))
	print('-' *40)
	print('')

	porcentagem = venda_bruta - (venda_bruta * 9 / 100)
	multi = 200 * semana
	media = venda_bruta - porcentagem
	res = multi + media

	if multi == 200 and multi <= 299:
		count_duz += 1

	elif multi == 300 and multi <= 399:
		count_tre += 1

	elif multi == 400 and multi <= 499:
		count_qua += 1

	elif multi == 500 and multi < 599:
		count_qui += 1

	elif multi == 600 and multi < 699:
		count_sex += 1

	elif multi == 700 and multi < 799:
		count_set += 1

	elif multi == 800 and multi < 899:
		count_oct += 1

	elif multi == 900 and multi < 999:
		count_nin += 1

	elif multi > 1000:
		count_max += 1

	else:
		print('=== PROGRAMA SENDO ENCERRADO ===')
		print('')
		sleep(2)
		break

print('-=' *30)
print('Resultados')
print('')
print(' Qtd de Trabalhadores {:>5} Tabela'.format(" "))
print('-' *40)
print('{:>10} {:>15} {}'.format(count_duz, " ", 'R$200 - R$299'))
print('{:>10} {:>15} {}'.format(count_tre, " ", 'R$300 - R$399'))
print('{:>10} {:>15} {}'.format(count_qua, " ", 'R$400 - R$499'))
print('{:>10} {:>15} {}'.format(count_qui, " ", 'R$500 - R$599'))
print('{:>10} {:>15} {}'.format(count_sex, " ", 'R$600 - R$699'))
print('{:>10} {:>15} {}'.format(count_set, " ", 'R$700 - R$799'))
print('{:>10} {:>15} {}'.format(count_oct, " ", 'R$800 - R$899'))
print('{:>10} {:>15} {}'.format(count_nin, " ", 'R$900 - R$999'))
print('{:>10} {:>15} {}'.format(count_max, " ", 'R$1000 adiante'))
print('-=' *30)
