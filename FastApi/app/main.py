from fastapi import FastAPI
from starlette.responses import RedirectResponse

#routes
from routes.user import users_route
from routes.product import products_route
from routes.payment import payments_route
from routes.order import orders_route
from routes.category import categories_route

# Base de datos
from database import database as connection
from contextlib import asynccontextmanager


#on startup
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

#on shutdown

#Docs
@app.get('/')
def read_root():
    return RedirectResponse('/docs')

#on routes
app.include_router(users_route, prefix="/users", tags=["users"])
app.include_router(products_route, prefix="/products", tags=["products"])
app.include_router(payments_route, prefix="/payments", tags=["payments"])
app.include_router(orders_route, prefix="/orders", tags=["orders"])
app.include_router(categories_route, prefix="/categories", tags=["categories"])
