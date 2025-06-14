from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.schemas import wishlist as wishlist_schema
from api.crud import wishlist as wishlist_crud

router = APIRouter(prefix="/wishlist", tags=["Wishlist"])

@router.post("/add", response_model=wishlist_schema.WishlistResponse)
def add_wishlist(wishlist: wishlist_schema.WishlistCreate, db: Session = Depends(get_db)):
    return wishlist_crud.create_wishlist(db, wishlist)

@router.get("/all", response_model=list[wishlist_schema.WishlistResponse])
def get_wishlist(db: Session = Depends(get_db)):
    return wishlist_crud.get_all_wishlist(db)

@router.get("/get/{user_id}", response_model=list[wishlist_schema.Wishlist])
def get_wishlist(user_id: int, db: Session = Depends(get_db)):
    return wishlist_crud.get_user_wishlist(db, user_id)

@router.delete("/delete/{wishlist_id}", response_model=wishlist_schema.WishlistResponse)
def delete_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    deleted_item = wishlist_crud.delete_wishlist(db, wishlist_id)
    if not deleted_item:
        raise HTTPException(status_code=404, detail="Wishlist item not found")
    return deleted_item

