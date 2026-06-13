from fastapi import APIRouter
from student_managment_api.database import SessionLocal
from student_managment_api.models.user_db import UserDB
from student_managment_api.schemas.user import UserCreate
from student_managment_api.schemas.user import UserLogin

router = APIRouter()

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    db_user = UserDB(
        username=user.username,
        email=user.email,
        password=user.password
    )

    db.add(db_user)
    db.commit()

    return {
        "message": "User registered successfully"
    }

@router.get("/users")
def get_users():

    db = SessionLocal()

    users = db.query(UserDB).all()

    return users

@router.post("/login")
def login(user: UserLogin):

    db = SessionLocal()

    db_user = (
        db.query(UserDB)
        .filter(UserDB.email == user.email)
        .first()
    )

    if db_user is None:
        return {"message": "User not found"}

    if db_user.password != user.password:
        return {"message": "Invalid password"}

    return {"message": "Login successful"}