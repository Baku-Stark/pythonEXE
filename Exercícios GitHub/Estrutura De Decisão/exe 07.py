Faça um programa que pergunte o preço de três produtos e informe qual produto 
você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

def preco_Produto(ptd, ptd2, ptd3):
	print('')
	if ptd < ptd2 and ptd < ptd3:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd))
	elif ptd2 < ptd and ptd2 < ptd3:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd2))
	elif ptd3 < ptd and ptd3 < ptd2:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd3))


###
ptd_1 = float(input('Preço Do 1° Produto \nr: '))
ptd_2 = float(input('Preço Do 2° Produto \nr: '))
ptd_3 = float(input('Preço Do 3° Produto \nr: '))
preco_Produto(ptd_1, ptd_2, ptd_3)
