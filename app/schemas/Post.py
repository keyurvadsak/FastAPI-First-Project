from pydantic import BaseModel
from .User import owner_data

class PostBase(BaseModel):
    title : str
    content: str
    
class CreatePost(PostBase):
    pass

class ResponsePost(BaseModel):
    id: int
    title:str
    content:str
    owner:owner_data
    
    class config:
        orm_mode= True
