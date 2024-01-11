from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from db import models
from db.database import engine
from routers import user, post

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)


@app.get("/")
def root():
    return "Hello World!"


# generate database
models.Base.metadata.create_all(engine)

# static files
app.mount("/images", StaticFiles(directory="images"), name="images")
