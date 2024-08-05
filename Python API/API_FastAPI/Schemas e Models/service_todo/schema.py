from typing import Annotated
from pydantic import BaseModel, Field

class TodoSchema(BaseModel):
    title : Annotated[str, Field(
        description="Titulo da tarefa",
        example="Futebol",
        max_length="100",
    )]
    description : Annotated[str, Field(
        description="Descrição da tarefa",
        example="Jogar bola no sábado",
        max_length="200"
    )]
    completed : bool = False

class TodoIn(TodoSchema):
    pass

class TodoUpdate(TodoSchema):
    title : Annotated[str, Field(
        description="Titulo da tarefa",
        example="Atualização de title",
        max_length="100",
    )]
    description : Annotated[str, Field(
        description="Descrição da tarefa",
        example="Atualização de descrição",
        max_length="200"
    )]

class TodoCompleted(BaseModel):
    completed : bool

    class config:
        orm_mode = True

class TodoItem(TodoSchema):
    id : int

    class config:
        orm_mode = True