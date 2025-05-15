from pydantic import BaseModel
from typing import List, Optional

class BookModel(BaseModel):
    id: int
    name : str
    book : str
    class Config:
        orm_mode = True
        from_attributes=True

class UpdateBookModel(BaseModel):
    name : Optional[str]
    book : Optional[str]
    class Config:
        orm_mode = True
        from_attributes=True
