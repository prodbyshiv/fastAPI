from student_managment_api.database import engine, Base

from student_managment_api.models.student_db import StudentDB
from student_managment_api.models.user_db import UserDB
from student_managment_api.models.notes_db import NoteDB

Base.metadata.create_all(bind=engine)