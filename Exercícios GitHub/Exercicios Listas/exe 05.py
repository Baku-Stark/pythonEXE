'''
Faça um Programa que leia 20 números inteiros e armazene-os num vetor. 
Armazene os números pares no vetor PAR e os números IMPARES no vetor impar.
Imprima os três vetores. 
'''

numeros = []
numeros_pares = []
numeros_impares = []

for n in range(1, 21):
	num = int(input('Registre o {}° número \nr: '.format(n)))
	numeros.append(num)
	print('')
	if num % 2 == 0:
		numeros_pares.append(num)
	else:
		numeros_impares.append(num)
print('-=' *30)
print('RESULTADOS')
print('')
print('\a Vetor de números PARES:   {}'.format(numeros_pares))
print('\a Vetor de números IMPARES: {}'.format(numeros_impares))
print('')
print('>>> Todos os números armazenados: {}'.format(numeros))
print('-=' *30)
