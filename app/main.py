from fastapi import FastAPI
from starlette.responses import RedirectResponse
from app.routes.user import user_route  # Asegúrate de que esta importación es correcta
from app.routes.car import car_route
from app.routes.animal import animal_route
from app.routes.bank import bank_route
from app.routes.library import library_route

app = FastAPI()

@app.get("/")
async def root():
    return RedirectResponse(url="/docs")

app.include_router(user_route, prefix="/users", tags=["users"])
app.include_router(car_route, prefix="/cars", tags=["cars"])
app.include_router(animal_route, prefix="/animals", tags=["animals"])
app.include_router(bank_route, prefix="/banks",     tags=["banks"])
app.include_router(library_route, prefix="/libraries", tags=["libraries"])