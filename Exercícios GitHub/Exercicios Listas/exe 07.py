'''
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a 
multiplicação e os números. 
'''

numeros = []
soma = 0
multi = 1

for x in xrange(1, 6):
	num = int(input('Registre o {}° número \nr: '.format(x)))
	print('')
	numeros.append(num)
	soma += num
	multi *= num
print('-=' *30)
print('Resultados')
print('')
print('\a Números Selecionados: {}'.format(numeros))
print('\a Soma total:    {}'.format(soma))
print('\a Multiplicação: {}'.format(multi))
print('-=' *30)
