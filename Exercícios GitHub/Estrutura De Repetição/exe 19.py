'''
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. 
Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:

Fatorial de: 5
5! =  5 . 4 . 3 . 2 . 1 = 120 
'''

num = int(input('\a Escolha um número para fazer o fatorial \nr: '))
count_fator = num
print('')
print('-=' *30)
print('FATORIAL DE {}!'.format(num))
print('')
print('{}! = '.format(num)),
for x in xrange(num, 0, -1):
	print('{} > '.format(x)),
print('0')
while count_fator > 1:
		count_fator = count_fator - 1
		num = num * count_fator
print('\a Resultado: {}'.format(num))
print('-=' *30)
