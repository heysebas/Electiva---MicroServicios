from fastapi import APIRouter
from app.models.category import Category
from starlette.exceptions import HTTPException
from database import CategoryModel

categories_route = APIRouter()

@categories_route.get('/')
async def get_categories():
    try:
        categories = list(CategoryModel.select())
        return categories
    except Exception as e:
        print(e)


@categories_route.get("/{category_id}")
def get_category(category_id: int):
    try:
        category = CategoryModel.get(CategoryModel.id == category_id)
        return category
    except CategoryModel.DoesNotExist:
        raise HTTPException(404, "Category not found")

@categories_route.post('/')
async def create_category(category: Category):
    try:
        CategoryModel.create(name=category.name, species=category.species, age=category.age, weight=category.weight)
        return category
    except Exception as e:
        print(e)

@categories_route.put('/{categories_id}')
async def update_category(category_id: int, category: Category):
    return {"category_id": category_id, **category.dict()}

@categories_route.delete('/{category_id}')
async def delete_category(category_id: int):
      try:
        category = CategoryModel.Delete(CategoryModel.id == category_id)
        return category
    except CategoryModel.DoesNotExist:
        raise HTTPException(404, "Category not found")