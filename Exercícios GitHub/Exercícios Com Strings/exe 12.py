'''
Valida e corrige número de telefone. Faça um programa que leia um número de telefone, 
e corrija o número no caso deste conter somente 7 dígitos, acrescentando o '3' na frente. 
O usuário pode informar o número com ou sem o traço separador.

	Valida e corrige número de telefone
	Telefone: 461-0133
	Telefone possui 7 dígitos. Vou acrescentar o digito três na frente.
	Telefone corrigido sem formatação: 34610133
	Telefone corrigido com formatação: 3461-0133
'''


num_tel = str(input('Registre o número de telefone \nr: ')).strip()
print('')
if len(num_tel) < 7:
	print('Número de telefone inválido!')
	print('\a Quantidade de digitos menor que o necessário para correção.')

elif len(num_tel) == 7:
	print('O número de telefone deve possuir 7 digitos. Acrescentando o digito 3 na frente.')
	print('Telefone: 3{}-{}'.format(num_tel[0:4], num_tel[3:]))

elif len(num_tel) > 8:
	print('Número de telefone inválido!')
	print('\a Quantidade maior que o necessário (7).')

else:
	print('Telefone: {}-{}'.format(num_tel[0:4], num_tel[4:]))
