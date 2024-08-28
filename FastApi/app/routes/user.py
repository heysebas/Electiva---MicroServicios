from fastapi import APIRouter, Body
from models.user import User
from database import UserModel
from peewee import DoesNotExist
from starlette.exceptions import HTTPException

user_route = APIRouter()


@user_route.get("/")
def get_users():
    # Usar un método de clase para obtener todos los usuarios
    users = list(UserModel.select())
    return users


@user_route.get("/{user_id}")
def get_user(user_id: int):
    try:
        user = UserModel.get(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@user_route.post("/")
def create_user(user: User = Body(...)):
    UserModel.create(username=user.username, email=user.email, password=user.password)
    return user


@user_route.put("/{user_id}")
def update_user(user_id: int, user_data: dict):
    # Logic to update a user by ID
    pass


@user_route.delete("/{user_id}")
def delete_user(user_id: int):
    try:
        user = UserModel.Delete(UserModel.id == user_id)
        return user
    except UserModel.DoesNotExist:
        raise HTTPException(404, "User not found")