from fastapi import APIRouter
from app.models.product import Product
from starlette.exceptions import HTTPException
from database import ProductModel

products_route = APIRouter()

@products_route.get('/')
async def get_products():
    try:
        products = ProductModel.select()
        return [product.dict() for product in products]
    except Exception as e:
        print(e)

@Products_route.get("/{Product_id}")
def get_Product(Product_id: int):
    try:
        product = ProductModel.get(ProductModel.id == product_id)
        return product
    except ProductModel.DoesNotExist:
        raise HTTPException(404, "Product not found")

@products_route.post('/')
async def create_product(product: Product):
    try:
        ProductModel.create(name=product.name, description=product.description, price=product.price)
        return {"message": "producto creado con éxito"}
    except Exception as e:
        print(e)

@products_route.put('/{products_id}')
async def update_product(product_id: int, product: Product):
    return {"product_id": product_id, **product.dict()}

@products_route.delete('/{product_id}')
async def delete_product(product_id: int):
    try:
        product = ProductModel.Delete(ProductModel.id == product_id)
        return product
    except ProductModel.DoesNotExist:
        raise HTTPException(404, "Product not found")
