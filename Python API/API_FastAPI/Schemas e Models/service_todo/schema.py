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