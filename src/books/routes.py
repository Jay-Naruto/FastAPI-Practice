from fastapi import APIRouter, status, Depends
from typing import Optional, List
from src.books.models import BookModel, UpdateBookModel
from fastapi.exceptions import HTTPException
from src.db.main import session_local, BookDB
from sqlalchemy.orm import Session
from src.parser.parse import hl7_parse

book_router = APIRouter()

def get_db():
    db = session_local()
    try:
        yield db
    finally:
        db.close()

@book_router.get("/", response_model=List[BookModel])
async def get_books(db: Session=Depends(get_db)):
    books = db.query(BookDB).all()
    return [BookModel.from_orm(book) for book in books]

@book_router.get("/{book_id}", response_model=BookModel)
async def get_book_by_id(book_id: int,db: Session=Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")
    return BookModel.from_orm(book)

@book_router.post("/create_book", response_model=BookModel)
async def create_book_endpoint(book_data: BookModel, db: Session=Depends(get_db)):
    new_book = BookDB(
        id= book_data.id,
        name=book_data.name,
        book=book_data.book
    )
    db.add(new_book)
    db.commit()
    db.refresh(new_book)

    return BookModel.from_orm(new_book)

@book_router.patch("/{book_id}", response_model=BookModel)
async def update_book_by_id(book_id: int, book_data: UpdateBookModel,  db: Session=Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")

    if book_data.name:
        book.name = book_data.name
    if book_data.book:
        book.book = book_data.book

    db.commit()
    db.refresh(book)
    return BookModel.from_orm(book)


@book_router.delete("/{book_id}", response_model=BookModel)
async def delete_book_by_id(book_id: int, db: Session=Depends(get_db)):
    book = db.query(BookDB).filter(BookDB.id == book_id).first()
    if book is None:
        raise HTTPException(status_code = status.HTTP_404_NOT_FOUND, detail = "Book not found")
    
    db.delete(book)
    db.commit()

    return BookModel.from_orm(book)

@book_router.get("/parse/hl7")
async def hl7_endpoint():
    result = hl7_parse()
    return result
    