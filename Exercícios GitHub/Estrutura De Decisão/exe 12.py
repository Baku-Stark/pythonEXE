Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('''
[ 1 ] -- Domingo
[ 2 ] -- Segunda
[ 3 ] -- Terça
[ 4 ] -- Quarta
[ 5 ] -- Quinta
[ 6 ] -- Sexta
[ 7 ] -- Sábado''')
print('')
semana = int(input('Escolha o dia da semana: '))
if semana == 1:
	print('\a DOMINGO')
elif semana == 2:
	print('\a SEGUNDA-FEIRA!')
elif semana == 3:
	print('\a TERÇA-FEIRA!')
elif semana == 4:
	print('\a QUARTA-FEIRA!')
elif semana == 5:
	print('\a QUINTA-FEIRA!')
elif semana == 6:
	print('\a SEXTA-FEIRA!')
elif semana == 7:
	print('\a DOMINGO!')
else:
	print('\a [ERRO] Dia Da Semana Inválido!')
