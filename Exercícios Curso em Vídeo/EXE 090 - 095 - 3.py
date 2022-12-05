>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/dicionarios-em-python/modulos/exercicio-90-dicionario-em-python/
--------------------------------------------------------

Exercício Python 90: Faça um programa que leia nome e média de um aluno, guardando 
também a situação em um dicionário. No final, mostre o conteúdo da estrutura na tela.

aluno = {}
aluno ['nome'] = str(input('Nome do(a) aluno(a): ')).capitalize()
aluno ['média'] = float(input('Registre a média do(a) {}: '.format(aluno["nome"])))
print('')
print('-=' *30)
if aluno['média'] >= 7:
	aluno['situação'] = '\033[0;34mAprovado[m'
elif 5 <= aluno['média'] < 7:
	aluno['situação'] = '\033[0;33mRecuperação[m'
else:
	aluno['situação'] = '\033[0;31mReprovado[m'
print('')
for k, v in aluno.items():
	print('{} é igual a {}.'.format(k, v))
print('-=' *30)
print('')
--------------------------------------------------------

Exercício Python 91: Crie um programa onde 4 jogadores joguem um dado e tenham 
resultados aleatórios. Guarde esses resultados em um dicionário em Python. 
No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior 
número no dado.

from random import randint
from operator import itemgetter
jogadores = {}
ranking = {}
print('-=' *30)
for n in range(1, 5):
	jogadores['nome'] = str(input('>>> Registre o {}° jogador: '.format(n))).capitalize()
	jogadores['dado'] = randint(1, 6)
	print('O dado caiu no valor [{}].'.format(jogadores['dado']))
	print('>>> Jogador {} registrado!'.format(jogadores["nome"]))
	print('-' *15)
	print('')
print('-=' *30)
print('--- Registro finalizado !!! ---')
print('Resultados!')
ranking = sorted(jogadores.items(), key=itemgetter(1))
print('Vencedor é: {}!'.format(ranking))
--------------------------------------------------------

Exercício Python 92: Crie um programa que leia nome, ano de nascimento e carteira de 
trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de 
ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente,
além da idade, com quantos anos a pessoa vai se aposentar.


from datetime import date
#Obs.: aposentadoria em 35 anos de contribuição.
dados_trabalhador = {}
ano_atual = date.today().year
dados_trabalhador['Nome'] = str(input('> Nome do empregado \nr: ')).capitalize()
print('--' *10)
ano_nascimento = int(input('> Ano de nascimento \nr: '))
dados_trabalhador['Idade'] = ano_atual - ano_nascimento
print('--' *10)
dados_trabalhador['Carteira'] = int(input('''> Número da carteira de trabalho 
(CTPS - "0" caso não possua) \nr: '''))
print('')
print('--' *10)
if dados_trabalhador['Carteira'] > 0:
	dados_trabalhador['Contratação'] = int(input('> Ano de Contratação \nr: '))
	dados_trabalhador['Salário'] = float(input('> Salário \nr: '))
	dados_trabalhador['Aposentadoria'] = dados_trabalhador['Contratação'] + 35
else:
	print('{} não possui carteira de trabalho.'.format(dados_trabalhador["Nome"]))
print('--' *10)
print('')
print('')
print('')
print('=' *30)
print(dados_trabalhador)
print('- Nome: {}.'.format(dados_trabalhador["Nome"]))
print('- Idade: {}.'.format(dados_trabalhador["Idade"]))
print('- Ano de Nascimento: {}.'.format(ano_nascimento))
if dados_trabalhador['Carteira'] > 0:
	print('- Salário: R${:.2f}'.format(dados_trabalhador["Salário"]))
	print('- {} vai se aposentar em {}.'.format(dados_trabalhador["Nome"], dados_trabalhador['Aposentadoria']))
print('=' *30)
--------------------------------------------------------

Exercício Python 93: Crie um programa que gerencie o aproveitamento de um jogador de 
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
durante o campeonato.

jogador = {}
partidas =[]
jogador['Nome'] = str(input('Nome do Jogador \nr: ')).capitalize()
tot = int(input('Quantas partidas {} jogou? \nr: '.format(jogador["Nome"])))
print('-' *15)
print('')
for x in range(1, tot +1):
	partidas.append(int(input('>>> Quantos gols na {}ª partida? \nr: '
		.format(x))))
jogador['Gols'] = partidas[:]
jogador['Total'] = sum(partidas)
print('')
print('-=' *30)
print(jogador)
print('-=' *30)
for k, v in jogador.items():
	print('>>> O campo {} tem o valor {}.'.format(k, v))
print('-=' *30)
print('[O jogador {} jogou {} partidas]'
	.format(jogador["Nome"], len(jogador["Gols"])))
for i, v in enumerate(jogador["Gols"]):
	print('   => Na partida {}, fez {} gols.'
		.format(i, v))
print('---- Foi um total de {} gols.'.format(jogador["Total"]))
--------------------------------------------------------

Exercício Python 94: Crie um programa que leia nome, sexo e idade de várias pessoas, 
guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. 
No final, mostre: 
A) Quantas pessoas foram cadastradas 
B) A média de idade 
C) Uma lista com as mulheres 
D) Uma lista de pessoas com idade acima da média

totcadastro = media = 0
galera = []
pessoa = {}
while True:
	pessoa.clear()
	pessoa['Nome'] = str(input('>>> Nome: ')).capitalize()
	while True:
		pessoa['Sexo'] = str(input('>>> Sexo [M/F]: ')).upper()[0]
		if pessoa['Sexo'] in 'MF':
			break
		print('ERRO! Por favor, digite apenas [M] ou [F]!')
	pessoa['Idade'] = int(input('>>> Idade: '))
	totcadastro += pessoa['Idade']
	galera.append(pessoa.copy())
	print('')
	while True:
		resp = str(input('Deseja continuar? \n[S/N]: ')).upper()[0]
		if resp in 'SN':
			break
		print('ERRO! Digite apenas [S] - Sim ou [N] - Não!')
	if resp == 'N':
		break
print('')
print('-=' *30)
print('--- Foram {} pessoas cadastradas.'.format(len(galera)))
media = totcadastro / len(galera)
print('--- A média de idade é de {:5.2f} anos.'.format(media))
print('--- As mulheres cadastradas foram de'),
for p in galera:
	if p['Sexo'] in 'Ff':
		print('{}'.format(p["Nome"])),
print('')
print('--- Lista das pessoas acima da média:')
for p in galera:
	if p['Idade'] >= media:
		print('   '),
		for k, v in p.items():
			print('{} = {}'.format(k, v)),
		print('')
print('--- ENCERRADO! ---')
print('-=' *30)
--------------------------------------------------------

Exercício Python 95: Aprimore o desafio 93 para que ele funcione com vários jogadores, 
incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador.
--- '''[Exercício Python 93]: Crie um programa que gerencie o aproveitamento de um jogador de 
futebol. O programa vai ler o nome do jogador e quantas partidas ele jogou. 
Depois vai ler a quantidade de gols feitos em cada partida. 
No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos 
durante o campeonato.'''
#del lista[:]

jogador = {}
partidas =[]
time = []
while True:
	jogador.clear()
	jogador['Nome'] = str(input('Nome do Jogador \nr: ')).capitalize()
	tot = int(input('Quantas partidas {} jogou? \nr: '.format(jogador["Nome"])))
	del partidas[:]
	print('-' *15)
	for x in range(1, tot +1):
		partidas.append(int(input('>>> Quantos gols na {}ª partida? \nr: '
			.format(x))))
		print('-' *15)
	print('')
	jogador['Gols'] = partidas[:]
	jogador['Total'] = sum(partidas)
	time.append(jogador.copy())
	while True:
		resp = str(input('>>> Quer continuar? [S/N] \nr: ')).upper()[0]
		if resp in 'SN':
			break
			print('-' *15)
		print('ERRO! Responda apenas Sim(S) ou Não(N)!')
	if resp == 'N':
		break
		print('-' *15)
print('')
print('-=' *30)
print('Cod  '),
for i in jogador.keys():
	print('{:<15}'.format(i)),
print('')
print('-=' *30)
for k, v in enumerate(time):
	print('{:>4} '.format(k)),
	for d in v.values():
		print('{:<15}'.format(str(d))),
	print('')
print('-=' *30)
print('')
while True:
	busca = int(input('Mostrar qual jogador (999 para interromper)? \nr: '))
	if busca == 999:
		break
	if busca >= len(time):
		print('ERRO! Jogador não existe.')
	else:
		print('--- LEVANTAMENTO DO JOGADOR {} ---'
			.format(time[busca]["Nome"]))
		for i, g in enumerate(time[busca]["Gols"]):
			print('     No jogo {} fez {} gols.'
				.format(i+1, g))
	print('-' *25)
print('')
print('<<< Volte Sempre !!! >>>')
--------------------------------------------------------