Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho 
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta 
é de 1 litro para cada 6 metros quadrados e que a tinta é vendida 
em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, 
que custam R$ 25,00. 

	Informe ao usuário as quantidades de tinta a serem compradas e os 
	respectivos preços em 3 situações:

	Comprar apenas latas de 18 litros;

	Comprar apenas galões de 3,6 litros;

	Misturar latas e galões, de forma que o desperdício de tinta seja menor. 
	Acrescente 10% de folga e sempre arredonde os valores para cima, 
	isto é, considere latas cheias. 

from time import sleep

print('-=' *30)
print('=== TINTASOL ===')
print('-=' *30)
print('')
tamanho = float(input('>>> Área da parede \nr: '))
litros = tamanho / 6
latas = litros / 18
print('')
print('-=' *30)
print('Calculando...')
sleep(1)
if latas % 18 != 0:
	latas += 1
preco = latas * 80
galoes = litros / 3.6

if galoes % 3.6 != 0:
	galoes += 1
preco2 = galoes * 25

#mistura galoes/tintas
mistura_lata = int(litros/18.0)
mistura_galao = int((litros - (mistura_lata * 18)) / 3.6)
if litros - (mistura_lata * 18) % 3.6 != 0:
	mistura_galao += 1
print('')
print('Apenas latas de 18 litros: {}L'.format(latas))
print('--- PREÇO: R${:.2f}'.format(preco))
print('')
print('Apenas galões de 3.6 litros: {}'.format(galoes))
print('--- PREÇO: R${:.2f}'.format(preco2))
print('')
print('Mistura: {} latas e {} galões = {:.2f}'
	.format(mistura_lata, mistura_galao, (mistura_lata * 80) + (mistura_galao * 25)))
print('-=' *30)
