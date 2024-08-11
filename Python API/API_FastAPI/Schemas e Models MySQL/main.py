import uvicorn

from fastapi import FastAPI, status
from routers import api_router
app = FastAPI(title="Schemas e Models")

app.include_router(api_router)

@app.get("/", status_code=status.HTTP_200_OK)
async def home():
    return {"message" : "Hello"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=8000, reload=True)