from pydantic import BaseModel
from pydantic.types import conint

class Vote(BaseModel):
    post_id : int
    dit: conint(le=1) # type: ignore
    
    