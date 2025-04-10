from beanie import init_beanie
from .database import client
from models.ReviewModel import Review

async def init_db():
    document_models = [Review]
    await init_beanie(database=client['25_internship_fast'], document_models=document_models)
    print("Database initialized successfully")