from fastapi import FastAPI
from starlette.responses import RedirectResponse

#routes
from routes.user import users_route
from routes.product import products_route
from routes.payment import payments_route
from routes.order import orders_route
from routes.category import categories_route

app = FastAPI()


#on startup
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
