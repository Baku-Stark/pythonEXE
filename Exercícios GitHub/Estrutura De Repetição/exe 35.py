'''
Desenvolver um programa para verificar a nota do aluno em uma prova com 10 questões, 
o programa deve perguntar ao aluno a resposta de cada questão e ao final 
comparar com o gabarito da prova e assim calcular o total de acertos e a nota 
(atribuir 1 ponto por resposta certa). Após cada aluno utilizar o sistema deve ser 
feita uma pergunta se outro aluno vai utilizar o sistema. Após todos os alunos terem 
respondido informar: 

	Maior e Menor Acerto;
	Total de Alunos que utilizaram o sistema; 
	A Média das Notas da Turma. 
	
	Gabarito da Prova:

	01 - A
	02 - B
	03 - C
	04 - D
	05 - E
	06 - E
	07 - D
	08 - C
	09 - B
	10 - A

Após concluir isto você poderia incrementar o programa permitindo que o professor 
digite o gabarito da prova antes dos alunos usarem o programa. 
'''

def clear():
	print('\n' *15)


# Banco de Dados (aluno) ----------------------
gabarito_aluno = '' # gabarito do aluno
acerto_aluno = 0    # acertos do aluno
tot_acertos = 0     # total de acertos
qtd_aluno = 0       # quantidade de alunos


# Banco de Dados (professor) ------------------
gabarito_prof = ('ACDCBEABCD')
maior = 0
menor = 0

print('-=' *30)
continuar = ' '
print('ALUNO')
print('')
print('Alternativas [A, B, C, D, E]')
print('')
while continuar not in 'N':
	tot_acertos = 0     # total de acertos (ZERADO)

	for a in range(1, 11):
		print('{}ª Questão'.format(a))
		resposta = input('Registre a alternativa marcada \nr: ').strip().upper()[0]
		print('')
		if a == 1:
			if resposta == gabarito_prof[0]:
				acerto_aluno += 1
				tot_acertos += 1
		
		if a == 2:
			if resposta == gabarito_prof[1]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 3:
			if resposta == gabarito_prof[2]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 4:
			if resposta == gabarito_prof[3]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 5:
			if resposta == gabarito_prof[4]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 6:
			if resposta == gabarito_prof[5]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 7:
			if resposta == gabarito_prof[6]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 8:
			if resposta == gabarito_prof[7]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 9:
			if resposta == gabarito_prof[8]:
				acerto_aluno += 1
				tot_acertos += 1

		if a == 10:
			if resposta == gabarito_prof[9]:
				acerto_aluno += 1
				tot_acertos += 1
			qtd_aluno += 1
			print('-' *20)
			continuar = str(input('\a Quer continuar? \n[N] para sair: ')).strip().upper()[0]
			print('')
				

		if tot_acertos > maior:
			maior = tot_acertos

		elif tot_acertos < menor or tot_acertos == 1:
			menor = tot_acertos
print('-=' *30)
clear()
print('-=' *30)
print('SITUAÇÃO')
print('')
print('Total de acertos:  {}'.format(acerto_aluno))
print('Pontos adquiridos: {}'.format(acerto_aluno))
print('\a Maior quantidade de acertos: {}'.format(maior))
print('\a Menor quantidade de acertos: {}'.format(menor))
print('\a Quantidade de alunos que utilizaram o sistema: {}'.format(qtd_aluno))
print('-=' *30)
