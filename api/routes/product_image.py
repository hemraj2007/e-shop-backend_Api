from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from api.database.connection import get_db
import api.crud as crud
from api.database.schemas.product_image import ProductImageCreate, ProductImageResponse

router = APIRouter()

# ✅ 1. Get All Product Images
@router.get("/product_images", response_model=List[ProductImageResponse])
def list_product_images(db: Session = Depends(get_db)):
    return crud.get_all_product_images(db)

# ✅ 2. Get Product Images by Product ID
@router.get("/product_images/{product_id}", response_model=List[ProductImageResponse])
def get_images(product_id: int, db: Session = Depends(get_db)):
    return crud.get_images_by_product_id(db, product_id)

# ✅ 3. Add a New Product Image
@router.post("/product_images", response_model=ProductImageResponse)
def add_image(image_data: ProductImageCreate, db: Session = Depends(get_db)):
    return crud.create_product_image(db, image_data)  # ✅ Corrected Function Call

# ✅ 4. Delete Product Image
@router.delete("/product_images/{image_id}")
def remove_image(image_id: int, db: Session = Depends(get_db)):
    return crud.delete_product_image(db, image_id)
