'''
Faça um programa para imprimir:

        1
        1   2
        1   2   3
        .....
        1   2   3   ...  n

para um n informado pelo usuário. Use uma função que receba um valor n inteiro imprima 
até a n-ésima linha. 
'''

def num_Crescente(n: int):
	for linha in xrange(1, n + 1):
		for coluna in xrange(1, linha +1):
			print(coluna, end= '   ')
		print('')


# ---
print('Triângulo com 1')
num_Crescente(1)
print('Triângulo com 2')
num_Crescente(2)
print('Triângulo com 3')
num_Crescente(3)
