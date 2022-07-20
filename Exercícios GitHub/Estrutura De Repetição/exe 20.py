'''
Desenvolva um programa que faça a tabuada de um número qualquer inteiro que será 
digitado pelo usuário, mas a tabuada não deve necessariamente iniciar em 1 e terminar 
em 10, o valor inicial e final devem ser informados também pelo usuário, 
conforme exemplo abaixo: 

Montar a tabuada de: 5
Começar por: 4
Terminar em: 7

Vou montar a tabuada de 5 começando em 4 e terminando em 7:
5 X 4 = 20
5 X 5 = 25
5 X 6 = 30
5 X 7 = 35
'''

finish = 0

num = int(input('\a Númerador \nr: '))
print('')
start = int(input('\a Início Da Tabuada de {} \nr: '.format(num)))
print('')
finish = int(input('\a Final Da Tabuada de {} \nr: '.format(num)))
while finish == 0:
	finish = int(input('\a Por favor, informe o Final Da Tabuada de {} \nr: '.format(num)))
print('')
if start == finish:
	print('--- O Início e Final não podem ser iguais')
	print('--- O Final passará a valer como 10')
	finish = 10
print('-=' *30)
print('''
Tabuada de: {}
Início:     {}
Final:      {}
'''.format(num, start, finish))
print('')
for x in xrange(start, finish+1):
	multi = num * x
	print('{} X {:>2} = {}'.format(num, x, multi))
print('-=' *30)
