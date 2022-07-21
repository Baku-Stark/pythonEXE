'''
Faça um programa que peça para n pessoas a sua idade, ao final o programa devera 
verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior que 60; 
e então, dizer se a turma é jovem, adulta ou idosa, conforme a média calculada.

0  -  25:     Jovem
26 - 60:      Adulta
maior que 60: Idosa 
'''

jovem = []
count_jovem = 0

adult = []
count_adult = 0 

idosa = []
count_idosa = 0



qtd = int(input('Quantidade de alunos na turma \nr: '))
print('')
print('-=' *30)
print('DADOS DA TURMA')
print('')
for n in xrange(1, qtd+1):
	idade = int(input('Idade do {}° aluno(a) \nr: '.format(n)))
	print('')
	if idade > 0 and idade <= 25:
		jovem.append(idade)
		count_jovem += 1

	elif idade > 26 and idade <= 60:
		adult.append(idade)
		count_adult += 1

	else:
		idosa.append(idade)
		count_idosa += 1

	### Média da turma
if count_jovem > count_adult and count_jovem > count_idosa:
	print('\a A média da turma é de JOVENS!')
	print('Quantidade de alunos entre 0 a 25 anos: {}'.format(count_jovem))

elif count_adult > count_jovem and count_adult > count_idosa:
	print('\a A média da turma é de ADULTOS!')
	print('Quantidade de alunos entre 26 a 60 anos: {}'.format(count_adult))

elif count_idosa > count_jovem and count_idosa > count_adult:
	print('\a A média da turma é de IDOSOS!')
	print('Quantidade de alunos acima dos 60 anos: {}'.format(count_idosa))

else:
	print('\a A média da turma está equilibrada entre os alunos!')
print('-=' *30)
