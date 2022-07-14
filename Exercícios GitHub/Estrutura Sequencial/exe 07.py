Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro 
desta área para o usuário. 
a = b * h

print('--- Área do Quadrado ---')
print('Escolha o comprimento da base entre [m] e [cm]')
print('')
select = str(input('r: ')).upper().strip()
print('')
print('-=' *30)
if select == 'M':
	print('   [Cálculo em METROS]   ')
	print('')
	base = int(input('>>> Base: '))
	altu = int(input('>>> Altura: '))
	area = base * altu
	if base == altu:
		print('>>> A escolha foi um QUADRADO')
	elif base != altu:
		print('>>> A escolha foi um RETÂNGULO')
	print('')
	print('--- Área: {}m²'.format(area))
elif select == 'CM':
	print('   [Cálculo em CENTÍMETROS]   ')
	print('')
	base = int(input('>>> Base: '))
	altu = int(input('>>> Altura: '))
	area = base * altu
	if base == altu:
		print('>>> A escolha foi um QUADRADO')
	elif base != altu:
		print('>>> A escolha foi um RETÂNGULO')
	print('')
	print('--- Área: {}cm²'.format(area))
print('-=' *30)
