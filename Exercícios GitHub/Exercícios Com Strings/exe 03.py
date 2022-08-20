'''
Nome na vertical. Faça um programa que solicite o nome do usuário e imprima-o na vertical.

    F
    U
    L
    A
    N
    O
'''

nome = str(input('Digite seu nome \nr: ')).upper()
print('')
for n in range(0, len(nome)):
	print('{}\n'.format(nome[n]))
