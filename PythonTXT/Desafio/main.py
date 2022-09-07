inscritos = [
    'jhonatan',
    'Patricio Silva',
    'Kid Boy 3000',
    'Ricardo Piedade',
    'Victor Ravagnani',
    'Eder Macario',
    'Luiz Guilherme',
    'Lucimar Chiamulera',	
    'vinicius queiroz',
    'Jonatas Alves',
    'Giuliano Richards',
    'Hugo Marques',
    'Marcelo M.',
    'Luiz Alberto Araujo',
    'Niwber Cavalcante	',	
    'Andre Neves',
    'Borges	Borges',
    'Alex Marciel',
    'Davi Adelino',
    '90Tão Games',
    'jose valderi',
    'Márcio Lopes',
    'Mikael',
    'Tálisson Neiva'
]

# Faça todos os desafios a seguir e depois clique a "Share", copie o código e mande no comentário do vídeo, para que eu veja que você conseguiu (ou não) fazer! Eu confio em VOCÊ!


# Desafio 1 - Exiba todos os nomes dos inscritos que estão no arquivo inscritos.txt no console
with open('inscritos.txt', 'w') as arquivo:
    for nomes in inscritos:
        arquivo.write(str(nomes) + '\n')

with open('inscritos.txt', 'r') as arquivo:
    for nomes in inscritos:
        print(nomes)

# Desafio 2 - Adicione o seu nome na lista de inscritos e depois todos os nomes que estão no arquivo inscritos.txt no console
with open('inscritos.txt', 'a') as arquivo:
    arquivo.write('Wallace De Freitas')

# Desafio 3 - Com o seu nome já na lista de inscritos, exiba o nome de cada pessoas que está inscrito na lista + o número que ele representa na lista em ordem crescente (ex: 1 jhonatan , 2 Patricio Silva, 3 Kid Boy 3000)
with open('inscritos.txt', 'r') as arquivo:
    for n, nomes in enumerate(inscritos):
        print(f'{n + 1}  {nomes}')