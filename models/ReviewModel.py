from beanie import Document
from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime

class Review(Document):
    name: Optional[str] = "Anonymous"
    review: str = Field(..., min_length=1)
    rating: int = Field(..., ge=1, le=5)
    created_at: datetime = Field(default_factory=datetime.utcnow)

    class Settings:
        name = "reviews"  # Fixed collection name setting

class ReviewBase(BaseModel):
    name: Optional[str] = "Anonymous"
    review: str
    rating: int
