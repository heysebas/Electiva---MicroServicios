from fastapi import FastAPI
from starlette.responses import RedirectResponse

from routes.bank_route import bank_route
from routes.library_route import library_route
from routes.car_route import car_route

from routes.animal_route import animal_route
# Base de datos
from database import database as connection
from routes.user_route import user_route
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Conectar a la base de datos si la conexión está cerrada
    if connection.is_closed():
        connection.connect()
    try:
        yield  # Aquí es donde se ejecutará la aplicación
    finally:
        # Cerrar la conexión cuando la aplicación se detenga
        if not connection.is_closed():
            connection.close()


app = FastAPI(lifespan=lifespan)


@app.get("/")
def read_root():
    return RedirectResponse(url="/docs")


app.include_router(user_route, prefix="/api/users", tags=["users"])
app.include_router(library_route, prefix="/api/librarys", tags=["librarys"])
app.include_router(car_route, prefix="/api/cars", tags=["cars"])
app.include_router(bank_route, prefix="/api/banks", tags=["banks"])
app.include_router(animal_route, prefix="/api/animals", tags=["animals"])
