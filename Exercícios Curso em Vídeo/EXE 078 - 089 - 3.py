>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/listas-em-python/modulos/exercicio-78-maior-e-menor-valores-na-lista/
--------------------------------------------------------

Exercício Python 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

listanum = []
mai = 0
men = 0
for c in xrange(0, 5):
	listanum.append(int(input('Digite um número na posição {} \nr: '.format(0))))
	if c == 0:
		mai = men = listanum[c]
	else:
		if listanum[c] > mai:
			mai = listanum[c]
		if listanum[c] < men:
			men = listanum[c]
print('=-' *30)
print('>>> Você digitou os valores: {}'.format(listanum))
print('>>> O maior número foi [{}] nas posições'.format(mai)),
for i, v in enumerate(listanum):
	if v == mai:
		print('[{}].'.format(i))
print('')
print('O menor valor digitado foi [{}] nas posições'.format(men)),
for i, v in enumerate(listanum):
	if v == men:
		print('[{}].'.format(i))
print('=-' *30)
print('')
--------------------------------------------------------

Exercício Python 79: Crie um programa onde o usuário possa digitar vários valores numéricos e 
cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado. No final, 
serão exibidos todos os valores únicos digitados, em ordem crescente.

numeros = list()
print('~~' *15)
while True:
	n = int(input('Digite um valor: '))
	if n not in numeros:
		numeros.append(n)
		print('--- Valor adicionado com sucesso... ---')
	else:
		print('--- Valor recusado... Duplicação! ---')
	r = str(input('>>> Quer continuar? [S/N] \nr: ')).upper().strip()[0]
	if r == 'N':
		break
	print('')
	print('~~' *15)
print('-=' *30)
numeros.sort()
print('Você digitou os valores: {}'.format(numeros))
--------------------------------------------------------

Exercício Python 80: Crie um programa onde o usuário possa digitar cinco valores numéricos e 
cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, 
mostre a lista ordenada na tela.

lista = []
for c in xrange(0, 5):
	n = int(input('Digite um valor: '))
	if c == 0 or n > lista[-1]:
		lista.append(n)
		print('--- Adicionado ao FINAL da lista! ---')
	else:
		pos = 0
		while pos < len(lista):
			if n <= lista[pos]:
				lista.insert(pos, n)
				print('--- Seletado na posição {} da lista! ---'.format(pos))
				break
			pos += 1
print('-=' *30)
print('Os valores digitados em ordem foram {}'.format(lista))
--------------------------------------------------------

Exercício Python 81: Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:                                                    
A) Quantos números foram digitados. ---              
B) A lista de valores, ordenada de forma decrescente. ---                                                                                        
C) Se o valor 5 foi digitado e está ou não na lista. ---

numeros = []
cont = 0
cont5 = 0
print('-=' *30)
while True:
	cont += 1
	n = int(input('Digite um número \nr: '))
	numeros.append(n)
	if n == 5:
		cont5 += 1
		#print(registro feito!)
	print('')
	r = str(input('>>> Continuar [S/N]: ')).upper().strip()
	if r == 'N':
		break
	print('~~' *15)
	print('')
print('-=' *30)
print('--- RESULTADOS ---')
print('Foram digitados {} números!'.format(cont)),
print(numeros)
numeros.sort(reverse=True)
print('Ordem decrescente dos números: {}.'.format(numeros))
if cont5 >= 1:
	print('''O número 5 foi digitado e está na lista!''')
else:
	print('O número 5 NÃO foi digitado!')
print('>>> Acabou!')
--------------------------------------------------------

Exercício Python 82: Crie um programa que vai ler vários números e 
colocar em uma lista. Depois disso, crie duas listas extras que vão conter apenas 
os valores pares e os valores ímpares digitados, respectivamente. Ao final, mostre o 
conteúdo das três listas geradas.

numerospares = []
numerosimpares = []
contpar = 0
contimpar = 0
print('-=' *30)
while True:
	n = int(input('Digite um valor \nr: '))
	if n % 2 == 0:
		contpar += 1
		numerospares.append(n)
	else:
		contimpar += 1
		numerosimpares.append(n)
	r = str(input('Continuar \n[S/N]:')).upper().strip()
	if r == 'N':
		break
	print('~~' *15)
	print('')
print('-=' *30)
print('--- Números Pares:')
print(numerospares)
print('--- Números Impares:')
print(numerosimpares)
print('>>> Foi digitado {} números PARES e {} IMPARES!!!'.format(contpar, contimpar))
--------------------------------------------------------

Exercício Python 83: Crie um programa onde o usuário digite uma expressão qualquer que use 
parênteses. Seu aplicativo deverá analisar se a expressão passada está com os parênteses 
abertos e fechados na ordem correta.

expressao = str(input('Escreva sua expressao: '))
pilha = []
for simb in expressao:
	if simb in "(":
		pilha.append('(')
	elif simb in ")":
		if len(pilha) > 0:
			pilha.pop()
		else:
			pilha.append(')')
			break
if len(pilha) == 0:
	print('>>> Sua expressão está válida!')
else:
	print('>>> Expressão inválida!')
--------------------------------------------------------
{PARTE 2}
Exercício Python 84: Faça um programa que leia nome e peso de várias pessoas,                                      
guardando tudo em uma lista. No final, mostre:                                                                                                    
A) Quantas pessoas foram cadastradas.                                                                                                                
B) Uma listagem com as pessoas mais pesadas.                                                                                                    
C) Uma listagem com as pessoas mais leves.

temp = []
princ = []
mai = men = 0
print('-' *30)
while True:
	temp.append(str(input('>>> Nome \nr: ')))
	temp.append(float(input('>>> Peso \nr: ')))
	if len(princ) == 0:
		mai = men == temp[1]
	else:
		if temp[1] > mai:
			mai = temp[1]
		if temp[1] < men:
			men = temp[1]
	princ.append(temp[:])
	temp.clear()
	print('')
	print('=' *15)
	r = str(input('>>> Deseja continuar \n[S/N]: ')).upper().strip()
	if r == 'N':
		break
		print('=' *15)
		print('')
	print('=' *15)
	print('')
print('-' *30)
print('Ao todo, você cadastrou {} pessoas'.format(len(princ)))
print('O maior peso foi de: {}kg.'.format(mai))
for p in princ:
	if p[1] == mai:
		print('{}'.format(p[0]))
print('')
print('O menor peso foi de: {}kg'.format(men))
print('-' *30)
--------------------------------------------------------

Exercício Python 85: Crie um programa onde o usuário possa digitar 
sete valores numéricos e cadastre-os em uma lista única que mantenha separados os 
valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.

num = [[], []]
valor = 0
print('-' *20)
for n in range(1, 8):
	valor = int(input('Digite o {}° número: '.format(n)))
	if valor % 2 == 0:
		num[0].append(valor) 
	else:
		num[1].append(valor)
	print('-' *20)
print('')
print('')
print('=' *30)
num[0].sort()
num[1].sort()
print('>>>Lista: {}'.format(num))
print('{} são pares!'.format(num[0]))
print('{} são impares'.format(num[1]))
print('=' *30)
--------------------------------------------------------

Exercício Python 86: Crie um programa que declare uma matriz de dimensão 3×3 e preencha com 
valores lidos pelo teclado. No final, mostre a matriz na tela, com a formatação correta.

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print('')
for l in range(0, 3):
	for c in range(0 ,3):
		matriz[l][c] = int(input('>>> Digite o valor para a [{}, {}] \nr: '.format(l, c)))
print('')
print('=' *30)
print('Listagem: {}'.format(matriz))
print('-' *15)
print('')
for l in range(0, 3):
	for c in range(0 ,3):
		print('{}'.format(matriz[l][c])),
	print('')
print('=' *30)
--------------------------------------------------------

Exercício Python 87: Aprimore o desafio anterior, mostrando no final:                                                    
A) A soma de todos os valores pares digitados.                                                                                                  
B) A soma dos valores da terceira coluna.                                                                                                                
C) O maior valor da segunda linha. ---

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
spar = mai = scol = 0
for l in range(0, 3):
	for c in range(0, 3):
		matriz[l][c] = int(input('>>> Digite o valor para a [{}, {}] \nr: '.format(l, c)))
print('=' *30)
print('Listagem: {}'.format(matriz))
print('-' *15)
print('')
for l in range(0, 3):
	for c in range(0, 3):
		print('{}'.format(matriz[l][c])),
		if matriz[l][c] % 2 == 0:
			spar += matriz[l][c]
	print('')
print('=' *30)
print('')
print('')
print('A soma dos valores pares é: {}.'.format(spar))
for l in range(0, 3):
	scol += matriz[l][2]
print('')
print('A soma dos valores da terceira coluna é: {}.'.format(scol))
print('')
for c in range(0, 3):
	if c == 0:
		mai = matriz[1][c]
	elif matriz[1][c] > mai:
		mai = matriz[1][c]
print('O maior valor da SEGUNDA LINHA é: {}.'.format(mai))
--------------------------------------------------------

Exercício Python 88: Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear 6 números entre 1 e 60 
para cada jogo, cadastrando tudo em uma lista composta.

from random import randint
lista = list()
jogos = list()
print('=' *30)
print('--- SORTEIO DA MEGA SENA ---')
print('=' *30)
print('')
quant = int(input('Quantos jogos você quer que eu sorteie? \nr: '))
real = quant - 1
tot = 0
while tot <= real:
	cont = 0
	while True:
		num = randint(1, 60)
		if num not in lista:
			lista.append(num)
			cont += 1
		if cont >= 6:
			break
	jogos.append(lista[:])
	del lista[:]
	tot += 1
print('')
print('')
print('=' *30)
print('   Sorteando {} jogos!    '.format(quant))
for i, l in enumerate(jogos):
	print('--- {}° JOGO: {}.'.format(i+1, l))
print('=' *30)
--------------------------------------------------------

Exercício Python 89: Crie um programa que leia nome e duas notas de vários alunos e guarde 
tudo em uma lista composta. No final, mostre um boletim contendo a média de cada um e 
permita que o usuário possa mostrar as notas de cada aluno individualmente.

ficha = list()
while True:
	nome = str(input('Nome do(a) aluno(a): ')).capitalize().strip()
	nota1 = float(input('1ª Nota: '))
	nota2 = float(input('2º Nota: '))
	media = (nota1 + nota2) / 2
	print('')
	ficha.append([nome, [nota1, nota2], media])
	r = str(input('Mostrar outro aluno? \n[S/N] r: ')).upper()
	if r == 'N':
		break
		print('')
	print('')
print('=-' *30)
print('"N°."{:<4}"NOME"{:<10}"MÉDIA"{:>8}')
print('-' *26)
for i, a in enumerate(ficha):
	print('{:<4}{:<10}{:>8.1f}'.format(i+1, a[0], a[2]))
print('')
print('>>> Fechou!')
--------------------------------------------------------