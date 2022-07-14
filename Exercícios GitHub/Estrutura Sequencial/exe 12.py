João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar 
o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes 
maior que o estabelecido pelo regulamento de pesca do estado de 
São Paulo (50 quilos) deve pagar uma multa de R$4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) 
e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do 
limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas. 

nome_peixe = str(input('Nome Do Peixe: '))
print('')
peso_peixe = float(input('Peso Do Peixo \nKG: '))
print('')
print('-=' *30)
print('TOTAL')
print('Peso Do {} vale: {:.1f} KG'.format(nome_peixe, peso_peixe))
print('')
if peso_peixe > 50.0:
	print('O peso excedeu!!!')
	total = peso_peixe - 50.0
	tot_multa = total * 4
	print('>>> Valor da multa: R${:.2f}'.format(tot_multa))
else:
	print('Peso Ideal!!!')
	print('>>> Não há multa.')
print('-=' *30)
