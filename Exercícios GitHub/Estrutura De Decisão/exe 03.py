Faça um Programa que verifique se uma letra digitada é "F" ou "M". 
Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

sexo = str(input('Sexo do usuário [M/F]: ')).upper().strip()
print('')
if sexo == 'M':
 	print('\aSexo Masculino ') 
elif sexo == 'F':
	print('\aSexo Feminino')
else:
	print('\aSexo Inválido!')
