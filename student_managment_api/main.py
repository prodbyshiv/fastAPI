from fastapi import FastAPI
from student_managment_api.routers.student import router

app = FastAPI()

app.include_router(router)

