from fastapi import APIRouter
from app.models.payment import Payment

payments_route = APIRouter()

@payments_route.get('/')
async def get_payments():
    try:
        return {"message": "lista de pagos"}
    except Exception as e:
        print(e)

@payments_route.post('/')
async def create_payment(payment: Payment):
    try:
        return {"message": "pago creado con éxito"}
    except Exception as e:
        print(e)


@payments_route.put('/{payment_id}')
async def update_payment(payment_id: int, payment: Payment):
    return {"payment_id": payment_id, **payment.dict()}

@payments_route.delete('/{payment_id}')
async def delete_payment(payment_id: int):
    return {"payment_id": payment_id}