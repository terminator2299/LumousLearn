from fastapi import FastAPI
from api.routes import recommend_router

app = FastAPI(title="LumousLearn - Learning Path Recommender")

app.include_router(recommend_router, prefix="/api")
