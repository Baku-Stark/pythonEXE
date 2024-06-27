from fastapi import APIRouter, Body, HTTPException, status
router = APIRouter()

from service_todo.schema import TodoIn
from service_sql import create_todo

@router.post("/", summary="Criar uma nova tarefa", status_code=status.HTTP_201_CREATED)
async def post(todo_item : TodoIn = Body(...)):
    try:
        #print(todo_item.model_dump().values())
        
        todo = list(value for value in todo_item.model_dump().values())
        #print(todo)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error
    
    finally:
        create_todo(todo)
    
    return todo_item.model_dump_json()