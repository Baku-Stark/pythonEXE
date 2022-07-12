Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
print('')
if num1 > num2:
	print('{} é maior que {}'.format(num1, num2))
else:
	print('{} é maior que {}'.format(num2, num1))
  
_________________________________________________________________________
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

num = int(input('Digite um valor: '))
print('')
if (num > 0):
	print('>>> O número é positivo.')
else:
	print('>>> O número é negativo.')

_________________________________________________________________________
Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Sexo do usuário [M/F]: ')).upper().strip()
print('')
if sexo == 'M':
 	print('\aSexo Masculino ') 
elif sexo == 'F':
	print('\aSexo Feminino')
else:
	print('\aSexo Inválido!')

_________________________________________________________________________
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

tot_vogal = 0

word = str(input('Digite uma letra \nr: ')).lower().strip()
print('')
if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
	print('É UMA VOGAL!')
else:
	print('É UMA CONSOANTE!')

_________________________________________________________________________
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

aluno = str(input('Nome Do(a) aluno(a) \nr: '))
print('')
bim_1 = float(input('Nota do 1° Bimestre: '))
bim_2 = float(input('Nota do 2° Bimestre: '))
media = bim_1 + bim_2
print('')
print('[RESULTADO DO ALUNO]')
if media >= 7 and media <= 9:
	print('\a {} está APROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media < 7:
	print('\a {} está REPROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media == 10:
	print('\a {} está APROVADO COM DISTINÇÃO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
	
_________________________________________________________________________
Faça um Programa que leia três números e mostre o maior e o menor deles. 

num1 = float(input('Digite o 1° número: '))
print('')
num2 = float(input('Digite o 2° número: '))
print('')
num3 = float(input('Digite o 3° número: '))
print('')
print('-=' *30)
### MOSTRAR O MAIOR
if num1 > num2 and num1 > num3:
	print('\a O número {:.0f} é o maior'.format(num1))
elif num2 > num1 and num2 > num3:
	print('\a O número {:.0f} é o maior'.format(num2))
elif num3 > num1 and num3 > num2:
	print('\a O número {:.0f} é o maior'.format(num3))
print('')
### MOSTRAR O MENOR
if num1 < num2 and num1 < num3:
	print('\a O número {:.0f} é o menor'.format(num1))
elif num2 < num1 and num2 < num3:
	print('\a O número {:.0f} é o menor'.format(num2))
elif num3 < num1 and num3 < num2:
	print('\a O número {:.0f} é o menor'.format(num3))
print('-=' *30)

_________________________________________________________________________
Faça um programa que pergunte o preço de três produtos e informe qual produto 
você deve comprar, sabendo que a decisão é sempre pelo mais barato. 

def preco_Produto(ptd, ptd2, ptd3):
	print('')
	if ptd < ptd2 and ptd < ptd3:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd))
	elif ptd2 < ptd and ptd2 < ptd3:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd2))
	elif ptd3 < ptd and ptd3 < ptd2:
		print('\a O produto de R${:.2f} é o mais barato.'.format(ptd3))


###
ptd_1 = float(input('Preço Do 1° Produto \nr: '))
ptd_2 = float(input('Preço Do 2° Produto \nr: '))
ptd_3 = float(input('Preço Do 3° Produto \nr: '))
preco_Produto(ptd_1, ptd_2, ptd_3)

_________________________________________________________________________
Faça um Programa que leia três números e mostre-os em ordem decrescente. 

listanum = []
for n in xrange(1, 4):
	listanum.append(int(input('Digite o {}° número \nr: '.format(n))))
	print('')
listanum.sort(reverse=True)
print('Os números na ordem descrescente: {}'.format(listanum))

_________________________________________________________________________
Faça um Programa que pergunte em que turno você estuda. Peça para digitar 
'M-matutino' ou 'V-Vespertino' ou 'N-Noturno'. Imprima a mensagem 
"Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.

def dia_Turno(turno):
	print('')
	if turno == 'MANHÃ':
		print('\a Turno da Manhã: BOM DIA!')
	elif turno == 'TARDE':
		print('\a Turno da Tarde: BOA TARDE!')
	elif turno == 'NOITE':
		print('\a Turno da Noite: BOA NOITE!')
	else:
		print('[ERRO] Resposta Inválida!')


###
dia = str(input('''Turno De Estudo
[MANHÃ]
[TARDE]
[NOITE]

\nr: ''')).upper()
dia_Turno(dia)

_________________________________________________________________________
As Organizações Tabajara resolveram dar um aumento de salário aos seus 
colaboradores e lhe contraram para desenvolver o programa que calculará os 
reajustes.

    Faça um programa que recebe o salário de um colaborador e o reajuste 
    segundo o seguinte critério, baseado no salário atual:
    []Salários até R$ 280,00 (incluindo) : aumento de 20%

    []Salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
    
    []Salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
    
    []Salários de R$ 1500,00 em diante : aumento de 5% 
    
    Após o aumento ser realizado, informe na tela:
    []O salário antes do reajuste;

    []O percentual de aumento aplicado;

    []O valor do aumento;
    
    []O novo salário, após o aumento. 

print('-=' *30)
print('   TABAJARA   ')
print('-=' *30)
print('')
salario = float(input('Salário Do Usuário R$'))
print('')
## <= 280 == 20%
if salario <= 280:
	percentual = 20
	aumento = salario + (salario * 20/100)
	valor_aumento = aumento - salario
## > 280 <= 700 == 15%
elif salario > 280 and salario <= 700:
	percentual = 15
	aumento = salario + (salario * 15/100)
	valor_aumento = aumento - salario
## > 700 <= 1500 == 10%
elif salario > 700 and salario <= 1500:
	percentual = 10
	aumento = salario + (salario * 10/100)
	valor_aumento = aumento - salario
## > 1500 == 5%
elif salario > 1500:
	percentual = 5
	aumento = salario + (salario * 5/100)
	valor_aumento = aumento - salario
print('-=' *30)
print('TOTAL:')
print('')
print('--- Salário antes do reajuste: R${:.2f}'.format(salario))
print('--- Percentual de aumento aplicado: {}%'.format(percentual))
print('--- O valor do aumento: R${:.2f}'.format(valor_aumento))
print('')
print('    Novo Salário: R${:.2f}'.format(aumento))
print('-=' *30)

_________________________________________________________________________
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os 
descontos são do Imposto de Renda, que depende do salário bruto 
(conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde 
a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). 
O Salário Líquido corresponde ao Salário Bruto menos os descontos. 
O programa deverá pedir ao usuário o valor da sua hora e a quantidade de 
horas trabalhadas no mês. 
	Desconto do IR: 
	[] Salário Bruto até 900 (inclusive) - isento

	[] Salário Bruto até 1500 (inclusive) - desconto de 5% 

	[] Salário Bruto até 2500 (inclusive) - desconto de 10% 

	[] Salário Bruto acima de 2500 - desconto de 20% 
	Imprima na tela as informações, dispostas conforme o exemplo abaixo.

print('-=' *30)
print('   FOLHA DE PAGAMENTO   ')
print('-=' *30)
print('')
dia = int(input('Dias Trabalhados \nr: '))
print('')
sal_hora = float(input('Salário Por Hora \nR$'))
salario = sal_hora * dia
print('')
print('-=' *30)
print('TOTAL:')
print('')
## INSENTO
if salario <= 900:
	print('Salário Insento!')
	print('Salário Bruto:  R${:.2f}'.format(salario))
	salario_liq = salario

## IR (5%) + INSS (10%)
elif salario > 900 and salario <= 1500:
	print('Desconto De 15% (IR + INSS)')
	print('Salário Bruto:  R${:.2f}'.format(salario))
	salario_liq = salario - (salario * 15/100)
	tot_desconto = salario - salario_liq

## IR (10%) + INSS (10%)
elif salario > 1500 and salario <= 2500:
	print('Desconto de 20% (IR + INSS)')
	print('Salário Bruto:  R${:.2f}'.format(salario))
	salario_liq = salario - (salario * 20/100)
	tot_desconto = salario - salario_liq

## IR (20%) + INSS (10%)
elif salario > 2500:
	print('Desconto de 30% (IR + INSS)')
	print('Salário Bruto:  R${:.2f}'.format(salario))
	salario_liq = salario - (salario * 30/100)
	tot_desconto = salario - salario_liq

## FGTS (11%)
desc = salario - (salario * 11/100)
fgts = salario - desc
print('--- FGTS (11%): R${:.2f}'.format(fgts))
print('--- Total De Descontos: R${:.2f}'.format(tot_desconto))
print('')
print('    Salário Liquido: R${:.2f}'.format(salario_liq))
print('-=' *30)

_________________________________________________________________________
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.

print('''
[ 1 ] -- Domingo
[ 2 ] -- Segunda
[ 3 ] -- Terça
[ 4 ] -- Quarta
[ 5 ] -- Quinta
[ 6 ] -- Sexta
[ 7 ] -- Sábado''')
print('')
semana = int(input('Escolha o dia da semana: '))
if semana == 1:
	print('\a DOMINGO')
elif semana == 2:
	print('\a SEGUNDA-FEIRA!')
elif semana == 3:
	print('\a TERÇA-FEIRA!')
elif semana == 4:
	print('\a QUARTA-FEIRA!')
elif semana == 5:
	print('\a QUINTA-FEIRA!')
elif semana == 6:
	print('\a SEXTA-FEIRA!')
elif semana == 7:
	print('\a DOMINGO!')
else:
	print('\a [ERRO] Dia Da Semana Inválido!')
	
_________________________________________________________________________
