'''
Faça um programa que leia um número indeterminado de valores, correspondentes a notas, 
encerrando a entrada de dados quando for informado um valor igual a -1 
(que não deve ser armazenado). Após esta entrada de dados, faça:

    Mostre a quantidade de valores que foram lidos; [x]
    Exiba todos os valores na ordem em que foram informados, um ao lado do outro; [x]
    Exiba todos os valores na ordem inversa à que foram informados, um abaixo do outro; [x]
    Calcule e mostre a soma dos valores; [x]
    Calcule e mostre a média dos valores; [x]
    Calcule e mostre a quantidade de valores acima da média calculada; 
    Calcule e mostre a quantidade de valores abaixo de sete; [x]
    Encerre o programa com uma mensagem; [x]
'''

# ----- DADOS -----
up = []
sub = []
numeros = []
count_num = 0

# ----- FUNÇÃO DEF -----
def clear():
	print('\n' *15)

while True:
	num = int(input('Digite um número \nr: '))
	print('')

	if num >= 0:
		count_num += 1
		numeros.append(num)

	if num < 7:
		sub.append(num)

	if num < 0:
		print('\a Registro Encerrado!')
		break

clear()
print('-=' *30)
print('Resultado Do Registro')
print('')
print('\a Números (na ordem de registro):         {}'.format(numeros))
numeros.sort(reverse=True)
print('\a Números (na ordem INVERTA de registro): {}'.format(numeros))
soma = sum(numeros)
print('\a Todos os números da lista somados:      {}'.format(soma))
media = sum(numeros) / len(numeros)
print('\a A média dos valores registados:         {}'.format(media))

for i in range(0, len(numeros)):
	if numeros[i] > media:
		up.append(numeros[i])
sub.sort()
print('\a Valores acima da média:                 {}'.format(up))
print('\a Números registados menor que 7:         {}'.format(sub[1:]))
print('-=' *30)
