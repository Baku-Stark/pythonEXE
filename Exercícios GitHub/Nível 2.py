Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa. Pergunte o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 
30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa \nR$'))
print('')
salario = float(input('Salário do comprador \nR$'))
print('')
anos = float(input('Quantos anos de pagamento \nR$'))
print('')
print('-=' *30)
print('--- Resultado Bancário ---')
prestacao = casa / (anos*2)
minus = casa * 30/100
print('')
print('''Dados da compra 
>>> Salário: R${:.2f} 
>>> Ano(s): {:.0f} ano(s)'''.format(salario, anos))
print('>>> Prestação: R${:.2f}'.format(prestacao))
if prestacao <= minus:
	print('    --- PRESTAÇÃO APROVADA!!!')

else:
	print('    --- PRESTAÇÃO REPROVADA!!!')
print('-=' *30)

_________________________________________________________________________
Escreva um programa em Python que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a base de conversão: 
>>> https://www.to-convert.com/pt/index.php#body

1 para binário;
2 para octal; 
3 para hexadecimal.

print('--- CONVERSÃO ---')
print('')
num = int(input('Escolha um número \nr: '))
print('')
print(''' TABELA DE CONVERSÃO
[ 1 ] - Para Binário
[ 2 ] - Para Octal
[ 3 ] - Para Hexadecimal''')
print('')
escolha = str(input('>>> Escolha o tipo de conversão \nr: '))
print('')
print('-=' *30)
if escolha == '1':
	print('Conversão para BINÁRIO: {}'.format(bin(num)[2:]))
elif escolha == '2':
	print('Conversão para OCTAL: {}'.format(oct(num)[1:]))
elif escolha == '3':
	print('Conversão para HEXADECIMAL: {}'.format(hex(num)[2:]))
else:
	print('ERROR!!! Escolha apenas um dos números entre 1 a 3!')
print('-=' *30)

_________________________________________________________________________
Escreva um programa que leia dois números inteiros e 
compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais


num1 = float(input('Digite o ° número: '))
num2 = float(input('Digite o ° número: '))
print('')
print('-=' *30)
if num1 > num2:
	print('{} é maior que {}'.format(num1, num2))
elif num2 > num1:
	print('{} é maior que {}'.format(num2, num1))
elif num1 == num2:
	print('{} e {} são iguais'.format(num1, num2))
print('-=' *30)

_________________________________________________________________________
Faça um programa que leia o ano de nascimento de um jovem e 
informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

import datetime 

currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
print('Current Year -> {}'.format(year))
--------------------------------------------

nome = str(input('Nome completo \nr: '))
print('')
idade = int(input('Idade do candidato \nr: '))
print('')
print('--- Data De Nascimento ---')
dia = int(input('Dia: '))
mes = int(input('Mês: '))
ano = int(input('Ano: '))
print('')
print('-=' *30)
if idade < 18:
	log = 18 - idade
	print('Nascido em: {}/{}/{}'.format(dia, mes, ano))
	print('>>> O alistamento só poderá ser efetuado daqui {} ano(s).'.format(log))
elif idade == 18:
	print('Nascido em: {}/{}/{}'.format(dia, mes, ano))
	print('>>> O candidato, {}, deverá fazer o alistamento neste ano!'.format(nome))
elif idade > 18:
	exp = idade - 18
	print('Nascido em: {}/{}/{}'.format(dia, mes, ano))
	print('>>> O alistamento expirou à {} ano(s) atrás!'.format(exp))
print('-=' *30)

_________________________________________________________________________
Crie um programa que leia duas notas de um aluno e 
calcule sua média, mostrando uma mensagem no final, de acordo com a média 
atingida:

– Média abaixo de 15.0: REPROVADO

– Média entre 15.5 e 19.0: RECUPERAÇÃO

– Média 20.0 ou superior: APROVADO

nome_aluno = str(input('Nome do(a) aluno(a): '))
print('')
print('-=' *30)
nota1_aluno = float(input('Nota (1° Bimestre) do(a) aluno(a): '))
nota2_aluno = float(input('Nota (2° Bimestre) do(a) aluno(a): '))
media1_s = nota1_aluno + nota2_aluno
print('')
print('-' *30)
nota3_aluno = float(input('Nota (3° Bimestre) do(a) aluno(a): '))
nota4_aluno = float(input('Nota (4° Bimestre) do(a) aluno(a): '))
media2_s = nota3_aluno + nota4_aluno
media_final = media1_s + media2_s
print('')
if media_final < 15.0:
	print('{} está REPROVADO.'.format(nome_aluno))
	print('>>> Nota Final: {:.1f}'.format(media_final))
elif media_final == 15.5 or media_final <= 19.0:
	print('{} está em RECUPERAÇÃO.'.format(nome_aluno))
	print('>>> Nota Final: {:.1f}'.format(media_final))
elif media_final >= 20.0:
	print('{} está APROVADO.'.format(nome_aluno))
	print('>>> Nota Final: {:.1f}'.format(media_final))
print('-=' *30)

_________________________________________________________________________
A Confederação Nacional de Natação precisa de um programa 
que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo 
com a idade:

– Até 9 anos: MIRIM

– Até 14 anos: INFANTIL

– Até 19 anos: JÚNIOR

– Até 25 anos: SÊNIOR

– Acima de 25 anos: MASTER

import datetime 
print('-=' *30)
print('--- PROGRAMA DE NATAÇÃO ---')
print('-=' *30)
print('')
print('TABELA DE IDADE')
print('''
[MIRIM] ------- 9  anos
[INFANTIL] ---- 14 anos 
[JÚNIOR] ------ 19 anos
[SÊNIOR] ------ 25 anos
[MASTER] ------ 25 anos >
	''')
currentDateTime = datetime.datetime.now()
date = currentDateTime.date()
year = date.strftime("%Y")
#print('Current Year -> {}'.format(year))
year_ano = int(year)
print('')
nome = str(input('Nome Do(a) Aluno(a) \nr: '))
print('')
print('[Data De Nascimento]')
dia = int(input('	Dia: '))
mes = int(input('	Mês: '))
ano = int(input('	Ano: '))
idade = year_ano - ano
print('')
print('	Idade do(a) aluno(a): {} anos.'.format(idade))
print('')
print('-=' *30)
if idade == 9 or idade < 13:
	print('{} está na classe: MIRIM.'.format(nome))
	print('--- Informações ---')
	print('– {}/{}/{}'.format(dia, mes, ano))
	print('– Até 9 anos: MIRIM')

elif idade == 14 or idade < 18:
	print('{} está na classe: INFANTIL.'.format(nome))
	print('--- Informações ---')
	print('– {}/{}/{}'.format(dia, mes, ano))
	print('– Até 14 anos: INFANTIL')

elif idade == 19 or idade < 25:
	print('{} está na classe: JÚNIOR.'.format(nome))
	print('--- Informações ---')
	print('– {}/{}/{}'.format(dia, mes, ano))
	print('– Até 19 anos: JÚNIOR')

elif idade == 25:
	print('{} está na classe: SÊNIOR.'.format(nome))
	print('--- Informações ---')
	print('– {}/{}/{}'.format(dia, mes, ano))
	print('– Até 25 anos: SÊNIOR')

elif idade > 25:
	print('{} está na classe: MASTER.'.format(nome))
	print('--- Informações ---')
	print('– {}/{}/{}'.format(dia, mes, ano))
	print('– Acima de 25 anos: MASTER')

print('-=' *30)

_________________________________________________________________________
Refaça o DESAFIO 35 dos triângulos, 
acrescentando o recurso de mostrar que tipo de triângulo será formado:

– EQUILÁTERO: todos os lados iguais

– ISÓSCELES: dois lados iguais, um diferente

– ESCALENO: todos os lados diferentes

resultado = True
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
	resultado = False
print('')
if resultado == False:
	print('-=' *30)
	print('O triângulo do usuário é:')
	print('>>> SOLUÇÃO INVÁLIDA!!!')
	print('-=' *30)
else:
	print('-=' *30)
	print('--- Formação do Triângulo ---')
	print('''
	[EQUILÁTERO] - Todos os lados iguais

	[ISÓSCELES] -- Dois lados iguais, um diferente

	[ESCALENO] --- Todos os lados diferentes''')
	print('')
	print('O triângulo do usuário é:')
	if r1 == r2 == r3:
		print('EQUILÁTERO: Todos os lados iguais')
	elif r1 == r2 or r1 == r3 or r2 == r3:
		print('>>> ISÓSCELES: Dois lados iguais, um diferente')
	else:
		print('>>> ESCALENO: Todos os lados diferentes.')
	print('-=' *30)

_________________________________________________________________________
Desenvolva uma lógica que leia o peso e a altura de uma 
pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de 
acordo com a tabela abaixo:

– IMC abaixo de 18,5: Abaixo do Peso

– Entre 18,5 e 25: Peso Ideal

– 25 até 30: Sobrepeso

– 30 até 40: Obesidade

– Acima de 40: Obesidade Mórbida 

---- imc = peso / (alt ** 2) kg/m²

nome = str (input('Digite seu nome \nr: '))
print('')
peso = float (input('Digite seu peso [Kg] \nr: '))
print('')
altura = float (input('Digite sua altura [metros] \nr: '))
print('')
imc = peso / (altura ** 2)
print('-=' *30)
print('''
IMC abaixo de 18,5: Abaixo do Peso

Entre 18,5 e 25: Peso Ideal

25 até 30: Sobrepeso

30 até 40: Obesidade

Acima de 40: Obesidade Mórbida''')
print('.')
print('.')
print('.')
print('.')
print('--- Dados Do Usuário ---')
if imc < 18.5:
	print('[Abaixo do Peso]')
elif imc == 18.5 and imc < 25:
	print('[Peso Ideal]')
elif imc == 25 and imc < 30:
	print('[Sobrepeso]')
elif imc == 30 and imc <= 40:
	print('[Obesidade]')
elif imc > 40:
	print('[Obesidade Mórbida]')
print('>>> O IMC de {} está em: {:.1f}km/g²'.format(nome, imc))
print('-=' *30)

_________________________________________________________________________
Elabore um programa que calcule o valor a ser pago por um 
produto, considerando o seu preço normal e condição de pagamento:

– à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros

print('-=' *15)
print('=== LOJA FREITAS ===')
print('-=' *15)
print('')
produto = float(input('Preço Do Produto \nr: '))
print('')
select = int(input('''
- Escolha Do Pagamento: 
[ 1 ] -- Dinheiro/Cheque 
[ 2 ] -- Cartão

r: '''))
print('')
print('-=' *30)
print('TOTAL')
print('')
if select == 1:
	total_10 = produto - (produto * 10/100)
	print('À vista dinheiro/cheque: 10% de desconto')
	print('>>> Preço Do Produto: R${:.2f}'.format(total_10))
elif select == 2:
	print('Cartão De Crédio!')
	print('')
	parcela = int(input('- Parcelamento: '))
	print('')
	if parcela == 0 or parcela == 1:
		total_5 = produto - (produto * 5/100)
		print('À vista no cartão: 5% de desconto')
		print('>>> Preço Do Produto: R${:.2f}'.format(total_5))
	elif parcela == 2:
		tot_normal = produto / 2
		print('Em até 2x no cartão: preço formal')
		print('>>> Produto: R${:.2f}'.format(tot_normal))
	elif parcela >= 3:
		total_parcela = produto / parcela
		tot_parcela = total_parcela - (total_parcela * 20/100)
		print('3x ou mais no cartão: 20% de juros')
		print('>>> Preço Do Produto: R${:.2f}'.format(tot_parcela))
else:
	print('ERRO! Nenhuma opção de pagamento foi selecionada!')
print('-=' *30)
_________________________________________________________________________
