'''
Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro 
fornecido pelo usuário. O programa deverá mostrar também o número de divisões que ele 
executou para encontrar os números primos. Serão avaliados o funcionamento, o estilo 
e o número de testes (divisões) executados. 

'''

primo = False
count = 1

num = int(input('\a Informe um número \nr: '))
print('')
print('-=' *30)
print('RESULTADO')
print('')
if num == 1 or num == 2:
	print('\a O número {} é primo e 0 divisões foram executadas.'.format(num))

elif num % 2 == 0:
	print('\a {} não é um número primo e foi executada uma divisão para descobrir isso.'
		.format(num))

else:
	primo = True
	for n in xrange(3, num, 2):
		count += 1
		if num % n == 0:
			primo = False
			break
	if primo:
		print('\a {} é um número primo e foram executadas {} divisões para provar isso.'
			.format(num, count))
	
	else:
		print('\a {} não é um número primo e foram executadas {} divisões para provar isso.'
			.format(num, count))
print('-=' *30)
