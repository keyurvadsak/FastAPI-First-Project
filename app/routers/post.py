from typing import List
from fastapi import Response, status, HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..models.models import get_db
from ..models.Post import post
from ..schemas.Post import ResponsePost,CreatePost
from .Oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=["Posts"]

)

@router.get("/",response_model= List[ResponsePost])
def get_post(db:Session = Depends(get_db),current_user = Depends(get_current_user) ):
    posts = db.query(post).all()
    return posts

@router.get("/own_posts",response_model= List[ResponsePost])
def get_post(db:Session = Depends(get_db),current_user = Depends(get_current_user) ):
    posts = db.query(post).filter(post.owner_id == current_user.id).all()
    return posts

@router.post("/",response_model = ResponsePost)
def create_post(addpost: CreatePost,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    new_post = post(**addpost.dict(),owner_id = current_user.id)
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post 


# @router.get("/{id}",response_model = ResponsePost)
# def get_post(id: int, db:Session = Depends(get_db)):
    
#     posts = db.query(post).filter(post.id == id).first()
#     if posts == None:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
#     return posts

@router.delete("/{id}")
def delete_post(id,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    
    d_post = db.query(post).filter(post.id == id).filter(post.owner_id == current_user.id)
    if d_post.first() == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
    d_post.delete(synchronize_session=False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)

@router.put("/{id}",response_model = ResponsePost)
def update_post(id:int, posts : CreatePost, db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    
    print(current_user.id ,"and" , id)
    update_post = db.query(post).filter(post.id == id).filter(post.owner_id == current_user.id)
    updated_post = update_post.first()
    
    if updated_post == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Post id {id} not found")
    update_post.update(posts.dict(),synchronize_session=False)
    db.commit()
    return update_post.first()


