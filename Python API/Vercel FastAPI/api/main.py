import os

try:
    # link: https://fastapi.tiangolo.com/
    # pip install fastapi
    import uvicorn
    from fastapi import FastAPI, status

except ModuleNotFoundError:
    os.system('pip install -r requirements.txt')

finally:
    print(
        '=====Todos as libs estão instaladas com sucesso!====='
    )

    # UVICORN -> LINK: https://pypi.org/project/uvicorn/

    # --- pegando o nome do arquivo atual
    # current_file = str(os.path.basename(__file__))
    # --- uvicorn example:app
    # os.system(f'uvicorn {current_file[0:3]}:app --reload')


app = FastAPI()

@app.get("/", status_code=status.HTTP_200_OK, tags=["Root"])
async def hello():
    return {"RESPONSE": "Hello World!"}

if __name__ == '__main__':
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host='0.0.0.0', port=port, reload=True)