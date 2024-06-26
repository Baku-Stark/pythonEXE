from fastapi import APIRouter, Body, HTTPException, status
router = APIRouter()

from service_todo.schema import TodoIn

@router.post("/", summary="Criar uma nova tarefa", status_code=status.HTTP_201_CREATED)
async def post(todo_item : TodoIn = Body(...)):
    print(todo_item.json())