'''
Faça um programa que leia e valide as seguintes informações: 

	Nome: maior que 3 caracteres; 

	Idade: entre 0 e 150; 

	Salário: maior que zero;

	Sexo: 'f' ou 'm';

	Estado Civil: 's', 'c', 'v', 'd'; 
		Solteiro
		Casado
		Viúvo
		Divorciado
'''


# Nome
while True:
	nome = str(input('\a Nome Do Usuário \nr: ')).capitalize()
	print('')
	if len(nome) > 3:
		break
	else:
		print('>>> Nome inválido! Faça o registro novamente!')
		print('-=' *30)
		print('')
print('')

# Idade
while True:
	idade = int(input('\a Idade Do Usuário \nr: '))
	print('')
	if idade >= 0 and idade <= 150:
		break
	else:
		print('>>> Idade inválida! Faça o registro novamente!')
		print('-=' *30)
		print('')
print('')

# Salário
while True:
	salario = float(input('\a Salário Do Usuário \nR$'))
	print('')
	if salario > 0:
		break
	else:
		print('>>> Salário inválido! Faça o registro novamente!')
		print('-=' *30)
		print('')
print('')

# Sexo
while True:
	sexo = str(input('Sexo Do Usuário \nr: ')).upper()
	if sexo == "M" or sexo == "F":
		if sexo == "M":
			sexo = "Masculino"
			break
		else:
			sexo == "Feminino"
			break
	else:
		print('>>> Sexo inválido! Faça o registro novamente!')
		print('-=' *30)
		print('')
print('')

# Estado Civil
while True:
	print('\a Estado Civil do Usuário')
	print('[ V ] -- Viúvo \n[ C ] -- Casado \n[ S ] -- Solteiro \n[ D ] -- Divorciado')
	print('')
	estado_civ = str(input('Respota: ')).upper()
	print('')
	if estado_civ == "V" or estado_civ == "C" or estado_civ == "S" or estado_civ == "D":
		if estado_civ == "V":
			estado_civ = "Viúvo"
			break
		elif estado_civ == "Cc":
			estado_civ = "Casado"
			break
		elif estado_civ == "S":
			estado_civ = "Solteiro"
			break
		elif estado_civ == "D":
			estado_civ = "Divorciado"
			break
	else:
		print('>>> Estado Civil inválido! Faça o registro novamente!')
		print('-=' *30)
		print('')
print('')

print('-=' *30)
print('--- Informações Do Usuário ---')
print('')
print('Nome:{:>9}{}'.format(' ', nome))
print('Salário:{:>6}R${:.2f}'.format(' ', salario))
print('Idade:{:>8}{}'.format(' ', idade))
print('Sexo:{:>9}{}'.format(' ', sexo))
print('Estado Civil: {}'.format(estado_civ))
print('-=' *30)
