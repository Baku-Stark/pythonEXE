'''
Verificação de CPF. Desenvolva um programa que solicite a digitação de um número de CPF 
no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido através da validação 
dos dígitos verificadores edos caracteres de formatação. 
'''

print('Modelo de CPF: xxx.xxx.xxx-xx')
print('')
cpf = str(input('Registre seu CPF \nr: '))
print('')
if len(cpf) > 11:
	print('[ERRO] \a Caracteres maior que 11!')
	while len(cpf) > 11:
		cpf = str(input('[REFAZENDO] Registre seu CPF \nr: '))
		print('')

elif len(cpf) < 11:
	print('[ERRO] \a Caracteres menor que 11!')
	while len(cpf) < 11:
		cpf = str(input('[REFAZENDO] Registre seu CPF \nr: '))
		print('')

print('-' *15)
print('')
print('CPF do usuário: {}.{}.{}-{}'.format(cpf[0:3], cpf[3:6], cpf[6:9], cpf[9:]))
