'''
Faça um programa que simule um lançamento de dados. Lance o dado 100 vezes e armazene os 
resultados em um vetor . Depois, mostre quantas vezes cada valor foi conseguido. 
Dica: use um vetor de contadores(1-6) e uma função para gerar numeros aleatórios, 
simulando os lançamentos dos dados. 
'''

# === DADOS ===
lancamentos = []


from random import randint


for x in xrange(0, 100):
	random = (randint(1, 6))
	lancamentos.append(random)

print('-=' *30)
print('Resultado')
print('')
print('\a O número 1 apareceu {} vezes.'.format(lancamentos.count(1)))
print('\a O número 2 apareceu {} vezes.'.format(lancamentos.count(2)))
print('\a O número 3 apareceu {} vezes.'.format(lancamentos.count(3)))
print('\a O número 4 apareceu {} vezes.'.format(lancamentos.count(4)))
print('\a O número 5 apareceu {} vezes.'.format(lancamentos.count(5)))
print('\a O número 6 apareceu {} vezes.'.format(lancamentos.count(6)))
print('-='*30)
