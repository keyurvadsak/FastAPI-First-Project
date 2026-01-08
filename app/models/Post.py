from ..database.database import Base
from sqlalchemy import Column,Integer, String, Boolean, TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship




class post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published = Column(Boolean, default=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False,server_default='now()')
    owner_id = Column(Integer,ForeignKey("User.id",ondelete="CASCADE"),nullable=False)
    owner = relationship("User")