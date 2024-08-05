O FastAPI é um framework moderno para construção de APIs com Python baseado em tipagem e com excelente desempenho. Ele utiliza a biblioteca Pydantic para validação de dados e definição de schemas, e o SQLAlchemy ou Tortoise-ORM para a manipulação de modelos de banco de dados. Aqui está uma visão geral de como schemas e modelos funcionam no FastAPI:

### Schemas (Pydantic Models)

Os schemas no FastAPI são definidos usando Pydantic. Eles são usados para validação e serialização de dados de entrada e saída. 

#### Exemplo de Schema

```python
from pydantic import BaseModel
from typing import Optional

class ItemSchema(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    tax: Optional[float] = None

    class Config:
        orm_mode = True
```

- **`BaseModel`**: A classe base para todos os modelos Pydantic.
- **Atributos**: Os campos do modelo, onde você define os tipos de dados (e.g., `str`, `float`) e valores padrão.
- **`orm_mode`**: Permite a compatibilidade com ORM, facilitando a conversão entre modelos Pydantic e objetos ORM.

### Models (SQLAlchemy ou Tortoise-ORM)

Os modelos representam as tabelas do banco de dados. Aqui, mostrarei um exemplo usando SQLAlchemy.

#### Exemplo de Model

```python
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ItemModel(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    description = Column(String, index=True)
    price = Column(Float)
    tax = Column(Float)
```

- **`declarative_base`**: Uma função que retorna uma classe base a partir da qual todos os modelos ORM devem herdar.
- **`__tablename__`**: O nome da tabela no banco de dados.
- **Colunas**: Definem os atributos do modelo e seus tipos no banco de dados (e.g., `Integer`, `String`, `Float`).

### Integração no FastAPI

Vamos integrar os schemas e models no FastAPI.

#### Definindo Dependências

Primeiro, configure a conexão com o banco de dados:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)
```

#### Criando Rotas

```python
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/items/", response_model=ItemSchema)
def create_item(item: ItemSchema, db: Session = Depends(get_db)):
    db_item = ItemModel(**item.dict())
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=ItemSchema)
def read_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(ItemModel).filter(ItemModel.id == item_id).first()
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item
```

- **Dependências**: `get_db` é uma dependência que fornece uma sessão de banco de dados.
- **Rotas**: `create_item` e `read_item` são exemplos de rotas para criar e ler itens, respectivamente.
- **Serialização e Deserialização**: As rotas usam os schemas Pydantic para validar a entrada e serializar a saída.

### Explicação Resumida

1. **Schemas** (Pydantic Models): Usados para validação de dados de entrada e saída.
2. **Models** (SQLAlchemy Models): Representam tabelas e interagem com o banco de dados.
3. **Dependências**: Gerenciam a sessão do banco de dados no FastAPI.
4. **Rotas**: Definem os endpoints da API, utilizando schemas para validação e models para manipulação de dados.

Esse é um guia básico sobre como usar schemas e models no FastAPI. Se precisar de mais detalhes ou exemplos específicos, sinta-se à vontade para perguntar!
