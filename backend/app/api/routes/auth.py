from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import crud, schemas
# from app.api.deps import get_db
from app.api.database import get_db

router = APIRouter()

@router.post("/signup/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_username(db=db, username=user.username)
    if db_user:
        raise HTTPException(status_code=400, detail="Username already registered")
    return crud.create_user(db=db, user=user)