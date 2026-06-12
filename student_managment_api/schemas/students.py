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
