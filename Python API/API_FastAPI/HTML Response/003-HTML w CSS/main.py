import uvicorn, os
from fastapi.responses import HTMLResponse
from fastapi import FastAPI, Request, status
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

os.system('cls')

templates = Jinja2Templates(directory="Page")

app = FastAPI()
app.mount("/static", StaticFiles(directory="Page/static"), name="static")

@app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
            "name": "Wallace",
            "data": {
                "age": 23,
                "job": [
                    "Developer",
                    "Teacher"
                ]
            }
        }
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)