from fastapi import Response, status, HTTPException,Depends,APIRouter
from sqlalchemy.orm import Session
from ..models.models import get_db
from ..models.Votes import votes
from ..schemas.Votes import Vote
from .Oauth2 import get_current_user

router = APIRouter(
    prefix="/votes",
    tags=["Votes"]
)

@router.post("/")
def vote(vote: Vote, db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    post_vote = db.query(votes).filter(votes.post_id == vote.post_id,votes.user_id == current_user.id)
    
    found_vote = post_vote.first()
    
    if (vote.dit == 1):
        if found_vote == None:
            new_vote = votes(post_id = vote.post_id,user_id = current_user.id)
            db.add(new_vote)
            db.commit()
            return {"message":"successfully added vote"}
        else:   
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"user {current_user.id} has already voted on post {vote.post_id}")
        

    else:
        if found_vote == None:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Vote not found")
        
        post_vote.delete(synchronize_session=False)
        db.commit()
        return {"message":"successfully deleted vote"}
    