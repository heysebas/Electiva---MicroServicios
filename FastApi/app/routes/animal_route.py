from fastapi import APIRouter, Body
from models.animal import Animal
from starlette.exceptions import HTTPException
from database import AnimalModel

animal_route = APIRouter()


@animal_route.get("/animals")
def get_animals():
    animals = list(AnimalModel.select())
    return animals


@animal_route.get("/animals/{animal_id}")
def get_animal(animal_id: int):
    try:
        animal = AnimalModel.get(AnimalModel.id == animal_id)
        return animal
    except AnimalModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@animal_route.post("/animals")
def create_animal(animal: Animal = Body(...)):
    AnimalModel.create(name=animal.name, species=animal.species, age=animal.age, weight=animal.weight)
    return animal


@animal_route.put("/animals/{animal_id}")
def update_animal(animal_id: int, animal_data: dict):
    # Logic to update a animal by ID
    pass


@animal_route.delete("/animals/{animal_id}")
def delete_animal(animal_id: int):
    try:
        animal = AnimalModel.Delete(AnimalModel.id == animal_id)
        return animal

    except AnimalModel.DoesNotExist:
        raise HTTPException(404, "User not found")
