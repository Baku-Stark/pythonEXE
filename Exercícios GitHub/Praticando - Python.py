https://wiki.python.org.br/ListaDeExercicios
>>> Lista de Exercícios em Python (Python Brasil)

{Estrutura Sequencial}
Faça um Programa que mostre a mensagem "Alo mundo" na tela. 
print('Olá, Mundo!')

_________________________________________________________________________
Faça um Programa que peça um número e então mostre a mensagem 
'O número informado foi [número]'.
num = int(input('Registre um número: '))
print('O número informado foi {}'.format(num))

_________________________________________________________________________
Faça um Programa que peça dois números e imprima a soma. 
num1 = int(input('Digite o primeiro número: '))
num2 = int(input('Digite o segundo número: '))
print('')
soma = num1 + num2
print('>>> {} + {} = {}'.format(num1, num2, soma))

_________________________________________________________________________
Faça um Programa que peça as 4 notas bimestrais e mostre a média.
bim1 = float(input('Nota do 1° Bimestre \nr: '))
print('')
bim2 = float(input('Nota do 2° Bimestre \nr: '))
print('')
media_1 = bim1 + bim2
print('-' *10)
bim3 = float(input('Nota do 3° Bimestre \nr: '))
print('')
bim4 = float(input('Nota do 4° Bimestre \nr: '))
print('')
media_2 = bim3 + bim4
print('')
print('-=' *30)
media_final = media_1 + media_2
print('A média do primeiro semestre: {:.1f}'.format(media_1))
print('A média do segundo semestre: {:.1f}'.format(media_2))
print('')
print('>>> Média final do(a) aluno(a): {:.1f}'.format(media_final))
print('-=' *30)

_________________________________________________________________________
Faça um Programa que converta metros para centímetros.
1m -> 100cm 

metros = float(input('Comprimento para ser convertido [m]: '))
cm = metros * 100
print('{:.1f} metros ---> {:.1f} centímetros'.format(metros, cm))

_________________________________________________________________________
Faça um Programa que peça o raio de um círculo, calcule e mostre sua área. 
3.14 * r²

raio = float(input('Registre o valor do raio: '))
area = 3.14 * raio
print('')
print('>>> A área do círculo é de {:.1f}m²'.format(area))

_________________________________________________________________________
_________________________________________________________________________
Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro 
desta área para o usuário. 
a = b * h

print('--- Área do Quadrado ---')
print('Escolha o comprimento da base entre [m] e [cm]')
print('')
select = str(input('r: ')).upper().strip()
print('')
print('-=' *30)
if select == 'M':
	print('   [Cálculo em METROS]   ')
	print('')
	base = int(input('>>> Base: '))
	altu = int(input('>>> Altura: '))
	area = base * altu
	if base == altu:
		print('>>> A escolha foi um QUADRADO')
	elif base != altu:
		print('>>> A escolha foi um RETÂNGULO')
	print('')
	print('--- Área: {}m²'.format(area))
elif select == 'CM':
	print('   [Cálculo em CENTÍMETROS]   ')
	print('')
	base = int(input('>>> Base: '))
	altu = int(input('>>> Altura: '))
	area = base * altu
	if base == altu:
		print('>>> A escolha foi um QUADRADO')
	elif base != altu:
		print('>>> A escolha foi um RETÂNGULO')
	print('')
	print('--- Área: {}cm²'.format(area))
print('-=' *30)

_________________________________________________________________________
Faça um Programa que pergunte quanto você ganha por hora e o número de horas 
trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

salario_hora = float(input('>>> Salário por hora: R$'))
horas_trab = int(input('>>> Horas trabalhadas: '))
print('')
print('-=' *30)
salario = salario_hora * horas_trab
print('O salário no final do mês é de: R${:.2f}'.format(salario))
print('-=' *30)

_________________________________________________________________________
Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e 
mostre a temperatura em graus Celsius.  

print('--- Fahrenheit > Celsius ---')
### ([número] °F − 32) × 5/9 = °C
temp = float(input('Registre a temperatura em Fahrenheit (°F): '))
print('')
print('-=' *30)
print('({} °F − 32) × 5/9 = °C'.format(temp))
celsius = (temp - 32) * 5/9
print('')
print('Fahrenheit >>> Celsius: {:.1f}°C'.format(celsius))
print('-=' *30)

Faça um Programa que peça a temperatura em graus Celsius, transforme e 
mostre em graus Fahrenheit. 

print('--- Celsius > Fahrenheit ---')
### ([número] °C × 9/5) + 32 = 32 °F
temp = float(input('Registre a temperatura em Celsius (°C): '))
print('')
print('-=' *30)
print('({} °C × 9/5) + 32 = 32 °F'.format(temp))
fahrenheit = (temp * 9/5) + 32
print('')
print('Celsius >>> Fahrenheit: {}°F'.format(fahrenheit))
print('-=' *30)

_________________________________________________________________________
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

    o produto do dobro do primeiro com metade do segundo .
    a soma do triplo do primeiro com o terceiro.
    o terceiro elevado ao cubo. 

num1 = int(input('Registre o 1° número inteiro: '))
num2 = int(input('Registre o 2° número inteiro: '))
num3_f = float(input('Registre um número real: '))
print('')
print('-=' *30)
print('--- O produto do dobro do primeiro com metade do segundo ---')
pri_op = (num1 * 2) * (num2/2)
print('({} * 2) * ({}/2) = {}'.format(num1, num2, pri_op))
print('')
print('--- A soma do triplo do primeiro com o terceiro ---')
seg_op = (2 * num1) + num3_f
print('(2 * {}) + {} = {}'.format(num1, num3_f, seg_op))
print('')
print('--- O terceiro elevado ao cubo ---')
tri_op = num3_f **3
print('{}³ = {:.2f}'.format(num3_f, tri_op))
print('-=' *30)

_________________________________________________________________________
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58 

altura = float(input('Registre sua altura: '))
peso = (72.7 * altura) - 58 
print('')
print('>>> Seu peso é de: {}kg'.format(peso))

Tendo como dado de entrada a altura (altura) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7 * altura) - 58
    Para mulheres: (62.1 * altura) - 44.7 

altura = float(input('Registre sua altura: '))
sexo = str(input('Sexo [M/F]: ')).upper().strip()
print('')
print('-=' *30)
if sexo == 'M':
	print('--- MASCULINO ---')
	peso = (72.7 * altura) - 58
	print('>>> Seu peso é de: {}kg'.format(peso))
elif sexo == 'F':
	print('--- FEMININO ---')
	peso = (62.1 * altura) - 44.7
	print('>>> Seu peso é de: {}kg'.format(peso))
print('-=' *30)

_________________________________________________________________________
