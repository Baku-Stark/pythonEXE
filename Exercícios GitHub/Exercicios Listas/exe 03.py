'''
Faça um Programa que leia 4 notas, mostre as notas e a média na tela. 
'''

notas_list = []
soma = 0

for x in xrange(1, 5):
	nota = float(input('Registre a {}ª nota \nr: '.format(x)))
	soma += nota
	notas_list.append(nota)
	print('')
media = soma / x
print('Números: {}'.format(notas_list))
print('\a Média: {}'.format(media))
