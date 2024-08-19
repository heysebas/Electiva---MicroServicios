from fastapi import APIRouter, Body
from app.schemas.bank_schema import Bank

bank_route = APIRouter()

@bank_route.post("/")
def create_banks(bank: Bank = Body(...)):
    try:
        return {"bank": bank}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al crear el banco"}

@bank_route.get("/banks/{bank_id}")
def read_bank(bank_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede recuperar el banco"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al recuperar el banco"}

@bank_route.delete("/banks/{bank_id}")
def delete_bank(bank_id: int):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede eliminar el banco"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al eliminar el banco"}

@bank_route.put("/banks/{bank_id}")
def update_bank(bank_id: int, bank: Bank = Body(...)):
    try:
        return {"error": "No se está usando almacenamiento, así que no se puede actualizar el banco"}
    except Exception as e:
        print(e)  # Registrar el error en el log
        return {"error": "Ocurrió un error al actualizar el banco"}
