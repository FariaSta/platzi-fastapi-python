from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHadler
from routers.movie import movie_router
from routers.users import users_router
from fastapi.responses import HTMLResponse
from uvicorn import uvicorn
import os

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0",
    port=int(os.environ.get("PORT", 8000)))

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

app.add_middleware(ErrorHadler)
app.include_router(movie_router)
app.include_router(users_router)

Base.metadata.create_all(bind=engine)

@app.get('/', tags=['home'])
def message():
    return HTMLResponse('<h1>Hello World</h1>')