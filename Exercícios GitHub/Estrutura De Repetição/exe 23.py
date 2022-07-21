'''
O Sr. Manoel Joaquim possui uma grande loja de artigos de R$ 1,99, com cerca de 10 caixas. 
Para agilizar o cálculo de quanto cada cliente deve pagar ele desenvolveu um tabela 
que contém o número de itens que o cliente comprou e ao lado o valor da conta. 
Desta forma a atendente do caixa precisa apenas contar quantos itens o cliente está 
levando e olhar na tabela de preços. Você foi contratado para desenvolver o programa 
que monta esta tabela de preços, que conterá os preços de 1 até 50 produtos, conforme 
o exemplo abaixo: 
'''

linha = '=' *40
local = 'LOJAS QUASE DOIS - TABELA DE PREÇOS'

print(linha)
print(local.ljust(40))
print('')
for a in range(1, 10):
	valor = 1.99 * a
	print('{:2>} -  R${:.2f}'.format(a, valor))
for b in range(10, 51):
	valor_2 = 1.99 * b
	print('{:2>} - R${:.2f}'.format(b, valor_2))
print(linha)
