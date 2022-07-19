'''
Faça um programa que leia 5 números e informe o maior número. 
'''

lista = []

for x in xrange(1, 6):
	lista.append(input('\a Digite o {}° número \nr: '.format(x)))
print('')
print('>>> O maior número da lista é o {}'.format(max(lista)))
print('>>> O menor número da lista é o {}'.format(min(lista)))
