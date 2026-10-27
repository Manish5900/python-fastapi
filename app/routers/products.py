from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.core.database import get_db
from app.crud import product
from app.schemas.product import Product

router = APIRouter(tags=["products"])

@router.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    return product.get_all_products(db)

@router.get("/product/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = product.get_product_by_id(db, id)
    if db_product:
        return db_product
    return {"error": "Product not found"}

@router.post("/product")
def add_product(product: Product, db: Session = Depends(get_db)):
    return product.create_product(db, product.model_dump(exclude={"id"}))

@router.put("/product/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = product.update_product(
        db, id, product.model_dump(exclude={"id"})
    )
    if db_product:
        return "Product updated successfully"
    return {"error": "Product not found"}

@router.delete("/product/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = product.delete_product(db, id)
    if db_product:
        return "Product deleted successfully"
    return {"error": "Product not found"}
