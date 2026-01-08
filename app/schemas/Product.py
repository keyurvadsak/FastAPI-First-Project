from pydantic import BaseModel
from typing import Optional
from .User import owner_data


class ProductBase(BaseModel):
    name: str
    price: int
    Inventry: int
    is_sale: Optional[bool] = False
    
class CreateProduct(ProductBase):
    pass

class ResponseProduct(BaseModel):
    name: str
    price: int
    Inventry: int
    is_sale: bool
    owner: owner_data
    
    class config:
        orm_mode = True
        