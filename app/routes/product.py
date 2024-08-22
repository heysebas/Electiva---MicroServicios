from fastapi import APIRouter
from app.models.product import Product

products_route = APIRouter()

@products_route.get('/')
async def get_products():
    try:
        return {"message": "lista de productos"}
    except Exception as e:
        print(e)

@products_route.post('/')
async def create_product(product: Product):
    try:
        return {"message": "producto creado con éxito"}
    except Exception as e:
        print(e)

@products_route.put('/{products_id}')
async def update_product(product_id: int, product: Product):
    return {"product_id": product_id, **product.dict()}

@products_route.delete('/{product_id}')
async def delete_product(product_id: int):
    return {"product_id": product_id}