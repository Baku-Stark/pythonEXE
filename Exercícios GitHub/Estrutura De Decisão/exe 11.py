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
