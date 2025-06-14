from sqlalchemy.orm import Session
from api.database.models.products import Products
from api.database.schemas.products import ProductsCreate, ProductUpdate
from datetime import datetime


# ✅ Create Product
def create_product(db: Session, product: ProductsCreate):
    created_at = product.created_at or datetime.utcnow()

    db_product = Products(
        category_id=product.category_id,
        name=product.name,
        slug=product.slug,
        description=product.description,
        mrp=product.mrp,
        net_price=product.net_price,
        quantity_in_stock=product.quantity_in_stock,
        image=product.image,
        product_cat=product.product_cat,
        created_at=product.created_at,
        updated_at=product.updated_at,
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product


# ✅ Delete Product by Slug
def delete_product(db: Session, product_id: int):
    product = db.query(Products).filter(Products.id == product_id).first()  # slug ko id se replace kar diya
    if product:
        db.delete(product)
        db.commit()
        return {"success": True, "message": "Product deleted successfully"}
    return {"success": False, "message": "Product not found"}



# ✅ Get All Products
def get_all_products(db: Session):
    return db.query(Products).all()


# ✅ Get Product by Slug
def get_product_by_id(db: Session, slug: str):
    return db.query(Products).filter(Products.slug == slug).first()


# ✅ Get Product by Category
def get_products_by_category(db: Session, product_cat: str):
    return db.query(Products).filter(Products.product_cat == product_cat).all()

# ✅ Update product by ID
def update_product_by_id(db: Session, product_id: int, updated_data: ProductUpdate):
    product = db.query(Products).filter(Products.id == product_id).first()
    if not product:
        return None

    for key, value in updated_data.dict(exclude_unset=True).items():
        setattr(product, key, value)

    product.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(product)
    return product


# ✅ Get Product by ID (numeric ID)
def get_product_by_id_db(db: Session, product_id: int):
    return db.query(Products).filter(Products.id == product_id).first()
