Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 

num1 = int(input('Registre o 1° número inteiro: '))
num2 = int(input('Registre o 2° número inteiro: '))
num3_f = float(input('Registre um número real: '))
print('')
print('-=' *30)
print('--- O produto do dobro do primeiro com metade do segundo ---')
pri_op = (num1 * 2) * (num2/2)
print('({} * 2) * ({}/2) = {}'.format(num1, num2, pri_op))
print('')
print('--- A soma do triplo do primeiro com o terceiro ---')
seg_op = (2 * num1) + num3_f
print('(2 * {}) + {} = {}'.format(num1, num3_f, seg_op))
print('')
print('--- O terceiro elevado ao cubo ---')
tri_op = num3_f **3
print('{}³ = {:.2f}'.format(num3_f, tri_op))
print('-=' *30)
