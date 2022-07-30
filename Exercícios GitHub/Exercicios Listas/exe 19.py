'''
Uma empresa de pesquisas precisa tabular os resultados da seguinte enquete feita a um 
grande quantidade de organizações:

"Qual o melhor Sistema Operacional para uso em servidores?"

As possíveis respostas são:

1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro

Você foi contratado para desenvolver um programa que leia o resultado da enquete e 
informe ao final o resultado da mesma. O programa deverá ler os valores até ser 
informado o valor 0, que encerra a entrada dos dados. Não deverão ser aceitos valores 
além dos válidos para o programa (0 a 5). Os valores referentes a cada uma das opções 
devem ser armazenados num vetor. Após os dados terem sido completamente informados, 
o programa deverá calcular a percentual de cada um dos concorrentes e informar o 
vencedor da enquete. O formato da saída foi dado pela empresa, e é o seguinte:

Sistema Operacional     Votos   %
-------------------     -----   ---
Windows Server           1500   17%
Unix                     3500   40%
Linux                    3000   34%
Netware                   500    5%
Mac OS                    150    2%
Outro                     150    2%
-------------------     -----
Total                    8800
'''
# === DADOS ===
opcoes = ["Windows Server", "Unix", "Linux", "Netware" "Mac OS", "Outros"]
sistemas = [0] * 6

print('''
1- Windows Server
2- Unix
3- Linux
4- Netware
5- Mac OS
6- Outro
''')
print('')
while True:
    while True:
        opcao = int(input('Escolha uma opção de Sistema Operacional \nr: '))
        print('')
        if opcao > 6 or opcao < 0:
            print('\033[32mOpção Inválida!\033[m')
            print('')
        
        else:
            break
    
    if opcao == 0:
        break
    sistemas[opcao - 1] = sistemas[opcao - 1] + 1
print('Sistema Operacional     Votos     Porcentagem(%)')
print('-' *60)
count = 0
melhor = 0
melhorSis = ''
perc = 0

for s in sistemas:
    print(f'{opcoes[count]}     {s}     {(s * 100) / sum(sistemas):.2f} %')

    if s > melhor:
        melhor = s
        melhorSis = opcoes[count]
        perc = (s * 100) / sum(sistemas)
    count += 1

print('-' *60)
print(f'Total: {sum(sistemas)}')
print(f'''O Sistema Operacional mais votado foi o {melhorSis},
com {melhor} votos, correspondendo a {perc:.2f} dos votos''')
