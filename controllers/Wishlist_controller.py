from fastapi import APIRouter, HTTPException, Depends
from bson import ObjectId
from models.user import users_collection
from models.product import products_collection
from schemas.user import user_helper
from routes.auth import get_current_user  # Assuming authentication middleware

wishlist_router = APIRouter()

@wishlist_router.post("/add_to_wishlist/{product_id}")
async def add_to_wishlist(product_id: str, current_user: dict = Depends(get_current_user)):
    user_id = current_user["id"]
    
    user = users_collection.find_one({"_id": ObjectId(user_id)})
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    product = products_collection.find_one({"_id": ObjectId(product_id)})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    
    if product_id in user.get("wishlist", []):
        raise HTTPException(status_code=400, detail="Product already in wishlist")
    
    users_collection.update_one(
        {"_id": ObjectId(user_id)},
        {"$push": {"wishlist": product_id}}
    )
    
    return {"message": "Product added to wishlist"}
