>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/repeticoes-em-python-for/modulos/exercicio-46-contagem-regressiva/
--------------------------------------------------------

Exercício Python 46: Faça um programa que mostre na tela uma contagem 
regressiva para o estouro de fogos de artifício, indo de 10 até 0, com uma 
pausa de 1 segundo entre eles.

from time import sleep
for x in xrange(1, 11):
	sleep(1)
	print(x)
print('Feliz ANO NOVO!!!')
--------------------------------------------------------

Exercício Python 47: Crie um programa que mostre na tela todos os números 
pares que estão no intervalo entre 1 e 50. 

for x in xrange(1, 51):
	if x % 2 == 0:
		print(x)
print('Acabou!')

for n in xrange(1, 51, 2):
	print(n, end= ' ')
print('Acabou')
--------------------------------------------------------

Exercício Python 48: Faça um programa que calcule a soma entre todos os 
números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma = 0
cont = 0
for x in xrange(1, 501, 2):
	if x % 3 == 0:
		cont = cont + 1
		soma = soma + x
print('''A soma de todos os valores é: {}.
	Com {} solicitações.'''.format(soma, cont))
# Outro Método
		cont += 1
		soma += x
--------------------------------------------------------

Exercício Python 49: Refaça o DESAFIO 9, mostrando a tabuada de um número 
que o usuário escolher, só que agora utilizando um laço for.

n = int(input('Escolha o numerador: '))
print('')
print('-=' *20)
print('>>> Tabuada de {}! <<<'.format(n))
print('')
for x in xrange(1, 11):
	res = n * x
	print('{} x {:2} = {}'.format(n, x, res))
print('-=' *20)
--------------------------------------------------------

Exercício Python 50: Desenvolva um programa que leia seis números 
inteiros e mostre a soma apenas daqueles que forem pares. Se o valor 
digitado for ímpar, desconsidere-o.

soma = 0
cont = 0
for x in xrange(1, 7):
	num = int(input('Digite o {}° valor: '.format(x)))
	if num % 2 == 0:
		soma += num
		cont += 1
print('A soma dos números (apenas PARES) é: {}'.format(soma))
	