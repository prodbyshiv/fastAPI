from sqlalchemy import Column, Integer, String, Float
from student_managment_api.database import Base

class StudentDB(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    email = Column(String)
    cgpa = Column(Float)