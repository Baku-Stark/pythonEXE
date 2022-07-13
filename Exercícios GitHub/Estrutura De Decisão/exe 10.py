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
