>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/condicoes-em-python-if-elif/modulos/exercicio-41-classificando-atletas/
--------------------------------------------------------

Exercício Python 41: A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a 
idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

from time import sleep
print('''
	> Confederação Nacional de Natação (CNN) <
''')
print('''Vamos realizar alguns procedimentos para análise...
	Veja a lista à baixo: 
	[MIRIM] --- Até 9 anos
	[INFANTIL] --- Até 14 anos
	[JÚNIOR] --- Até 19 anos
	[SÊNIOR] --- Até 25 anos
	[MASTER] --- Acima de 25 anos
	''')
print('')
nome = str(input('Nome do aluno(a): '))
idade = int(input('Idade do(a) aluno(a): '))
print('>>> Data de nascimento')
dia = int(input('DIA: '))
mes = int(input('MÊS: '))
ano = int(input('ANO: '))
print('Processando...')
sleep(2)
print('')
print('-=' *15)
if idade <= 9:
	print(''' O aluno {}, nascido em {}/{}/{}
		pertence ao grupo MIRIM de natação!'''.format(nome, dia, mes, ano))
elif idade == 10 or idade <= 14:
	print(''' O aluno {}, nascido em {}/{}/{}
		pertence ao grupo INFANTIL de natação!'''.format(nome, dia, mes, ano))
elif idade == 15 or idade <= 19:
	print(''' O aluno {}, nascido em {}/{}/{}
		pertence ao grupo JÚNIOR de natação!'''.format(nome, dia, mes, ano))
elif idade == 20 or idade <= 25:
	print(''' O aluno {}, nascido em {}/{}/{}
		pertence ao grupo SÊNIOR de natação!'''.format(nome, dia, mes, ano))
else:
	print(''' O aluno {}, nascido em {}/{}/{}
		pertence ao grupo MASTER de natação!'''.format(nome, dia, mes, ano))
print('-=' *15)
--------------------------------------------------------

Exercício Python 42: Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

La = float(input('Primeiro Segmento: '))
Lb = float(input('Segundo Segmento: '))
Lc =  float(input('Terceiro Segmento: '))
print('')
print('''
	[EQUILÁTERO] todos os lados iguais

	[ISÓSCELES] dois lados iguais, um diferente

	[ESCALENO] todos os lados diferentes
''')
print('')
if La < Lb + Lc and Lb < La + Lc and Lc < La + Lb:
	print('Os segmentos acima PODEM FORMAR um triângulo!')
	if La == Lb and Lb == Lc:
		print(' >>> Tipo de triângulo: EQUILÁTERO.')
	elif La != Lb != Lc != La:
		print(' >>> Tipo de triângulo: ESCALENO.')
	else:
		print(' >>> Tipo de triângulo: ISÓSCELES.')
else: 
	print('Os segmentos acima NÃO PODEM FORMAR um triângulo!')
--------------------------------------------------------

Exercício Python 43: Desenvolva uma lógica que leia o peso e a altura de uma 
pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de 
acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida 

nome = str(input('Nome do paciente: '))
alt = float(input('Registre a Altura (m): '))
peso = float(input('Registre seu Peso (Kg): '))
print('')
imc = peso / (alt ** 2)
#print(imc)
# O IMC é dado em kg/m²
print('')
print('''
	 Abaixo de 18.5: 'Abaixo do Peso'
	 Entre 18.6 e 25: 'Peso ideal'
	 25 até 30: 'Sobrepeso'
	 30 até 40: 'Obesidade'
	 Acima de 40: 'Obesidade Mórbida'
''')
print('-=' *15)
print('Seu IMC é {:.1f}kg/m²'.format(imc))
if imc <= 18.5:
	print('O paciente {} está Abaixo do Peso!'.format(nome))
elif imc == 18.6 or imc < 25:
	print('O paciente {} está no Peso ideal!'.format(nome))
elif imc == 25 or imc < 30:
	print('O paciente {} está Sobrepeso!'.format(nome))
elif imc == 30 or imc < 40:
	print('O paciente {} está com Obesidade!'.format(nome))
else:
	print('O paciente {} está com Obesidade Mórbida!'.format(nome))
print('-=' *15)
--------------------------------------------------------

Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um 
produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

print('===== LOJAS FREITAS =====')
print('')
compras = float(input('Preço TOTAL das compras: R$'))
print('')
print('FORMAS DE PAGAMENTO:')
print('''
	[1] À vista Dinheiro/cheque: 10% de desconto

	[2] À vista no cartão: 5% de desconto

	[3] Em até 2x no cartão: preço formal 

	[4] 3x ou mais no cartão: 20% de juros
''')
pagamento = int(input('Qual forma de pagamento você seleciona: '))
print('')
print('-=' *15)
print('')
if pagamento == 1:
	print('10% De Desconto!')
	total = compras - (compras * 10 / 100)
	print('>>> Total a pagar: R${:.2f}!'.format(total))
elif pagamento == 2:
	print('5% De Desconto!')
	total2 = compras - (compras * 5 / 100)
	print('>>> Total a pagar: R${:.2f}!'.format(total2))
elif pagamento == 3:
	print('Parcelamento (2x - cartão): Preço normal.')
	total3 = compras
	parcela = total3 / 2
	print('>>> Total a pagar (2 meses): R${:.2f}!'.format(parcela))
elif pagamento == 4:
	res = compras + (compras * 20 / 100)
	print('Parcelamento (3x ou mais - cartão): 20% De Juros.')
	totalreal = int(input('Quantas Parcelas: '))
	parcela2 = res / totalreal
	print('>>> Total a pagar ({} meses + JUROS): R${:.2f}!'.format(totalreal, parcela2))
else:
	print('OPÇÃO INCORRETA DE PAGAMENTO!')
print('')
print('-=' *15)
--------------------------------------------------------

Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô 
com você.

from random import choice
from time import sleep
print('''
	=== JOKENPÔ GAME !!! ===
''')
lista = ["pedra", "papel", "tesoura"]
print('''
	Computador: Vamos jogar JOKENPÔ!
	>>> Regras:
			Pedra >> Tesoura
			Tesoura >> Papel
			Papel >> Pedra
''')
print('')
player = str(input('Qual opção você escolhe (pedra, papel ou tesoura): \n')).lower()
print('')
print('JO')
sleep(0.50)
print('KEN')
sleep(0.5)
print('PÔ!!!')
print('')
computador = choice(lista)
vencedor = ""
print('''
JOGADOR: {}	
COMPUTADOR: {}'''.format(player, computador))
print('')
print('-' *20)
if (player != "pedra" and player != str("papel") and player != str("tesoura")):
	print('Escolha errada!'.format(player))
elif player == computador:
	print('EMPATE!!!')
elif player == "pedra" and computador == "tesoura":
	print('O JOGADOR VENCEU!!!')
elif computador == "pedra" and player == "tesoura":
	print('O COMPUTADOR VENCEU!!!')
elif player == "papel" and computador == "pedra":
	print('O JOGADOR VENCEU!!!')
elif computador == "papel" and player == "pedra":
	print('O COMPUTADOR VENCEU!!!')
elif player == "tesoura" and computador == "papel":
	print('O JOGADOR VENCEU!!!')
elif computador == "tesoura" and player == "papel":
	print('O COMPUTADOR VENCEU!!!')
print('-' *20)
--------------------------------------------------------
