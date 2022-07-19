'''
Faça um programa que imprima na tela os números de 1 a 20, um abaixo do outro. 
Depois modifique o programa para que ele mostre os números um ao lado do outro. 
'''

# 1 a 20 pulando linha
for x in xrange(1, 21):
	print('{} \n'.format(x))

# 1 a 20 na mesma linha
for x in xrange(1, 21):
	print(x),

for x in xrange(1, 21):
	print(x, end="")

import sys

for x in xrange(1, 21):
	sys.stdout.write('{} '.format(x))
