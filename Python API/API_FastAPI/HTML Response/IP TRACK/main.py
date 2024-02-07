import uvicorn, os, requests, json
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, status
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

os.system('cls')

templates = Jinja2Templates(directory="Page")

app = FastAPI()
app.mount("/static", StaticFiles(directory="Page/static"), name="static")

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", status_code=status.HTTP_200_OK, response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        name="index.html",
        context={
            "request": request,
        }
    )

@app.get("/user_ip_address_={request}", status_code=status.HTTP_202_ACCEPTED)
async def request_user_ip(request: str) -> dict:
    api_user_ip = f"http://ip-api.com/json/{request}?fields=status,message,continent,continentCode,country,countryCode,region,regionName,city,district,zip,lat,lon,timezone,offset,currency,isp,org,as,asname,reverse,mobile,proxy,hosting,query"
    response = requests.get(api_user_ip, timeout=2.50)
    user_ip = response.json()
    # print(user_ip)

    return user_ip

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)