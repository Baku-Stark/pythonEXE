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

Você foi contratado para desenvolver um programa que leia o resultado da enquete e informe 
ao final o resultado da mesma. O programa deverá ler os valores até ser informado o valor 0, 
que encerra a entrada dos dados. Não deverão ser aceitos valores além dos válidos para o 
programa (0 a 6). Os valores referentes a cada uma das opções devem ser armazenados num 
vetor. Após os dados terem sido completamente informados, o programa deverá calcular a 
percentual de cada um dos concorrentes e informar o vencedor da enquete. O formato da saída 
foi dado pela empresa, e é o seguinte: 

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

O Sistema Operacional mais votado foi o Unix, com 3500 votos, correspondendo a 40% dos votos.
'''

# === DADOS ===
opcoes = ['Windows Server', 'Unix', 'Linux', 'Netware', 'Mac OS', 'Outro']
sistemas = [0] * 6

# === LIMPAR TELA ===
def clear():
	print('\n' *10)


# ---
print('Qual o melhor Sistema Operacional para uso em servidores?')
print('''
[ 1 ] - Windows Server
[ 2 ] - Unix
[ 3 ] - Linux
[ 4 ] - Netware
[ 5 ] - Mac OS
[ 6 ] - Outro
''')
print('')
while True:
	while True:
		opcao = int(input('Escolha a sua opção \nr: '))
		print('')

		if opcao < 0 or opcao > 6:
			print('\a Opção Inválida! Tente novamente')
			print('-' *25)
			print('')

		else:
			break

	if opcao == 0:
		break
	sistemas[opcao - 1] = sistemas[opcao - 1] + 1

print('Sistema Operacional   Votos   Porcentagem(%)')
print('-' *45)
cont = 0
melhor = 0
perc = 0
melhorSis = ''
for s in sistemas:
	print('{:>15}{:>12}   {:.2f}%'.ljust(40).format(opcoes[cont], s, (s * 100) / sum(sistemas)))
	if s > melhor:
		melhor = s
		melhorSis = opcoes[cont]
		perc = (s * 100) / sum(sistemas)
	cont += 1
print('-' *45)
clear()
print('\a Total: {}'.format(sum(sistemas)))
print('\a O Sistema Operacional mais votador: {}'.format(melhorSis))
print('\a Porcentagem de votos: {}'.format(perc))
print('\a Votos: {}'.format(melhor))
