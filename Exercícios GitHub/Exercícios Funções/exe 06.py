'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. 
Por exemplo, o programa deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
Deve haver pelo menos duas funções: uma para fazer a conversão e uma para a saída. 
Registre a informação A.M./P.M. como um valor ‘A’ para A.M. e ‘P’ para P.M. Assim, 
a função para efetuar as conversões terá um parâmetro formal para registrar se é 
A.M. ou P.M. Inclua um loop que permita que o usuário repita esse cálculo para novos 
valores de entrada todas as vezes que desejar. 
'''

def convertaHora(hora, minuto):
	if hora > 23 or minuto > 59:
		print('[ERRO] Valor de horário inválido!')

	elif hora >= 0 and hora <= 12:
		print('{}:{} A.M.'.format(hora, minuto))

	elif hora > 12 and hora <= 23:
		hora -= 12
		print('{}:{} P.M.'.format(hora, minuto))


# ===
print('Conversão De Horário')
print('''
[A.M.] -> Antes do meio-dia
[P.M.] -> Depois do meio-dia''')
print('\a Digite "999" para cancelar.')
print('')
while True:
	h = int(input('Digite as horas \nr: '))
	print('')
	m = int(input('Digite os minutos \nr: '))
	print('')

	if h == 999 or m == 999:
		print('Conversão Encerrada!')
		break

	convertaHora(h, m)
	print('-=' *15)
	print('')
