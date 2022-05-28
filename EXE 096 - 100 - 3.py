>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/funcoes-em-python/modulos/exercicio-96-funcao-que-calcula-area/
--------------------------------------------------------

Exercício Python 96: Faça um programa que tenha uma função chamada área(), 
que receba as dimensões de um terreno retangular (largura e comprimento) e mostre a 
área do terreno.


def area(base, altura):
	area_retangular = base * altura
	print('A área de {}x{} é de {}m².'.format(base, altura, area_retangular))


print('Controle de terreno')
print('-' *20)
print('')
base = float(input('- Base (m): '))
altura = float(input('- Altura (m): '))
area(base, altura)
--------------------------------------------------------

Exercício Python 97: Faça um programa que tenha uma função chamada escreva(), 
que receba um texto qualquer como parâmetro e mostre uma mensagem com tamanho adaptável.

def escreva(msg):
	tamanho = len(msg) +4
	print('-' *tamanho)
	print('  {}'.format(msg))
	print('-' *tamanho)


escreva('Wallace De Freitas Moura Dos Santos')
--------------------------------------------------------

Exercício Python 98: Faça um programa que tenha uma função chamada contador(), 
que receba três parâmetros: início, fim e passo. Seu programa tem que realizar três contagens
através da função criada:      

a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada

from time import sleep


def contador(i, f, p):
	if p < 0:
		p *= -1
	if p == 0:
		p = 1
	print('-=' *20)
	print('>>> Contagem de {} até {} de {} em {}:'.format(i , f, p, p))
	sleep(0.5)

	if i < f:
		cont = i
		while cont <= f:
			print('{}'.format(cont)),
			sleep(0.5)
			cont += p
		print('... FIM!')
	else: 
		cont = i
		while cont >= f:
			print('{}'.format(cont)),
			sleep(0.5)
			cont -= p
		print('... FIM!')


# -----
print('')
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' *20)
print('')
print('--- Faça uma contagem personalizada ---')
ini = int(input('>>> Início: '))
fim = int(input('>>> Fim: '))
pas = int(input('>>> Passo: '))
contador(ini, fim, pas)
--------------------------------------------------------

Exercício Python 99: Faça um programa que tenha uma função chamada maior(), que receba vários 
parâmetros com valores inteiros. Seu programa tem que analisar todos os valores e dizer qual deles 
é o maior.

from time import sleep

def maior(* num):
	cont = maior  = 0
	print('-=' *30)
	print('Analisando os valores passados... ')
	for valor in num:
		print('{}'.format(valor)),
		sleep(0.3)
		if cont == 0:
			maior = valor
		else:
			if valor > maior:
				maior = valor
		cont += 1
	print('Foram informados {} valor ao todo.'.format(cont))
	print('O maior valor informado foi {}.'.format(maior))
	print('-=' *30)
	print('')


# -----
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
--------------------------------------------------------

Exercício Python 100: Faça um programa que tenha uma lista chamada números e duas funções chamadas 
sorteia() e somaPar(). A primeira função vai sortear 5 números e vai colocá-los dentro da lista e a 
segunda função vai mostrar a soma entre todos os valores pares sorteados pela função anterior.

from random import randint
from time import sleep

def sorteia(lista):
	print('-=' *25)
	print('--- Sorteando 5 valores: ')
	for cont in range(0, 5):
		n = randint(1, 10)
		lista.append((n))
		print('{}'.format(n)),
		sleep(0.3)
	print('Finalizado!!!')
	print('-=' *25)
	print('')

def somaPar(lista):
	soma = 0
	for valor in lista:
		if valor % 2 ==0:
			soma += valor
	print('>>> Somando os valores pares de {}, temos: {}.'.format(lista, soma))
numeros = []
sorteia(numeros)
somaPar(numeros)
#print(numeros)
--------------------------------------------------------