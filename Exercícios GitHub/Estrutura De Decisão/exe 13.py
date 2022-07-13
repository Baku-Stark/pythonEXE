Faça um programa que lê as duas notas parciais obtidas por um aluno numa 
disciplina ao longo de um semestre, e calcule a sua média. 
A atribuição de conceitos obedece à tabela abaixo: 

Média de Aproveitamento  Conceito
  Entre 9.0 e 10.0        A
  Entre 7.5 e 9.0         B
  Entre 6.0 e 7.5         C
  Entre 4.0 e 6.0         D
  Entre 4.0 e zero        E

O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e a 
mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se o conceito for 
D ou E. 

nota_1 = float(input('Nota Do 1° Bimestre \nr: '))
print('')
nota_2 = float(input('Nota Do 2° Bimestre \nr: '))
media = nota_1 + nota_2
print('')
print('-=' *30)
print('Resultado Do Aluno:')
print('')
print('Média de Aproveitamento: {:.1f}'.format(media))
# Reprovado
if media == 0 and media < 4.0:
	print('\a Conceito Da Média: E')
	print('----- REPROVADO')

elif media >= 4.0 and media < 6.0:
	print('\a Conceito Da Média: D')
	print('----- REPROVADO')

# Aprovado
elif media >= 6.0 and media < 7.5:
	print('\a Conceito Da Média: C')
	print('----- APROVADO')

elif media >= 7.5 and media < 9.0:
	print('\a Conceito Da Média: B')
	print('----- APROVADO')

elif media >= 9.0 and media <= 10.0:
	print('\a Conceito Da Média: A')
	print('----- APROVADO')
print('-=' *30)
