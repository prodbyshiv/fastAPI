from student_managment_api.database import SessionLocal
from models import StudentDB

db = SessionLocal()
# creates a session to connects to the database

student = StudentDB(
    name="shivam",
    age=21,
    email="shivam@gmail.com",
    cgpa=8.5
)
db.add(student)
db.commit()
#Actually save it permanently

students = db.query(StudentDB).all()

print(students)

students = db.query(StudentDB).all()

for student in students:
    print(
        student.id,
        student.name,
        student.age,
        student.email,
        student.cgpa
    )

    # u crete a blueprint like studentdb
    # when u call it like studentdb() it creates an object of that type.