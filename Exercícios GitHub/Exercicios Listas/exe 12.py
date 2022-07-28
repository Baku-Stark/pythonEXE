'''
Foram anotadas as idades e alturas de 5 alunos. Faça um Programa que determine quantos 
alunos com mais de 13 anos possuem altura inferior à média de altura desses alunos. 
'''

# Fiz utilizando 5.

ida = []
alt = []
qtd_alunos = 0

def clear():
	print('\n' *10)

for a in xrange(1, 6):
	ida.append(input('Idade da {}ª pessoa \nr: '.format(a)))
	print('')
	alt.append(input('Altura da {}ª pessoa \nr: '.format(a)))
	print('')
	print('-=' *30)

media = sum(alt) / len(alt)

for i in xrange(0, len(ida)):
	if ida[i] > 13 and alt[i] < media:
		qtd_alunos += 1
clear()
print('-=' *30)
print('Resultados')
print('')
print('\a A média de altura: {:.2f}'.format(media))
print('\a A quantidade de alunos inferior à média de altura são de: {}'.format(qtd_alunos))
print('-=' *30)
