from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.database.schemas.contact import ContactCreate, ContactOut
from api.crud import contact as contact_crud
from api.database.connection import get_db
from typing import List

# Create a new router instance
router = APIRouter()

# POST endpoint to create a new contact
@router.post("/contacts", response_model=ContactOut)
def create_contact(contact: ContactCreate, db: Session = Depends(get_db)):
    return contact_crud.create_contact(db, contact)

# GET endpoint to fetch all contacts
@router.get("/contacts", response_model=List[ContactOut])
def get_all_contacts(db: Session = Depends(get_db)):
    return contact_crud.get_all_contacts(db)