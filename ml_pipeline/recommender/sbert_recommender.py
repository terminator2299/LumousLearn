from sentence_transformers import SentenceTransformer, util
import torch

class SBERTRecommender:
    def __init__(self, model_name='all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)
        # Predefined topics and descriptions (example)
        self.topics = [
            {"topic": "Data Structures", "desc": "Learn about arrays, lists, trees, graphs."},
            {"topic": "Machine Learning", "desc": "Supervised and unsupervised learning basics."},
            {"topic": "Model Deployment", "desc": "Deploy ML models using Docker and APIs."},
            {"topic": "Python Programming", "desc": "Python fundamentals and advanced topics."},
            {"topic": "Databases", "desc": "SQL and NoSQL databases concepts."}
        ]
        # Precompute embeddings for topics
        self.topic_embeddings = self.model.encode([t['desc'] for t in self.topics], convert_to_tensor=True)

    def recommend(self, user_profile_desc, top_k=3):
        # Encode user profile description
        user_embedding = self.model.encode(user_profile_desc, convert_to_tensor=True)
        # Compute cosine similarity
        cos_scores = util.cos_sim(user_embedding, self.topic_embeddings)[0]
        # Get top k topic indices
        top_results = torch.topk(cos_scores, k=top_k)
        recommendations = []
        for score, idx in zip(top_results.values, top_results.indices):
            recommendations.append({
                "topic": self.topics[idx]['topic'],
                "score": float(score)
            })
        return recommendations
