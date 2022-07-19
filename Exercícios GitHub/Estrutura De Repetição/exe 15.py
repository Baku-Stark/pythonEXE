'''
Faça um programa que, dado um conjunto de N números, determine o menor valor, 
o maior valor e a soma dos valores. 
'''

numeros = []
count = 0
numero_soma = 0

while True:
	num = int(input('\a Registre um número \nr: '))
	numero_soma += num
	count += 1
	numeros.append(num) 
	print('')
	res = str(input('\a Deseja registrar outro número? \nr: ')).upper()
	if res == "NÃO" or res == "NAO":
		print('')
		break
	else:
		print('-' *30)
		print('')
print('-=' *30)
print('Lista Do Usuário:')
count -= 1
print('')
print('Números: {}'.format(numeros))
numeros.sort() #tornou os números na ordem crescente
print('\a O menor número: {}'.format(numeros[0]))
print('\a O maior número: {}'.format(numeros[count]))
print('\a Soma de todos os números: {}'.format(numero_soma))
print('-=' *30)
