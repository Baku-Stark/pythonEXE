Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

aluno = str(input('Nome Do(a) aluno(a) \nr: '))
print('')
bim_1 = float(input('Nota do 1° Bimestre: '))
bim_2 = float(input('Nota do 2° Bimestre: '))
media = bim_1 + bim_2
print('')
print('[RESULTADO DO ALUNO]')
if media >= 7 and media <= 9:
	print('\a {} está APROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media < 7:
	print('\a {} está REPROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media == 10:
	print('\a {} está APROVADO COM DISTINÇÃO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
