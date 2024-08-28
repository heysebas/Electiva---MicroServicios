from fastapi import APIRouter
from app.models.order import Order
from starlette.exceptions import HTTPException
from database import OrderModel

orders_route = APIRouter()

@orders_route.get('/')
async def get_orders():
    try:
        orders = list(OrderModel.select())
        return orders
    except Exception as e:
        print(e)

@orders_route.get("/{order_id}")
def get_order(order_id: int):
    try:
        order = OrderModel.get(OrderModel.id == order_id)
        return order
    except OrderModel.DoesNotExist:
        raise HTTPException(404, "Order not found")

@orders_route.post('/')
async def create_order(order: Order):
    try:
        OrderModel.create(customer_id=order.customer_id, products=order.products, total=order.total)
        return {"message": "pedido creado con éxito"}
    except Exception as e:
        print(e)

@orders_route.put('/{orders_id}')
async def update_item(order_id: int, order: Order):
    return {"order_id": order_id, **order.dict()}

@orders_route.delete('/{order_id}')
async def delete_order(order_id: int):
    try:
        order = OrderModel.Delete(OrderModel.id == order_id)
        return order
    except OrderModel.DoesNotExist:
        raise HTTPException(404, "Order not found")
