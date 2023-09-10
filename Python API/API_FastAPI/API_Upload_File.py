import os
import uuid
import json

try:
    import uvicorn
    from fastapi import FastAPI, File, UploadFile, status

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')

os.system('cls')
app = FastAPI()

class Register(BaseModel):
    user: str
    email: str
    password: str

@app.get("/", status_code=status.HTTP_200_OK, tags=['Root'])
async def home():
    return "Hello World!"

@app.post("/", status_code=status.HTTP_202_ACCEPTED, tags=['Root'])
async def RegisterRequest(file: UploadFile = File(...)):
    file.filename = f"{uuid.uuid4()}.jpg"
    content = await file.read()

    # --- save file
    save_file = open(f"api/IMAGES/{file.filename}", 'wb')
    save_file.write(content)
    save_file.close()

    return file.filename

if __name__ == '__main__':
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)