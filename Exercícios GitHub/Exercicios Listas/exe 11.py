'''
Altere o programa anterior, intercalando 3 vetores de 10 elementos cada. 
'''

vetor_A = []
vetor_B = []
vetor_C = []
vetor_ABC = []

def clear():
	print('\n' *10)

print('LISTA [A]')
for a in xrange(1, 11):
	num = int(input('Registre o {}° número \nr: '.format(a)))
	vetor_A.append(num)
	print('')
print('-=' *30)
print('LISTA [B]')
for b in xrange(1, 11):
	num = int(input('Registre o {}° número \nr: '.format(b)))
	vetor_B.append(num)
	print('')
print('-=' *30)
print('LISTA [C]')
for c in xrange(1, 11):
	num = int(input('Registre o {}° número \nr: '.format(c)))
	vetor_C.append(num)
	print('')
clear()
print('-=' *30)
print('Resultado')
print('')
print('\a Listagem A: {}'.format(vetor_A))
print('\a Listagem B: {}'.format(vetor_B))
print('\a Listagem C: {}'.format(vetor_C))
vetor_ABC.append(vetor_A + vetor_B + vetor_C)
vetor_ABC.sort()
print('>>> Vetores unificados: {}'.format(vetor_ABC))
print('-=' *30)
