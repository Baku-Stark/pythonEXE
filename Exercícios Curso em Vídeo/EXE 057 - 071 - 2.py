>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/repeticoes-em-python-while/modulos/exercicio-57-validacao-de-dados/
--------------------------------------------------------

Exercício Python 57: Faça um programa que leia o sexo de uma pessoa, 
mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, peça a digitação 
novamente até ter um valor correto.

sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
#print(sexo)
while sexo not in 'MF':
	sexo = str(input('>>> Novamente: Informe seu sexo [M/F]: ')).upper()[0].strip()
print('')
print('-' *20)
sexom = 'M'
sexof = 'F'
if sexo == sexom:
	print('Sexo MASCULINO registrado com sucesso!')
else:
	print('Sexo FEMININO registrado com sucesso!')
print('-' *20)
--------------------------------------------------------

Exercício Python 58: Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número 
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final 
quantos palpites foram necessários para vencer.

from random import randint
friday = randint (0, 10)
print('Olá! Sou o sistema SEXTA-FEIRA!!!')
print('Chefe, acabei de pensar em um número de 0 até 10...')
print('')
acertou = False
palpites = 0
while not acertou:
	numero = int(input('''Qual número eu selecionei?
		r: '''))
	palpites += 1
	if numero == friday:
		acertou = True
print('')
print('-=' *15)
print('>>> Você acertou após {} tentativa(s)!!!'.format(palpites))
print('-=' *15)
.
.
.
.
.
from random import randint
friday = randint (0, 10)
print('Olá! Sou o sistema SEXTA-FEIRA!!!')
print('Chefe, acabei de pensar em um número de 0 até 10...')
print('')
acertou = False
palpites = 0
while not acertou:
	numero = int(input('''Qual número eu selecionei?
		r: '''))
	palpites += 1
	if numero == friday:
		acertou = True
	else:
		if numero < friday:
			print('>> O número é menor...')
		elif numero > friday:
			print('>> O número é maior...')
		print('')
print('')
print('-=' *15)
print('>>> Você acertou após {} tentativa(s)!!!'.format(palpites))
print('-=' *15)
--------------------------------------------------------

Exercício Python 59: Crie um programa que leia dois valores e mostre um menu na tela:

[ 1 ] somar

[ 2 ] multiplicar

[ 3 ] maior

[ 4 ] novos números

[ 5 ] sair do programa

Seu programa deverá realizar a operação solicitada em cada caso.

from time import sleep
n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
op = 0
print('')
print('-=' *15)
while op != 5:
	print(''' MAPA DE SINAIS
		[ 1 ] somar
		[ 2 ] multiplicar
		[ 3 ] maior
		[ 4 ] novos números
		[ 5 ] sair do programa
		''')
	op = int(input('>>> Qual sua opção: '))
	if op == 1:
		ressoma = n1 + n2
		print('>>> {} + {} = {}.'.format(n1, n2, ressoma))
	elif op == 2:
		resmulti = n1 * n2
		print('>>> {} X {} = {}.'.format(n1, n2, resmulti))
	elif op == 3:
		if n1 > n2:
			print('>>> {} é maior que {}.'.format(n1, n2))
		elif n1 == n2:
			print('>>> {} e {} são iguais!'.format(n1, n2))
		else:
			maior = n2
			print('>>> {} é menor que {}.'.format(n1, maior))
	elif op == 4:
		n1 = int(input('>>> Digite o primeiro valor: '))
		n2 = int(input('>>> Digite o segundo valor: '))
	elif op == 5:
		print('>>> Finalizando...')
		sleep(2)
	else:
		print('>>> Opção Inválida! <<<')
	print('')
	print('-=' *15)
print('')
print('Fim do programa!!!')
--------------------------------------------------------

Exercício Python 60: Faça um programa que leia um número qualquer e mostre o seu fatorial. 
Exemplo: 
5! = 5 x 4 x 3 x 2 x 1 = 120

from math import factorial
fatorial = int(input('Digite o valor: '))
f = factorial(fatorial)
print('>> Fatorial de {}! é: {}'.format(fatorial, f))
.
.
.
.
.
n = int(input('Digite um número para calcular o seu FATORIAL: '))
c = n
f = 1
print('Calculando {}! = '.format(n))
while c > 0:
	print('{}'.format(c), end='')
	print(' x ' if c > 1 else ' = ', end='')
	f *= c
	c -= 1
print('{}'.format(f))
--------------------------------------------------------

Exercício Python 61: Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, 
mostrando os 10 primeiros termos da progressão usando a estrutura while.
print('-=' *15)
print('Gerador de PA')
print('-=' *15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
while cont <= 10:
	print('- {}'.format(termo))
	termo += razao
	cont += 1
print('FIM!!')
.
.
.
.
.
print('-=' *15)
print('10 TERMOS DE UMA PA')
print('-=' *15)
print('')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for x in xrange(primeiro, decimo  + razao, razao):
	print('---')
	print('{}'.format(x))
	print('---')
print('ACABOU!')
--------------------------------------------------------
Exercício Python 62: Melhore o DESAFIO 61, perguntando para o usuário se ele quer 
mostrar mais alguns termos. O programa encerrará quando ele disser que quer mostrar 0 termos. 

print('-=' *15)
print('Gerador de PA')
print('-=' *15)
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
	total = total + mais
	while cont <= total:
		print('- {}'.format(termo))
		termo += razao
		cont += 1
	print('>>> PAUSE <<<')
	mais = int(input('Quer adicionar mais termos? Quantos: '))
print('')
print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM!!!')
--------------------------------------------------------

Exercício Python 63: Escreva um programa que leia um número N inteiro qualquer e mostre na 
tela os N primeiros elementos de uma Sequência de Fibonacci. Exemplo:
0 1 1 2 3 5 8 

print('-=' *15)
print('> Sequência de Fibonacci <')
print('-=' *15)
print('')
n = int(input('Quantos termos você quer mostrar: '))
t1 = 0
t2 = 1
print('{} -> {}'.format(t1, t2)), 
cont = 3
while cont <= n:
	t3 = t1 + t2
	print('-> {}'.format(t3)),
	t1 = t2
	t2 = t3
	cont += 1
print('[ FIM!!! ]')
--------------------------------------------------------

Exercício Python 64: Crie um programa que leia vários números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre eles 
(desconsiderando o flag).

n = 0
cont = 0
n = cont = soma = 0
while n != 999:
	n = int(input('''Digite um número (999 interrompe): 
		r: '''))
	soma = soma + n
	cont += 1
print('')
print('~~' *5)
print('''Você digitou {} números.
A soma entre eles é igual a {}'''.format(cont - 1, soma - 999))
print('FIM !!!')
--------------------------------------------------------

Exercício Python 65: Crie um programa que leia vários números inteiros pelo teclado. 
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor 
valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

soma = cont = media = maior = menor = 0
n = 0
cont = 0
r = 'S'
while r in 'S':
	print('-=' *5)
	n = int(input('Digite um número: '))
	soma += n
	cont += 1
	if cont == 1:
		maior = menor = n
	else:
		if n > maior:
			maior = n
		if n < menor:
			menor = n
	r = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
	print('-=' *5)
	print('')
media = soma / cont
print('')
print('Você digitou {} números e a média foi {}.'.format(cont, media))
print('''O maior valor: {}
O menor valor: {}'''.format(maior, menor))
print('Sessão encerrada!')
--------------------------------------------------------

Exercício Python 66: Crie um programa que leia números inteiros pelo teclado. 
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
No final, mostre quantos números foram digitados e qual foi a soma entre elas 
(desconsiderando o flag).


cont = soma = 0
while True:
	n = int(input('>>> Digite um número: \nr:'))
	soma += n
	cont += 1
	if n == 999:
		break
print('')
print('''A soma de todos os números é: {}
Foi digitado {} número(s) diferente(s)'''.format(soma -999, cont -1))
--------------------------------------------------------

Exercício Python 67: Faça um programa que mostre a tabuada de vários números, 
um de cada vez, para cada valor digitado pelo usuário. O programa será interrompido 
quando o número solicitado for negativo. 

while True:
	print('-=' *15)
	n = int(input('Numerador \nr: '))
	print('')
	print('[ TABUADA DE {}! ]'.format(n))
	print('~~' *5)
	if n <= 0:
		print('>>> Registro negativo...')
		print('~~' *5)
		break
	else:
		for x in xrange(0, 10):
			x += 1
			res = n * x
			print('{} x {} = {}'.format(n, x, res))
		print('~~' *5)
print('-=' *15)
print('')
print('>>>> Processo finalizado!!!!')
--------------------------------------------------------

Exercício Python 68: Faça um programa que jogue par ou ímpar com o computador. 
O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias 
consecutivas que ele conquistou no final do jogo. 

from random import randint
v = 0
while True:
	jogador = int(input('Escolha um número: '))
	friday = randint (0, 11)
	total = jogador + friday
	escolha = ' '
	print('~~' *5)
	while escolha not in 'PI':
		escolha = str(input('Escolha entre Par [P] ou Impar [I]: \nr: ')).strip().upper()[0]
	print('''	Jogador escolheu: {}
	Friday escolheu: {}
	>>> O resultado é: {}'''.format(jogador, friday, total))
	print('')
	if escolha == 'P':
		if total % 2 == 0:
			print('Jogador VENCEU!!!')
			v += 1
		else:
			print('Friday VENCEU!!!')
			break
	elif escolha == 'I':
		if total % 2 == 1:
			print('Jogador VENCEU!!!')
			v += 1
		else:
			print('Friday VENCEU!!!')
			break
	print('Vamos jogar novamente...')
	print('')
	print('~~' *5)
print('~~' *5)
print('''>>> GAME OVER!!!
O Jogador venceu {}x!'''.format(v))
--------------------------------------------------------

Exercício Python 69: Crie um programa que leia a idade e o sexo de várias pessoas. 
A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
No final, mostre:

A) quantas pessoas tem mais de 18 anos.

B) quantos homens foram cadastrados.

C) quantas mulheres tem menos de 20 anos. 


contp = contm = contf = 0
print('-=' *15)
while True:
	idade = int(input('>> Idade << \nr: '))	
	sexo = ' '
	while sexo not in 'MF':
		sexo = str(input('SEXO [M/F]: \nr: ')).upper().strip()[0]
	if idade >= 18:
		contp += 1
	if sexo == 'M':
		contm += 1
	if sexo == 'F' and idade < 20:
		contf += 1
	print('~~' *8)
	r = ' '
	while r not in 'SN':
		r = str(input('>>> Deseja continuar o registro? [S/N]\nr: ')).upper().strip()[0]
	if r == 'N':
		break
	print('~~' *8)
print('-=' *15)
print(''' RESULTADOS!!!
	>>> {} pessoa(s) tem mais de 18 anos;
	>>> {} homem(ns) foram registrados;
	>>> {} mulhere(es) possuem menos de 20 anos.'''.format(contp, contm, contf))
--------------------------------------------------------

Exercício Python 70: Crie um programa que leia o nome e o preço de vários produtos. 
O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:

A) qual é o total gasto na compra.

B) quantos produtos custam mais de R$1000.

C) qual é o nome do produto mais barato. 

print('-=' *15)
print('--- LOJA DO SEU TOBA ---')
print('-=' *15)
print('')
total = totmil = menor = cont = 0
barato = ' '
while True:
	nomeproduto = str(input('>>> Nome do Produto \nr: ')).strip().capitalize()
	preco = float(input('Preço do produto \nr: '))
	cont += 1
	total += preco
	if preco > 1000:
		totmil += 1
	if cont == 1 or preco < menor:
		menor = preco
		barato = nomeproduto
	print('')
	print('~~' *10)
	r = ' '
	while r not in 'SN':
		r = str(input('Registrar outro produto [S/N]? \nr: ')).upper().strip()
	if r == 'N':
		break
	print('~~' *10)
	print('')
print('| CHEQUE TOTAL DA COMPRA!!! |')
print('''  [ 1 ] - O total: R${:.2f} 
	[ 2 ] - Produtos acima de R$1000,00: {} 
	[ 3 ] - Produtos mais barato: {} -> R${:.2f}'''.format(total, totmil, barato, menor))
--------------------------------------------------------

Exercício Python 071: Crie um programa que simule o funcionamento de um caixa eletrônico. 
No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) e o programa 
vai informar quantas cédulas de cada valor serão entregues. OBS:

considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-=' *15)
print('--- BANCO CEV ---')
print('-=' *15)
print('')
valor = int(input('>>> Valor Do Saque \nr: '))
total = valor
ced = 50
totced = 0
while True:
	if total >= ced:
		total -= ced 
		totced += 1
	else:
		if totced > 0:
			print('[ Total de {} cédulas de R${} ! ]'.format(totced, ced))
		if ced == 50:
			ced = 20
		elif ced == 20:
			ced = 10
		elif ced == 10:
			ced = 1
		totced = 0
		if total == 0:
			break
print('=' *30)
print('Saque FINALIZADO! Volte sempre!!!')
--------------------------------------------------------

for x in xrange(0, 5):
	print(x)