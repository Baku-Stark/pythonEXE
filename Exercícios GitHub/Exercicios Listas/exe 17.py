'''
Em uma competição de salto em distância cada atleta tem direito a cinco saltos. O resultado do atleta será determinado 
pela média dos cinco valores restantes. Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas 
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos. O programa deve ser encerrado quando 
não for informado o nome do atleta. A saída do programa deve ser conforme o exemplo abaixo:

Atleta: Rodrigo Curvêllo
 
Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
'''

saltos = []

def clear():
    print('\n' *10)


# ---
while True:
    nome = str(input('Nome Do Atleta \nr: ')).capitalize().strip()
    print('')
    if nome == "":
        print('Encerrando o programa (motivo: NOME não foi informado!)')
        break
    else:
        for s in range(1, 6):
            saltos.append(float(input(f'{s}° Salto \nr: ')))
            print('')
        clear()
        print('-=' *30)
        print(f'Saltos Do Atleta {nome}')
        print('')
        print((f'''
        Primeiro Salto: {saltos[0]:.1f}m
        Segundo Salto:  {saltos[1]:.1f}m
        Terceiro Salto: {saltos[2]:.1f}m
        Quarto Salto:   {saltos[3]:.1f}m
        Quinto Salto:   {saltos[4]:.1f}m
        '''))
        media = sum(saltos) / len(saltos)
        print('')
        print('=== Resultado Final ===')
        print(f'Atleta: {nome}')
        print(f'Saltos: {saltos}')
        print('')
        saltos.sort()
        print(f'Melhor salto:    {saltos[4]:.1f}m')
        print(f'Pior salto:      {saltos[0]:.1f}m')
        print(f'Média dos saltos: {media:.1f}m')
        print('-=' *30)
        break