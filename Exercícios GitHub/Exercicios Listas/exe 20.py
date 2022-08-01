'''
As Organizações Tabajara resolveram dar um abono aos seus colaboradores em reconhecimento 
ao bom resultado alcançado durante o ano que passou. Para isto contratou você para 
desenvolver a aplicação que servirá como uma projeção de quanto será gasto com o pagamento 
deste abono. 
Após reuniões envolvendo a diretoria executiva, a diretoria financeira e os representantes 
do sindicato laboral, chegou-se a seguinte forma de cálculo:
	a)Cada funcionário receberá o equivalente a 20% do seu salário bruto de dezembro; a.
	O piso do abono será de 100 reais, isto é, aqueles funcionários cujo salário for muito 
	baixo, recebem este valor mínimo; Neste momento, não se deve ter nenhuma preocupação 
	com colaboradores com tempo menor de casa, descontos, impostos ou outras particularidades. 
	Seu programa deverá permitir a digitação do salário de um número indefinido 
	(desconhecido) de salários. Um valor de salário igual a 0 (zero) encerra a digitação. 
	Após a entrada de todos os dados o programa deverá calcular o valor do abono concedido 
	a cada colaborador, de acordo com a regra definida acima. Ao final, o programa deverá 
	apresentar: 
		*O salário de cada funcionário, juntamente com o valor do abono; 

		*O número total de funcionário processados; 

		*O valor total a ser gasto com o pagamento do abono; 

		*O número de funcionário que receberá o valor mínimo de 100 reais; 

		*O maior valor pago como abono; A tela abaixo é um exemplo de execução do programa,
		apenas para fins ilustrativos. Os valores podem mudar a cada execução do programa.

Projeção de Gastos com Abono
============================ 
 
Salário: 1000
Salário: 300
Salário: 500
Salário: 100
Salário: 4500
Salário: 0
 
Salário    - Abono     
R$ 1000.00 - R$  200.00
R$  300.00 - R$  100.00
R$  500.00 - R$  100.00
R$  100.00 - R$  100.00
R$ 4500.00 - R$  900.00
 
Foram processados 5 colaboradores
Total gasto com abonos: R$ 1400.00
Valor mínimo pago a 3 colaboradores
Maior valor de abono pago: R$ 900.00 
'''

# === DADOS ===
abonos_res = []
salario = []
abonos = 0
minimo = 0
maior = 0
s = 0

# === FUNÇÃO DEF CLEAR ===
def clear():
	print('\n' *10)

print('=== Registro ("0" encerra o programa) ===')

while True:
	sal = float(input('Digite o salário \nR$'))
	abono = (sal * 20) / 100
	print('')
	if abono < 100:
		abono = 100

	if abono > maior:
		maior = abono
	
	elif sal == 0:
		break

	salario.append(sal)
	abonos_res.append(abono)
	abonos += abono
clear()
print('Projeção De Gastos Com Abono')
print('=' *30)
print('Salário - Abono')

for s in range(0, len(salario)):
	print('R${:.2f} - R${:.2f}'.format(salario[s], abonos_res[s]))

print('=' *30)
print('')
print('=' *30)
print('Resultados')
print('')
print('\a Foram processados {} colaboradores.'.format(len(salario)))
print('\a Total gasto com abonos R${:.2f}'.format(abonos))
print('\a Valor mínimo pago a {} colaboradores'.format(minimo))
print('\a Maior valor de abono pago: R${:.2f}'.format(maior))
print('=' *30)
