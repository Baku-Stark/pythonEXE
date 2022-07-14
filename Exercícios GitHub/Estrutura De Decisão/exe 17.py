Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a 
mesma é uma data válida. 

valida = False
dia = int(input('Dia do nascimento \nr: '))
mes = int(input('Mês do nascimento \nr: '))
ano = int(input('Ano do nascimento \nr: '))
print('')
# Meses com 31 Dias
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
	if dia <= 31:
		valida = True
# Meses com 30 Dias
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:	
	if dia <= 30:
		valida = True
# Ano Bissexto
elif mes == 2:
	if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
		valida = True
		print('O ano {} é bissexto.'.format(ano))
	elif dia <= 28:
		valida = True
		print('O ano {} não é bissexto.'.format(ano))
if valida == True:
	print('Data Válida!')
	print('Data De Nasicmento: {}/{}/{}'.format(dia, mes, ano))
else:
	print('Data Inválida!')
