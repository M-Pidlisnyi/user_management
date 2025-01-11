from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    id: int | None
    username: Annotated[str, Field(min_length=3)]
    email: str = Field(min_length=5)


users_db = [
    User(id=0, username="mike", email="kime@gmail.com"),
]


app = FastAPI()


@app.get("/users")
def get_users():
    return users_db

@app.get("/user/{id}")
def get_single_user(id:int):
    for user in users_db:
        if user.id == id:
            return user
        
@app.post("/create_user")
def create_user(user:User):
    users_db.append(user)
    return user
    
