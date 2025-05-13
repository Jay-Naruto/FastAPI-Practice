from fastapi import APIRouter, status
from typing import Optional, List
from src.books.models import BookModel, UpdateBookModel
from fastapi.exceptions import HTTPException

book_router = APIRouter()
books =[
   { "id": 1,
    "name":"Jay1",
    "book":"Book 1"},
       { "id": 2,
    "name":"Jay2",
    "book":"Book 2"},
       { "id": 3,
    "name":"Jay3",
    "book":"Book 3"},
       { "id": 4,
    "name":"Jay4",
    "book":"Book 4"}
]


@book_router.get("/", response_model=List[BookModel])
async def get_books():
    return books

@book_router.get("/{book_id}", response_model=BookModel)
async def get_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")

@book_router.post("/create_book", response_model=List[BookModel])
async def create_book_endpoint(book_data: BookModel):
    books.append(book_data.dict())
    return books

@book_router.patch("/{book_id}", response_model=BookModel)
async def update_book_by_id(book_id: int, book_data: UpdateBookModel):
    for book in books:
        if book['id'] == book_id:
            if book_data.name is not None:
                book['name'] = book_data.name
            if book_data.book is not None:
                book['book'] = book_data.book
            return book

    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")

@book_router.delete("/{book_id}", response_model=BookModel)
async def delete_book_by_id(book_id: int):
    for book in books:
        if book['id'] == book_id:
            books.remove(book)
            return book
    raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")
    