'''
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... 
Faça um programa que gere a série até que o valor seja maior que 500
'''

termo = 0
count = 3
ultimo = 1
penultimo = 1


while True:
	termo = ultimo + penultimo
	penultimo = ultimo
	ultimo = termo
	count += 1
	if termo > 500:
		maior = termo
		break
	print('{} '.format(termo)),
print('{}'.format(maior)),
