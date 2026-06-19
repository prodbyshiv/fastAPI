from fastapi import APIRouter
from student_managment_api.database import SessionLocal
from student_managment_api.models.notes_db import NoteDB
from student_managment_api.schemas.notes import NoteCreate
from student_managment_api.jwt_handler import verify_token

router = APIRouter()

@router.post("/notes")
def create_note(
    note: NoteCreate,
    token: str
):

    db = SessionLocal()

    payload = verify_token(token) #token jo string me aa rha hai usko token ke roop m bana de rha hai..

    user_id = payload["user_id"]

    db_note = NoteDB(
        title=note.title,
        content=note.content,
        user_id=user_id
    )

    db.add(db_note)
    db.commit()

    return {
        "message": "Note created"
    }

@router.get("/notes")
def get_notes(token: str):

    db = SessionLocal()

    payload = verify_token(token)

    user_id = payload["user_id"]

    notes = (
        db.query(NoteDB)
        .filter(NoteDB.user_id == user_id)
        .all()
    )

    return notes