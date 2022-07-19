'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de 
crescimento iniciais. Valide a entrada e permita repetir a operação. 
'''

popu_a = int(input('População A: '))
porcentagem_a = float(input('Taxa De Cresimento (A) \nr: '))
cres_a = porcentagem_a / 100
print('')
popu_b = int(input('População B: '))
porcentagem_b = float(input('Taxa De Cresimento (B) \nr: '))
cres_b = porcentagem_b / 100
print('')
ano = 0

while popu_a <= popu_b:
	ano += 1
	popu_a += popu_a * cres_a
	popu_b += popu_b * cres_b

print('Para a população A igualar a popução B são necessários {} ano(s)'.format(ano))
print('')
print('-=' *30)
print('Em {} ano(s):'.format(ano))
print('')
print('\a População A: {:.0f}'.format(popu_a))
print('\a População B: {:.0f}'.format(popu_b))
print('-=' *30)
