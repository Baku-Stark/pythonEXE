valores_celulares = [850, 2230, 1500, 3500, 5000]

'''
'r'  -> Usado somente para ler algo;
'w'  -> Usado somente para escrever algo;
'r+' -> Usado para LER e ESCREVER algo;
'a'  -> Usado para acrescentar algo.
'''


with open('valores_celulares.txt', 'r') as arquivo:
    for valor in valores_celulares:
        print(valor)

with open('valores_celulares.txt', 'w') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')

with open('valores_celulares.txt', 'r+') as arquivo:
    for valor in valores_celulares:
        print(valor)
    arquivo.write('9000s')

with open('valores_celulares.txt', 'a') as arquivo:
    for valor in valores_celulares:
        arquivo.write(str(valor) + '\n')