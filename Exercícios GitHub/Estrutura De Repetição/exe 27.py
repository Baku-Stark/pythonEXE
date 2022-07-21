'''
O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora possui uma loja de conveniências.
Faça um programa que implemente uma caixa registradora rudimentar.
O programa deverá receber um número desconhecido de valores referentes aos preços das mercadorias.
Um valor zero deve ser informado pelo operador para indicar o final da compra.
O programa deve então mostrar o total da compra e perguntar o valor em dinheiro que o cliente forneceu,
para então calcular e mostrar o valor do troco. Após esta operação, o programa deverá voltar ao ponto inicial,
para registrar a próxima compra.
'''

loja = 'LOJAS TABAJARA'
linha = '-' *40

def barra():
	print('\n' *3)

def clear():
	print('\n' * 10)

while True:
	print(linha)
	print(loja.center(40))
	print('')
	n = 1
	total = 0

	while True:
		preco = float(input('Preço do {}° produto: \nR$'.format(n)))
		print('')
		n += 1
		total += preco
		if preco == 0:
			break
	clear()
	print(linha)
	print('Total: R${:.2f}'.format(total))
	print('')
	pagamento = float(input('Pagamento \nR$'))
	print('')
	while pagamento < total:
		print('---- Pagamento Inválido!!!')
		pagamento = float(input('Refaça o pagamento \nR$'))
		print('')
		if pagamento >= total:
			troco = pagamento - total
	barra()
	print('\a Troco: R${:.2f}'.format(troco))
	print(linha)
	print('')
	print('Pressione "0" para resetar | "1" para encerrar')
	select = int(input('r: '))
	if select == 0:
		clear()
		continue
	else:
		clear
		print('Encerrando caixa registradora...')
		break
