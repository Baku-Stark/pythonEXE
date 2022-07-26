'''
Faça um programa que peça um numero inteiro positivo e em seguida mostre este numero 
invertido.

    Exemplo:

      12376489
      => 98467321
'''

num = int(input('Escolha um número: '))
str_num = str(num)
print('')
print('\a Número invertido: {}'.format(str_num[::-1]))
