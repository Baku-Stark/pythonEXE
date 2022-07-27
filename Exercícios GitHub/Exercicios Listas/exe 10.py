'''
Faça um Programa que leia dois vetores com 10 elementos cada. 
Gere um terceiro vetor de 20 elementos, cujos valores deverão ser 
compostos pelos elementos intercalados dos dois outros vetores.
'''

vetor_A = []
vetor_B = []
vetor_AB = []

def clear():
    print('\n' *10)

# ----- PARAM. (A) -----
for a in range(1, 11):
    print('')
    vetor_A.append(int(input(f'Escolha o {a}° número (Lista A) \nr: ')))
print('-=' *30)
# ----- PARAM. (B) -----
for b in range(1, 11):
    print('')
    vetor_B.append(int((input(f'Escolha o {b}° número (Lista B) \nr: '))))
print('-=' *30)
clear()
print('-=' *30)
print('Lista Unificada:')
print('')
vetor_AB.append(vetor_A + vetor_B)
vetor_AB.sort()
print(f'>>> {vetor_AB}')
print('-=' *30)
