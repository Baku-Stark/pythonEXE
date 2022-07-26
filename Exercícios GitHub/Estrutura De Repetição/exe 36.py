'''
Faça um programa que mostre os n termos da Série a seguir:

      S = 1/1 + 2/3 + 3/5 + 4/7 + 5/9 + ... + n/m. 

    Imprima no final a soma da série. 
'''

soma = 0
m = 1

num = int(input('Número de séries: '))
print('')
print('S = '),
for n in range(1, num+1):
	print('{} / {}... '.format(n, m)),
	if n < num and num > 1:
		print(' + '),
	else:
		print('FIM!')
	soma += n / m
	m += 2
print('')
print('\a A soma da série é: {:.2f}'.format(soma))
