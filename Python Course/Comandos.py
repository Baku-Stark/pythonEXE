>>> Comandos Python
		# coding=utf-8 [Ínicio do código no PyCharm]

		class Curso Python YouTube (Aulas):
			"""Wallace de Freitas"""
			def __intro__(Comandos, https://docs.python.org/3/library/) 
						 (https://rpubs.com/gomes555/comandos_python):
_______________________________________________________________________________________________________________________________________________________________
>>> {NÚMEROS}
n = int(input('Digite um número:')) ------ Números Inteiros ('1, 2, 3, 4, etc')
n = float(input('Digite um número:')) ---- Números Flutuantes ('1.0, 2.0, 3.0, -15.678')
n = str(input('Digite um número')) ------- Números Strings ('Sempre está no progama - Utilizar o "type(n) para mostrá-lo" - números entre as aspas')
n = bool(input('Digite um número')) ------ Números Booleanos 'True' ou 'False'

+ = Adição
- = Subtração
* = Multiplicação
/ = Divisão
** = Potência ---> pow (n1, n2)
**(0.5) = Raiz Quadrada
**(1/3) = Raiz Cúbica

// = Divisão Inteira (Resultados sem vírgula)
% = Resto da Divisão (Resto da Divisão)
				
				Exemplo: 5 | 2
						-4	 2 -> Divisão Inteira (Sem vírgula)
						 1 -> Resto da Divisão

Ordem de Precedência
1 --- ()
2 --- **
3 --- *, /, //, %
4 --- +, -

"ceil" - arredondamento up
"floor" - arredondamento down
"trunc" - eliminar da vígula para frente
"pow" - potência
"sqrt" - raiz quadrada
"factorial" - fatorial
"random" - randomizar número
"randint" - número random INTEIRO

Import Math
--> import + example 	comando Generalizado
--> from + example + import = pudim	comando Específico
Exemplos
from random import randint
-- exemplo = randint (0, 10)

from time import sleep
-- sleep(tempo)

from datetime import date
-- ano_atual = date.today().year
_______________________________________________________________________________________________________________________________________________________________
>> {TEXTO}

* Listagem
-- Tupla >>> ()
---> add()
---> clear()
---> pop()
---> union()
---> issuperset()
---> issubset()
---> intersection() 
---> difference ()
---> isdisjoint() 
---> setdiscard()
---> copy()

-- Lista >>> []
---> append() >>> Adicionar um novo elemento na lista
---> copy()
---> count()
---> insert() >>> Ele usa dois parâmetros: o primeiro para indicar a 
				posição da lista em que o elemento será inserido e o segundo para informar o 
				item a ser adicionado na lista. (1, 'Wallace')
---> reverse()
---> remove() >>> Remover item
---> sort()
---> pop() >>> Remove o PRIMEIRO item da lista
---> extend()
---> index()
---> clear() >>> Limpar elemento da lista

-- Dicionário >>> {}
---> copy()
---> clear() >>> Limpar Dicionário
---> fromkeys() >>> Utilizar as chaves
---> items() >>> Itens do Dicionário
---> get() 
---> keys() >>> Chaves do Dicionário
---> pop() >>> Remove o PRIMEIRO item do Dicionário
---> values() >>> Values do Dicionário
---> update()
---> setdefault()
---> popitem()


{CENTRALIZA, JUSTIFICAR-DIREITA E JUSTIFICAR-ESQUERDA}

linha = '-' * 50
titulo = 'Aulas de Python'

#Justificar para esquerda
print(titulo.ljust(50))
print(linha)

#centralizar
print(titulo.center(50))
print(linha)

#justificar para a direita
print(titulo.rjust(50))
print(linha)

{ESPAÇAMENTO}
print('{:>5}'.format('Texto')) # espaçamento em 5 para a direita


--------------------------------------------------------

* Números
-- randint (0, 10) >>> randomizar números de desejo (INTEIRO)
-- max() >>> MAIOR número
-- min() >>> MENOR número
-- sort() >>> ordem CRESCENTE dos números

* Fatiamento
-- len(frase)
-- sorted() >>> Deixar em ordem alfabética
-- .format(example.index()) >> Localizar na Tupla
-- frase.count('example') >>> contar quantas letras tem.
-- frase.count('o', 0, 13) >>> contagem com FATIAMENTO
-- frase.find('deo') >>> encontrar a exata frase na posição da string
-- frase.find('Exemplo não existente') >>> retorna com o valor '-1'
	-- frase.replace('Python', 'ANDROID') >>> Substituir frases
-- frase.upper() >>> deixar toda a string em maíusculo
-- frase.lower() >>> deixar toda a string em minúsculo
-- frase.capitalize() >>> transformar todos os caracteres em minúsculo, menos o primeiro caracter
-- frase.title() >>> analisar as palavras na string e transformar o primeiro caracter ápos o espaço
-- frase.strip() >>> remover os ESPAÇOS inúteis
	-- frase.rstrip() >>> remover os ESPAÇOS inúteis da DIREITA (RIGHT)
	-- frase.lstrip( >>> remover os ESPAÇOS inúteis da ESQUERDA (LEFT)
-- frase.split() >>> remove os ESPAÇOS e separa em uma lista
	-- '-'.join(frase) >>> junta toda a lista
-- 'Curso' in frase >>> Verificar certa frase (operador)
frase [9] --> Ler a letra usando o caracter
frase [:5] --> Ler a string do caractere ZERO até o número selecionado (5)
frase [15:] --> Ler a string do caractere à partir do 15 (sem final)
frase [9:3] --> Ler a string até o final pulando duas casas
frase [9:13] --> Ler uma cadeia fechada (não contando o último valor)
frase [9:21:2] --> Ler uma cadeia fechada (porém, pulando um caracter)
_______________________________________________________________________________________________________________________________________________________________
>> {USANDO O TAB}

Exemplos básicos (Estrutura Condicional): 

se cara.esquerda()          if carro.esquerda():
	bloco_V_					bloco True

senão                       else:
	bloco_F_					bloco False


tempo = int(input('Quantos tem seu carro?'))
if tempo<=3:
	print('Carro Novo')
else:
	print('Carro Velho')
print('-- FIM ! --')

tempo = int(input('Quantos tem seu carro?'))
print('Carro Novo'if tempo<=3 else'Carro Velho')
print('-- FIM ! --')

nome = str(input('Qual o seu nome? '))
print('')
if nome == 'Wallace':
	print('Seu nome é muito bonito!!')
elif nome == 'Tony Stark' or nome == 'Thor' or nome == 'Hulk' or nome == 'Steve':
	print('Pertence aos Vingadores!')
else:
	print('Um nome comum.')
print('')
print('Tenha um bom dia, {}!'.format(nome))
_______________________________________________________________________________________________________________________________________________________________
>> {CÓDIGO DE CORES, FONTE E ESTILO}

ANSI - escape sequence

\033[0;33;44m(String exemplo)\033[m

STYLE			TEXT				FUNDO
0 Nenhum		30				40			Branco
1 Negrito		31				41			Vermelho
4 Sublinhado		32				42			Verde
7 Inverter		33				43			Amarelo
			34				44			Azul
			35				45			Roxo
			36				46			Ciano
			37 				47			Cinza
_______________________________________________________________________________________________________________________________________________________________
>> {ESTRUTURA DE REPETIÇÃO "for"}
Por exemplo:
for c in range(0, 4):
print(c)
print(‘Acabou’)


Exemplo:
laço c no intervalo(1, 10)
	passo
pega


Comando real > ('''for c in xrange(1,10):
					pass''')
for x in xrange(1,10):
	pass
{Repetir 10x}
for x in xrange(0,10):
	print('Oi!')
print('FIM!!!')

{Contagem de 1 a 10}
for x in xrange(1,11):
	print(x)

_______________________________________________________________________________________________________________________________________________________________
>> {ESTRUTURA DE REPETIÇÃO "while"}

while enquanto não maça:
	if bloco:
		passo
	if espaço:
		pula
	if coin:
		pega
pega #maçã

c = 1
while c < 10:
	print(c)
	c += 1
print('Acabou!')

n = 1
while n != 0:
	n = int(input('Digite um número: '))
print('Finalizou!')

n = s = 0
while n != 999:
	n = int(input('Digite um número: '))
	s += n
print('A soma vale {}.'.format(s))

n = cont = 0
while cont < 5:
	n = int(input('Digite um número: '))
	cont += 1

r = 'S'
while r == 'S':
	print('-=' *5)
	n = int(input('Digite um número: '))
	r = str(input('Deseja continuar [S/N]: ')).upper()
	print('-=' *5)
	print('')
print('Sessão encerrada!')

>>> PARANDO A ESTRUTURA #(break)
n = s = 0
while True:
	n = int(input('Digite um número: '))
	if n == 999:
		break
	s += n
print('A soma vale {}.'.format(s))
_______________________________________________________________________________________________________________________________________________________________
>> {FUNÇÃO "def"}

def mostraLinha():
	print('------------------------------')


mostraLinha()
print('     SISTEMA DE ALUNOS     ')
mostraLinha()
print('')
mostraLinha()
print('     CADASTRO DE ALUNOS     ')
mostraLinha()
print('')
mostraLinha()
print('     SISTEMA ESCOLAR     ')
mostraLinha()

--------------------------------------------------------

def mensagem(msg):
	print('------------------------------')
	print(msg)
	print('------------------------------')


mensagem('     SISTEMA DE ALUNOS     ')
--------------------------------------------------------
>>> UTILIZANDO O "def" com números
def soma(a, b):
	print('--- A = {} e B = {} ---'.format(a, b))
	s = a + b
	print('{} + {} = {}'.format(a, b, s))
	print('')


# Main
soma(1, 4)  #5
soma(5, 5)  #10
soma(5, 10) #15
--------------------------------------------------------
>>> EMPACOTAMENTO EM "def"

def contador(* num):
	print(num)


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)

def contador(* num):
	for valor in num:
		print(valor),


contador(5, 7, 3, 1, 4)
contador(8, 4, 7)
--------------------------------------------------------
--->>> Interactive Help
--- help()
print("string exemplo (input, print, etc".__doc__)

###

#Fazendo Docstring
def function(i, f, p):
	"""
	-> Faz uma contagem e mostra na tela.
	:param i: Início da contagem
	:param f: Fim da contagem
	:param p: Passo da contagem
	:return: Sem retorno
	Função criada por Wallace de Freitas
	"""
	c = i
	while c <= f:
		print('{}'.format(c)),
		c += p
	print('Fim!')

function(2, 10, 2)
help(function)

--->>> Parâmetros opcionais

def somar(a=0, b=0, c=0):
	"""
	-> Faz a soma dos números e mostra na tela.
	:param a: 1° Valor
	:param b: 2° Valor
	:param c: 3° Valor
	:return: Sem retorno
	Função criada por Wallace de Freitas
	"""
	s = a + b + c
	print('A soma vale {}'.format(s))

somar(3, 2, 5)
somar(8, 4)
somar()
help(somar)

--->>> Escopo de Variáveis

def teste():
	x = 8
	print('Na função teste, n vale {}.'.format(n))
	print('Na função teste, x vale {}.'.format(x))


# -----
n = 2
teste()
print('No programa principal, n vale {}.'.format(n))


def teste(b):
	global a
	a = 8
	b += 4
	c = 2
	print('[A] dentro vale {}.'.format(a))
	print('[B]dentro vale {}.'.format(b))
	print('[C]dentro vale {}.'.format(c))


# ---
a = 5
teste(a)
print('[A] fora vale {}.'.format(a))


--->>> Retornando Valores
def somar(a=0, b=0, c=0):
	s = a + b + c
	return s


# ===
resp1 = somar(3, 2, 5)
resp2 = somar(2, 2)
resp3 = somar(6)
print('Todas as somas foram: {} {} e {}'.format(resp1, resp2, resp3))
_______________________________________________________________________________________________________________________________________________________________
