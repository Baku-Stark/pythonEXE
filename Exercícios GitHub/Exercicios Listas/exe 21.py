'''
Faça um programa que carregue uma lista com os modelos de cinco carros 
(exemplo de modelos: FUSCA, GOL, VECTRA etc). 
Carregue uma outra lista com o consumo desses carros, isto é, quantos quilômetros 
cada um desses carros faz com um litro de combustível. Calcule e mostre:

    O modelo do carro mais econômico;

    Quantos litros de combustível cada um dos carros cadastrados consome para percorrer uma 
    distância de 1000 quilômetros e quanto isto custará, considerando um que a gasolina custe 
    R$ 2,25 o litro. Abaixo segue uma tela de exemplo. O disposição das informações deve 
    ser o mais próxima possível ao exemplo. Os dados são fictícios e podem mudar a cada 
    execução do programa. 

Comparativo de Consumo de Combustível

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
 1 - fusca           -    7.0 -  142.9 litros - R$ 321.43
 2 - gol             -   10.0 -  100.0 litros - R$ 225.00
 3 - uno             -   12.5 -   80.0 litros - R$ 180.00
 4 - vectra          -    9.0 -  111.1 litros - R$ 250.00
 5 - peugeout        -   14.5 -   69.0 litros - R$ 155.17
O menor consumo é do peugeout.
'''

# === DADOS ===
carros = []
litros = []
custo = []
km = []

# === FUNÇÃO DEF CLEAR ===
def clear():
	print('\n' *10)

print('\a 1 Litro = R$2,25')
print('\a 1000 / Litros')
print('')
for x in xrange(1, 6):
	nome = str(input('Registre o nome do {}° carro \nr: '.format(x))).capitalize()
	carros.append(nome)
	print('')
print('-' *40)
for n in xrange(0, len(carros)):
	litro = float(input('Consumo de um {} \nr: '.format(carros[n])))
	litros.append(litro)

	# Custo dos litros
	res_custo = litro * 2.25
	custo.append(res_custo)

	# Distancia que vai percorrer
	res_km = 1000 / litro
	km.append(res_km)
	print('')
print('-' *40)
clear()
print('-=' *30)
print('Resultado Final')
print('')
for c in range(0, len(carros)):
	print(('''
	Veículo {}
	Nome: {}
	Km por Litro: {:.2f}'''.format(c+1, carros[c], km[c])))
	print('')
for a in range(0, len(carros)):
	print('\a {} - {}    -    {:2.f}Km  -  {} Litros - R${:.2f}\n'.format(a+1, carros[a], km[a], litros[a], custo[a]))
print('')
print('')
print('\a O menor consumo é do {}'.format(carros[litros.index(min(litros))]))
print('-=' *30)
