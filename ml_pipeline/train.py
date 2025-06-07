import mlflow
from mlflow import log_metric, log_param, log_artifacts
from mlflow.models.signature import infer_signature
from sentence_transformers import SentenceTransformer
import torch
from recommender.sbert_recommender import SBERTRecommender

def train():
    mlflow.set_experiment("LumousLearn-SBERT-Recommender")

    with mlflow.start_run():
        model_name = 'all-MiniLM-L6-v2'
        mlflow.log_param("model_name", model_name)

        # Load SBERT model
        model = SentenceTransformer(model_name)

        # Initialize recommender
        recommender = SBERTRecommender(model_name=model_name)

        # Dummy metric: average similarity score for user profile example
        user_profile = "I know Python and SQL and want to become a machine learning engineer."
        recommendations = recommender.recommend(user_profile, top_k=3)
        avg_score = sum([r['score'] for r in recommendations]) / len(recommendations)

        mlflow.log_metric("avg_recommendation_score", avg_score)

        # Log model - here, just save the SentenceTransformer model locally and log it
        model_save_path = "sbert_model"
        model.save(model_save_path)
        mlflow.log_artifacts(model_save_path, artifact_path="model")

        print(f"Logged SBERT model and metrics with avg score: {avg_score:.4f}")

if __name__ == "__main__":
    train()
