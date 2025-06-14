from pydantic import BaseModel
from typing import Optional
from datetime import date
import enum

# Enums same jaise model me
class DiscountTypeEnum(str, enum.Enum):
    percentage = "percentage"
    fixed = "fixed"

class StatusEnum(str, enum.Enum):
    yes = "yes"
    no = "no"

# Base schema
class PromocodeBase(BaseModel):
    name: str
    description: Optional[str] = None
    discount_type: DiscountTypeEnum
    discount_value: int
    expiry_date: date
    status: StatusEnum

# For create
class PromocodeCreate(PromocodeBase):
    pass

# For response
class PromocodeOut(PromocodeBase):
    id: int

    class Config:
        from_attributes = True
