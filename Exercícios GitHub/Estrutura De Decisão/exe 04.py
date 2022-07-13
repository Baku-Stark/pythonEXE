Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

word = str(input('Digite uma letra \nr: ')).lower().strip()
print('')
if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
	print('É UMA VOGAL!')
else:
	print('É UMA CONSOANTE!')
