'''
Faça um Programa para um caixa eletrônico. 
O programa deverá perguntar ao usuário a valor do saque e depois informar quantas 
notas de cada valor serão fornecidas. 
As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. 
O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.

    Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100,
    uma nota de 50, uma nota de 5 e uma nota de 1;
    Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, 
    uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1. 
'''

print('-=' *30)
print('--- CAIXA ELETRÔNICO ---')
print('-=' *30)
print('')
saque = int(input('Valor De Saque (10 até 600) \nR$'))
saque_res = saque
print('')
if saque > 600:
	print('-=' *30)
	print('Não é possivel sacar essa quantia. Encerrando programa...')
	print('-=' *30)
else:
	print('-=' *30)
	# Notas de 100
	cem = int(saque / 100)
	saque = saque % 100

	# Notas de 50
	cinquenta = int(saque / 50)
	saque = saque % 50

	# Notas de 10
	dez = int(saque / 10)
	saque = saque % 10

	# Notas de 5
	cinco = int(saque / 5)
	saque = saque % 5
	
	# Nota de 1
	um = saque

	print('TOTAL:')
	print('')
	print('\a Notas R$100,00 = {}'.format(cem))
	print('\a Notas R$50,00  = {}'.format(cinquenta))
	print('\a Notas R$10,00  = {}'.format(dez))
	print('\a Notas R$5,00   = {}'.format(cinco))
	print('\a Notas R$1,00   = {}'.format(um))
	print('')
	print('--- Saque Do Cliente: R${:.2f}'.format(saque_res))
	print('-=' *30)
