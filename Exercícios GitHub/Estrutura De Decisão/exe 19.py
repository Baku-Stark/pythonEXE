Faça um Programa para leitura de três notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e presentar: 

	A mensagem "Aprovado", se a média for maior ou igual a 7, com a 
	respectiva média alcançada;

	A mensagem "Reprovado", se a média for menor do que 7, 
	com a respectiva média alcançada;

	A mensagem "Aprovado com Distinção", se a média for igual a 10. 

bim_1 = float(input('1ª Nota: '))
bim_2 = float(input('2ª Nota: '))
bim_3 = float(input('3ª Nota: '))
nota = bim_1 + bim_2 + bim_3
print('')
if nota >= 7 and nota <= 9.9:
	print('\a Aprovado! --- Média: {:.1f}'.format(nota))
elif nota < 7:
	print('\a Reprovado! --- Média: {:.1f}'.format(nota))
elif nota == 10:
	print('\a Aprovado Com Distinção --- Média: {:.1f}'.format(nota))
