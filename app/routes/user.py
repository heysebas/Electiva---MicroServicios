from fastapi import APIRouter, Body
from app.schemas.user_schema import User

user_route = APIRouter()

@user_route.post("/")
def create_users(user: User = Body(...)):
    try:
        return {"user": user}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al crear el usuario"}

@user_route.get("/users/{user_id}")
def read_user(user_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede recuperar el usuario"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al recuperar el usuario"}

@user_route.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede eliminar el usuario"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al eliminar el usuario"}

@user_route.put("/users/{user_id}")
def update_user(user_id: int, user: User = Body(...)):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede actualizar el usuario"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al actualizar el usuario"}
