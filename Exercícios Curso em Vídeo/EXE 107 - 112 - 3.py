>>> - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-3/aulas/modularizacao-em-python/modulos/exercicio-107-exercitando-modulos-em-python/
--------------------------------------------------------

Exercício Python 107: Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), 
diminuir(), dobro() e metade(). Faça também um programa que importe esse módulo e use algumas 
dessas funções.

Exercício Python 108: Adapte o código do desafio #107, criando uma função adicional chamada 
moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(q, taxa):
    resp = q + (q * taxa/100)
    return resp

def diminuir(q , taxa):
    resp = q - (q * taxa/100)
    return resp

def dobro(q):
    resp = q * 2
    return resp

def metade(q):
    resp = q / 2
    return resp

# ---
import moeda

quantia = float(input('Registre a quantia: \nR$'))
print('')
print('-=' *30)
aum = moeda.aumentar(quantia, 10)
print('--- Aumentando 10% da taxa, temos: R${:.2f}'.format(aum))
sub = moeda.diminuir(quantia, 10)
print('--- Diminuindo 10% da taxa, temos: R${:.2f}'.format(sub))
db = moeda.dobro(quantia)
print('--- O dobro desse valor é: R${:.2f}'.format(db))
met = moeda.metade(quantia)
print('--- A metade desse valor é: R${:.2f}'.format(met))
print('-=' *30)
--------------------------------------------------------

Exercício Python 109: Modifique as funções que form criadas no desafio 107 para que elas aceitem um 
parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), 
desenvolvida no desafio 108.

def aumentar(q=0, taxa=0, formato=False):
    resp = q + (q * taxa/100)
    return resp if formato is False else moeda(resp)

def diminuir(q=0 , taxa=0, formato=False):
    resp = q - (q * taxa/100)
    return resp if formato is False else moeda(resp)

def dobro(q=0, formato=False):
    resp = q * 2
    return resp if not formato else moeda(resp)

def metade(q=0, formato=False):
    resp = q / 2
    return resp if not formato else moeda(resp)
    
def moeda(q=0, moeda='R$'):
    return f'{moeda}{q:>.2f}'.replace('.', ',')


# ---
import moeda

quantia = float(input('Registre a quantia: \nR$'))
print('')
print('-=' *30)
aum = moeda.aumentar(quantia, 10, True)
print('--- Aumentando 10% da taxa, temos: R${}'.format(aum))
sub = moeda.diminuir(quantia, 10, True)
print('--- Diminuindo 10% da taxa, temos: R${}'.format(sub))
db = moeda.dobro(quantia, True)
print('--- O dobro desse valor é: R${}'.format(db))
met = moeda.metade(quantia, True)
print('--- A metade desse valor é: R${}'.format(met))
print('-=' *30)
--------------------------------------------------------

Exercício Python 110: Adicione o módulo moeda.py criado nos desafios anteriores, 
uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos 
no módulo criado até aqui.

def aumentar(q=0, taxa=0, formato=False):
    """
    ->Calcula o aumento de um determinado preço, retornando
    o resultado com ou sem formataçao.
    :param. preço: O preço que se quer reajustar;
    :param. taxa: Qual é a porcentagem do aumento;
    :param. formato: Quer a saída formatada ou não?
    :return: O valor reajustado, com ou sem formato.
    """
    resp = q + (q * taxa/100)
    return resp if formato is False else moeda(resp)

def diminuir(q=0 , taxa=0, formato=False):
    resp = q - (q * taxa/100)
    return resp if formato is False else moeda(resp)

def dobro(q=0, formato=False):
    resp = q * 2
    return resp if not formato else moeda(resp)

def metade(q=0, formato=False):
    resp = q / 2
    return resp if not formato else moeda(resp)
    
def moeda(q=0, moeda='R$'):
    return f'{moeda}{q:>.2f}'.replace('.', ',')


def resumo(q=0, taxaa=10, taxar=5):
    print('-=' *30)
    print('RESUMO DO VALOR'.center(30))
    print('-=' *30)
    print('Preço Analisado: \t{}'.format(moeda(q)))
    print('Dobro da quantia: \t{}'.format(dobro(q, True)))
    print('Metade da quantia: \t{}'.format(metade(q, True)))
    print('>> Com {}% de aumento: \t{}'.format(taxaa, aumentar(q, taxaa, True)))
    print('>> Com {}% de redução: \t{}'.format(taxar, diminuir(q, taxar, True)))
    print('-=' *30)


#---
import moeda

quantia = float(input('Registre a quantia: \nR$'))
moeda.resumo(quantia, 20, 12)
print('')
help(moeda)
--------------------------------------------------------

Exercício Python 111: Crie um pacote chamado utilidadesCeV que tenha dois módulos internos chamados 
moeda e dado. Transfira todas as funções utilizadas nos desafios 107, 108 e 109 para o primeiro 
pacote e mantenha tudo funcionando.


Exercício Python 112: Dentro do pacote utilidadesCeV que criamos no desafio 111, temos um módulo 
chamado dado. Crie uma função chamada leiaDinheiro() que seja capaz de funcionar como a função imputa(),
mas com uma validação de dados para aceitar apenas valores que seja monetários.

-- exe111
	-- utilidadescev
		-- dado
		def leiaDinheiro(msg):
			valido = False
			while not valido:
				entrada = str(input(msg)).replace(','m '.').strip()
				if entrada.isalpha() or entrada == '':
					print('\033[0;31[mERRO: \"{}\" é um preço inválido!\033[m'.format(entrada))
				else:
					valido = True
					return float(entrada)

		-- moeda
			__init__.py
			def aumentar(q=0, taxa=0, formato=False):
			    """
			    ->Calcula o aumento de um determinado preço, retornando
			    o resultado com ou sem formataçao.
			    :param. preço: O preço que se quer reajustar;
			    :param. taxa: Qual é a porcentagem do aumento;
			    :param. formato: Quer a saída formatada ou não?
			    :return: O valor reajustado, com ou sem formato.
			    
			    ~~~~~~~

			    """
			    resp = q + (q * taxa/100)
			    return resp if formato is False else moeda(resp)

			def diminuir(q=0 , taxa=0, formato=False):
			    resp = q - (q * taxa/100)
			    return resp if formato is False else moeda(resp)

			def dobro(q=0, formato=False):
			    resp = q * 2
			    return resp if not formato else moeda(resp)

			def metade(q=0, formato=False):
			    resp = q / 2
			    return resp if not formato else moeda(resp)
			    
			def moeda(q=0, moeda='R$'):
			    return f'{moeda}{q:>.2f}'.replace('.', ',')


			def resumo(q=0, taxaa=10, taxar=5):
			    print('-=' *30)
			    print('RESUMO DO VALOR'.center(30))
			    print('-=' *30)
			    print('Preço Analisado: \t{}'.format(moeda(q)))
			    print('Dobro da quantia: \t{}'.format(dobro(q, True)))
			    print('Metade da quantia: \t{}'.format(metade(q, True)))
			    print('>> Com {}% de aumento: \t{}'.format(taxaa, aumentar(q, taxaa, True)))
			    print('>> Com {}% de redução: \t{}'.format(taxar, diminuir(q, taxar, True)))
			    print('-=' *30)
					-- painel
		-- painel 
		from exe111.utilidadescev import moeda
		from exe111.utilidadescev import moeda
		-

		quantia = dado.leiaDinheiro('Registre a quantia: \nR$'))
		moeda.resumo(quantia, 20, 12)
		print('')
		help(moeda)
.
.
.
.
.
.
.
.
.
.
-- pythontest
	-- vendas
	-- Python Packages (__init__.py)
		-- calc_preco
		def aumento(valor, porcentagem):
    		r = valor + (valor * (porcentagem/100))
    		return r

		def reducao(valor, porcentagem):
		    r = valor - (valor * (porcentagem/100))
		    return r
		-- painel 
		import vendas.calc__preco

		preco = 49.90
		preco_com_aumento = vendas.calc_preco.aumento(preco, 15)
		print(preco_com_aumento)
--------------------------------------------------------

