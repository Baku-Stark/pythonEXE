'''Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento. 
'''
 
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento. 

num = float(input('Digite um número: '))
print('')
if num % 1 == 0:
	print('\f - Número Inteiro')
else:
	print('\f - Número Decimal')
