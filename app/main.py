from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.database import engine, session
from app.crud.product import seed_products
from app.models.product import Base
from app.routers import products

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)

app.include_router(products.router)

INITIAL_PRODUCTS = [
    {"id": 1, "name": "Product 1", "description": "Description", "price": 10.99, "quantity": 100},
    {"id": 2, "name": "Product 2", "description": "Description for Product 2", "price": 20.99, "quantity": 50},
    {"id": 3, "name": "Product 3", "description": "Description for Product 3", "price": 30.99, "quantity": 25},
]


def init_db():
    db = session()
    try:
        seed_products(db, INITIAL_PRODUCTS)
    finally:
        db.close()


init_db()


@app.get("/")
def greet():
    return "API server is running..."
