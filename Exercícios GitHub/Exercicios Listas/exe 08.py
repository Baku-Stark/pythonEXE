'''
Faça um Programa que peça a idade e a altura de 5 pessoas, 
armazene cada informação no seu respectivo vetor. 
Imprima a idade e a altura na ordem inversa a ordem lida.
'''

idade = []
altura = []

for n in range(1, 6):
    idade.append(int(input(f'{n}ª Pessoa - \033[1;34mIdade\033[m \nr: ')))
    print('')
    altura.append(float(input(f'{n}ª Pessoa - \033[1;36mAltura\033[m \nr: ')))
    print('-=' *30)
    print('')

print('-=' *30)
print('Resultados')
print('')
print(f'\a Lista IDADE:  {idade[::-1]}')
print(f'\a Lista ALTURA: {altura[::-1]}')
print('-=' *30)
