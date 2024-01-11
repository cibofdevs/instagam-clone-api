from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from auth import authentication
from db import models
from db.database import engine
from routers import user, post, comment

app = FastAPI()
app.include_router(user.router)
app.include_router(post.router)
app.include_router(authentication.router)
app.include_router(comment.router)


@app.get("/")
def root():
    return "Hello World!"


# cors configuration
origins = [
    "http://localhost:3000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

# generate database
models.Base.metadata.create_all(engine)

# static files
app.mount("/images", StaticFiles(directory="images"), name="images")
