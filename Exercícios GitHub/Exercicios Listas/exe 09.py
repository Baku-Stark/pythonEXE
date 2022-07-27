'''
Faça um Programa que leia um vetor A com 10 números inteiros, 
calcule e mostre a soma dos quadrados dos elementos do vetor.
'''

vetorA = []
vetor_quadrado = []
soma = 0

def clear():
    print('\n' *10)


# ---
for n in range(1, 11):
    num = int(input(f'Registe o {n}° número \nr: '))
    print('')
    vetorA.append(num)
    quadrado = num * num
    vetor_quadrado.append(quadrado)
    soma += quadrado
clear()
print('-=' *30)
print('Resultados')
print('')
print(f'\a Lista De Números:    {vetorA}')
print(f'\a Números Elevado a 2: {vetor_quadrado}')
print(f'\a Soma Dos Quadrados:  {soma}')
print('-=' *30)
