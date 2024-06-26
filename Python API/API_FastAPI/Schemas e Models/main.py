import uvicorn

from fastapi import FastAPI
from routers import api_router
app = FastAPI(title="Schemas e Models")

from service_sql import init_db
init_db()

app.include_router(api_router)


if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)