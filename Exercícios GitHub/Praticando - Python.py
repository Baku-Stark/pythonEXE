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