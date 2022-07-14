Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, usando a seguinte fórmula: (72.7 * altura) - 58 

altura = float(input('Registre sua altura: '))
peso = (72.7 * altura) - 58 
print('')
print('>>> Seu peso é de: {}kg'.format(peso))

Tendo como dado de entrada a altura (altura) de uma pessoa, construa um algoritmo 
que calcule seu peso ideal, utilizando as seguintes fórmulas:

    Para homens: (72.7 * altura) - 58
    Para mulheres: (62.1 * altura) - 44.7 

altura = float(input('Registre sua altura: '))
sexo = str(input('Sexo [M/F]: ')).upper().strip()
print('')
print('-=' *30)
if sexo == 'M':
	print('--- MASCULINO ---')
	peso = (72.7 * altura) - 58
	print('>>> Seu peso é de: {}kg'.format(peso))
elif sexo == 'F':
	print('--- FEMININO ---')
	peso = (62.1 * altura) - 44.7
	print('>>> Seu peso é de: {}kg'.format(peso))
print('-=' *30)
