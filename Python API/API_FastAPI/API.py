import os

try:
    # link: https://fastapi.tiangolo.com/
    # pip install fastapi
    from fastapi import FastAPI

except ModuleNotFoundError:
    os.system('pip install fastapi')
    os.system('pip install uvicorn')

finally:
    print(
        '=====Todos as libs estão instaladas com sucesso!====='
    )

    # UVICORN -> LINK: https://pypi.org/project/uvicorn/

    # --- pegando o nome do arquivo atual
    # current_file = str(os.path.basename(__file__))
    # --- uvicorn example:app
    # os.system(f'uvicorn {current_file[0:3]}:app --reload')

    app = FastAPI()

    vendas = {
        1: {
            "item": "lata",
            "preco_unitario": 4,
            "quantidade": 5
        },
        2: {
            "item": "garrafa 2L",
            "preco_unitario": 15,
            "quantidade": 5
        },
        3: {
            "item": "garrafa 750ml",
            "preco_unitario": 10,
            "quantidade": 5
        },
        4: {
            "item": "lata mini",
            "preco_unitario": 2,
            "quantidade": 5
        }
    }

    @app.get("/")
    def home():
        """
            Home Page.
        """
    
        return {
            "API_SUCCESS": "HELLO WORLD!",
            "VENDAS": len(vendas)
        }

    @app.get("/vendas/{id}")
    def id_venda(id: int):
        """
            Consultar uma venda específica.
        """

        if id in vendas:
            return {
                "API_SUCCESS": "HELLO WORLD!",
                "VENDAS": vendas[id]
            }

        else:
            return {
                "ERROR 404": "NOT FOUND!!"
            }