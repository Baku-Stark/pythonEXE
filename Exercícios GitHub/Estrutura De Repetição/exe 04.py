'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50. 
'''

# Imprimir Números Impares
for x in xrange(1, 51, 2):
		print('{} \n'.format(x))

# Imprimir Números Pares:
for x in xrange(1, 51):
	if x % 2 == 0:
		print('{} \n'.format(x))
