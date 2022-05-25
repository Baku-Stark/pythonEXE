>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/condicoes-em-python-if-else/modulos/exercicio-29-radar-eletronico/
--------------------------------------------------------

Exercício Python 29: Escreva um programa que leia a velocidade de um carro. 
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
A multa vai custar R$7,00 por cada Km acima do limite.

from time import sleep
consulta = int(input('Digite a velocidade em Km/h: '))
print('')
print('Analisando...')
sleep(2)
print('')
if consulta <= 80:
	print('Velocidade não ultrapassou os limites! BOA VIAGEM!')
else:
	adc = consulta - 80
	multa = adc * 7 
	print('Sua multa é de R${},00'.format(multa))
--------------------------------------------------------

Exercício Python 30: Crie um programa que leia um número inteiro e mostre na 
tela se ele é PAR ou ÍMPAR.

num = int(input('Escolha um número: '))
resultado = num % 2
print('')
print('-' *20)
print('')
if resultado == 0:
	print('O número {} é PAR'.format(resultado))
else:
	print('O número {} é ÌMPAR'.format(resultado))
print('')
print('-' *20)
--------------------------------------------------------

Exercício Python 31: Desenvolva um programa que pergunte a distância de uma 
viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens 
de até 200Km e R$0,45 parta viagens mais longas.

viagem = float(input('Distânca: '))
print('Sua viagem tem a seguinte distância: {}'.format(viagem))
print('')
print('-=' *15)
print('')
if viagem <= 200:
	print('Sua viagem curta vale R$0,50 por Km.')
	print('')
	valor = viagem * 0.50
	print('O valor da passagem é de: R${:.2f}'.format(valor))
else:
	print('Sua viagem longa vale R$0,45 por Km.')
	print('')
	valor2 = viagem * 0.45
	print('O valor da passagem é de: R${:.2f}'.format(valor2))
print('')
print('-=' *15)
--------------------------------------------------------

Exercício Python 32: Faça um programa que leia um ano qualquer e mostre se ele 
é bissexto.

ano = int(input('Escolha um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
	print('O ano {} é BISSEXTO'.format(ano))
else:
	print('O ano {} não é BISSEXTO.'.format(ano))
--------------------------------------------------------