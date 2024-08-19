from pydantic import BaseModel

class Library(BaseModel):
    id: int
    namer: str
    category: str
    color: str
    author: str
