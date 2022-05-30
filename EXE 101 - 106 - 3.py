>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/funcoes-em-python/modulos/exercicio-101-funcoes-para-votacao/
--------------------------------------------------------

Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como 
parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa 
tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

print('-=' *30)
def voto(ano_nascimento):
	from datetime import date
	ano_atual = date.today().year
	idade_candidato = ano_atual - ano_nascimento
	global idade_candidato
	if idade_candidato < 16:
		return '>>> Com {} anos: NÃO VOTA!'.format(idade_candidato)
	elif 16 <= idade_candidato < 18 or idade_candidato > 65:
		return '>>> Com {} anos: VOTO OPCIONAL!'.format(idade_candidato)
	else:
		return '>>> Com {} anos: VOTO OBRIGATÓRIO!'.format(idade_candidato)

# ---
ano = int(input('-- Digite o ANO DE NASCIMENTO \nr:'))
print('')
print(voto(ano))
print('O eleitor foi registrado com {} anos.'.format(idade_candidato))
print('-=' *30)
--------------------------------------------------------

Exercício Python 102: Crie um programa que tenha uma função fatorial() que receba dois parâmetros: 
o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) 
indicando se será mostrado ou não na tela o processo de cálculo do fatorial.

print('-=' *30)
def fatorial(n, show=False):
	"""
	-> Calculo de Fatorial
	:param. nc: Número que será calculado;
	:param. show: Mostrar o fatorial;
	:return: retorno.

	---- Código desenvolvido por [Wallace]
	"""
	f = 1
	for c in range(n, 0, -1):
		if show:
			print(c, end='')
			if c > 1:
				print(' x ', end='')
			else:
				print(' = ', end='')
		f *= c
	return f


# ---
print(fatorial(5, show=True))
print('')
help(fatorial)
print('-=' *30)
--------------------------------------------------------

Exercício Python 103: Faça um programa que tenha uma função chamada ficha(), 
que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido 
informado corretamente.

def ficha(jog='<desconhecido>', gol=0):
	print('O jogador {} fez {} gol(s) no campeonato'
		.format(jog, gol))
# ---
n = str(input('Nome do Jogador: ')).capitalize()
g = str(input('Número de Gols: '))

if g.isnumeric():
	g = int(g)
else:
	g = 0
if n.strip() == '':
	ficha(gol=g)
else:
	ficha(n, g)
--------------------------------------------------------

Exercício Python 104: Crie um programa que tenha a função leiaInt(), que vai funcionar de forma 
semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor 
numérico. Ex: n = leiaInt(‘Digite um n: ‘)

print('-=' *30)
def leiaInt(msg):
	valor = 0
	while True:
		num = str(input(msg))
		if n.isnumeric():
			valor = int(num)
			ok = True
		else:
			print('ERRO! Digite um númer inteiro válido.')
		if ok:
			break
	return valor
# --
num = leiaInt('Digite um número: ')
print('--- Você digitou o número {}.'.format(num))
print('-=' *30)
--------------------------------------------------------

Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de 
alunos e vai retornar um dicionário com as seguintes informações:

– Quantidade de notas                                                                                                                                                  
– A maior nota                                                                                                                                                                
– A menor nota                                                                                                                                                              
– A média da turma                                                                                                                                                      
– A situação (opcional)

def notas(*n, sit=False):
	"""
	-> Função para analisar notas e situações de vários alunos.
	: param. n: uma ou mais notas dos alunos (aceitando várias);
	: param. sit: Valor opcional, indicando se deixe ou não adicionar a situação;
	: return: Dicionário com várias informações sobre a situação da turma.

	--- SISTEMA ESCOLAR BRASILEIRO ---
	"""

	r = {}
	r['Total'] = len(n)
	r['Maior'] = max(n)
	r['Menor'] = min(n)
	r['Média'] = sum(n)/len(n)
	if sit:
		if r['Média'] >= 7:
			r['Situação'] = 'BOA'
		elif r['Média'] >= 5:
			r['Situação'] = 'RAZOÁVEL'
		else:
			r['Situação'] = 'RUIM'
	return r


# ---
resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
help(notas)
--------------------------------------------------------

Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. 
O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra ‘FIM’, 
o programa se encerrará. Importante: use cores.

from time import sleep
c = {'\033[m',         # 0 - Sem cores
	 '\033[0;30; 41m', # 1 - Vermelho
	 '\033[0;30; 42m', # 2 - Verde
	 '\033[0;30; 43m', # 3 - Amarelo
	 '\033[0;30; 44m', # 4 - Azul
	 '\033[0;30; 45m', # 5 - Roxo
	 '\033[7;30',      # 6 - Branco
	};

def ajuda(com):
	título('Acessando o manual do comando \'{}\''.format(com), 4)
	print(c[6], end='')
	help(com)
	print(c[0], end='')
	sleep(2)

def título(msg, cor=0):
	tam = leg(msg) + 4
	print(c[cor], end='')
	print('~' * tam)
	print('{}'.format(msg))
	print('~' * tam)
	print(c[0], end='')
	sleep(1)

# ---
comando = ''
while True:
	titulo('SISTEMA DE AJUDA PyHELP', 2)
	comando = str(input('Função ou BiBlioteca > '))
	if comando.upper() == 'FIM':
		break
	else:
		ajuda(comando)
titulo('ATÉ LOGO!', 1)
--------------------------------------------------------