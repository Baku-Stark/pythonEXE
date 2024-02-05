import uvicorn, os
from fastapi import FastAPI, Request, status
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

os.system('cls')

app = FastAPI()

templates = Jinja2Templates(directory="Page")

@app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(name="index.html", context={"request": request})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)