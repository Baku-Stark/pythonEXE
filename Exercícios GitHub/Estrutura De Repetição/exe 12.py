'''
A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o n−ésimo termo. 
'''

num = int(input('Digite o termo \nr: '))
ultimo = 1
penultimo = 1
print('')

if (num == 1) or (num == 2):
	print('\a 1')
else:
	count = 3
	while count <= num:
		termo = ultimo + penultimo
		penultimo = ultimo
		ultimo = termo
		count += 1
	print('\a O termo {} vale: {}'.format(num, termo))
