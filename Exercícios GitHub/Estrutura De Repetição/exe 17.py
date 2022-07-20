'''
Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16. 
'''

from time import sleep

while True:
	fatorial = int(input('\a Informe um número \nr: '))
	print('')
	while fatorial < 0 or fatorial > 16:
		print('[ERRO] Número fatorial negativo ou maior que 16!')
		sleep(1)
		fatorial = int(input('\a Informe um número \nr: '))
		print('')
	else:
		count_fator = fatorial
		print('')
		print('-=' *30)
		print('FATORIAL DE {}!'.format(fatorial))
		while count_fator > 1:
			count_fator = count_fator - 1
			fatorial = fatorial * count_fator
			print('{} > '.format(count_fator)),
		print('0')
		print('')
		print('\a Resultado: {} '.format(fatorial))
	print('-=' *30)
	print('')
