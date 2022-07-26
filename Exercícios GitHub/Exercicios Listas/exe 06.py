'''
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene 
num vetor a média de cada aluno, imprima o número de alunos com média maior ou 
igual a 7.0. 
'''

def clear():
	print('\n' *15)

notas_alunos = []
media_alunos = []

for n in range(1, 6):
	print('-=' *30)
	print('\a {}° Aluno'.format(n))
	soma = 0
	print('')
	for x in range(1, 5):
		nota = float(input('Nota do {}° Bimestre \nr: '.format(x)))
		print('')
		soma += nota
		if x == 4:
			print('\a Soma de todas as notas: {}'.format(soma))
			media = soma / 4
			notas_alunos.append(media)
			if media > 7.0:
				media_alunos.append(media)
print('-=' *30)
clear()
print('-=' *30)
print('Total:')
print('')
print('\a Notas no total: {}'.format(notas_alunos))
print('\a Alunos acima de 7.0: {}'.format(media_alunos))
print('-=' *30)
