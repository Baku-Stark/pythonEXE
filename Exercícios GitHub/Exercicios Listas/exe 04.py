'''
Faça um Programa que leia um vetor de 10 caracteres, e diga 
quantas consoantes foram lidas. Imprima as consoantes. 
'''

x = 0
caracteres = []
cont_conso = 0

print('')
while x <= 10:
	entrada = str(input('Registre os caracteres \nr: ')).upper()
	print('')
	x += 1
	caracteres.append(entrada)
print('')
caracteres.remove("A")
caracteres.remove("E")
caracteres.remove("I")
caracteres.remove("O")
caracteres.remove("U")
print('\a Lista (sem vogais): {}'.format(caracteres))
print('\a Consoantes: {}'.format(len(caracteres)))
