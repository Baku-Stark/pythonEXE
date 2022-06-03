>>> - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/tratamento-de-erros-em-python/modulos/exercicio-113-funcoes-aprofundadas-em-python/
--------------------------------------------------------

Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, 
incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie 
também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
	while True:
		try:
			n = int(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERRO: Número Inteiro inválido!\033[m')
			continue
		except (KeyboardInterrupt):
			print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
			return 0
		else:
			return n

def leiaFloat(msg):
	while True:
		try:
			n = float(input(msg))
		except (ValueError, TypeError):
			print('\033[31mERRO: Número Real inválido!\033[m')
			continue
		except (KeyboardInterrupt):
			print('\n\033[31mO usuário preferiu não digitar esse número.\033[m')
			return 0
		else:
			return n


# ---
n1 = leiaInt('--- Digite um número: ')
print('[Registrado!]')
print('')
n2 = leiaFloat('--- Digite um número: ')
print('[Registrado!]')
print('')
print('-=' *30)
print('O valor inteiro digitado foi {} e o valor real recebeu {}'.format(n1, n2))
print('-=' *30)
--------------------------------------------------------

Exercício Python 114: Crie um código em Python que teste se o site pudim está acessível pelo 
computador usado.

import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('>>> O site pudim não está acessível no momento. Tente mais tarde!!')
else:
    print('>>> O site está acessível!')
    print(site.read()) #Ler o site
--------------------------------------------------------

Exercício Python 115(a): Vamos criar um menu em Python, usando modularização.