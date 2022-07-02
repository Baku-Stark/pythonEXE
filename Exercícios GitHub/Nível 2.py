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
