from fastapi import FastAPI, HTTPException, Depends # type: ignore
from pydantic import BaseModel # type: ignore
from typing import List, Optional
from datetime import datetime
from motor.motor_asyncio import AsyncIOMotorClient # type: ignore
from bson import ObjectId # type: ignore

app = FastAPI()

# MongoDB connection
MONGO_URI = "mongodb://localhost:27017"
client = AsyncIOMotorClient(MONGO_URI)
db = client.user_db
collection = db.reviews

class ReviewBase(BaseModel):
    name: Optional[str] = "Anonymous"
    review: str
    rating: int
    created_at: datetime = datetime.utcnow()

class ReviewResponse(ReviewBase):
    id: str

@app.post("/reviews/", response_model=ReviewResponse)
async def add_review(review: ReviewBase):
    review_dict = review.dict()
    result = await collection.insert_one(review_dict)
    review_dict["id"] = str(result.inserted_id)
    return review_dict

@app.get("/reviews/", response_model=List[ReviewResponse])
async def get_reviews():
    reviews = await collection.find().to_list(None)
    for review in reviews:
        review["id"] = str(review["_id"])
        del review["_id"]
    return reviews

@app.get("/reviews/{review_id}", response_model=ReviewResponse)
async def get_review_by_id(review_id: str):
    review = await collection.find_one({"_id": ObjectId(review_id)})
    if not review:
        raise HTTPException(status_code=404, detail="Review not found")
    review["id"] = str(review["_id"])
    del review["_id"]
    return review

@app.put("/reviews/{review_id}", response_model=ReviewResponse)
async def update_review(review_id: str, review: ReviewBase):
    result = await collection.find_one_and_update(
        {"_id": ObjectId(review_id)},
        {"$set": review.dict()},
        return_document=True
    )
    if not result:
        raise HTTPException(status_code=404, detail="Review not found")
    result["id"] = str(result["_id"])
    del result["_id"]
    return result

@app.delete("/reviews/{review_id}")
async def delete_review(review_id: str):
    result = await collection.find_one_and_delete({"_id": ObjectId(review_id)})
    if not result:
        raise HTTPException(status_code=404, detail="Review not found")
    return {"message": "success"}
