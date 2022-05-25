>>>  - Exercício Python 
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/condicoes-em-python-if-else/modulos/exercicio-33-maior-e-menor-valores/
--------------------------------------------------------

Exercício Python 33: Faça um programa que leia três números e mostre qual é o 
maior e qual é o menor.

v1 = int(input('Primeiro valor: '))
v2 = int(input('Segundo valor: '))
v3 = int(input('Terceiro valor: '))
print('')
#Valor MENOR!!!
print('')
print('-' *20)
if v1<v2 and v1<v3:
	menor = v1
if v2<v1 and v2<v3:
	menor = v2
if v3<v1 and v3<v2:
	menor = v3
print('O MENOR valor é: {}.'.format(menor))
print('')
#Valor MAIOR!!!
print('')
if v1>v2 and v1>v3:
	maior = v1
if v2>v1 and v2>v3:
	maior = v2
if v3>v1 and v3>v2:
	maior = v3
print('O MAIOR valor é: {}.'.format(maior))
print('-' *20)
--------------------------------------------------------

Exercício Python 34: Escreva um programa que pergunte o salário de um 
funcionário e calcule o valor do seu aumento. Para salários superiores a 
R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é 
de 15%.

print('Sistema de cálculo salárial.')
print('>>> Superior a R$1250,00 terá aumento de 10%. Abaixo desse valor será 15%.')
print('Registre seu valor logo a baixo!')
print('')
print('-' *20)
salario = float(input('O seu atual salário: R$'))
print('')
if salario <= 1250:
	soma1 = salario + (salario * 15 / 100)
	print('Seu aumento é de: R${:.2f}.'.format(soma1))
else:
	soma2 = salario + (salario * 10 / 100)
	print('Seu aumento é de: R${:.2f}.'.format(soma2))
print('-' *20)
--------------------------------------------------------

Exercício Python 35: Desenvolva um programa que leia o comprimento de três retas
e diga ao usuário se elas podem ou não formar um triângulo.

print('-=' *15)
print('Vamos criar um triângulo!')
print('-=' *15)
print('')
r1 = float(input('Primeira Reta: '))
r2 = float(input('Segunda Reta: '))
r3 = float(input('Terceira Reta: '))
print('')
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
	print('---> Os segmentos podem formar um triângulo!')
else:
	print('---> Os segmentos acima são incapazes de formar um triângulo.')
--------------------------------------------------------