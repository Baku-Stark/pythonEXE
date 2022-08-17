'''
Quadrado mágico. Um quadrado mágico é aquele dividido em linhas e colunas, 
com um número em cada posição e no qual a soma das linhas, colunas e diagonais é a mesma. 
Por exemplo, veja um quadrado mágico de lado 3, com números de 1 a 9: 

8 3 4
1 5 9
6 7 2

Elabore uma função que identifica e mostra na tela todos os quadrados mágicos com as 
características acima. Dica: produza todas as combinações possíveis e verifique a soma 
quando completar cada quadrado. Usar um vetor de 1 a 9 parece ser mais simples que usar 
uma matriz 3×3.
'''

n=int(input("Número \nr: "))
print('')
A = []
for i in range(n):
    l = []
    for j in range(n):
        l.append(int(input('Digite o valor de [' + str(i) + ',' + str(j) + ']:')))
    A.append(l)

#diagonal principal
magico=0
for i in range(n):
    magico = magico + A[i][i]
    
#diagonal secundaria
soma=0
for i in range(n):
    soma = soma + A[i][n-1-i]
if (soma != magico):
    print("Não é mágico")

#linhas
for i in range(n):
    soma=0
    for j in range(n):
        soma=soma+A[i][j]
    if (soma != magico):
        print("Não é mágico")
        
#colunas
for j in range(n):
    soma=0
    for i in range(n):
        soma=soma+A[i][j]
    if (soma != magico):
        print("Não é mágico")
        
print("É magico")
