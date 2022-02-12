from random import randrange
from xml.etree.ElementPath import find
from fastapi import FastAPI,status,HTTPException
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange

app = FastAPI()


class Post(BaseModel):
    title: str
    con: str
    
    
my_posts=[{"title":"1","con":"sdfb","id":1},{"title":"2","con":"sdfb","id":2},{"title":"3","con":"sedga","id":3}]


def find_post(id):
    for p in my_posts:
        if p["id"]==id:
            return p

def find_index_post(id):
    for i,p in enumerate(my_posts):
        if  p['id']==id:
            return i


@app.get("/")
def root():
    return {"message": "Hellewrwq vo Worldjga ndlkfgnd"}


@app.get("/posts")
def root():
    return {"data": my_posts}


@app.post("/posts")
def create_posts(new_post: Post ):
    post_dict=new_post.dict()
    post_dict["id"]=randrange(0,10000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_posts(id):
    postr=find_post(int(id))
    if not postr:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    return {"data": postr}



@app.delete("/posts/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_posts(id:int):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    my_posts.pop(index)
    return {'message' : "deleted"}


@app.put("/posts/{id}")
def update_post(id:int,post:Post):
    index=find_index_post(id)
    if index==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"{id} not found")
    post_dict=post.dict()
    post_dict["id"]=id
    my_posts[index]=post_dict
    return{"data": post_dict}

