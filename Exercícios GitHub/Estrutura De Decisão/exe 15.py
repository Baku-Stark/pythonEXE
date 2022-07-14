Faça um programa que calcule as raízes de uma equação do segundo grau, 
na forma ax2 + bx + c. 
O programa deverá pedir os valores de a, b e c e fazer as consistências, 
informando ao usuário nas seguintes situações:

    Se o usuário informar o valor de A igual a zero, a equação não é do segundo 
    grau e o programa não deve fazer pedir os demais valores, sendo encerrado;

    Se o delta calculado for negativo, a equação não possui raizes reais. 
    Informe ao usuário e encerre o programa;

    Se o delta calculado for igual a zero a equação possui apenas uma raiz real; 
    informe-a ao usuário;

    Se o delta for positivo, a equação possui duas raiz reais; informe-as ao usuário; 


'''ax² + bx + c = 0
x = - b +- raiz b² - 4 * a * c '''

raiz_mais = (- b + math.sqrt(delta)) / (2 * a)
raiz_meno = (- b - math.sqrt(delta)) / (2 * a)

import math

print('--- EQUAÇÃO DO SEGUNDO GRAU ---')

a = int(input('Escolha o segmento A \nr: '))
print('')
if a == 0:
	print('\a A equação não é do Segundo Grau. Finalizando Programa!')
	print('Motivo: Valor de A = 0')
else:
	b = int(input('Escolha o segmento B \nr: '))
	print('')
	c = int(input('Escolha o segmento C \nr: '))
	delta = b * b - (4 * a * c)
	print('')
	if delta < 0:
		print('Delta menor que 0. Finalizando Programa!')
		print('Motivo: Raízes imaginárias')
	elif delta == 0:
		raiz = - b / (2 * a)
		print('Delta = 0 || Raíz = {}'.format(raiz))
	else:
		raiz_mais = (- b + math.sqrt(delta)) / (2 * a)
		raiz_meno = (- b - math.sqrt(delta)) / (2 * a)
		print('Resultado: {} e {}'.format(raiz_mais, raiz_meno))
