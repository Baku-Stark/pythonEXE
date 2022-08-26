'''
Jogo da palavra embaralhada. Desenvolva um jogo em que o usuário tenha que adivinhar 
uma palavra que será mostrada com as letras embaralhadas. O programa terá uma lista de 
palavras lidas de um arquivo texto e escolherá uma aleatoriamente. O jogador terá seis 
tentativas para adivinhar a palavra. Ao final a palavra deve ser mostrada na tela, 
informando se o usuário ganhou ou perdeu o jogo. 
'''

import random

def main():
	while True:
		input('\a Pressione ENTER para sortear uma nova palavra.')
		print('')
		palavra_oculta, dica = EscolhePalavra()
		palavra_embaralhada = EmbaralhaPalavra(palavra_oculta)
		palavra_embaralhada = palavra_embaralhada.lower()
		palavra_oculta = palavra_oculta.lower()

		tentativas = 6

		while tentativas != 0:
			print('A palavra embaralhada: {}'.format(palavra_embaralhada))
			print('A dica é: {}'.format(dica))
			print('Você ainda tem {} tentativas'.format(tentativas))
			print('')
			palpite = input('Digite seu palpite \nr: ')

			if palpite == palavra_oculta:
				print('PARABÉNS! VOCÊ ACERTOU!')

			else:
				print('Ainda não. Tente novamente!')
			
			tentativas -= 1

			if tentativas == 0:
				print('Você perdeu!')
				print('\a A palavra correta era {}'.format(palavra_oculta))

			else:
				print('PARABÉNS! VOCÊ ACERTOU A PALAVRA!')

def EscolhePalavra():
	lista_arquivos = {'Animais.txt': 'Animal',
						'Frutas.txt': 'Fruta',
						'Objetos.txt': 'Objeto',
						'Pessoas.txt': 'Pessoa',
						'Profissões.txt': 'Profissão'}
	arquivo_escolhido = random.choice(list(lista_arquivos.keys()))
	linhas = open(arquivo_escolhido).read().splitlines()
	palavra = random.choice(linhas)
	dica = lista_arquivos[arquivo_escolhido]
	return(palavra, dica)

def EmbaralhaPalavra(palavra):
	palavra = palavra.strip()
	palavra = list(palavra)
	random.shuffle(palavra)
	palavra = ''.join(palavra)

	return palavra

	if __name__ == '__main__':
		main()
