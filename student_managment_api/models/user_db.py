from sqlalchemy import Column, Integer, String
from student_managment_api.database import Base

class UserDB(Base):

    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    username = Column(String)

    email = Column(String)

    password = Column(String)