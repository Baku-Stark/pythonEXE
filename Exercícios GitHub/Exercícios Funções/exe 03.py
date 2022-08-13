'''
Faça um programa, com uma função que necessite de três argumentos, e que forneça a soma 
desses três argumentos. 
'''

num = []

def clear():
	print('\n' *10)

def soma(n1, n2, n3):
	resultado = n1 + n2 + n3
	print('\a A soma dos números: {}'.format(resultado))


# ---
for n in xrange(1, 4):
	num.append(int(input('Registre o {}° número \nr: '.format(n))))
	print('')
clear()
print('-=' *30)
soma(num[0], num[1], num[2])
print('-=' *30)
