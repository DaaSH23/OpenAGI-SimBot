from pydantic import BaseModel
from typing import List, Optional

# Base schema for User
class UserBase(BaseModel):
    username: str
    email: str

# Schema for creating the user
class UserCreate(UserBase):
    password: str

# user schema for additional fields
class User(UserBase):
    id: int
    is_Active: bool
    crt_Date: Optional[str] = None
    upt_Date: Optional[str] = None

    class config:
        orm_mode: True

# base schema for stack
class StackBase(BaseModel):
    stackname: str
    description: Optional[str] = None

# schema for creating stack
class StackCreate(StackBase):
    userId: int

# stack schema for additional fields 
class Stack(BaseModel):
    id: int
    userId: int
    crt_Date: Optional[str] = None
    upt_Date: Optional[str] = None

    class config:
        orm_mode = True

# schema for listing user with their stacks
class userWithStacks(User):
    stacks: List[Stack] = []

    class config:
        orm_mode = True
        
class AgentRequest(BaseModel):
    query: str
    description: str