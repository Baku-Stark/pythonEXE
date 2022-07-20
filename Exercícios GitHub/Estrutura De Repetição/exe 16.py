'''
Altere o programa anterior para que ele aceite apenas números entre 0 e 1000. 
'''

numeros = []
numero_soma = 0
count = 0


while True:
	num = int(input('\a Registre um número entre 0 e 1000 \nr: '))
	if num < 0 or num > 1000:
		while num < 0 or num > 1000:
			print('')
			print('[ERRO] O número não pode ser registrado')
			num = int(input('\a Por favor, registre um número entre 0 e 1000 \nr: '))
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
