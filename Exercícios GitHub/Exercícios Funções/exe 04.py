'''
Faça um programa, com uma função que necessite de um argumento. A função retorna o valor de 
caractere ‘P’, se seu argumento for positivo, e ‘N’, se seu argumento for zero ou negativo. 
'''

def check(num):
	if num >= 0:
		print('\a "P" -> Número Positivo.')
	else:
		print('\a "N" -> Número Negativo.')


# --
num = int(input('Escolha um número \nr: '))
print('')
check(num)
