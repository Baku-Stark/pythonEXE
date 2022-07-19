'''
Supondo que a população de um país A seja da ordem de 80.000 habitantes com uma 
taxa anual de crescimento de 3% e que a população de B seja 200.000 habitantes com uma 
taxa de crescimento de 1.5%. Faça um programa que calcule e escreva o número de anos 
necessários para que a população do país A ultrapasse ou iguale a população do país B, 
mantidas as taxas de crescimento. 
'''

# População A
1 ano ---> 3% de crescimento populacional
(50 anos ---> 150% para igualar a 200.000)

# População B
1 ano ---> 1.5% de crescimento populacional

popu_a = 80000
popu_b = 200000
ano = 0

while popu_a <= popu_b:
	ano += 1
	popu_a += popu_a * 0.03
	popu_b += popu_b * 0.015

print('Para a população A igualar a popução B são necessários {} ano(s)'.format(ano))
print('')
print('-=' *30)
print('Em {} ano(s):'.format(ano))
print('')
print('\a População A: {:.0f}'.format(popu_a))
print('\a População B: {:.0f}'.format(popu_b))
print('-=' *30)
