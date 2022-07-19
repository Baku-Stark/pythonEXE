'''
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de 
números pares e a quantidade de números impares. 
'''

pares = []
impares = []
count_par = 0
count_imp = 0

for x in xrange(1, 11):
	num = int(input('Digite o {}° número \nr: '.format(x)))
	if num % 2 == 0:
		pares.append(num)
		count_par += 1
	else:
		impares.append(num)
		count_imp += 1
	print('')
print('-=' *30)
print('\a Todos os números pares são:  {}'.format(pares))
print('\a Quantidade de números pares: {}'.format(count_par))
print('')
print('\a Todos os números impares são:  {}'.format(impares))
print('\a Quantidade de números impares: {}'.format(count_imp))
print('-=' *30)
