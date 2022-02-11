from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    Title: str
    con: str


@app.get("/")
def root():
    return {"message": "Hellewrwq vo Worldjga ndlkfgnd"}


@app.get("/posts")
def root():
    return {"data": "THis is your posts"}


@app.post("/create")
def root(new_post: Post ):
    print(new_post.Title)
    return {"data": "new_post"}