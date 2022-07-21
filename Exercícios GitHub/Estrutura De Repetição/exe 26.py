'''
Faça um programa que calcule o mostre a média aritmética de N notas. 
'''

boletim = 'REGISTRO DE NOTAS'
linha = '-=' *40


def clear():
	print('\n' *5)

while True:
	print(linha)
	print(boletim.center(40))
	print('\a Sistema de Notas')
	print('')
	n = 1
	total = 0

	while True:
		print('')
		nota = float(input('{}ª Nota \nr: '.format(n)))
		print('')
		if nota == 0:
			break
		else:
			n += 1
			total += nota
	if nota == 0:
		break
clear()
media = total / (n - 1)
print(linha)
print('Tota: {:.1f}'.format(total))
print('\a Média das notas: {:.1f}'.format(media))

print(linha)
