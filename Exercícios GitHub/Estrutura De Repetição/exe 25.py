count_1 = 0
count_2 = 0
count_3 = 0


print('''
[ 1 ] - Candidato Tony

[ 2 ] - Candidato Steve

[ 3 ] - Candidato Thor
''')
print('')
votantes = int(input('Quantas pessoa votarão? \nr: '))
print('')
print('-=' *30)
for x in range(1, votantes+1):
	voto = int(input('Escolha o eleitor \nr: '))
	if voto == 1:
		count_1 += 1

	elif voto == 2:
		count_2 += 1

	elif voto == 3:
		count_3 += 1

	else:
		#print('Voto nulo!')
	print('')
print('RESULTADO DAS ELEIÇÕES')
print('')
if count_1 > count_2 and count_1 > count_3:
	print('O Candidato Tony venceu as eleições')
	print('\a Quantidade de votos: {}'.format(count_1))

elif count_2 > count_1 and count_2 > count_3:
	print('O Candidato Steve venceu as eleições')
	print('\a Quantidade de votos: {}'.format(count_2))

elif count_3 > count_2 and count_3 > count_1:
	print('O Candidato Thor venceu as eleições')
	print('\a Quantidade de votos: {}'.format(count_3))

else:
	print('Ocorreu um EMPATE!')
print('-=' *30)
