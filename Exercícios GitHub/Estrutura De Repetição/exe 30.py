'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. 
No final da série de saltos de cada atleta, o melhor e o pior resultados são eliminados. 
O seu resultado fica sendo a média dos três valores restantes. Você deve fazer um 
programa que receba o nome e as cinco distâncias alcançadas pelo atleta em seus saltos e 
depois informe a média dos saltos conforme a descrição acima informada 
(retirar o melhor e o pior salto e depois calcular a média). 
Faça uso de uma lista para armazenar os saltos. Os saltos são informados na ordem da 
execução, portanto não são ordenados. O programa deve ser encerrado quando não for 
informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Melhor salto:  6.5 m
Pior salto: 5.3 m
Média dos demais saltos: 5.9 m

Resultado final:
Rodrigo Curvêllo: 5.9 m 
'''

metros = []
soma = 0
count_salto = 0 

def clear():
	print('\n' * 5)

nome = str(input('Nome do atleta \nr: ')).capitalize()
print('')

for jump in range(1, 6):
	salto = float(input('Distância do {}° salto \nr: '.format(jump)))
	soma += salto
	count_salto += 1
	metros.append(salto)
	print('')
clear()
print('-=' * 30)
print('RESULTADOS:')
print('')
print('Atleta: {}'.format(nome))
print('')
print('Primeiro Salto: {:.1f}m'.format(metros[0]))
print('Segundo Salto:  {:.1f}m'.format(metros[1]))
print('Terceiro Salto: {:.1f}m'.format(metros[2]))
print('Quarto Salto:   {:.1f}m'.format(metros[3]))
print('Quinto Salto:   {:.1f}m'.format(metros[4]))
print('')
metros.sort() # Ordem crescente
print('Melhor salto: {:.1f}m'.format(metros[-1]))
print('Pior salto:   {:.1f}m'.format(metros[0]))
print('Média dos demais saltos: {:.1f}m'.format(soma/5))
print('')
print('{}: {:.1f}m'.format(nome, soma/5))
print('-=' * 30)
