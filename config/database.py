from motor.motor_asyncio import AsyncIOMotorClient  # type: ignore
import os

# Retrieve environment variables with defaults if they're not set
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017/")
DATABASE_NAME = os.getenv("DATABASE_NAME", "25_internship_fast")

# Initialize the Motor client and create the database reference
client = AsyncIOMotorClient(MONGO_URL)
db = client[DATABASE_NAME]

# Define your collections
role_collection = db["roles"]
user_collection = db["users"]
state_collection = db["states"]
city_collection = db["cities"]
category_collection = db["categories"]
sub_category_collection = db["sub_categories"]
product_collection = db["products"]
review_collection = db["reviews"]
