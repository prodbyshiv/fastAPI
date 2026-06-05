from fastapi import FastAPI
from pydantic import BaseModel

class User(BaseModel):

    name: str
    age: int

app = FastAPI() # this create the web application

@app.get("/")
def home():
    return {"message": "Hello FastAPI"}


@app.get("/about")
def about():
    return {"Name": "Shivam"}

@app.get("/skills")
def skills():
    return {
        "skills": ["Python", "DSA", "FastAPI"]
    }

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return{
        "user_id": user_id
    }

@app.get("/students/{name}/{marks}")
def student(name: str,marks: int):
    return{
        "name": name,
        "marks": marks
    }

@app.get("/search")
def search(name: str):

    return {
        "name": name
    }

@app.get("/profile/{name}")
def profile(name: str):
    return{
        "name": name
    }

@app.get("/square/{number}")
def profile(number: int):
    return{
        "square": number*number
    }

@app.get("/greet")
def profile(name: str):
    return{
        "greet": f"hello {name}"
    }

@app.post("/create")
def create():

    return {
        "message": "User created"
    }