from fastapi import APIRouter, Body
from app.schemas.animal_schema import Animal

animal_route = APIRouter()

@animal_route.post("/")
def create_animals(animal: Animal = Body(...)):
    try:
        return {"animal": animal}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al crear el animal"}

@animal_route.get("/animals/{animal_id}")
def read_animal(animal_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede recuperar el animal"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al recuperar el animal"}

@animal_route.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede eliminar el animal"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al eliminar el animal"}

@animal_route.put("/animals/{animal_id}")
def update_animal(animal_id: int, animal: Animal = Body(...)):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede actualizar el animal"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al actualizar el animal"}
