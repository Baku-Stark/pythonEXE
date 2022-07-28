'''
Faça um programa que receba a temperatura média de cada mês do ano e armazene-as em uma 
lista. Após isto, calcule a média anual das temperaturas e mostre todas as temperaturas 
acima da média anual, e em que mês elas ocorreram (mostrar o mês por extenso: 
-1 – Janeiro, 2 – Fevereiro, . . . ). 
'''

meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
	"Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

media_temp = []

def clear():
	print('\n' *10)

for c in xrange(1, 13):
	media_temp.append(float(input('\a Temperatura média do {}° mês \nr: '.format(c))))
	print('')
clear()
print('-=' *30)
print('Resultado Das Pesquisas')
print('')
print('Mês {:>8} Temperatura Média'.format(''))
for x in xrange(0, len(media_temp)):
	print('{} - {:>4}°C'.format(meses[x], media_temp[x]))
print('-=' *30)
