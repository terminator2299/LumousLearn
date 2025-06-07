from sbert_recommender import SBERTRecommender

if __name__ == "__main__":
    recommender = SBERTRecommender()
    user_profile = "I know Python and SQL and want to become a machine learning engineer."
    recs = recommender.recommend(user_profile)
    for r in recs:
        print(f"Topic: {r['topic']}, Score: {r['score']:.4f}")
