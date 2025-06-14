from sqlalchemy import Column, Integer, String, Enum, Date
from api.database.base import Base
import enum

# Enum for discount_type
class DiscountTypeEnum(str, enum.Enum):
    percentage = "percentage"
    fixed = "fixed"

# Enum for status
class StatusEnum(str, enum.Enum):
    yes = "yes"
    no = "no"

class Promocode(Base):
    __tablename__ = "promocodes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, nullable=False)
    description = Column(String(255), nullable=True)
    discount_type = Column(Enum(DiscountTypeEnum), nullable=False)
    discount_value = Column(Integer, nullable=False)
    expiry_date = Column(Date, nullable=False)
    status = Column(Enum(StatusEnum), default="yes")
