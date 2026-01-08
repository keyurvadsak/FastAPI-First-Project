from ..database.database import Base,sessionLocal






    
    

    
def get_db():
    db = sessionLocal()
    try:
        yield db
    finally:
        db.close()
    