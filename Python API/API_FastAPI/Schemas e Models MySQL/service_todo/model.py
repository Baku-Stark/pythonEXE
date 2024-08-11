from sqlalchemy import Column, Integer, String, Boolean
from service_todo.database import Base

class TodoItem(Base):
    __tablename__ = "todo_items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(50), index=True)
    description = Column(String(200), index=True)
    completed = Column(Boolean, default=False)
