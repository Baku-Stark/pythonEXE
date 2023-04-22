# API - Lugar para disponibilizar recursos
#   1. Objetivo - Criar uma API de disponibilidade de CRUD
#   2. Objetivo - URL base - localhost

#   3. Objetivo - Endpoints
#                   - localhost/livros(GET)
#                   - localhost/livros/id (GET)
#                   - localhost/livros/id (PUT)
#                   - localhost/livros/id (DELETE)

#   4. Objetivo - Quais recursos [LIVROS]

# pip install flask
from flask import Flask, jsonify, request

app = Flask(__name__)

livros = [
    {
        'id': 1,
        'title': 'Harry Potter E O Cálice De Fogo',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 2,
        'title': 'Harry Potter E As Relíquias Da Morte',
        'autor': 'J. K. Rowling'
    },
    {
        'id': 3,
        'title': 'Hogwarts Legacy',
        'autor': 'J. K. Rowling'
    },
]

# [CRUD] -> LER TODOS OS DADOS DA API
# http://localhost:5000/livros
@app.route('/livros', methods=['GET'])
def read_books():
    return jsonify(livros)

# [CRUD] -> LER POR ID
@app.route('/livros/<int:id>', methods=['GET'])
def read_books_id(id:int):
    for livro in livros:
        if livro.get('id') == id:
            return jsonify(livro)
            
# [CRUD] -> CRIAR UM LIVRO
@app.route('/livros', methods=['POST'])
def create_book():
    novo_livro = request.get_json()
    livros.append(novo_livro)

    return jsonify(livros)
        
# [CRUD] -> ATUALIZAR LIVRO
@app.route('/livros/<int:id>', methods=['PUT'])
def update_books_id(id:int):
    livro_updated = request.get_json()

    for ind, livro in enumerate(livros):
        if livro.get('id') == id:
            livros[ind].update(livro_updated)
            return jsonify(livros[ind])
        
# [CRUD] -> DELETAR LIVRO
@app.route('/livros/<int:id>', methods=['DELETE'])
def delete_books_id(id:int):
    for ind, livro in enumerate(livros):
        if livro.get('id') == id:
            del livros[ind]
    
    return jsonify(livros)

app.run(port=5000, host='localhost', debug=True)