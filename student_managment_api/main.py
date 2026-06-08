from fastapi import FastAPI
from pydantic import BaseModel, Field, EmailStr

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

students = []

@app.post("/students")
def add_student(student: Student):

    # students.append(student)
    student_dict = student.model_dump() # convert student in to a dictionary
    student_dict["id"] = len(students) + 1 # now student.id = length of the student means? +1.
    students.append(student_dict) # now append that student dic
    return {

        "message": "student added successfully"
    }

@app.get("/students", response_model=list[StudentResponse]) #I expect a LIST. Every item inside that list
# should match StudentResponse.


def get_student():

    return students