from pydantic import BaseModel


class Library(BaseModel):
    id: int
    name: str
    category: str
    color: str
    author: str