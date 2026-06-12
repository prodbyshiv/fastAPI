from fastapi import APIRouter

from student_managment_api.database import SessionLocal
from student_managment_api.models.student_db import StudentDB
from student_managment_api.schemas.students import Student, StudentResponse

router = APIRouter()
 
@router.post("/students")
#FastAPI, create a Student object from the incoming JSON and give it to me.
def add_student(student: Student):
# function created that will store student obj of type Student
    db  = SessionLocal() # created a session to interact with database
    #to add something to database u can't send a pydantic object so you craeted db_sudent
    # # create a StudentDB object using data from the Pydantic student object
    db_student = StudentDB(

        name=student.name,
        age=student.age,
        email=student.email,
        cgpa=student.cgpa
    )
    db.add(db_student) # it expects an SQLalchemy model not pydantic model.
    db.commit()
    return {

        "message": "student added successfully"
    }

@router.get("/students", response_model=list[StudentResponse]) 
#Whatever I return should be sent back as a list of StudentResponse objects.
def get_students():

    db = SessionLocal()

    students = db.query(StudentDB).all() # give evrything from database in StudentDB format

    return students

@router.get("/students/{student_id}")
def get_students_by_id(student_id: int):
    db  = SessionLocal()
    student = (
        db.query(StudentDB)
        .filter(StudentDB.id == student_id)
        .first()
    )
    return student

@router.delete("/students/{student_id}")
def delete_students(student_id: int):
    db  = SessionLocal()
    student = (
        db.query(StudentDB)
        .filter(StudentDB.id == student_id)
        .first()
    )
    # this first() always return a StudentDb object
    db.delete(student)

    db.commit()


    if student is None:
        return {"message": "Student not found"}

    return {
        "message": "student deleted"
    }

@router.put("/students/{student_id}")
def update_student(student_id: int, updated_student: Student):

    db = SessionLocal()

    student = (
        db.query(StudentDB)
        .filter(StudentDB.id == student_id)
        .first()
    )

    if student is None:
        return {"message": "Student not found"}

    student.name = updated_student.name
    student.age = updated_student.age
    student.email = updated_student.email
    student.cgpa = updated_student.cgpa

    db.commit()

    return {"message": "Student updated"}