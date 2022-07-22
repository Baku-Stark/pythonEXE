'''
O cardápio de uma lanchonete é o seguinte:

    Especificação   Código  Preço
    Cachorro Quente 100     R$ 1,20
    Bauru Simples   101     R$ 1,30
    Bauru com ovo   102     R$ 1,50
    Hambúrguer      103     R$ 1,20
    Cheeseburguer   104     R$ 1,30
    Refrigerante    105     R$ 1,00

Faça um programa que leia o código dos itens pedidos e as quantidades desejadas. 
Calcule e mostre o valor a ser pago por item (preço * quantidade) e o total geral do 
pedido. Considere que o cliente deve informar quando o pedido deve ser encerrado. 
'''

produto = ''
linha = '=' * 41
linha_div = '-' *42
valor_produto = 0
count_produto = 0
count_somado = 0

def clear():
	print('\n' * 10)

print(linha)
print('''
  Especificação   Código  Preço
----------------------------------
\a Cachorro Quente 100     R$ 1,20
\a Bauru Simples   101     R$ 1,30
\a Bauru com ovo   102     R$ 1,50
\a Hambúrguer      103     R$ 1,20
\a Cheeseburguer   104     R$ 1,30
\a Refrigerante    105     R$ 1,00
''')
print(linha)
print('')
while True:
	print(linha_div)
	# Seleção do produto
	cod = int(input('\a Escolha o código do produto \nr: '))
	print('')
	while cod > 105 or cod < 100:
		print('[ERRO] Produto não catalogado! ')
		cod = int(input('\a Escolha o código do produto \nr: '))
		print('')
	# -----SISTEMA DE SELEÇÃO-----
	if cod == 100:
		produto = 'Cachorro Quente'
		qtd = int(input('Quantidade de {} \nr: '.format(produto)))
		valor_produto = 1.20 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')

	elif cod == 101:
		produto = 'Bauru Simples'
		qtd = int(input('Quantidade de {} \nr: '.format(produto)))
		valor_produto = 1.30 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')

	elif cod == 102:
		produto = 'Bauru com ovo'
		qtd = int(input('Quantidade de {} \nr: '.format(produto)))
		valor_produto = 1.50 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')

	elif cod == 103:
		produto = 'Hambúrguer'
		qtd = int(input('Quantidade de {} \nr: '.format(produto)))
		valor_produto = 1.20 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')

	elif cod == 104:
		produto = 'Cheeseburguer'
		qtd = int(input('Quantidade de {} \nr: '.format(produto, valor_produto)))
		valor_produto = 1.30 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')

	elif cod == 105:
		produto = 'Refrigerante'
		qtd = int(input('Quantidade de {} \nr: '.format(produto)))
		valor_produto = 1.00 * qtd
		print('')
		print('\a {} UNI de {} = R${:.2f}'.format(qtd, produto, valor_produto))
		print('')
	# -----SISTEMA DE RESPOSTA-----
	select = str(input('DESEJA CONTINUAR? [ S ] - SIM | [ N ] - NÃO \nr: ')).upper()
	print('')
	if select == 'NAO' or select == 'NÃO':
		count_produto += valor_produto
		print(linha_div)
		break
	elif select == 'SIM':
		count_produto += valor_produto
		count_somado += count_produto
		continue
	else:
		while select != 'SIM' and select != 'NAO' and select != 'NÃO':
			print('[ERRO] Seleção inválida!')
			select = str(input('DESEJA CONTINUAR? [ S ] - SIM | [ N ] - NÃO \nr: ')).upper()
			print('')
clear()
print(linha)
if select == 'NAO' or select == 'NÃO':
	print('TOTAL A PAGAR: R${:.2f}'.format(count_produto))
elif select == 'SIM':
	print('TOTAL A PAGAR: R${:.2f}'.format(count_somado))
print(linha)
