from pydantic import BaseModel

class Bank(BaseModel):
    id: int
    number: str
    user: str
    balance: float
    type: str
