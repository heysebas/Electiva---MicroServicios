from fastapi import APIRouter, Body
from models.car import Car
from starlette.exceptions import HTTPException
from database import CarModel

car_route = APIRouter()


@car_route.get("/cars")
def get_cars():
    cars = list(CarModel.select())
    return cars


@car_route.get("/cars/{car_id}")
def get_car(car_id: int):
    try:
        car = CarModel.get(CarModel.id == car_id)
        return car
    except CarModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@car_route.post("/cars")
def create_car(car: Car = Body(...)):
    CarModel.create(planeNumber=car.planeNumber, type=car.type, color=car.color, cilindraje=car.cilindraje)
    return car

@car_route.put("/cars/{library_id}")
def update_car(car_id: int, car_data: dict):
    # Logic to update a user by ID
    pass


@car_route.delete("/cars/{car_id}")
def delete_car(car_id: int):
    try:
        car = CarModel.Delete(CarModel.id == car_id)
        return car

    except CarModel.DoesNotExist:
        raise HTTPException(404, "User not found")
