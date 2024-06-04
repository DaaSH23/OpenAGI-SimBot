from sqlalchemy import Column, Integer, String, ForeignKey, Boolean
from app.api.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    is_Active = Column(Boolean, default=True)
    crt_Date = Column(String)
    upt_Date = Column(String)

class Stack(Base):
    __tablename__ = "stacks"

    id = Column(Integer, primary_key=True, index=True)
    stackname = Column(String, index=True)
    description = Column(String)
    userId = Column(Integer, ForeignKey("users.id"))
    crt_Date = Column(String)
    upt_Date = Column(String)

    
