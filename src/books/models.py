from pydantic import BaseModel
from typing import List, Optional

class BookModel(BaseModel):
    id: int
    name : str
    book : str

class UpdateBookModel(BaseModel):
    name : Optional[str]
    book : Optional[str]
