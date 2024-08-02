from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

from db import schemas, models
from db.database import SessionLocal, engine
from db.crud import create_user, get_user, get_all_users



app = FastAPI()
models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()

@app.post("/user/new", response_model=schemas.User)
def create_user_endpoint(new_user: schemas.User, db: Session = Depends(get_db)):
    return create_user(db, new_user)

@app.get("/user/all", response_model=list[schemas.User])
def get_all_users_endpoint(db: Session = Depends(get_db)):
    return get_all_users(db)

@app.get("/user/{user_id}")
def get_user_endpoint(user_id:int, db:Session = Depends(get_db)):
    user = get_user(db, user_id)
    if user is None:
        return "user not found" 
    return user