from fastapi import FastAPI
from pydantic import BaseModel

class Book(BaseModel):
    id: int
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

@app.put("/books/{book_id}")

def update_book(book_id: int,update_book: Book):
    
    for index, book in enumerate(books):

        if book.id == book_id:

            book[index] = update_book

            return{
                "message": "book updated"
            }
        
        return{
            "message": "book not found"
        }
    
@app.delete("/books/{book_id}")

def delete_book(book_id: int):

    for index, book in enumerate(books):
        if book.id==book_id:
            books.pop(index)

            return{
                "message": "book deleted"
            }
    
    return{
            "message": "book not found"
        }