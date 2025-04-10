from motor.motor_asyncio import AsyncIOMotorClient # type: ignore

MONGO_URL = "mongodb://localhost:27017/"
DATABASE_NAME ="25_internship_fast"

client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]
role_collection = db["roles"]
user_collection = db["users"]
state_collection = db["states"]
city_collection = db["cities"]  
category_collection = db["categories"]
sub_category_collection = db["sub_categories"]
product_collection = db["products"]
review_collection = db["reviews"]
