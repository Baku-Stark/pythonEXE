'''
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número inteiro 
entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a tabuada. 
A saída deve ser conforme o exemplo abaixo: 
'''

num = int(input('Escolha O Numerador: '))
print('')
print('-=' *30)
print('TABUADA DE {}'.format(num))
print('')
for x in xrange(1, 11):
	print('{} x {:>2} = {}'.format(num, x, num*x))
print('-=' *30)
