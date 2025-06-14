from sqlalchemy.orm import Session
from api.database.models.contact import Contact
from api.database.schemas.contact import ContactCreate

def create_contact(db: Session, contact_data: ContactCreate):
    new_contact = Contact(
        name=contact_data.name,
        email=contact_data.email,
        message=contact_data.message
    )
    db.add(new_contact)
    db.commit()
    db.refresh(new_contact)
    return new_contact

def get_all_contacts(db: Session):
    return db.query(Contact).order_by(Contact.created_at.desc()).all()