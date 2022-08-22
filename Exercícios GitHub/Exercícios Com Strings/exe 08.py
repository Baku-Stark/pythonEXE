'''
Palíndromo. Um palíndromo é uma seqüência de caracteres cuja leitura é idêntica se 
feita da direita para esquerda ou vice−versa. Por exemplo: OSSO e OVO são palíndromos. 
Em textos mais complexos os espaços e pontuação são ignorados. A frase SUBI NO ONIBUS é o 
exemplo de uma frase palíndroma onde os espaços foram ignorados. Faça um programa que 
leia uma seqüência de caracteres, mostre−a e diga se é um palíndromo ou não. 
'''

frase = str(input('Digite uma frase para análise \nr: ')).strip().upper()
palidromo = frase[::-1]
print('')
if frase == palidromo:
	print('\a A frase é um palíndromo')
else:
	print('\a A frase não é um palíndromo')
