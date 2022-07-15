'''
Uma fruteira está vendendo frutas com a seguinte tabela de preços: 

				        Até 5 Kg           		  Acima de 5 Kg
Morango         R$ 2,50 por Kg          R$ 2,20 por Kg

Maçã            R$ 1,80 por Kg          R$ 1,50 por Kg

	Se o cliente comprar mais de 8 Kg em frutas ou o valor total da compra ultrapassar 
	R$ 25,00, receberá ainda um desconto de 10% sobre este total. 
	Escreva um algoritmo para ler a quantidade (em Kg) de morangos e a quantidade (em Kg) 
	de maças adquiridas e escreva o valor a ser pago pelo cliente. 
'''

maca = int(input('Quantidade De Maçãs (KG) \nr: '))
print('')
print('-=' *30)
print('TOTAL:')
print('')
if maca <= 5:
	preco = maca * 1.80
	print('ATÉ 5 KG:')
	print('\a Preço Da Maçã: R${:.2f}'.format(preco))
else:
	preco = maca * 1.50
	print('ACIMA DE 5 KG:')
	print('\a Preço Da Maçã: R${:.2f}'.format(preco))
	print('')
	if maca > 8:
		print('RECEBEU 10% DE DESCONTO!!!')
		desconto = preco - (preco * 10 / 100)
		print('\a Preço Da Maçã (com desconto - peso): R${:.2f}'.format(desconto))
	elif preco > 25.0:
		print('RECEBEU 10% DE DESCONTO!!!')
		desconto = preco - (preco * 10 / 100)
		print('\a Preço Da Maçã (com desconto - acima de R$25,00): R${:.2f}'.format(desconto))
print('-=' *30)
print('')
print('')
print('')
morango = int(input('Quantidade De Morangos (KG) \nr: '))
print('')
print('-=' *30)
print('TOTAL:')
print('')
if morango <= 5:
	preco = morango * 2.50
	print('ATÉ 5 KG:')
	print('\a Preço Do MORANGO: R${:.2f}'.format(preco))
else:
	preco = morango * 2.20
	print('ACIMA DE 5 KG:')
	print('\a Preço Do MORANGO: R${:.2f}'.format(preco))
	print('')
	if morango > 8:
		print('RECEBEU 10% DE DESCONTO!!!')
		desconto = preco - (preco * 10 / 100)
		print('\a Preço Do MORANGO (com desconto - peso): R${:.2f}'.format(desconto))
	elif preco > 25.0:
		print('RECEBEU 10% DE DESCONTO!!!')
		desconto = preco - (preco * 10 / 100)
		print('\a Preço Do MORANGO (com desconto - acima de R$25,00): R${:.2f}'.format(desconto))
print('-=' *30)
