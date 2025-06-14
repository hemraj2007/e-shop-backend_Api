from pydantic import BaseModel
from datetime import datetime
from typing import Optional  # Required for update schema

class CategoryCreate(BaseModel):
    name: str
    created_at: datetime
    updated_at: datetime

class CategoryUpdate(BaseModel):
    name: Optional[str] = None
    created_at: Optional[datetime] = None
    updated_at: Optional[datetime] = None



class CategoryResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
