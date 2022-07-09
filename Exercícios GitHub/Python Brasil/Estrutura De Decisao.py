Faça um Programa que peça dois números e imprima o maior deles.

num1 = float(input('Digite o 1° número: '))
num2 = float(input('Digite o 2° número: '))
print('')
if num1 > num2:
	print('{} é maior que {}'.format(num1, num2))
else:
	print('{} é maior que {}'.format(num2, num1))
  
_________________________________________________________________________
Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo. 

num = int(input('Digite um valor: '))
print('')
if (num > 0):
	print('>>> O número é positivo.')
else:
	print('>>> O número é negativo.')

_________________________________________________________________________
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

_________________________________________________________________________
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.

tot_vogal = 0

word = str(input('Digite uma letra \nr: ')).lower().strip()
print('')
if word == 'a' or word == 'e' or word == 'i' or word == 'o' or word == 'u':
	print('É UMA VOGAL!')
else:
	print('É UMA CONSOANTE!')

_________________________________________________________________________
Faça um programa para a leitura de duas notas parciais de um aluno. 
O programa deve calcular a média alcançada por aluno e apresentar:

    A mensagem "Aprovado", se a média alcançada for maior ou igual a sete;
    A mensagem "Reprovado", se a média for menor do que sete;
    A mensagem "Aprovado com Distinção", se a média for igual a dez.

aluno = str(input('Nome Do(a) aluno(a) \nr: '))
print('')
bim_1 = float(input('Nota do 1° Bimestre: '))
bim_2 = float(input('Nota do 2° Bimestre: '))
media = bim_1 + bim_2
print('')
print('[RESULTADO DO ALUNO]')
if media >= 7 and media <= 9:
	print('\a {} está APROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media < 7:
	print('\a {} está REPROVADO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
elif media == 10:
	print('\a {} está APROVADO COM DISTINÇÃO!'.format(aluno))
	print('>>> Média: {:.1f}'.format(media))
	
_________________________________________________________________________
Faça um Programa que leia três números e mostre o maior e o menor deles. 

num1 = float(input('Digite o 1° número: '))
print('')
num2 = float(input('Digite o 2° número: '))
print('')
num3 = float(input('Digite o 3° número: '))
print('')
print('-=' *30)
### MOSTRAR O MAIOR
if num1 > num2 and num1 > num3:
	print('\a O número {:.0f} é o maior'.format(num1))
elif num2 > num1 and num2 > num3:
	print('\a O número {:.0f} é o maior'.format(num2))
elif num3 > num1 and num3 > num2:
	print('\a O número {:.0f} é o maior'.format(num3))
print('')
### MOSTRAR O MENOR
if num1 < num2 and num1 < num3:
	print('\a O número {:.0f} é o menor'.format(num1))
elif num2 < num1 and num2 < num3:
	print('\a O número {:.0f} é o menor'.format(num2))
elif num3 < num1 and num3 < num2:
	print('\a O número {:.0f} é o menor'.format(num3))
print('-=' *30)

_________________________________________________________________________
