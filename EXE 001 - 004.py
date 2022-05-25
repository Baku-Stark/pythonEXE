>>> - Exercício Python
-> https://www.youtube.com/watch?v=nIHq1MtJaKs&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=7

--------------------------------------------------------

# Desafio 001:
print('Olá, Mundo!')
msg = 'Olá Mundo'
print(msg)
--------------------------------------------------------

# Desafio 002:
nome = input('Qual o seu nome?')
print('Bem-Vindo ao Python EXE', nome)
--- print('Bem-Vindo ao Python, {}!'.format(nome))
--------------------------------------------------------

#Desafio 003:
n1 = int(input('Primeiro Número:'))
n2 = int(input('Primeiro Número:'))
soma = n1 + n2
print(int(n1)+int(n2))
--- print ('O resultado é {} + {} = {}'.format(n1, n2, soma))
--------------------------------------------------------

#Desafio 004:
Mostrar o tipo primitivo:
a = input('Digite Algo:')
print('O tipo primitivo da sua resposta é', type(a))
print('O tipo primitivo da sua resposta é {}'.format(type(a)))
--- O tipo primitivo da sua resposta é <type 'str'>
Informações:
print('O valor é um número?', a.isnumeric())
print('O valor é um alfabeto?', a.isalpha())
print('O valor é um alfa-número?', a.isalnum())
