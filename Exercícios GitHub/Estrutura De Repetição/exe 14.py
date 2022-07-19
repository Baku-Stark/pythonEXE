'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120 
'''

import sys
count_fator = 0
resultado = 1
count = 1

fatorial = int(input('Escolha o fatorial \nr: '))

print('')
print('-=' *30)
print('FATORIAL DE {}!'.format(fatorial))
print('')
while count <= fatorial:
	count_fator += 1 
	resultado *= count
	count += 1
	print('{} > '.format(count_fator)),
sys.stdout.write('FIM!')
print('')
print('')
print('\a Resultado: {}'.format(resultado))
print('-=' *30)
