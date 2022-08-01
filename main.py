import re
from typing import Optional
from fastapi import FastAPI
from fastapi.params import Body
from pydantic import BaseModel
from random import randrange
app = FastAPI()

class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    rating : Optional [int] = None

my_posts = [{"title" : "First Post Title", "content" : "First Post Content", "id": 1},
                {"title" : "Second Post Title", "content" : "Second Post Content", "id": 2},
                {"title" : "Last Post Title", "content" : "Last Post Content", "id": 3}]

def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/posts")
def get_posts():
    return {"data": my_posts}

@app.post("/posts")
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict['id'] = randrange(0,100000)
    # print(post.title)
    # print(post.content)
    # print(post.published)
    # print(post.dict())
    my_posts.append(post_dict)
    return {"data": post_dict}

@app.get("/posts/{id}")
def get_post(id: int):
    
    post = find_post(id) 
    print(post)
    # return {"post_detail": f"Post id: {id} | and it returned by ID"}
    return {"post_detail": post}
  