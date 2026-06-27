from fastapi import Depends
from sqlalchemy.orm import Session

from student_managment_api.database import get_db
from student_managment_api.database import SessionLocal
from student_managment_api.jwt_handler import verify_token
from student_managment_api.models.user_db import UserDB
from fastapi.security import OAuth2PasswordBearer

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")


def get_current_user(
    token: str = Depends(oauth2_scheme)
):

    db = SessionLocal()

    payload = verify_token(token)

    user_id = payload["user_id"]

    user = (
        db.query(UserDB)
        .filter(UserDB.id == user_id)
        .first()
    )

    return user