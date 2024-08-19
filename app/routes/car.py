from fastapi import APIRouter, Body
from app.schemas.car_schema import Car

car_route = APIRouter()

@car_route.post("/")
def create_cars(car: Car = Body(...)):
    try:
        return {"car": car}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al crear el carro"}

@car_route.get("/cars/{car_id}")
def read_car(car_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede recuperar el carro"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al recuperar el carro"}

@car_route.delete("/cars/{car_id}")
def delete_car(car_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede eliminar el carro"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al eliminar el carro"}

@car_route.put("/cars/{car_id}")
def update_car(car_id: int, car: Car = Body(...)):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede actualizar el carro"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al actualizar el carro"}
