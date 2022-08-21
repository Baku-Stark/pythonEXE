'''
Conta espaços e vogais. Dado uma string com uma frase informada pelo usuário 
(incluindo espaços em branco), conte:

    quantos espaços em branco existem na frase.
    quantas vezes aparecem as vogais a, e, i, o, u. 
'''

def contagemSpace(frase):
	count_space = frase.count(' ')
	print('\a Quantidade de espaços: {}'.format(count_space))

def contagemVogal(frase):
	count_vogalA = frase.count("a") + frase.count("A")
	count_vogalE = frase.count("e") + frase.count("E")
	count_vogalI = frase.count("i") + frase.count("I")
	count_vogalO = frase.count("o") + frase.count("O")
	count_vogalU = frase.count("u") + frase.count("U")
	print('')
	print('\a Quantidade de vogais "A" na frase: {}'.format(count_vogalA))
	print('\a Quantidade de vogais "E" na frase: {}'.format(count_vogalE))
	print('\a Quantidade de vogais "I" na frase: {}'.format(count_vogalI))
	print('\a Quantidade de vogais "O" na frase: {}'.format(count_vogalO))
	print('\a Quantidade de vogais "U" na frase: {}'.format(count_vogalU))


# ===
frase = str(input('Digite a frase: '))
print('')
print('-=' *30)
contagemSpace(frase)
contagemVogal(frase)
print('-=' *30)
