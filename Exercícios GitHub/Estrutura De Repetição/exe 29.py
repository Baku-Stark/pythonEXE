'''
Faça um programa que calcule o número médio de alunos por turma. Para isto, peça a 
quantidade de turmas e a quantidade de alunos para cada turma. As turmas não podem ter 
mais de 40 alunos. 
'''

count_aluno = 0

qtd_turma = int(input('Quantidade de turmas \nr: '))
print('')
for t in range(1, qtd_turma+1):
	print('\a {}ª TURMA'.format(t))
	qtd_aluno = int(input('Quantidade de alunos \nr: '))
	print('')
	while qtd_aluno > 40:
		print('[ERRO] O número de alunos não pode passar de 40!')
		qtd_aluno = int(input('Quantidade de alunos \nr: '))
		print('')
	count_aluno += qtd_aluno
print('')
print('-=' * 30)
print('RESULTADOS:')
print('')
print('Total de turmas: {}'.format(qtd_turma))
print('\a A escola possui {} alunos.'.format(count_aluno))
print('-=' *30)
