Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
'M-matutino' ou 'V-Vespertino' ou 'N-Noturno'. Imprima a mensagem 
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def dia_Turno(turno):
	print('')
	if turno == 'MANHÃ':
		print('\a Turno da Manhã: BOM DIA!')
	elif turno == 'TARDE':
		print('\a Turno da Tarde: BOA TARDE!')
	elif turno == 'NOITE':
		print('\a Turno da Noite: BOA NOITE!')
	else:
		print('[ERRO] Resposta Inválida!')


###
dia = str(input('''Turno De Estudo
[MANHÃ]
[TARDE]
[NOITE]

\nr: ''')).upper()
dia_Turno(dia)
