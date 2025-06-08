from fastapi import APIRouter
from pydantic import BaseModel
from ml_pipeline.recommender.recommender_engine import LearningPathRecommender

# Initialize the router
recommend_router = APIRouter()

# Instantiate the recommendation engine
recommender = LearningPathRecommender()

# Define the expected input schema
class UserProfile(BaseModel):
    input_text: str  # User's current skill, interest, or goal

# POST endpoint for getting recommendations
@recommend_router.post("/recommend")
def recommend_path(user: UserProfile):
    recommendations = recommender.recommend(user.input_text)
    return {"input": user.input_text, "recommendations": recommendations}
