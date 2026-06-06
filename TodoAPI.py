from fastapi import FastAPI
from pydantic import BaseModel

class Task(BaseModel):

    title:str

app = FastAPI()
tasks = []


@app.post("/tasks")
def add_task(task:Task):
    tasks.append(task)

    return {
        "message": "Task Added"
    }

@app.get("/tasks")
def get_tasks():

    return tasks

