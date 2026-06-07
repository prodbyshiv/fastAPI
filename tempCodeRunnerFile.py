from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    title: str
    author: str
    page: int

app = FastAPI()

books = []

@app.post("/books")
def add_book(book: Book):

    books.append(book)

    return {
        "message": "book added successfully"
    }

@app.get("/books")
def get_books():

    return books