from sqlalchemy.orm import Session
from app.api import models, schemas
from app.core.security import get_password_hash

# For Creating User in db
def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(
        username=user.username,
        email=user.email,
        password=get_password_hash(user.password)
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

# For Getting User by username
def get_user_by_username(db: Session, username: str):
    return db.query(models.User).filter(models.User.username == username).first()

# For Creating stacks
def create_stack(db: Session, stack: schemas.StackCreate):
    db_stack = models.Stack(
        stackname = stack.stackname,
        description = stack.description,
        userId = stack.userId
    )
    db.add(db_stack)
    db.commit()
    db.refresh(db_stack)
    return db_stack

# For getting stack by stackname
def get_stack_by_stackname(db: Session, stackname: str):
    return db.query(models.Stack).filter(models.Stack.stackname == stackname).first()
