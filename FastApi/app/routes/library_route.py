from fastapi import APIRouter, Body
from models.library import Library
from starlette.exceptions import HTTPException
from database import LibraryModel

library_route = APIRouter()


@library_route.get("/librarys")
def get_librarys():
    librarys = list(LibraryModel.select())
    return librarys


@library_route.get("/librarys/{library_id}")
def get_library(library_id: int):
    try:
        library = LibraryModel.get(LibraryModel.id == library_id)
        return library
    except LibraryModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@library_route.post("/librarys")
def create_library(library: Library = Body(...)):
    LibraryModel.create(name=library.name, category=library.category, color=library.color, author=library.author)
    return library


@library_route.put("/librarys/{library_id}")
def update_library(library_id: int, library_data: dict):
    # Logic to update a user by ID
    pass


@library_route.delete("/librarys/{library_id}")
def delete_library(library_id: int):
    try:
        library = LibraryModel.Delete(LibraryModel.id == library_id)
        return library

    except LibraryModel.DoesNotExist:
        raise HTTPException(404, "User not found")
