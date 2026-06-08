from fastapi import APIRouter
from models.book import Book

router = APIRouter()

books = []

@router.post("/books")
def add_book(book: Book):

    books.append(book)

    return {
        "message": "Book Added"
    }


@router.get("/books")
def get_books():

    return books