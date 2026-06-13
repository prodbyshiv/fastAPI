from student_managment_api.database import engine, Base

from student_managment_api.models.student_db import StudentDB
from student_managment_api.models.user_db import UserDB


Base.metadata.create_all(bind=engine)