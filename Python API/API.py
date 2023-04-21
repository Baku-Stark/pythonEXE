# pip install requests
import requests
import json

pkmn_number = 151

def Poke_API():
    for pkmn in range(1, pkmn_number+1):
        # [timeout] ===> Opcional. Um número, ou uma tupla, indicando quantos segundos esperar para o cliente fazer uma conexão e/ou enviar uma resposta.
        # Padrão Nenhum, o que significa que a solicitação continuará até que a conexão seja encerrada
        poke_api = requests.get(f'https://pokeapi.co/api/v2/pokemon/{pkmn}', timeout=2.50)

        pokemon = poke_api.json()

        print(pokemon['forms'][0]['name'])

if __name__ == '__main__':
    Poke_API()