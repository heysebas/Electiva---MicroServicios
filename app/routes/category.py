from fastapi import APIRouter
from app.models.category import Category

categories_route = APIRouter()

@categories_route.get('/')
async def get_categories():
    try:
        return {"message": "lista de categorías"}
    except Exception as e:
        print(e)

@categories_route.post('/')
async def create_category(category: Category):
    try:
        # Aquí puedes agregar la lógica para crear una nueva categoría
        return {"message": "categoría creada con éxito"}
    except Exception as e:
        print(e)

@categories_route.put('/{categories_id}')
async def update_category(category_id: int, category: Category):
    return {"category_id": category_id, **category.dict()}

@categories_route.delete('/{category_id}')
async def delete_category(category_id: int):
    return {"category_id": category_id}