from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import crud, schemas
from app.api.database import get_db

router = APIRouter()

@router.post("/CreateStack/", response_model=schemas.Stack)
def create_stack(stack: schemas.StackCreate, db: Session = Depends(get_db)):
    db_stack = crud.get_stack_by_stackname(db=db, stackname=stack.stackname)
    if db_stack:
        raise HTTPException(status_code=400, detail="Stack with same name already created")
    return crud.create_stack(db=db, stack=stack)