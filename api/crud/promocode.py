from sqlalchemy.orm import Session
from api.database.models.promocode import Promocode
from api.database.schemas.promocode import PromocodeCreate

# ➕ Create Promocode
def create_promocode(db: Session, promocode_data: PromocodeCreate):
    promocode = Promocode(**promocode_data.dict())
    db.add(promocode)
    db.commit()
    db.refresh(promocode)
    return promocode

# 📥 Get All Promocodes
def get_all_promocodes(db: Session):
    return db.query(Promocode).all()

# ❌ Delete Promocode by ID
def delete_promocode_by_id(db: Session, promocode_id: int):
    promocode = db.query(Promocode).filter(Promocode.id == promocode_id).first()
    if promocode:
        db.delete(promocode)
        db.commit()
    return promocode
