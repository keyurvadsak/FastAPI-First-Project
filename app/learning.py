from fastapi import FastAPI,Response, status, HTTPException,Depends
import psycopg2
from psycopg2.extras import RealDictCursor
import time
from app.database.database import engine
from .utils import utils
from .models import models
from .schemas import schemas


# class Post(BaseModel):
#     title : str
#     content : str

# class UpdatePost(BaseModel):
#     title : str
#     content : str
    
# class Product(BaseModel):
#     name : str
#     price : int
#     Inventry : int
#     is_sale : Optional[bool]= False


 
# while True:

#     try: 
#         conn = psycopg2.connect(host="localhost",database ="fastAPI",user="postgres",password="keyur6634", cursor_factory=RealDictCursor)
#         cursor = conn.cursor()
#         print("Database connection was successful")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)



# @app.get("/")
# def user():
#     return {"message": "Hello World"}


# @app.post("/createpost")
# def create_post(payload: dict = Body(...)):
#     print(payload)
#     return {"new_post": f"Title: {payload['title']}, Content: {payload['content']}"}


# my_post = [{"title": "first post", "content": "this is the content of the first post","id": 1}
#          , {"title": "second post", "content": "this is the content of the second post","id": 2}
#          ,{"title": "third post", "content": "this is the content of the third post","id": 3}]


# def find_post(id):
#     for p in my_post:
#         if p['id'] == id:
#             return p
        
# def find_index_post(id):
#     for i, p in enumerate(my_post):
#         if p['id'] == id:
#             return i


# @app.get("/posts")
# def get_posts():
#     cursor.execute("SELECT * FROM posts")
#     psst = cursor.fetchall()
#     return psst


# @app.post("/createposts")
# def create_post(post: Post):
#     posts_dict = post.dict()
#     posts_dict['id'] = randrange(0,1000000)
#     my_post.append(posts_dict)
#     raise HTTPException (status_code= status.HTTP_201_CREATED, detail={"data": my_post})    


# @app.post("/createposts", status_code= status.HTTP_201_CREATED)
# def create_post(post: Post):
#     posts_dict = post.dict()
#     posts_dict['id'] = randrange(0,1000000)
#     my_post.append(posts_dict)
#     return {"data": my_post}

# @app.post("/createposts", status_code= status.HTTP_201_CREATED)
# def create_post(post: schemas.CreatePost):
#     cursor.execute("""INSERT INTO posts (title, content) VALUES (%s,%s) returning *""",(post.title, post.content))
#     posss = cursor.fetchall()  
#     conn.commit() 
#     return posss



# @app.get("/posts/{id}")
# def get_post(id):

#     if id.isdigit() == False:
#         return {"message": "Invalid ID format"}
#     else:
#         post = find_post(int(id))
#         print(post)
#     if post == None:
#         return {"message": "post not found"}
#     else:
#         return {"post_detail": post}

# @app.get("/posts/latest")
# def get_latest_post():
#     post = my_post[len(my_post)-1]
#     return {"latest_post": post}

# @app.get("/posts/latest")
# def get_latest_post():
#     post =cursor.execute("SELECT * FROM posts ORDER BY id DESC LIMIT 1")
#     post = cursor.fetchall()
#     return post

 
# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     print(post)
#     if post == None:
#         return {"message": "post not found"}
#     else:
#         return {"post_detail": post}


# @app.get("/posts/{id}")
# def get_post(id: int, response: Response):
#     post = find_post(id)
#     if not post:
#         response.status_code = status.HTTP_404_NOT_FOUND
#         return {"message": "post not found"}
#     else:
#         return {"post_detail": post}
    
# @app.get("/posts/{id}")
# def get_post(id: int):
#     post = find_post(id)
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
#     else:
#         return {"post_detail": post} 


# @app.get("/posts/{id}")
# def get_post(id: int):
#     cursor.execute(f"SELECT * FROM posts WHERE id = {id}")
#     post = cursor.fetchall()
#     if not post:
#         raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = f"post with id {id} not found")
#     else:
#         return post
    
    
# @app.delete("/posts/{id}")
# def delete_post(id: int):
#     cursor.execute("DELETE FROM posts WHERE id = %s returning *",(str(id),))
#     deleted_post = cursor.rowcount


#     if deleted_post == 0:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
#     else:
#         conn.commit()
#         raise HTTPException(status_code= status.HTTP_204_NO_CONTENT)


# @app.put("/posts/{id}")
# def update_post(id: int, post: UpdatePost):
#     index = find_index_post(id)
    
#     if index == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
#     else:
#         post_dict = post.dict()
#         post_dict['id'] = id
#         my_post[index] = post_dict
#         return {"data": my_post }


# @app.put("/posts/{id}")
# def update_post(id: int, post: schemas.CreatePost):
#     cursor.execute("""UPDATE posts SET title = %s, content = %s WHERE id = %s returning *""",
#                    (post.title, post.content, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
    
#     if updated_post == None:
#         raise HTTPException(status_code= status.HTTP_404_NOT_FOUND, detail= f"post with id {id} not found")
#     else:
#         return updated_post