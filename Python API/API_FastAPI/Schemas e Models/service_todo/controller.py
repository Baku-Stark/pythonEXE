import sqlite3
from sqlalchemy.orm import Session

from fastapi import APIRouter, Body, HTTPException, Depends, status
router = APIRouter()

from service_todo.schema import TodoIn, TodoUpdate
from service_sql import create_todo, delete_status_todo, read_all_todo, read_id_todo, update_status_todo, update_body_todo

from . import model, schema
import service_todo.database as database

model.Base.metadata.create_all(bind=database.engine)


# Dependência de sessão do banco de dados
def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/create_todo", summary="Criar uma nova tarefa", status_code=status.HTTP_201_CREATED, response_model=schema.TodoItem)
async def post(todo_item : schema.TodoIn, db: Session = Depends(get_db)):
    #print(todo_item.model_dump().values())
        
    #todo = list(value for value in todo_item.model_dump().values())
    #print(todo)

    db_todo = model.TodoItem(**todo_item.model_dump())

    try:
        #create_todo(todo)
        print(todo_item)
        db.add(db_todo)

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error
    
    finally:
        db.commit()
        db.refresh(db_todo)

    
    return db_todo

@router.get("/read_all_todo", summary="Adquirir todas as tarefas", status_code=status.HTTP_200_OK, response_model=list[schema.TodoSchema])
async def get_all_todo(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)) -> list[object]:
    try:
        todos = db.query(model.TodoItem).offset(skip).limit(limit).all()

    except Exception as error:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error)
        ) from error
    
    return todos

@router.get("/read_todo_={todo_id}", summary="Adquirir uma tarefa especifica", status_code=status.HTTP_200_OK, response_model=schema.TodoItem)
async def get_id_todo(todo_id: int, db: Session = Depends(get_db)) -> object:
    #print(todo_id)
    try:
        #todo_list = read_id_todo(todo_id)
        todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    return todo

@router.put("/update_todo_status_={todo_id}", summary="Atualizar o status de uma tarefa", status_code=status.HTTP_200_OK, response_model=schema.TodoItem)
async def update_status(todo_id: int, completed: schema.TodoCompleted, db: Session = Depends(get_db)):
    #print(id_todo)
    try:
        #todo_list = update_status_todo(id_todo)
        db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    finally:
        db_todo.completed = completed.completed
        db.commit()
        db.refresh(db_todo)

    #print(db_todo)
    return db_todo

@router.put("/update_todo_={todo_id}", summary="Atualizar uma tarefa", status_code=status.HTTP_200_OK)
async def update_todo(todo_id: int, todo: schema.TodoIn, db: Session = Depends(get_db)):
    # print(f"{id_todo} : {todo_item.model_dump()}")
    
    try:
        # todo = list(value for value in todo_item.model_dump().values())
        # todo_updated = update_body_todo(id_todo, todo)
        db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3
    
    finally:
        for key, value in todo.model_dump().items():
            setattr(db_todo, key, value)
        db.commit()
        db.refresh(db_todo)

    return db_todo

@router.delete("/delete_todo_={todo_id}", summary="Apagar uma tarefa pelo ID", status_code=status.HTTP_200_OK)
async def delete(todo_id: int, db: Session = Depends(get_db)) -> object:
    #print(id_todo)
    try:
        #todo_list = delete_status_todo(id_todo)
        db_todo = db.query(model.TodoItem).filter(model.TodoItem.id == todo_id).first()

    except sqlite3.ProgrammingError as error_sqlite3:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(error_sqlite3)
        ) from error_sqlite3

    finally:
        db.delete(db_todo)
        db.commit()

    #print(todo_list)
    return {"ok": True}