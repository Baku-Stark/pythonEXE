Faça um Programa que leia três números e mostre-os em ordem decrescente. 

listanum = []
for n in xrange(1, 4):
	listanum.append(int(input('Digite o {}° número \nr: '.format(n))))
	print('')
listanum.sort(reverse=True)
print('Os números na ordem descrescente: {}'.format(listanum))
