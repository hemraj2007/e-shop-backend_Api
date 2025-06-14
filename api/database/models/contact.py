from sqlalchemy import Column, Integer, String, DateTime
from api.database.base import Base
from datetime import datetime

class Contact(Base):
    __tablename__ = "contacts"  # 👈 Yeh line missing thi

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    message = Column(String(500), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
