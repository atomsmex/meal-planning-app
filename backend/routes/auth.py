from fastapi import APIRouter, HTTPException, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

router = APIRouter()

class User(BaseModel):
    username: str
    password: str

# Mock database
users_db = {}

@router.post("/register")
def register(user: User):
    if user.username in users_db:
        raise HTTPException(status_code=400, detail="Username already registered")
    users_db[user.username] = user.password  # Store password securely in a real app
    return {"msg": "User registered successfully"}

@router.post("/login")
def login(user: User):
    if user.username not in users_db or users_db[user.username] != user.password:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return {"msg": "Login successful"}