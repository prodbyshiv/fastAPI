from fastapi import FastAPI
from student_managment_api.routers.student import router
from student_managment_api.routers.user import router as user_router

app = FastAPI()

app.include_router(router)

app.include_router(user_router)
