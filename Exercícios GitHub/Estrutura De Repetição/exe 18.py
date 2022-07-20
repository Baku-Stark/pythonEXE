'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
'''

'''
Faça um programa que peça um número inteiro e determine se ele é ou não um número primo. 
Um número primo é aquele que é divisível somente por ele mesmo e por 1. 
'''

div = []
count = 0

num = int(input('\a Informe um número \nr: '))
print('')
for x in range(num):
	if num % (x+1) == 0:
		count += 1
		div.append(x + 1)

	else:
		count += 2
		
if count == 2:
	print('--- O número {}: É um número PRIMO'.format(num))
	print('Ele é divisível por {}'.format(div))
else:
	print('--- O número {}: Não um número PRIMO'.format(num))
	print('Ele é divisível por {}'.format(div))
