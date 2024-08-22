from fastapi import APIRouter
from app.models.order import Order

orders_route = APIRouter()

@orders_route.get('/')
async def get_orders():
    try:
        return {"message": "lista de pedidos"}
    except Exception as e:
        print(e)

@orders_route.post('/')
async def create_order(order: Order):
    try:
        return {"message": "pedido creado con éxito"}
    except Exception as e:
        print(e)

@orders_route.put('/{orders_id}')
async def update_item(order_id: int, order: Order):
    return {"order_id": order_id, **order.dict()}

@orders_route.delete('/{order_id}')
async def delete_order(order_id: int):
    return {"order_id": order_id}