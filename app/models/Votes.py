from ..database.database import Base
from sqlalchemy import Column,Integer,ForeignKey


class votes(Base):
    __tablename__= "Votes"
    
    user_id = Column(Integer,ForeignKey("User.id",ondelete="CASCADE"),primary_key=True)
    post_id = Column(Integer,ForeignKey("posts.id",ondelete="CASCADE"),primary_key=True)

    
    