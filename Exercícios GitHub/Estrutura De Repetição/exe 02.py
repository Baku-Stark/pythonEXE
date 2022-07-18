'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual 
ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações. 
'''

users = ""
senha = ""

while True:
	users = str(input('\a Registre Um Nome De Usuário \r: '))
	print('')
	senha = str(input('\a Registre Uma Senha \r: '))
	print('')
	if users == senha:
		print('>>> A senha não pode ser igual ao nome do usuário.')
		print('-=' *30)
		print('')
	else:
		print('>>> Conta Registrada com sucesso!!')
		break
