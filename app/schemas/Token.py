from pydantic import BaseModel
from typing import Optional



class Token(BaseModel):
    acsess_token : str
    token_type : str
    
    
        
class Token_data(BaseModel):
    id: Optional[int] = None