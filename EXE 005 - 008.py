>>> - Exercício Python
-> https://www.youtube.com/watch?v=664e0G_S9nU&list=PLHz_AreHm4dlKP6QQCekuIPky1CiwmdI6&index=13

--------------------------------------------------------

# Desafio 005
Faça um programa que leia um número inteiro e mostre na tela seu sucessor e seu antecessor

n = int(input('Digite um número:'))
ant = n - 1
suc = n + 1

print('O antecessor é: {}'.format(ant))
print('O sucessor é: {}'.format(suc))
- print('O antecessor é {} e o sucessor é {}'.format((n-1), (n+1)))
--------------------------------------------------------

#Desafio 006
Crie um algoritmo que leia um número e mostre seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número:'))
db = n *2
tr = n *3
rq = n **(1/2)
print('Dobro {}, Triplo {} e Raiz Quadrada {}'.format(db, tr, rq))
--------------------------------------------------------

#Desafio 007
Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a média

nb1 = float(input('Nota do 1° Bimestre: '))
nb2 = float(input('Nota do 2° Bimestre: '))
md = nb1 + nb2
print('A média é {}'.format(md))
nbm = float(input('Digite a média:'))
mdf = nbm /2
print('A Média Final é:'.format(mdf))
--------------------------------------------------------

#Desafio 008
Escreva um programa que um valor em metros e o exiba convertido em 
centímetros e milímetros.

m = int(input('Valor em Metros:'))
cm = m *100
print('O resultado é: {}'.format(cm))
ml = m *1000
print('Oresultado é: {}'.format(ml))
--------------------------------------------------------