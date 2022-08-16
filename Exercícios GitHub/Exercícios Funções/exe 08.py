'''
Faça uma função que informe a quantidade de dígitos de um determinado número inteiro 
informado. 
'''

def digitos(num):
	print('\a O número possui {} digito(s).'.format(len(num)))


# ===
num = str(input('Digite um número \nr: '))
print('')
digitos(num)
