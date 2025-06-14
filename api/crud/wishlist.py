from sqlalchemy.orm import Session
from api.database.models.wishlist import Wishlist
from api.database.schemas import wishlist as wishlist_schema

def create_wishlist(db: Session, wishlist: wishlist_schema.WishlistCreate):
    db_wishlist = Wishlist(**wishlist.dict())
    db.add(db_wishlist)
    db.commit()
    db.refresh(db_wishlist)
    return db_wishlist

def get_all_wishlist(db: Session):
    return db.query(Wishlist).all()

def get_user_wishlist(db: Session, user_id: int):
    return db.query(Wishlist).filter(Wishlist.user_id == user_id).all()


def delete_wishlist(db: Session, wishlist_id: int):
    wishlist_item = db.query(Wishlist).filter(Wishlist.id == wishlist_id).first()
    if not wishlist_item:
        return None
    db.delete(wishlist_item)
    db.commit()
    return wishlist_item
