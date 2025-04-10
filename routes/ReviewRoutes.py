from fastapi import APIRouter, HTTPException
from typing import List
from models.ReviewModel import Review, ReviewBase  # Fixed import

router = APIRouter()

@router.post("/reviews/", response_model=Review)  # Updated path
async def add_review(review: ReviewBase):
    new_review = Review(**review.dict())
    await new_review.insert()
    return new_review

@router.get("/reviews/", response_model=List[Review])  # Updated path
async def get_reviews():
    return await Review.find_all().to_list()

@router.get("/reviews/{id}", response_model=Review)  # Updated path
async def get_review_by_id(id: str):
    review = await Review.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    return review

@router.put("/reviews/{id}", response_model=Review)  # Updated path
async def update_review(id: str, review: ReviewBase):
    existing_review = await Review.get(id)
    if not existing_review:
        raise HTTPException(status_code=404, detail="Review not found")
    await existing_review.update({"$set": review.dict()})  # Fixed update syntax
    return existing_review

@router.delete("/reviews/{id}")  # Updated path
async def delete_review(id: str):
    review = await Review.get(id)
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    await review.delete()
    return {"message": "success"}
