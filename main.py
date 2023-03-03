from fastapi import FastAPI
from config.database import engine, Base
from middlewares.error_handler import ErrorHadler
from routers.movie import movie_router
from routers.users import users_router
from fastapi.responses import HTMLResponse

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