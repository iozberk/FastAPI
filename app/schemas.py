from pydantic import BaseModel


class Post(BaseModel):
    title: str
    content: str
    published: bool = True
    # rating : Optional [int] = None


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class CreatePost(PostBase):
    
    pass


# class UpdatePost(PostBase):
#     pass








