from fastapi import APIRouter
api_router = APIRouter()

from service_todo.controller import router as todo_item
api_router.include_router(todo_item, prefix="/todo_item", tags=['todo_item'])