from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from api.database.connection import get_db
from api.database.models.promocode import Promocode
from api.database.schemas.promocode import PromocodeCreate, PromocodeOut

router = APIRouter(
    prefix="/promocode",
    tags=["Promocode"]
)

# ➕ Create Promocode
@router.post("/add", response_model=PromocodeOut)
def create_promocode(promocode: PromocodeCreate, db: Session = Depends(get_db)):
    db_promocode = Promocode(**promocode.dict())
    db.add(db_promocode)
    db.commit()
    db.refresh(db_promocode)
    return db_promocode

# 📥 Get All Promocodes
@router.get("/all", response_model=list[PromocodeOut])
def get_all_promocodes(db: Session = Depends(get_db)):
    return db.query(Promocode).all()

# 🗑 Delete Promocode by ID
@router.delete("/delete/{id}")
def delete_promocode(id: int, db: Session = Depends(get_db)):
    promocode = db.query(Promocode).filter(Promocode.id == id).first()
    if not promocode:
        raise HTTPException(status_code=404, detail="Promocode not found")
    db.delete(promocode)
    db.commit()
    return {"message": "Promocode deleted successfully"}
