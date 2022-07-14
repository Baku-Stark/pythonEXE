Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em 
metros quadrados da área a ser pintada. Considere que a cobertura da 
tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em 
latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de 
latas de tinta a serem compradas e o preço total. 

from time import sleep
tot_litro = 80.00

print('-=' *30)
print('=== TINTASOL ===')
print('-=' *30)
print('')
area = float(input('Área Da Parede: '))
print('Área selecionada pelo usuário: {:.1f}m²'.format(area))
print('')
print('-=' *30)
select = str(input('Concorda com a escolha?\n[S/N]: ')).upper()
print('')
if select == 'S':
	print('>>> Iniciando o calculo...')
	'''     3  m² == 1 Litro
		    6  m² == 2 Litros
		    30 m² == 10 Litros
		    54 m² == 18 Litros'''
	### Lata de tinta (18 litros) == R$ 80.00
	sleep(1)
	quant = area / 3
	if area > 54:
		tot_litro *= 2 
	print('A área de {}m² vai precisar de {:.0f} litros.'.format(area, quant))
	print('')
	print('')
	print('Valor: R${:.2f}'.format(tot_litro))
	elif area > 108:
		tot_litro *= 3
	print('A área de {}m² vai precisar de {:.0f} litros.'.format(area, quant))
	print('')
	print('')
	print('Valor: R${:.2f}'.format(tot_litro))
else:
	print('>>> Encerrando programa... Tchau!!!')
print('-=' *30)
