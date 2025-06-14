from pydantic import BaseModel
from datetime import datetime

# Schema to create a wishlist entry
class WishlistCreate(BaseModel):
    user_id: int
    product_id: int

    class Config:
        from_attributes = True

# Schema for the response when fetching the wishlist
class WishlistResponse(BaseModel):
    id: int
    user_id: int
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True


class Wishlist(BaseModel):
    id: int
    user_id: int
    product_id: int
    created_at: datetime

    class Config:
        from_attributes = True