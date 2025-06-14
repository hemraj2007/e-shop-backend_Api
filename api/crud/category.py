from sqlalchemy.orm import Session
from api.database.models.categories import Categories
from api.database.schemas.categories import CategoryCreate, CategoryUpdate
from datetime import datetime

def create_category(db: Session, category: CategoryCreate):
    db_category = Categories(
        name=category.name,
        created_at=category.created_at,
        updated_at=category.updated_at
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)
    return db_category

def delete_category(db: Session, category_id: int):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if category:
        db.delete(category)
        db.commit()
        return {"success": True, "message": "Category deleted successfully"}
    return {"success": False, "message": "Category not found"}

def get_all_category(db: Session):
    return db.query(Categories).all()

def update_category(db: Session, category_id: int, category_data: CategoryUpdate):
    category = db.query(Categories).filter(Categories.id == category_id).first()
    if not category:
        return {"success": False, "message": "Category not found"}

    if category_data.name is not None:
        category.name = category_data.name
    if category_data.created_at is not None:
        category.created_at = category_data.created_at
    category.updated_at = category_data.updated_at or datetime.utcnow()

    db.commit()
    db.refresh(category)
    return {"success": True, "message": "Category updated successfully"}
