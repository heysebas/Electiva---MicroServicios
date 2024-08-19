from pydantic import BaseModel

class Car(BaseModel):
    id: int
    planeNumber: str
    type: str
    color: str
    cilindraje: str
