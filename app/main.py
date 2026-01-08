
from fastapi import FastAPI,Request
from app.database.database import engine
from .models import models
from .routers import post,product,User,auth,votes
import time

app = FastAPI()




@app.middleware('http')
async def process_time(request:Request, call_next):
    start = time.time()
    response = await call_next(request)
    process_time = time.time() - start
    response.headers["X-Process-Time"] = str(process_time)
    return response
    
    
models.Base.metadata.create_all(bind = engine)

app.include_router(post.router)
app.include_router(product.router)
app.include_router(User.router)
app.include_router(auth.router)
app.include_router(votes.router)





