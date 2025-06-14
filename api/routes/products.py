from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from typing import List, Optional
from api.database.connection import get_db
from api.database.schemas.products import ProductsCreate, ProductsResponse, ProductUpdate
from api.crud.product import (
    create_product,
    delete_product,
    get_all_products,
    get_product_by_id,
    get_products_by_category,
    update_product_by_id,
    get_product_by_id_db  # ✅ NEW import
)

router = APIRouter()

@router.post("/add", response_model=ProductsResponse)
def add(product: ProductsCreate, db: Session = Depends(get_db)):
    return create_product(db, product)

@router.get("/all_products", response_model=List[ProductsResponse])
def list_products(
    product_cat: Optional[str] = Query(None),
    db: Session = Depends(get_db)
):
    if product_cat:
        return get_products_by_category(db, product_cat)
    return get_all_products(db)


@router.get("/get_product/{slug}", response_model=ProductsResponse)
def get_single_product(slug: str, db: Session = Depends(get_db)):
    return get_product_by_id(db, slug)

@router.delete("/delete/{product_id}", response_model=dict)
def delete(product_id: int, db: Session = Depends(get_db)):
    return delete_product(db, product_id)


@router.put("/products/update/{product_id}", response_model=ProductsResponse)
def update_product(product_id: int, updated_data: ProductUpdate, db: Session = Depends(get_db)):
    product = update_product_by_id(db, product_id, updated_data)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

# ✅ ✅ ✅ NEW: Get product by product ID (not slug)
@router.get("/by-id/{product_id}", response_model=ProductsResponse)
def get_product_by_id_route(product_id: int, db: Session = Depends(get_db)):
    product = get_product_by_id_db(db, product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
