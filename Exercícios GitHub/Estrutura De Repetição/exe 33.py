'''
Em uma competição de ginástica, cada atleta recebe votos de sete jurados. A melhor e 
a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. 
Você deve fazer um programa que receba o nome do ginasta e as notas dos sete jurados 
alcançadas pelo atleta em sua apresentação e depois informe a sua média, conforme a 
descrição acima informada (retirar o melhor e o pior salto e depois calcular a 
média com as notas restantes). As notas não são informados ordenadas. 
Um exemplo de saída do programa deve ser conforme o exemplo abaixo: 

Atleta: Aparecido Parente
Nota: 9.9
Nota: 7.5
Nota: 9.5
Nota: 8.5
Nota: 9.0
Nota: 8.5
Nota: 9.7

Resultado final:
Atleta: Aparecido Parente
Melhor nota: 9.9
Pior nota: 7.5
Média: 9,04
'''

linha = '-' *41
titulo = 'CAMPEONATO DE GINÁSTICA BRASIL!'

notas = []
count_nota = 0

def clear():
	print('\n' *10)

print(linha)
print(titulo.center(41))
print(linha)
print('')
nome = str(input('Nome do(a) atleta \nr: ')).capitalize()
print('')
for n in xrange(1, 8):
	num = float(input('Nota do {}° jurado \nr: '.format(n)))
	print('')
	count_nota += num
	notas.append(num)
clear()
print(linha)
print('Atleta: {}'.format(nome))
print('')
for x in xrange(0, 7):
	print('\a Nota: {:.1f}'.format(notas[nx]))
print('')
print('>>> Resultado Final:')
print('Atleta: {}'.format(nome))
notas.sort()
print('\a Melhor Nota: {:.1f}'.format(notas[-1]))
print('\a Pior Nota:   {:.1f}'.format(notas[0]))
print('\a Média:       {:.1f}'.format(count_nota/7))
print(linha)
