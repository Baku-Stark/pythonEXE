Utilizar "print" e "input"

print('Olá, Mundo!!')

nome = input('Digite seu nome \nr: ')
print('Seja bem-vindo ao Python, {}!!!'.format(nome))

_________________________________________________________________________
Somar e Subtrair

num1 = int(input('Digite o 1° número: '))
num2 = int(input('Digite o 2° número: '))
soma = num1 + num2
print('')
print('Adição: {}'.format(soma)) 

if num1 > num2:
	sub = num1 - num2
	print('Subtração: {}'.format(sub))
else:
	sub = num2 - num1
	print('Subtração: {}'.format(sub))

_________________________________________________________________________
Mostrar o tipo primitivo:

a = input('Digite Algo: ')
print('>>> O tipo primitivo da sua resposta é {}'.format(type(a)))
### --- O tipo primitivo da sua resposta é <type 'str'>
## Informações:
print('O valor [{}] é um número?'.format(a.isnumeric()))
print('O valor [{}] é um alfabeto?'.format(a.isalpha()))
print('O valor [{}] é um alfa-número?'.format(a.isalnum()))

_________________________________________________________________________
Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

num = int(input('Registre um número: '))
print('')
antecessor = num - 1
sucessor = num + 1
print('-' *30)
print('''O Sucessor de {} é: {}
O Antecessor de {} é: {}'''.format(num, sucessor, num, antecessor))
print('-' *30)

_________________________________________________________________________
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

num = int(input('Registre número: '))
dobro = num *2
triplo = num *3
rq = num **(0.5)
print('')
print('-=' *30)
print('''Dobro: {}
Triplo: {}
Raiz Quadrada: {:.0f}'''.format(dobro, triplo, rq))
print('-=' *30)

_________________________________________________________________________
Escreva um programa que um valor em metros e o exiba convertido em 
centímetros e milímetros.

num = float(input('Registre um comprimento (metros) \nr: '))
cm = num *100
ml = num *1000
print('')
print('-=' *30)
print('--- Comprimento selecionado: {:.0f}'.format(num))
print('''Centímetros: {:.0f} --- multiplique por 100
Milímetros: {:.0f} ---	multiplique por 1000'''.format(cm, ml))

_________________________________________________________________________
Tabuada

print('-=' *30)
print('--- TABUADA ---')
print('-=' *30)
print('')
num = int(input('>>> Escolha um número \nr: '))
print('')
print('-' *30)
print('--- Numerador: {}'.format(num))
for n in xrange(1, 11):
	multi = num * n
	print('{} x {} = {}'.format(num, n, multi))
print('-' *30)

_________________________________________________________________________
Conversão

UR$1,00 = R$4,70
1 Real/BRL (790) = 0,2126528 Dólar dos Estados Unidos/USD (220) /divisão por 4,70
1 Dólar dos Estados Unidos/USD (220) = 4,7025001 Real/BRL (790) *multiplicação por 4,70

valor = float(input('>>> Digite o valor (Real): '))
conversao_dolar = valor / 4.70
print('')
print('-=' *30)
print('--- Conversão para Dólar ---')
print('>>  UR${:.2f}'.format(conversao_dolar))
print('-=' *30)
_________________________________________________________________________
Pintando A Parede (QUADRADO e RETANGULO) A = b x a

alt = float(input('Selecione a ALTURA: '))
larg = float(input('Selecione a LARGURA: '))
area = larg * alt
print('')
print('=-' *30)
print('Altura: {} --- Largura: {}'.format(alt, larg))
tinta = area / 2
print('Será nenecessário {}L de tinta para pintar uma parede de {}m² de área.'.format(tinta, area))
print('=-' *30)
_________________________________________________________________________
Calcular Desconto (5%)

produto = str(input('>>> Nome do produto: \nr: '))
pewant = float(input('>>> Preço do produto \nr: '))
desconto = pewant - (pewant * 5/100)
print('')
print('')
print('--' *30)
print('--- Total')
print('')
print('>>> {}'.format(produto))
print('>>> Seu desconto é de: {:.2f}.'.format(desconto))
print('--' *30)

_________________________________________________________________________
Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento.

salario = float(input('Registre seu salário \nr: '))
aumento = salario + (salario * 15/100)
print('')
print('-' *30)
print('O novo salário com 15% de aumento: R${:.2f}'.format(aumento))
print('-' *30)

_________________________________________________________________________
Escreva um programa que converta uma temperatura 
digitando em graus Celsius e converta para graus Fahrenheit.

Celsius 1°C -> Fahrenheit 41°F

celsius = float(input('>>> Registre a temperatura (°C) \nr:'))
fahrenheit = (celsius * 9/5) + 32
print('')
print('-' *30)
print('(0 * 9/5) + 32')
print(' >>> Temperatura convertida para Fahrenheit: {}°F'.format(fahrenheit))
print('-' *30)

_________________________________________________________________________
Escreva um programa que pergunte a quantidade de Km percorridos por um 
carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
R$0,15 por Km rodado.

1 dia = R$60,00
1 km = R$0,15

km = float(input('>>> Quilômetro percorrido (Km) \nr: '))
print('')
dia = int(input('>>> Tempo do aluguel \nr: '))
print('')
print('-' *30)
km_pagar = km * 0.15
dia_pagar = dia * 60
print('--- RESULTADO ---')
print('''KM: {}
Dia: {}'''.format(km_pagar, dia_pagar))
print('')
tot = dia_pagar + km_pagar
print('Total a pagar: R${}'.format(tot))
print('-' *30)

_________________________________________________________________________
Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um número: '))
print('')
print('A porção inteira dessa valor é: {}.'.format(int(num)))

_________________________________________________________________________
Faça um programa que leia o comprimento do cateto oposto 
e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento 
da hipotenusa.

 Teorema da Pitágoras: <a² = b² + c³ -> **2> 

cat_op = int(input(' Registre o CATETO OPOSTO: '))
cat_ad = int(input(' Registre o CATETO ADJACENTE: '))
hipotenusa = cat_op * cat_ad
print('')
print('-' *30)
print('A HIPOTENUSA vale: {}'.format(hipotenusa))
print('-' *30)

_________________________________________________________________________
Faça um programa que leia um ângulo qualquer e mostre na 
tela o valor do seno, cosseno e tangente desse ângulo. 

import math
angulo = float(input('Informe o ângulo \nr: '))
print('')
print('-' *30)
seno =  math.sin(math.radians(angulo))
print('O ângulo {:.0f}° vale: {:.2f} --- SENO'.format(angulo, seno))
print('')
cosseno = math.cos(math.radians(angulo))
print('O ângulo {:.0f}° vale: {:.2f} --- COSSENO'.format(angulo, cosseno))
print('')
tangente = math.tan(math.radians(angulo))
print('O ângulo {:.0f}° vale: {:.2f} --- TANGENTE'.format(angulo, tangente))
print('-' *30)

_________________________________________________________________________
Um professor quer sortear um dos seus quatro alunos para 
apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e 
escrevendo na tela o nome do escolhido.

from random import choice

num1 = str(input('Registre o 1° aluno: '))
num2 = str(input('Registre o 2° aluno: '))
num3 = str(input('Registre o 3° aluno: '))
num4 = str(input('Registre o 4° aluno: '))
print('')
print('-' *30)
lista = [num1, num2, num3, num4]
escolha = choice(lista)
print('O aluno selecionado foi... {}!!'.format(escolha))
print('-' *30)

O mesmo professor do desafio 19 quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 
quatro alunos e mostre a ordem sorteada.

from random import shuffle

num1 = str(input('Registre o 1° aluno: '))
num2 = str(input('Registre o 2° aluno: '))
num3 = str(input('Registre o 3° aluno: '))
num4 = str(input('Registre o 4° aluno: '))
print('')
print('-' *30)
lista = [num1, num2, num3, num4]
escolha = shuffle(lista)
print('A ordem da apresentação... {}!!'.format(lista))
print('-' *30)

_________________________________________________________________________
Faça um programa em Python que abra e reproduza o áudio 
de um arquivo MP3.

import pygame
pygame.init()
pygame.mixer.music.load('imp.mp3')
pygame.mixer.music.play()
pygame.event.wait()

#pip install playsound
from playsound import playsound
playsound('imp.mp3')

_________________________________________________________________________
Crie um programa que leia o nome completo de uma pessoa e 
mostre:

– O nome com todas as letras maiúsculas e minúsculas.

– Quantas letras ao todo (sem considerar espaços).

– Quantas letras tem o primeiro nome.

nome = str(input('Digite seu nome completo: '))
print('')
print('-' *30)
print('''>>> Seu nome MAIÚSCULO: {}
>>> Seu nome MINÚSCULO: {}'''.format(nome.upper(), nome.lower()))
print('')
print('>>> Seu nome possui {} letras.'.format(len(nome) - nome.count(' ')))
print('')
print('>>> O primeiro nome possui {} letras'.format(nome.find(' ')))
separa = nome.split()
print('----- E seu primeiro nome é: {}.'.format(separa[0]))
print('-' *30)

_________________________________________________________________________
Faça um programa que leia um número de 0 a 9999 e 
mostre na tela cada um dos dígitos separados.

valor = int(input('Digite um valor: '))
n = str(valor)
print('')
print('-=' *30)
print('Valor escolhido: {}'.format(valor))
print('-----')
print('[Unidade: {}]'.format(n[3]))
print('[Dezena:  {}]'.format(n[2]))
print('[Centena: {}]'.format(n[1]))
print('[Milhar:  {}]'.format(n[0]))
print('-=' *30)

_________________________________________________________________________
Crie um programa que leia o nome de uma cidade diga se 
ela começa ou não com o nome “SANTO”.

city = str(input('Nome da cidade: ')).capitalize().strip()
print('')
if city[:5] == "Santo":
	print('A cidade começa com SANTO.')
else:
	print('A cidade não começa com SANTO.')

_________________________________________________________________________
Crie um programa que leia o nome de uma pessoa e diga 
se ela tem “SILVA” no nome.

nome = str(input('Digite seu nome inteiro: ')).upper().strip()
print('')
print('>>> Seu nome possui Silva? \n{}'.format('SILVA' in nome))

_________________________________________________________________________
Faça um programa que leia uma frase pelo teclado e 
mostre quantas vezes aparece a letra “A”, em que posição ela aparece a 
primeira vez e em que posição ela aparece a última vez.
- #Quantas vezes aparece a letra "A" 
.count('A')
- #Em que posição ele aparece pela primeira vez 
.find('A')
- #Em que posição ele aparece pela última vez 
.rfind('A')

frase = str(input('Digite uma frase: ')).strip().upper()
print('')
print('-=' *30)
print('''>>> A letra "A" aparece: {}x
>>> A posição em que aparece pela 1ª vez: {}
>>> A posição em que aparece pela última vez: {}'''
.format(frase.count('A'), frase.find('A'), frase.rfind('A')))
print('-=' *30)

_________________________________________________________________________
Faça um programa que leia o nome completo de uma pessoa, 
mostrando em seguida o primeiro e o último nome separadamente. 

nome = str(input('Digite seu nome completo: '))
print('')
print('--- Prazer em conhece-lo, {}!'.format(nome))
print('')
print('-=' *30)
nomesplit = nome.split()
print('''>>> Seu primeiro nome é: {}
>>> Seu último nome é: {}'''.format(nomesplit[0], nomesplit[-1]))
print('-=' *30)

_________________________________________________________________________
Escreva um programa que faça o computador “pensar” em um 
número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o 
número escolhido pelo computador. O programa deverá escrever na tela se o 
usuário venceu ou perdeu.

from random import randint
from time import sleep

print('-=' *30)
print('--- JOGO DA ADIVINHAÇÃO!!! ---')
print('-=' *30)
print('')
computador = randint(0, 5)
print('COMPUTADOR: Já pensei em um número... Tente adivinhar!')
print('')
jogador = int(input('>>> Escolha um número de 0 à 5: '))
print('')
print('Processando resultado...')
sleep(1)
print('')
print('-' *30)
if jogador == computador:
	print('>>> \033[1;32mVocê acertou!!!\033[m')
else:
	print('>>> \033[1;31mVocê errou na adivinhação...\033[m')
print('-' *30)

_________________________________________________________________________
Crie um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep

registro = int(input('-- Registre a velocidade -- \nr [Km/h]: '))
print('')
print('-' *30)
if registro < 80:
	print('>>> O registro está sendo efetuado...')
	sleep(1)
	print('O motorista não possui nenhuma multa!!!')
else:
	print('>>> O registro está sendo efetuado...')
	sleep(1)
	limite = registro - 80
	multa = limite * 7
	print('')
	print('''Ultrapassou o limite!!!
	\033[1;34m--- Sua multa: R${:.2f}\033[m'''.format(multa))
print('-' *30)

_________________________________________________________________________
Crie um programa que leia um número inteiro e mostre na 
tela se ele é PAR ou ÍMPAR.

numr = int(input('Digite um número: '))
print('')
num = numr % 2
if num == 0:
	print('O número é PAR!!')
else:
	print('O número é ÍMPAR')

_________________________________________________________________________
Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 parta viagens mais longas.

print('=-' *30)
print('--- TAM VIAGENS ---')
print('=-' *30)
print('')
dist = float(input('>>> Registre a distância [Km]: '))
print('')
if dist <= 200:
	resultado = dist *0.50
	print('Custo da passagem (CURTA): R${:.2f}'.format(resultado))
if dist > 200:
	resultado_longa = dist *0.45
	print('Custo da passagem (LONGA): R${:.2f}'.format(resultado_longa))

_________________________________________________________________________
Faça um programa que leia um ano qualquer e mostre se ele 
é bissexto.

ano = int(input('Escolha o ano: '))
print('')
if ano % 4 == 0 and ano  % 100 != 0 or ano % 400 == 0:
	print('O ano {} é BISSEXTO'.format(ano))
else:
	print('O ano {} não é BISSEXTO'.format(ano)) 

_________________________________________________________________________
Faça um programa que leia três números e mostre qual é o 
maior e qual é o menor.

num1 = int(input('Escolha o 1° número \nr:'))
print('')
num2 = int(input('Escolha o 2° número \nr:'))
print('')
num3 = int(input('Escolha o 3° número \nr:'))
print('')
print('-=' *30)
print('\033[1;34m--- Resultado Dos Dados ---\033[m')
print('')
if num1 > num2 and num1 > num3:
	maior = num1
if num2 > num1 and num2 > num3:
	maior = num2
if num3 > num1 and num3 > num2:
	maior = num3
print('>>> O maior número é o {}.'.format(maior))
if num1 < num2 and num1 < num3:
	menor = num1
if num2 < num1 and num2 < num3:
	menor = num2
if num3 < num1 and num3 < num2:
	menor = num3
print('>>> O menor número é o {}.'.format(menor))
print('-=' *30)

_________________________________________________________________________
Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para salários superiores a 
R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é 
de 15%.

salario = float(input('Salário R$'))
print('')
if salario > 1250.00:
	aumento_sup = salario + (salario * 10/100)
	print('O aumento superior será de 10%: R${:.2f}'.format(aumento_sup))
else:
	aumento_inf = salario + (salario * 15/100)
	print('O aumento inferior será de 15%: R${:.2f}'.format(aumento_inf))

_________________________________________________________________________
Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.

r1 = float(input('Registre a 1ª reta \nr: '))
print('')
r2 = float(input('Registre a 2ª reta \nr: '))
print('')
r3 = float(input('Registre a 3ª reta \nr: '))
print('')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('---> Os segmentos podem criar um triângulo!!')
else:
	print('ERRO!!! Nenhma das retas consegue formar um triângulo.')
_________________________________________________________________________
