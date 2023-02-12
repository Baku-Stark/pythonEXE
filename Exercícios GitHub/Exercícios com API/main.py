# ACESSANDO A API
# SITE : https://docs.awesomeapi.com.br/api-de-moedas
# LINK DE REQUISIÇÃO : https://economia.awesomeapi.com.br/json/last/:moedas

import json

# IMPORT [pip install requests]
import requests

cotacoes = requests.get('https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL')
if cotacoes.status_code == 200:
    # Códigos de status de respostas HTTP
        # Respostas de informação (100-199),
        # Respostas de sucesso (200-299),
        # Redirecionamentos (300-399)
        # Erros do cliente (400-499)
        # Erros do servidor (500-599).

    print('API acessada com sucesso!')
    cotacoes = cotacoes.json()
    print(cotacoes)

    # COTAÇÕES DO DÓLAR
    # cotacoes['USDBRL']
    print(cotacoes['USDBRL'])

    # COTAÇÕES DO EURO
    # cotacoes['EURBRL']
    print(cotacoes['EURBRL'])

    # COTAÇÕES DO BITCOIN BRASILEIRO
    # cotacoes['BTCBRL']
    print(cotacoes['BTCBRL'])

else:
    print('Algo está errado... Verifique o link da API.')
