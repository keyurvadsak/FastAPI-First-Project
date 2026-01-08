from fastapi import APIRouter,Depends,status,HTTPException
from ..models.models import get_db
from sqlalchemy.orm import Session
from ..models.User import User
from ..utils.utils import verify
from .Oauth2 import create_access_token 
from fastapi.security.oauth2 import OAuth2PasswordRequestForm

router = APIRouter(
    tags=['Auth']
)


@router.post("/login")
def login(user_info:OAuth2PasswordRequestForm = Depends(),db:Session = Depends(get_db)):
    
    user = db.query(User).filter(User.email == user_info.username).first()
    
    if user == None:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail="Email is invalid.")
    if not verify(user_info.password , user.password):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail= "password is incorrect")
    
    access_token = create_access_token(data = {'user_id':user.id})
    return {"access_token":access_token,"token_type":"Bearer"}
    




