'''
Faça um programa que peça dois números, base e expoente, calcule e mostre o 
primeiro número elevado ao segundo número. 
Não utilize a função de potência da linguagem. 
'''

count = 1
potencia = 1

base = int(input('Registre a base \nr: '))
print('')
expo = int(input('Registre o expoente \nr: '))
print('')
while count <= expo:
	potencia *= base
	count += 1
print('')
print('Resultado: {}'.format(potencia))
