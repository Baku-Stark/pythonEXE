>>>  - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/usando-modulos-do-python/modulos/exercicio-25-procurando-uma-string-dentro-de-outra/
--------------------------------------------------------

Exercício Python 25: Crie um programa que leia o nome de uma pessoa e diga 
se ela tem “SILVA” no nome.

print('Descobrir se o nome possui SILVA!')
print('')
name = str(input('Digite seu nome completo: ')).capitalize().strip()
print('')
print('-' *20)
if name <= 'Silva':
	print('Veradeiro!!')
else:
	print('Falso!!!')
print('-' *20)
--------------------------------------------------------

Exercício Python 26: Faça um programa que leia uma frase pelo teclado e 
mostre quantas vezes aparece a letra “A”, em que posição ela aparece a 
primeira vez e em que posição ela aparece a última vez.


frase = str(input('Digite uma frase: ')).strip().upper()
print('')
print('Analisando o resultado....')
print('')
#Quantas vezes aparece a letra "A"
print('A letra "A" aparece: {} vez(es).'.format(frase.count('A')))
#Em que posição ele aparece pela primeira vez
print('A letra "A" aparece pela primeira vez na posição: {}'.format(frase.find('A')))
#Em que posição ele aparece pela última vez
print('A letra "A" aparece pela última vez na posição: {}'.format(frase.rfind('A')))
--------------------------------------------------------

Exercício Python 27: Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente. 

name = str(input('Digite seu nome completo: '))
print('Prazer em conhecê-lo, {}!'.format(name))
print('')
print('-' *20)
namesplit = name.split()
#print(namesplit)
print('Seu primeiro nome é {}.'.format(namesplit[0]))
print('')
print('Seu último nome é {}.'.format(namesplit[len(namesplit)-1]))
print('-' *20)
--------------------------------------------------------

Exercício Python 28: Escreva um programa que faça o computador “pensar” em um 
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
número escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.

from random import randint
from time import sleep
print('-=' *20)
print('\033[34mJOGO DA ADIVINHAÇÃO !!!\033[m')
print('-=' *20)
print('')
computador = randint (0, 5)
print('Pensei em um número!!!')
#print('Pensei no número {}'.format(computador))
print('')
player1 = int(input('Em que número eu pensei: '))
print('')
print('PROCESSANDO...')
sleep(4)
if player1 == computador:
	print('Parabéns!!! Você acertou e venceu o jogo!')
else:
	print('Não foi desta vez...')

