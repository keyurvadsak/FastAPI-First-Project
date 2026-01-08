from typing import List
from fastapi import FastAPI,Response, status, HTTPException,Depends,APIRouter
# from pydantic import BaseModel
from sqlalchemy.orm import Session
from app.database.database import engine
from app.models.models import get_db
from app.models.Product import Product
from app.schemas.Product import ResponseProduct,CreateProduct
from app.routers.Oauth2 import get_current_user


router = APIRouter(
    prefix="/products",
    tags= ["Products"]
)


@router.get("/",status_code=status.HTTP_201_CREATED,response_model = List[ResponseProduct])
def get_products(db:Session = Depends(get_db), current_user = Depends(get_current_user)):
    products = db.query(Product).all()
    return products


@router.get("/own_products",response_model= List[ResponseProduct])
def get_own_product(db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    products = db.query(Product).filter(Product.owner_id == current_user.id).all()

    return products

@router.post("/",response_model = ResponseProduct)
def add_product(product : CreateProduct,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    new_product = Product(**product.dict(), owner_id = current_user.id)
    
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product

@router.delete("/{id}",response_model = ResponseProduct)
def delete_product(id:int,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    product = db.query(Product).filter(Product.id == id).filter(Product.owner_id == current_user.id)
    if product.first() == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail = f"Product with id {id} not Found")
    product.delete(synchronize_session = False)
    db.commit()
    return Response(status_code = status.HTTP_204_NO_CONTENT)
    
@router.put("/{id}",response_model = ResponseProduct)
def update_product(id:int,product:CreateProduct,db:Session = Depends(get_db),current_user = Depends(get_current_user)):
    u_product = db.query(Product).filter(Product.id == id).filter(Product.owner_id == current_user.id)
    u_productd = u_product.first()
    if u_productd == None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"Product with id {id} not found")
    u_product.update(product.dict(),synchronize_session = False)
    db.commit()
    return u_product.first()