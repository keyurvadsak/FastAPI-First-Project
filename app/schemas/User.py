from pydantic import BaseModel,EmailStr
from datetime import datetime




class User(BaseModel):
    id:int
    create_at:datetime

    
class UserCreate(BaseModel):
    
    email :EmailStr
    name : str
    password: str

class UserCreateResponse(BaseModel):
    id : int
    name : str
    email:EmailStr
    created_at : datetime
    class config:
        orm_mode = True
        
        
class UserDataFetchResponse(BaseModel):
    id :int
    name: str
    email:EmailStr
    created_at:datetime
    
    class config:
        orm_code = True

class owner_data(BaseModel):
    name: str
    email: EmailStr
    
    class config:
        orm_mode = True


