from sqlalchemy.orm import Session

from app.models.product import Product


def get_all_products(db: Session):
    return db.query(Product).all()


def get_product_by_id(db: Session, id: int):
    return db.query(Product).filter(Product.id == id).first()


def create_product(db: Session, product_data: dict):
    db_product = Product(**product_data)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


def update_product(db: Session, id: int, product_data: dict):
    db_product = get_product_by_id(db, id)
    if not db_product:
        return None
    for key, value in product_data.items():
        setattr(db_product, key, value)
    db.commit()
    return db_product


def delete_product(db: Session, id: int):
    db_product = get_product_by_id(db, id)
    if not db_product:
        return None
    db.delete(db_product)
    db.commit()
    return db_product


def count_products(db: Session):
    return db.query(Product).count()


def seed_products(db: Session, products: list):
    if count_products(db) == 0:
        for product in products:
            db.add(Product(**product))
        db.commit()
