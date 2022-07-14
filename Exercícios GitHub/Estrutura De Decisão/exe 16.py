Faça um Programa que peça um número correspondente a um determinado ano e em 
seguida informe se este ano é ou não bissexto. 

ano = int(input('Escolha um ano: '))
print('')
if ano % 4 == 0:
	print('\a O ano {} é BISSEXTO.'.format(ano))
else:
	print('\a O ano {} NÃO é BISSEXTO.'.format(ano))
