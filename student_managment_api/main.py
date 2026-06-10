from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr
from database import SessionLocal
from models import StudentDB

class Student(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(gt=0)
    email: EmailStr
    cgpa: float = Field(ge=0, le=10)

class StudentResponse(BaseModel):
    name: str = Field(min_length=3)
    # age: int = Field(gt=0)
    email: EmailStr
    cgpa: float = Field(ge=0, le=10) 


app = FastAPI()



@app.post("/students")
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

@app.get("/students", response_model=list[StudentResponse]) 
#Whatever I return should be sent back as a list of StudentResponse objects.
def get_students():

    db = SessionLocal()

    students = db.query(StudentDB).all() # give evrything from database in StudentDB format

    return students