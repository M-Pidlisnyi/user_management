from .models import User as UserModel
from .schemas import User as UserSchema
from sqlalchemy.orm import Session

def create_user(db:Session, new_user: UserSchema):
    db_user = UserModel(
        username = new_user.username,
        email = new_user.email
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_user(db:Session, user_id:int):
    return db.query(UserModel).filter(UserModel.id == user_id).first()

def get_all_users(db:Session):
    return db.query(UserModel).all()


