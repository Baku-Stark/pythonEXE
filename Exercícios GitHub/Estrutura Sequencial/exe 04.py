Faça um Programa que peça as 4 notas bimestrais e mostre a média.

bim1 = float(input('Nota do 1° Bimestre \nr: '))
print('')
bim2 = float(input('Nota do 2° Bimestre \nr: '))
print('')
media_1 = bim1 + bim2
print('-' *10)
bim3 = float(input('Nota do 3° Bimestre \nr: '))
print('')
bim4 = float(input('Nota do 4° Bimestre \nr: '))
print('')
media_2 = bim3 + bim4
print('')
print('-=' *30)
media_final = media_1 + media_2
print('A média do primeiro semestre: {:.1f}'.format(media_1))
print('A média do segundo semestre: {:.1f}'.format(media_2))
print('')
print('>>> Média final do(a) aluno(a): {:.1f}'.format(media_final))
print('-=' *30)
