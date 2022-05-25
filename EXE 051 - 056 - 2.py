>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/repeticoes-em-python-for/modulos/exercicio-51-progressao-aritmetica/
--------------------------------------------------------

Exercício Python 51: Desenvolva um programa que leia o primeiro termo e a 
razão de uma PA. No final, mostre os 10 primeiros termos dessa progressão.

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

print('-=' *15)
print('10 TERMOS DE UMA PA')
print('-=' *15)
print('')
primeiro = int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = primeiro + (10 - 1) * razao
for x in xrange(primeiro, decimo  + razao, razao):
	print('---')
	print('{}'.format(x), end= '->>')
	print('---')
print('ACABOU!')
--------------------------------------------------------

Exercício Python 52: Faça um programa que leia um número inteiro e diga se 
ele é ou não um número primo. 

num = int(input('Digite um número: '))
tot = 0
for x in xrange(1, num +1):
	if num % x == 0:
		print('\033[34m') #Azul (Divisível)
		tot += 1
	else:
		print('\033[31m') #Vermelho (Não divisível)
	print('{}'.format(x))
print('')
print('\033[mNúmero {} foi divisível {}x!'.format(num, tot))
print('')
if tot == 2:
	print('O número {} é PRIMO!'.format(num))
else:
	print('O número {} NÃO é PRIMO!'.format(num))
--------------------------------------------------------

Exercício Python 53: Crie um programa que leia uma frase qualquer e diga se 
ela é um palíndromo, desconsiderando os espaços. Exemplos de palíndromos:

- APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, 
ANOTARAM A DATA DA MARATONA.
'''Exemplos de Palíndromos:
	[] - Apos a sopa
	[] - A sacada da casa
	[] - A torre da derrota
	[] - O lobo ama o bolo
	[] - Anotaram a data da maratona'''


frase = str(input('Digite uma frase: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
print('')
for letra in xrange(len(junto) - 1, - 1, -1):
	inverso += junto[letra]
print('''O inverso é: {}.'
'E a frase normal é: {}.'''.format(junto, inverso))
print('')
if inverso == junto:
	print('A frase é um palíndromo.')
else:
	print('A frase NÃO é um palíndromo.')
--------------------------------------------------------

Exercício Python 54: Crie um programa que leia o ano de nascimento de sete 
pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e 
quantas já são maiores.

from datetime import date
from time import sleep
atual = date.today().year
totmaior = 0
totmenor = 0
print('-=' *15)
for x in xrange(1, 8):
	nasc = int(input('''Em que ano a {}ª pessoa nasceu?
		r: '''.format(x)))
	print('')
	print('[Processo de análise...]')
	sleep(1)
	print('')
	resultado = atual - nasc
	if resultado >= 21:
		print('>>> Essa pessoa está na MAIORIDADE!')
		totmaior += 1
	else:
		totmenor += 1
		print('>>> Essa pessoa está na MENORIDADE!')
	print('')
print('-' *6)
print('Ao todo, {} pessoas são maiores.'.format(totmaior))
print('E {} pessoas são menores.'.format(totmenor))
print('-' *6)
print('-=' *15)
--------------------------------------------------------

Exercício Python 55: Faça um programa que leia o peso de cinco pessoas. 
No final, mostre qual foi o maior e o menor peso lidos.

maior = 0
menor = 0
for x in xrange(1, 6):
	peso = float(input('''Peso (Kg) da {}ª pessoa: 
		r: '''.format(x)))
	if x == 1:
		maior = peso
		menor = peso
	else:
		if peso > maior:
			maior = peso
		if peso < menor:
			menor = peso
print('')
print('A pessoa com MAIOR peso tem {}Kg'.format(maior))
print('A pessoa com MENOR peso tem {}Kg'.format(menor))
--------------------------------------------------------

Exercício Python 56: Desenvolva um programa que leia o nome, idade e sexo 
de 4 pessoas. No final do programa, mostre: a média de idade do grupo, 
qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.

somaidade = 0
mediaidade = 0
maioridadeh = 0
totmulher20 = 0
nomevelho = ''
for x in xrange(1, 5):
	print('--- {}ª PESSOA ---'.format(x))
	nome = str(input('Nome: ')).strip()
	idade = int(input('Idade: '))
	sexo = str(input('Sexo[M/F]: ')).strip().upper()
	somaidade += idade
	if x == 1 and sexo == 'M':
		maioridadeh = idade
		nomevelho = nome
	if sexo in "M" and idade > maioridadeh:
		maioridadeh = idade
		nomevelho = nome
	if sexo in "F" and idade < 20:
		totmulher20 += 1
	print('')
mediaidade = somaidade / 4
print('=====')
print('>>> A média de idade do grupo é de: {}.'.format(mediaidade))
print('')
print('''>>> O homem mais velho se chama {} e tem {} ano(s).
	'''.format(nomevelho, maioridadeh))
print('')
print('''>>> Ao todo, são {} mulheres com menos de 20 anos.
	'''.format(totmulher20))
--------------------------------------------------------