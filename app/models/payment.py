from pydantic import BaseModel

class Payment(BaseModel):
    id: int
    order_id: int
    payment_method: str
    amount: float