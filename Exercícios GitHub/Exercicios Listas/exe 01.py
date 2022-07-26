'''
Faça um Programa que leia um vetor de 5 números inteiros e mostre-os. 
'''

vetor_list = []

for n in range(1, 6):
	vetor_list.append(int(input('Registre o {}° número \nr: '.format(n))))
	print('')

print('\a {}'.format(vetor_list))
