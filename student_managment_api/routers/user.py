from fastapi import APIRouter
from student_managment_api.database import SessionLocal
from student_managment_api.models.user_db import UserDB
from student_managment_api.schemas.user import UserCreate
from student_managment_api.schemas.user import UserLogin
from student_managment_api.auth import hash_password
from student_managment_api.auth import verify_password
from student_managment_api.jwt_handler import create_access_token
from student_managment_api.jwt_handler import verify_token
from fastapi import Depends
from student_managment_api.dependencies import get_current_user
from student_managment_api.models.user_db import UserDB



router = APIRouter()

@router.post("/register")
def register(user: UserCreate):

    db = SessionLocal()

    db_user = UserDB(
        username=user.username,
        email=user.email,
        password=hash_password(user.password)
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
    
    print(user.password)
    print(db_user.password)
    
    if not verify_password(
    user.password,
    db_user.password
):
        return {"message": "Invalid password"}

    token = create_access_token(db_user.id)

    return {
        
    "access_token": token
}

@router.get("/me")
def get_me(
    current_user: UserDB = Depends(get_current_user)
):
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }
    

