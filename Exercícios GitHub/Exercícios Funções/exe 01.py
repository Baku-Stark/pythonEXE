'''
Faça um programa para imprimir: 

    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima 
até a n-ésima linha. 
'''

def prog(num):
	for n in range(num):
		n += 1
		print('{} '.format(str(n)*n))


# ---
num = int(input('Escolha um número \nr: '))
print('')
prog(num)
