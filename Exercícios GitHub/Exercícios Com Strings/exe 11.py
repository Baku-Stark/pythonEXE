'''
Jogo de Forca. Desenvolva um jogo da forca. O programa terá uma lista de palavras lidas 
de um arquivo texto e escolherá uma aleatoriamente. O jogador poderá errar 6 vezes antes 
de ser enforcado. 

	Digite uma letra: A
	-> Você errou pela 1ª vez. Tente de novo!

	Digite uma letra: O
	A palavra é: _ _ _ _ O

	Digite uma letra: E
	A palavra é: _ E _ _ O

	Digite uma letra: S
	-> Você errou pela 2ª vez. Tente de novo!
'''

import random

def print_forca(forca):
	print(' '.join(forca))
	print('')

print('-=' *30)
print('JOGO DA FORCA')
print('-=' *30)
print('')
palavras = ["PROGRAMA", "ARQUIVO", "TEXTO", "ALEATORIAMENTE", "JOGADOR", "ENFORCADO"]
palavra = random.choice(palavras)

if palavra == "PROGRAMA":
	print('Dica!')
	print('\a A própria composição do espetáculo, concerto ou cerimônia.')

elif palavra == "ARQUIVO":
	print('Dica!')
	print('\a Recinto onde se guardam esses documentos.')

elif palavra == "TEXTO":
	print('Dica!')
	print('\a Conjunto das palavras escritas, em livro, folheto, documento etc.')

elif palavra == "ALEATORIAMENTE":
	print('Dica!')
	print('\a Sujeito às incertezas do acaso.')

elif palavra == "JOGADOR":
	print('Dica!')
	print('\a Que ou aquele que tem por profissão jogar.')

elif palavra == "ENFORCADO":
	print('Dica!')
	print('\a Que ou quem foi supliciado na forca ou se enforcou.')

forca = ['_' for  i in range(len(palavra))]
erros = 0
ganhou = False
print('')
while erros < 6 and not ganhou:
	print_forca(forca)
	chute = str(input('Digite uma letra \nr: ')).upper()
	print('')

	if chute not in palavra:
		erros += 1
		print('\a Você errou pela {}ª vez. Tente novamente!'.format(erros))
		print('=' *30)
		print('')
		continue

	for index, letra in enumerate(palavra):
		if letra == chute:
			forca[index] = chute
			print('=' *30)
			print('')

	if '_' not in forca:
		ganhou = True

if ganhou:
	print('YOU WIN!')

else:
	print('YOU LOSE!')
