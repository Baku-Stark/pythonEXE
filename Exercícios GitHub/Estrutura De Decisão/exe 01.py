Faça um Programa que peça dois números e imprima o maior deles. 

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
print('')
if num1 > num2:
	print('{} é maior que {}'.format(num1, num2))
else:
	print('{} é maior que {}'.format(num2, num1))
