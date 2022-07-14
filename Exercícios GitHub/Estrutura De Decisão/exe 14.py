Faça um Programa que peça os 3 lados de um triângulo. O programa deverá informar 
se os valores podem ser um triângulo. Indique, caso os lados formem um triângulo, 
se o mesmo é: equilátero, isósceles ou escaleno.

    Dicas:
    Três lados formam um triângulo quando a soma de quaisquer dois lados for 
    maior que o terceiro;
    Triângulo Equilátero: três lados iguais;
    Triângulo Isósceles: quaisquer dois lados iguais;
    Triângulo Escaleno: três lados diferentes; 


lado_1 = float(input('Informe o 1° lado \nr: '))
print('')
lado_2 = float(input('Informe o 2° lado \nr: '))
print('')
lado_3 = float(input('Informe o 3° lado \nr: '))
print('')
print('-=' *30)
if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_3 + lado_1 and lado_2:
	print('FORMOU UM TRIÂNGULO!')
	print('')
	print('É um triângulo...')
	if lado_1 == lado_2 == lado_3:
		print('\a EQUILÁTERO! [três lados iguais]')
	elif lado_1 == lado_2 or lado_1 == lado_3 or lado_2 == lado_3:
		print('\a ISÓSCELES! [quaisquer dois lados iguais]')
	else:
		print('\a ESCALENO! [três lados diferentes]')
else:
	print('Os lados informados não podem formar um triângulo.')
print('-=' *30)
