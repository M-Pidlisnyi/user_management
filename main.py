from fastapi import FastAPI
from pydantic import BaseModel, Field
from typing import Annotated

class User(BaseModel):
    id: int | None
    username: Annotated[str, Field(min_length=5)]
    email: str = Field(min_length=5)


users_db = [
    User(id=0, username="mike", email="kime@gmail.com"),
    ...,
    ...,
]


app = FastAPI()


@app.get("/users")
def get_users():
    return users_db

