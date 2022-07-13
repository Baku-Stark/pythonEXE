Faça um Programa que leia três números e mostre o maior e o menor deles. 

num1 = float(input('Digite o 1° número: '))
print('')
num2 = float(input('Digite o 2° número: '))
print('')
num3 = float(input('Digite o 3° número: '))
print('')
print('-=' *30)
### MOSTRAR O MAIOR
if num1 > num2 and num1 > num3:
	print('\a O número {:.0f} é o maior'.format(num1))
elif num2 > num1 and num2 > num3:
	print('\a O número {:.0f} é o maior'.format(num2))
elif num3 > num1 and num3 > num2:
	print('\a O número {:.0f} é o maior'.format(num3))
print('')
### MOSTRAR O MENOR
if num1 < num2 and num1 < num3:
	print('\a O número {:.0f} é o menor'.format(num1))
elif num2 < num1 and num2 < num3:
	print('\a O número {:.0f} é o menor'.format(num2))
elif num3 < num1 and num3 < num2:
	print('\a O número {:.0f} é o menor'.format(num3))
print('-=' *30)
