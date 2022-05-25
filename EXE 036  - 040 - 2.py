>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-2/aulas/condicoes-em-python-if-elif/modulos/exercicio-36-aprovando-emprestimo/
--------------------------------------------------------

Exercício Python 36: Escreva um programa para aprovar o empréstimo 
bancário para a compra de uma casa. Pergunte o valor da casa, o salário do 
comprador e em quantos anos ele vai pagar. A prestação mensal não pode exceder 
30% do salário ou então o empréstimo será negado.

casa = float(input('Valor da casa: R$'))
salario = float(input('Salário do comprador: R$'))
ano = int(input('Quantos anos de financiamento: '))
prest = casa / (ano * 12)
minus = salario * 30 / 100
print('')
print('Resolução: R${:.2f} em {} anos.'.format(casa, ano))
print('(A prestação será de R${:.2f})'.format(prest))
if prest <= minus:
	print('   --- Empréstimo APROVADO!')
else:
	print('   --- Empréstimo NEGADO!')
--------------------------------------------------------

Exercício Python 37: Escreva um programa em Python que leia um número inteiro 
qualquer e peça para o usuário escolher qual será a base de conversão: 
1 para binário; 
2 para octal; 
3 para hexadecimal.

num = int(input('Registre um número inteiro: '))
print('')
print(''' Escolha uma das opções para a conversão:
	[ 1 ] Para BINÁRIO
	[ 2 ] Para OCTAL
	[ 3 ] Para HEXADECIMAL''')
opc = str(input(' Qual opção para a base de conversão: '))
print('-=' *20)
if opc == '1':
	print('Conversão BINÁRIO: {}.'.format(bin(num)[2:]))
elif opc == '2':
	print('Conversão OCTAL: {}.'.format(oct(num)[1:]))
elif opc == '3':
	print('Conversão HEXADECIMAL: {}.'.format(hex(num)[2:]))
else:
	print('ERROR!!! Opção Inválida!')
print('-=' *20)
--------------------------------------------------------

Exercício Python 38: Escreva um programa que leia dois números inteiros e 
compare-os. mostrando na tela uma mensagem:

– O primeiro valor é maior

– O segundo valor é maior

– Não existe valor maior, os dois são iguais

num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
print('')
if num1 > num2:
	print('O PRIMEIRO valor é maior que o SEGUNDO.')
elif num1 < num2:
	print('O SEGUNDO valor é maior que o PRIMEIRO.')
else:
	print('Ambos VALORES são iguais.')
--------------------------------------------------------

Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e 
informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço 
militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

< 18
==18
> 18

print('''
	SERVIÇO MILITAR DO \033[32mBR\033[34mAS\033[33mIL\033[m!!!''')
print('    >>> SEJA BEM-VINDO(A) <<<!')
candidato = str(input('Digite seu nome: '))
idade = int(input('Registre sua idade: '))
print('Data de nascimento')
dia = int(input('DIA: '))
mes = int(input('MÊS: '))
ano = int(input('ANO: '))
print('')
print('-=' *15)
if idade < 18:
	resultado = 18 - idade
	print('Você deverá fazer seu alistamento daqui {} ano(s).'.format(resultado))
elif idade == 18:
	print('O seu alistamento é este ano!!!')
else:
	print('Você passou do seu prazo de alistamento.')
print('-=' *15)
--------------------------------------------------------

Exercício Python 40: Crie um programa que leia duas notas de um aluno e 
calcule sua média, mostrando uma mensagem no final, de acordo com a média 
atingida:

– Média abaixo de 5.0: REPROVADO

– Média entre 5.0 e 6.9: RECUPERAÇÃO

– Média 7.0 ou superior: APROVADO

print('''
	BOLETIM DO ALUNO!!!
''')
print('''Selecione a turma:
	[3001] -> Turmas A
	[3002] -> Turmas B
	[3003] -> Turmas C
	''')
print('')
select = int(input('Turma do aluno: '))
if select == 3001:
	print('''Os alunos da 3001 são:
		Tony Stark
		Bruce Banner
		Steve Rogers''')
elif select == 3002:
	print('''Os alunos da 3002 são:
		Natasha Romanoff
		Clint Barton
		Nick Fury''')
elif select == 3003:
	print('''Os alunos da 3003 são:
		Thor Odinson
		Hela Odinson
		Loki Lraufrenson''')
else:
	print('Nenhuma turma encontrada!!')
print('')
print('')
aluno = str(input('Nome do aluno(a): '))
nota1 = float(input('Nota do 1° BIMESTRE: '))
nota2 = float(input('Nota do 2° BIMESTRE: '))
somam = nota1 + nota2
nota3 = float(input('Nota di 3° BIMESTRE: '))
nota4 = float(input('Nota do 4° BIMESTRE: '))
somam2 = nota3 + nota4
somafn = somam + somam2
print('A média final é: {}'.format(somafn))
print('''
	Abaixo de 15.5: Reprovado
	Entre 16 e 19.5: Recuperação
	Igual ou acima de 20: Aprovado
''')
print('')
print('-=' *15)
if somafn < 15.5:
	print('{} está REPROVADO!'.format(aluno))
elif somafn == 16 or somafn <= 19.5:
	print('{} está em RECUPERAÇÃO!'.format(aluno))
else:
	print('{} está APROVADO! PARABÉNS!!!'.format(aluno))
print('-=' *15)
--------------------------------------------------------