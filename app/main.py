from typing import Union
from fastapi import FastAPI
from .models.user import User

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/users")
def create_user(user: User):
    return {"message": f"{user.id}: User {user.name} is {user.age} years old g."}