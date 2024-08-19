from fastapi import APIRouter, Body
from app.schemas.library_schema import Library

library_route = APIRouter()

@library_route.post("/")
def create_cars(library: Library = Body(...)):
    try:
        return {"library": library}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al crear la Biblioteca"}

@library_route.get("/libraries/{library_id}")
def read_car(library_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede recuperar la biblioteca"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al recuperar la biblioteca"}

@library_route.delete("/libraries/{library_id}")
def delete_car(library_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede eliminar la biblioteca"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al eliminar la biblioteca"}

@library_route.put("/libraries/{library_id}")
def update_car(library_id: int, library: Library = Body(...)):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede actualizar La biblioteca"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al actualizar el Biblioteca"}
