from fastapi import APIRouter, Body
from app.models.user import User

users_route = APIRouter()

@users_route.get('/')
async def get_user():
    try:
        return {"message": "user data"}
    except Exception as e:
        print(e)

@users_route.post('/')
async def create_user(user: User = Body(...)):
    return user

@users_route.put('/{users_id}')
async def update_item(user_id: int, user: User):
    return {"user_id": user_id, **user.dict()}

@users_route.delete('/{user_id}')
async def delete_user(user_id: int):
    return {"user_id": user_id}