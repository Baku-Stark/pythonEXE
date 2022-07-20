'''
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a 
metodologia da tabelinha, que já é um sucesso na sua loja de 1,99. 
Você foi contratado para desenvolver o programa que monta a tabela de preços de pães, 
de 1 até 50 pães, a partir do preço do pão informado pelo usuário, conforme o exemplo 
abaixo: 

Preço do pão: R$ 0.18
Panificadora Pão de Ontem - Tabela de preços
1 - R$ 0.18
2 - R$ 0.36
...
50 - R$ 9.00
'''

linha = '=' *40
local = 'PADARIA TABAJARA'

print(linha)
print(local.ljust(40))
print('')
for a in range(1, 10):
	valor = 0.18 * a
	print('{:2>} -  R${:.2f}'.format(a, valor))
for b in range(10, 51):
	valor_2 = 0.18 * b
	print('{:2>} - R${:.2f}'.format(b, valor_2))
print(linha)
