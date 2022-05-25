>>> - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tuplas-em-python/modulos/exercicio-72-numero-por-extenso/
--------------------------------------------------------

Exercício Python 72: Crie um programa que tenha uma dupla totalmente preenchida 
com uma contagem por extenso, de zero até vinte. 
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

r = 'S'
num = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", 
	"nove", "dez", "onze", "doze", "treze", "quatorze", "quinze", "dezesseis", 
	"dezessete", "dezoito", "dezenove", "vinte")
while r == 'S':
	pass
	while True:
		num1 = int(input('Digite um número entre 0 a 20: \nr: '))
		if 0 <= num1 <= 20:
			break
		print('Tente novamente!'),
	r = str(input('Deseja continuar [S/N]: '))
print('')
print('Você digitou o número {}'.format(num[num1]))
print('>>> Acabou!')
--------------------------------------------------------

Exercício Python 73: Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do 
Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:

a) Os 5 primeiros times.

b) Os últimos 4 colocados.

c) Times em ordem alfabética.

d) Em que posição está o time da Chapecoense.

time = ('Corinthians', 'Palmeiras', 'Santos', 'Grêmio',
	'Cruzeiro', 'Flamengo', 'Vasco', 'Chapecoense', 'Atlético', 'Botafogo', 'Atlético-PR',
	'Bahia', 'São Paulo', 'Fluminense', 'Sport Recife', 'EC Vitória', 'Coritiba',
	'Avaí', 'Ponte Preta', 'Atlético-GO')
print('==' *15)
print('Lista do Brasileiro: {}'.format(time))
print('==' *15)
print('')
print('==' *15)
print('Os 5 primeiros times são: {}.'.format(time[0:5]))
print('==' *15)
print('')
print('==' *15)
print('Os 4 últimos times são: {}'.format(time[-4:]))
print('==' *15)
print('')
print('==' *15)
print('Ordem alfabética: {}'.format(sorted(time)))
print('==' *15)
print('')
print('==' *15)
print('O Chapecoense está na {}ª posição.'.format(time.index("Chapecoense")+1))
print('==' *15)
--------------------------------------------------------

Exercício Python 74: Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla. 
Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que 
estão na tupla.

from random import randint
num = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
print(num)
print('')
print('>>> O maior número: {}'.format(max(num)))
print('>>> O menor número: {}'.format(min(num)))
--------------------------------------------------------

Exercício Python 75: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os 
em uma tupla. No final, mostre:

A) Quantas vezes apareceu o valor 9.

B) Em que posição foi digitado o primeiro valor 3.

C) Quais foram os números pares.
% 2 == 0

n = (int(input('Digite um número: ')),
	int(input('Digite um número: ')),
	int(input('Digite um número: ')),
	int(input('Digite um número: ')))	
print('')
print('>>> O número 9 apareceu: {}x'.format(n.count(9)))
if 3 in n:
	print('O número 3 apareceu na: {}ª posição'.format(n.index(3)+1))
else:
	print('O valor "3" não registrado.')
for x in n:
	if x % 2 == 0:
		print('Os números pares são: {}'.format(x))
--------------------------------------------------------

Exercício Python 76: Crie um programa que tenha uma tupla única com nomes de produtos e seus 
respectivos preços, na sequência. No final, mostre uma listagem de preços, organizando 
os dados em forma tabular.

listagem = ('Lápis', 1.75,
	'Borracha', 2,
	'Caderno', 15.90,
	'Estojo', 25,
	'Transferidor', 4.20,
	'Compasso', 9.99,
	'Mochila', 120.32,
	'Canetas', 22.30,
	'Livro', 34.90)
print('-' *40)
print(f'{"Tabela de Preços!":^40}')
print('-' *40)
print('')
for pos in range(0, len(listagem)):
	if pos % 2 == 0:
		print(f'{listagem[pos]:.<30}'),
	else: 
		print(f'R${listagem[pos]:>7.2f}')
print('=' *40)
--------------------------------------------------------

Exercício Python 077: Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

palavras =('Curso', 'em', 'video', 'python')
for p in palavras:
	print(f'\nNa palavra {p.upper()} temos', end= '')
	for letra in p:
		if letra.lower() in 'aeiou':
			print(letra, end= ' ')