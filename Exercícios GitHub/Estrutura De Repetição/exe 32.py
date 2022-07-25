'''
Em uma eleição presidencial existem quatro candidatos. Os votos são informados por meio de código. Os códigos utilizados são:
1 , 2, 3, 4  - Votos para os respectivos candidatos 
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco

Faça um programa que calcule e mostre:
    O total de votos para cada candidato;
    O total de votos nulos;
    O total de votos em branco;
    A percentagem de votos nulos sobre o total de votos;
    A percentagem de votos em branco sobre o total de votos. 
Para finalizar o conjunto de votos tem-se o valor zero.
'''

linha = '-' *41
word = 'ELEIÇÕES 2022!!!'

# CANDIDATOS E CONTAGEM ------------------------
cand_1 = 'Tony Stark'
count_tony = 0

cand_2 = 'Steve Rogers'
count_steve = 0

cand_3 = 'Bruce Wayne'
count_bruce = 0

cand_4 = 'Clark Kent'
count_clark = 0

count_nulo = 0
count_branco = 0

# SISTEMA DE VOTOS ------------------------
print(linha)
print(word.center(41))
print(linha)
print('Candidatos: ')
print('''
[ 1 ] - Tony Stark
[ 2 ] - Steve Rogers
[ 3 ] - Bruce Wayne
[ 4 ] - Clark Kent
[ 5 ] - \033[1;31mVoto Em Branco\033[m
[ 6 ] - \033[1;32mVoto Nulo\033[m''')
print(linha)
print('')
while True:
    escolha = int(input('Escolha o candidato para a eleição \nr: '))
    print('')
    while escolha > 6:
        escolha = int(input('Por favor, escolha o candidato para a eleição \nr: '))
        print('')
    # SISTEMA DE CONTAGEM -----------------------------
    if escolha == 1:
        count_tony += 1

    elif escolha == 2:
        count_steve += 1

    elif escolha == 3:
        count_bruce += 1

    elif escolha == 4:
        count_clark += 1

    elif escolha == 5:
        count_branco += 1
    
    elif escolha >= 6:
        count_nulo += 1

    res = str(input('\a Deseja realizar uma nova votação? \n[S/N]: ')).upper()
    print('')
    if res == 'S':
        print(linha)
        continue
    
    elif res == 'N':
        break
    
    else:
        while res != 'S' and res != 'N':
            print('[ERRO] Seleção errada!')
            res = str(input('\a Deseja realizar uma nova votação? \n[S/N]: ')).upper()
            print('')
print('')
print(linha)
print('RESULTADOS')
print('')
print('\a {}'.format(cand_1))
print('Qtd de votos: {}'.format(count_tony))
print('')
print('\a {}'.format(cand_2))
print('Qtd de votos: {}'.format(count_steve))
print('')
print('\a {}'.format(cand_3))
print('Qtd de votos: {}'.format(count_bruce))
print('')
print('\a {}'.format(cand_4))
print('Qtd de votos: {}'.format(count_clark))
print('')
print('\a Votos Nulos: {}'.format(count_nulo))
print('\a Votos Em Branco: {}'.format(count_branco))
print(linha)