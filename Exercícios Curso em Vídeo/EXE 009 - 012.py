>>>  - Exercício Python
https://www.cursoemvideo.com/curso/python-3-mundo-1/aulas/tratando-dados-e-fazendo-contas/modulos/exercicio-9-tabuada/
--------------------------------------------------------

# Exercício 9
Tabuada

nmulti = int(input('Escolha um número:'))
aux = 0
print('-' *20)
print('Tabuada de: {}'.format(nmulti))
print('-' *20)
print('')
while(aux <= 10):
	print('{} X {} = {}'.format(aux, nmulti, (aux * nmulti)))
	aux = aux + 1
print('')
print('-' *20)

--------------------------------------------------------

Conversão
UR$1,00 = R$4,70
1 Real/BRL (790) = 0,2126528 Dólar dos Estados Unidos/USD (220)
1 Dólar dos Estados Unidos/USD (220) = 4,7025001 Real/BRL (790) 

real = float(input('Valor em REAL:'))
dolar = real /4.70
print('A conversão real -> dólar é: UR${}'.format(dolar))

--------------------------------------------------------

Pintando A Parede (QUADRADO e RETANGULO) A = b x a

larg = int(input('Largura da parede:'))
alt = int(input('Altura da parede:'))
area = larg * alt
print('A área da parede é: {}m²'.format(area))
tinta = area /2
print('Você irá precisar de {}L de tinta'.format(tinta))

--------------------------------------------------------

Calcular desconto

R$10 ----- 100%
x    ----- 5%

pewant = float(input('Registre o preço: R$'))
pewnew = pewant - (pewant * 5 / 100)
print('O novo preço é: R${}'.format(pewnew))

--------------------------------------------------------
