Faça um Programa que peça um número inteiro e determine se ele é par ou impar. 
Dica: utilize o operador módulo (resto da divisão). 

num = int(input('Escolha um número: '))
print('')
if num % 2 == 0:
	print('O número {} é PAR.'.format(num))
else:
	print('O número´{} é ÍMPAR.'.format(num))
