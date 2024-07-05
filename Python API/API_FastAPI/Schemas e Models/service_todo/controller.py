import sqlite3

from fastapi import APIRouter, Body, HTTPException, status
router = APIRouter()

from service_todo.schema import TodoIn, TodoUpdate
from service_sql import create_todo, delete_status_todo, read_all_todo, read_id_todo, update_status_todo, update_body_todo

@router.post("/create_todo", summary="Criar uma nova tarefa", status_code=status.HTTP_201_CREATED)
async def post(todo_item : TodoIn = Body(...)):
    #print(todo_item.model_dump().values())
        
    todo = list(value for value in todo_item.model_dump().values())
    #print(todo)
    try:
        create_todo(todo)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error
    
    return todo_item.model_dump_json()

@router.get("/read_all_todo", summary="Adquirir todas as tarefas", status_code=status.HTTP_200_OK)
async def get_all_todo() -> list[list]:
    try:
        todo_list = read_all_todo()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error
    
    return todo_list

@router.get("/read_todo_={id_todo}", summary="Adquirir uma tarefa especifica", status_code=status.HTTP_200_OK)
async def get_id_todo(id_todo : int) -> list:
    #print(id_todo)
    try:
        todo_list = read_id_todo(id_todo)

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    return todo_list

@router.put("/update_todo_status_={id_todo}", summary="Atualizar o status de uma tarefa", status_code=status.HTTP_200_OK)
async def update_status(id_todo : int) -> list:
    #print(id_todo)
    try:
        todo_list = update_status_todo(id_todo)

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    #print(todo_list)
    return todo_list

@router.put("/update_todo_={id_todo}", summary="Atualizar uma tarefa", status_code=status.HTTP_200_OK)
async def update_todo(id_todo : int, todo_item : TodoUpdate = Body(...)):
    # print(f"{id_todo} : {todo_item.model_dump()}")
    
    try:
        todo = list(value for value in todo_item.model_dump().values())
        todo_updated = update_body_todo(id_todo, todo)

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    return todo_updated

@router.delete("/delete_todo_={id_todo}", summary="Apagar uma tarefa pelo ID", status_code=status.HTTP_200_OK)
async def delete(id_todo : int) -> list:
    #print(id_todo)
    try:
        todo_list = delete_status_todo(id_todo)

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    #print(todo_list)
    return todo_list