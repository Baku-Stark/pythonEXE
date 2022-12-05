 >>>  - Exercício Python
 https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/usando-modulos-do-python/modulos/exercicio-17-catetos-e-hipotenusa/
 --------------------------------------------------------

 Exercício Python 17: Faça um programa que leia o comprimento do cateto oposto 
 e do cateto adjacente de um triângulo retângulo. Calcule e mostre o comprimento 
 da hipotenusa.

 Teorema da Pitágoras: <a² = b² + c³ -> **2> 
 (https://brasilescola.uol.com.br/matematica/teorema-pitagoras.htm)

 catetoop = int(input('Informe o cateto oposto:'))
 catetoadj = int(input('Informe o cateto adjacente:'))
 hipotenusa = catetoop **2 + catetoadj **2
 print('A hipotenusa é {}'.format(hipotenusa))

 catetoop = float(input('Informe o cateto oposto:'))
 catetoadj = float(input('Informe o cateto adjacente:'))
 hipotenusa = catetoop **2 + catetoadj **2
 print('A hipotenusa é {:.2f}'.format(hipotenusa))

 --------------------------------------------------------

 Exercício Python 18: Faça um programa que leia um ângulo qualquer e mostre na 
 tela o valor do seno, cosseno e tangente desse ângulo. 

 >Seno (Sen alfa )

 sen a = cateto oposto
 		 ---------------
         hipotenusa 
#Seno
catetoop = float(input('Informe o Cateto Oposto:'))
hipo = float(input('Informe a hipotenusa:'))
sen = catetoop / hipo
print('O \033[1mSeno[m é {:.2f}'.format(sen))

> Cosseno (Cos alfa)

cos a = cateto adjacente
	    ---------------
		hipotenusa
#Cosseno
catetoadj = float(input('Informe o Cateto Adjacente:'))
hipo = float(input('Informe a Hipotenusa:'))
cos = catetoadj / hipo
print('O \033[1mCosseno[m é {:.2f}'.format(cos))

> Tangente (Tg alfa)
tg a = cateto oposto
	    ---------------
		cateto adjacente
#Tangente
catetoop = float(input('Informe o Cateto Oposto:'))
catetoadj = float(input('Informe o Cateto Adjacente:'))
tg = catetoop / catetoadj
print('A \033[1mTangente[m é {:.2f}'.format(tg))

import math
angulo = float(input(('Digite o ângulo:')))
seno = math.sin(math.radians(angulo))
print('O ângulo de {}° é: {:.2f} - Seno'.format(angulo, seno))
cos = math.cos(math.radians(angulo))
print('O ângulo de {}° é: {:.2f} - Cosseno'.format(angulo, cos))
tan = math.tan(math.radians(angulo))
print('O ângulo de {}° é: {:.2f} - Tangente'.format(angulo, tan))

--------------------------------------------------------

Exercício Python 19: Um professor quer sortear um dos seus quatro alunos para 
apagar o quadro. Faça um programa que ajude ele, lendo o nome dos alunos e 
escrevendo na tela o nome do escolhido.

from random import choice
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quarto Aluno:'))
lista = [n1, n2, n3, n4]
escolhido = choice(lista)
print('O aluno escolhido foi o {}'.format(escolhido))

--------------------------------------------------------

Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de 
apresentação de trabalhos dos alunos. Faça um programa que leia o nome dos 
quatro alunos e mostre a ordem sorteada.

from random import shuffle
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quarto Aluno:'))
lista = [n1, n2, n3, n4]
escolhido = shuffle(lista)
print('')
print('-' *20)
print('A ordem é:')
print(lista)
print('-' *20)