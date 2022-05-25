>>>  - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/tratando-dados-e-fazendo-contas/modulos/exercicio-13-reajuste-salarial/
--------------------------------------------------------

* Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento.

salario = float(input('Digite o salário: R$'))
newsalario = salario + (salario * 15 / 100)
print('Seu novo salário é: R${}'.format(newsalario))

--------------------------------------------------------

* Exercício Python 14: Escreva um programa que converta uma temperatura 
digitando em graus Celsius e converta para graus Fahrenheit.

tempc = float(input('Registre a temperatura em Celsius (°C):'))
fahr = tempc + (tempc * 9/5) 
print('A temperatura em Fahrenheit (F) é: {}'.format(fahr))

--------------------------------------------------------

*Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos por um 
carro alugado e a quantidade de dias pelos quais ele foi alugado. 
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e 
R$0,15 por Km rodado.

1 dia = 60.00
1 km = 0.15
print('1 dia = R$60.00')
dias = int(input('Quantos dias o carro foi alugado:'))
print('')
print('1 km = R$0.15')
km = float(input('Km rodados:'))
diasrod = dias *60.00
#print(diasrod)
kmrod = km *0.15
#print(kmrod)
resultado = diasrod + kmrod
print('')
print('-' *20)
print('O valor total a pagar é: {}'.format(resultado))
print('-' *20)
print('')

--------------------------------------------------------

* Exercício Python 16: Crie um programa que leia um número Real qualquer 
pelo teclado e mostre na tela a sua porção Inteira.

num = float(input('Digite um valor:'))
print('A porção inteira é {}'.format(int(num)))