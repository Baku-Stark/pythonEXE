'''
Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação 
ele deseja realizar. 
O resultado da operação deve ser acompanhado de uma frase que diga se o número é:

    par ou ímpar;
    positivo ou negativo;
    inteiro ou decimal. 
'''

num1 = float(input('Digite o 1° número \nr: '))
print('')
num2 = float(input('Digite o 2° número \nr: '))
print('')
print('-=' *30)
print('RESULTADOS')
print('')
# Num 1
if num1 % 2 == 0:
	print('\a O número {} é PAR.'.format(num1))
else:
	print('\a O número {} é IMPAR.'.format(num1))

if num1 > 0:
	print('\a O número {} é POSITIVO.'.format(num1))
else:
	print('\a O número {} é NEGATIVO.'.format(num1))

if num1 % 1 == 0:
	print('\a O número {} é INTEIRO.'.format(num1))
else:
	print('\a O número {} é DECIMAL.'.format(num1))
print('')
# Num 2
if num2 % 2 == 0:
	print('\a O número {} é PAR.'.format(num2))
else:
	print('\a O número {} é IMPAR.'.format(num2))

if num2 > 0:
	print('\a O número {} é POSITIVO.'.format(num2))
else:
	print('\a O número {} é NEGATIVO.'.format(num2))

if num2 % 1 == 0:
	print('\a O número {} é INTEIRO.'.format(num2))
else:
	print('\a O número {} é DECIMAL.'.format(num2))
print('-=' *30)
