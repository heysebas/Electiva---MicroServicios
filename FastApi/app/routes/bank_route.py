from fastapi import APIRouter, Body
from models.bank import Bank
from starlette.exceptions import HTTPException
from database import BankModel

bank_route = APIRouter()





@bank_route.get("/banks")
def get_bannks():
    banks = list(BankModel.select())
    return banks


@bank_route.get("/banks/{bank_id}")
def get_bank(bank_id: int):
    try:
        bank = BankModel.get(BankModel.id == bank_id)
        return bank
    except BankModel.DoesNotExist:
        raise HTTPException(404, "User not found")


@bank_route.post("/banks")
def create_bank(bank: Bank = Body(...)):
    BankModel.create(number=bank.number, user=bank.user, balance=bank.balance, type=bank.type)
    return bank


@bank_route.put("/banks/{bank_id}")
def update_bank(bank_id: int, bank_data: dict):
    # Logic to update a bank by ID
    pass


@bank_route.delete("/banks/{bank_id}")
def delete_bank(bank_id: int):
    try:
        bank = BankModel.Delete(BankModel.id == bank_id)
        return bank

    except BankModel.DoesNotExist:
        raise HTTPException(404, "User not found")