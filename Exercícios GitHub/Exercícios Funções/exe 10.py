'''
Jogo de Craps. Faça um programa de implemente um jogo de Craps. O jogador lança um par de 
dados, obtendo um valor entre 2 e 12. Se, na primeira jogada, você tirar 7 ou 11, você um 
"natural" e ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" 
e você perdeu. Se, na primeira jogada, você fez um 4, 5, 6, 8, 9 ou 10,este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você 
perde, no entanto, se tirar um 7 antes de tirar este Ponto novamente. 
'''

import random

def lancar_dados():
	return random.randint(2, 12)


# ===
entrada = ""
jogada = 0
ponto = 0

print('\a Digite "sair" para sair.')
print('\a Aperte ENTER para rolar os dados.')
print('')
while (entrada != "sair"):
	jogada += 1
	print('Jogada: {}'.format(jogada))
	entrada = raw_input("Esperando ação: ")

	if entrada == "sair":
		print('Saindo do jogo... Tchau!')
		print('')

	else:
		if jogada > 1:
			print('Sua pontação é: {}'.format(ponto))
			print('')
	valor = lancar_dados()
	print('O valor do dado é {}\n\n'.format(valor))
	print('')
	if jogada == 1:
		if valor == 7 or valor == 11: 
			print('Você tirou um natural e ganhou. Parabéns!!!')
			print('-=' *15)
			print('')

		elif valor == 2 or valor == 3 or valor == 12:
			print('Você tirou um craps e perdeu. Melhor sorte na próxima vez...')
			print('-=' *15)
			print('')

		else:
			ponto = valor

	else:
		if valor == 7:
			print('Você tirou um 7 antes de repetir seu ponto. Você perdeu!')

		elif ponto == valor:
			print('Você conseguiu repetir seu ponto e ganhou. Parabéns!')
