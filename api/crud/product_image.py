from sqlalchemy.orm import Session
from api.database.models.product_image import ProductImage

# ✅ Function to get all product images
def get_all_product_images(db: Session):
    return db.query(ProductImage).all()

# ✅ Function to get images by product_id
def get_images_by_product_id(db: Session, product_id: int):
    return db.query(ProductImage).filter(ProductImage.product_id == product_id).all()

# ✅ Function to create a new product image
def create_product_image(db: Session, image_data):
    new_image = ProductImage(
        product_id=image_data.product_id,
        image=image_data.image
    )
    db.add(new_image)
    db.commit()
    db.refresh(new_image)
    return new_image

# ✅ Function to delete a product image
def delete_product_image(db: Session, image_id: int):
    image = db.query(ProductImage).filter(ProductImage.id == image_id).first()
    if image:
        db.delete(image)
        db.commit()
        return {"message": "Product image deleted successfully"}
    return {"error": "Product image not found"}
