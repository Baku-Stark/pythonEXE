'''
Faça um Programa que leia um vetor de 10 números reais e mostre-os na 
ordem inversa. 
'''

vetor_list = []

for n in range(1, 11):
	vetor_list.append(int(input('Registre o {}° número \nr: '.format(n))))
	print('')

print('\a Ordem inversa: {}'.format(vetor_list[::-1]))
