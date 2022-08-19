'''
Tamanho de strings. Faça um programa que leia 2 strings e informe o conteúdo delas seguido 
do seu comprimento. Informe também se as duas strings possuem o mesmo comprimento e são 
iguais ou diferentes no conteúdo. 

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
'''

def tamanho(string1, string2):
	len_str1 = len(string1)
	len_str2 = len(string2)

	if len_str1 != len_str2:
		print('\a As duas strings possuem tamanhos diferentes.')
	else:
		print('\a As strings possuem o mesmo tamanho.')


# ===
string1 = str(input('Digite a primeira string \nr: '))
print('')
string2 = str(input('Digite a segunda string \nr: '))
print('')
print('-=' *30)
print('Resultados:')
print('')
print('A 1ª STRING possui: {} letra(s).'.format(len(string1)))
print('A 2ª STRING possui: {} letra(s).'.format(len(string2)))
print('')
tamanho(string1, string2)
print('-=' *30)
