from fastapi import status, HTTPException,Depends,APIRouter
# from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.models.models import get_db
from app.models.User import User
from app.schemas.User import UserDataFetchResponse,UserCreateResponse,UserCreate
from app.utils.utils import hash

router = APIRouter(
    prefix="/User",
    tags=["User"]
)

@router.post("/",status_code= status.HTTP_201_CREATED,response_model= UserCreateResponse)
def Create_User(user:UserCreate , db:Session = Depends(get_db)):
    paswd = user.password
    
    print("paswd: ",paswd)
    hash_password = hash(paswd)
    print(hash_password)
    user.password = hash_password 
    new_user = User(**user.dict())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get("/{id}",response_model = UserDataFetchResponse)
def get_User(id: int,db:Session = Depends(get_db)):
    user = db.query(User).filter(User.id == id).first()
    if user == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND,detail=f"Post with id {id} is not found")
    return user
    