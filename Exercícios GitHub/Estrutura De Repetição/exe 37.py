'''
Sendo H= 1 + 1/2 + 1/3 + 1/4 + ... + 1/N, 
Faça um programa que calcule o valor de H com N termos. 
'''
num = int(input('Número de séries: '))
h = 0
print('')
for n in xrange(1, num +1):
	h = h + 1/n
	print('{} / {}'.format('1', n)),
	if n < num and num > 1:
		print(' + '),
	else:
		print('FIM!')
print('')
print('\a A soma da série é: {:.2f}'.format(h))
