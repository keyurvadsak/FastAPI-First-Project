from ..database.database import Base
from sqlalchemy import Column,Integer, String, Boolean, TIMESTAMP,ForeignKey
from sqlalchemy.orm import relationship




class Product(Base):
    __tablename__ = "products"
    
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String, nullable=False)
    price = Column(Integer, nullable=False)
    is_sale = Column(Boolean, default=False, nullable=False)
    Inventry = Column(Integer, nullable=False)
    owner_id = Column(Integer,ForeignKey("User.id",ondelete="CASCADE"),nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False,server_default="now()" )
    owner = relationship("User")