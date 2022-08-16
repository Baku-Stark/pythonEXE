'''
Reverso do número. Faça uma função que retorne o reverso de um número inteiro informado. 
Por exemplo: 127 -> 721. 
'''

def reverse(num):
	print('\a {} -> {} [reverse]'.format(num, num[::-1]))


# ===
num = str(input('Escolha um número \nr: '))
print('')
reverse(num)
