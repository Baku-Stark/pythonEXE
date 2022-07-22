'''
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um programa 
que leia as um conjunto indeterminado de temperaturas, e informe ao final a menor e a 
maior temperaturas informadas, bem como a média das temperaturas. 
'''

temperaturas = []
linha = '-' * 40
aux = 1

print(linha)
print('{}'.format('Departamento Estadual de Meteorologia'.center(40)))
print(linha)
print('')
print('{}'.format('[ 0 ] Para o programa!'))
while True:
	registro = float(input('Informe a {}ª temperatura \nr: '.format(aux)))
	temperaturas.append(registro)
	print
	aux += 1
	if (registro == 0):
		aux -= 1
		break
print('')
print('-=' *30)
print('RESULTADOS:')
print('')
temperaturas.sort() # Ordem crescente
del(temperaturas[0])
print('Foram registradas: {} tipos de temperaturas'.format(aux-1))
print('\a A menor temperatura catalogada: {}°C'.format(temperaturas[0]))
print('\a A maior temperatura catalogada: {}°C'.format(temperaturas[-1]))
print('-=' *30)
