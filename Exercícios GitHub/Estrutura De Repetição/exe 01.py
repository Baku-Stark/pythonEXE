'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário 
informe um valor válido. 
'''

while True:
	num = int(input('Digite um número entre 0 e 10 \nr: '))
	print('')
	if num >= 0 and num <= 10:
		print('\a Número Escolhido Pelo Usuário: {}'.format(num))
		print('')
		print('>>> Encerrando programa!')
		break
	elif num < 0 or num > 10:
		print('\a Valor Inválido! Faça o processo de novo!')
		print('-=' *25)
		print('')
	else:
		print('\a Valor Inválido! Faça o processo de novo!')
		print('-=' *25)
		print('')
