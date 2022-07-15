'''
Um posto está vendendo combustíveis com a seguinte tabela de descontos: 

	Álcool:
	até 20 litros, desconto de 3% por litro
	acima de 20 litros, desconto de 5% por litro

	Gasolina:
	até 20 litros, desconto de 4% por litro
	acima de 20 litros, desconto de 6% por litro 

	Escreva um algoritmo que leia o número de litros vendidos, 
	o tipo de combustível (codificado da seguinte forma: A-álcool, G-gasolina), 
	calcule e imprima o valor a ser pago pelo cliente sabendo-se que o preço do 
	litro da gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90. 
'''

combustivel = int(input('''Tipo Do Abastecimento
[ 1 ] - Álcool
[ 2 ] - Gasolina

r: '''))
print('')
print('-=' *30)
print('   POSTO IPIRANGA   ')
print('')
print('RESULTADO: ')
# Álcool R$1,90
if combustivel == 1:
	litros = float(input('Quantos litros de Álcool? \nr: '))
	print('')
	if litros <= 20.0:
		a_alcool = litros * 1.90
		preco = a_alcool - (a_alcool * 3 / 100)
		print('\a Total A Pagar: R${:.2f}'.format(preco))
	elif litros > 20.0:
		a_alcool = litros * 1.90
		preco = a_alcool - (a_alcool * 5 / 100)
		print('\a Total A Pagar: R${:.2f}'.format(preco))

# Gasolina R$2,50
elif combustivel == 2:
	litros = float(input('Quantos litros de Gasolina? \nr: '))
	print('')
	if litros <= 20.0:
		g_gasolina = litros * 2.50
		preco = g_gasolina - (g_gasolina * 4 / 100)
		print('\a Total A Pagar: R${:.2f}'.format(preco))
	elif litros > 20.0:
		g_gasolina = litros  * 2.50
		preco = g_gasolina - (g_gasolina * 6 / 100)
		print('\a Total A Pagar: R${:.2f}'.format(preco))

# N.D.O
else:
	print('Nenhuma opção foi selecionada. Até mais!')
print('-=' *30)
