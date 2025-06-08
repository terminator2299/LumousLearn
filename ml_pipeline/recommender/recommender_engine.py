from sentence_transformers import SentenceTransformer, util
import torch

class LearningPathRecommender:
    def __init__(self, model_name='sentence-transformers/all-MiniLM-L6-v2'):
        self.model = SentenceTransformer(model_name)

        # Dummy content database
        self.resources = [
            {"topic": "Linear Regression", "desc": "Basic linear models", "url": "https://..."},
            {"topic": "Neural Networks", "desc": "Intro to neural nets", "url": "https://..."},
            {"topic": "SQL Joins", "desc": "Deep dive into joins", "url": "https://..."}
        ]

        self.corpus = [r["topic"] + " - " + r["desc"] for r in self.resources]
        self.corpus_embeddings = self.model.encode(self.corpus, convert_to_tensor=True)

    def recommend(self, user_input: str, top_k=2):
        query_embedding = self.model.encode(user_input, convert_to_tensor=True)
        scores = util.pytorch_cos_sim(query_embedding, self.corpus_embeddings)[0]
        top_results = torch.topk(scores, k=top_k)

        recommendations = []
        for idx in top_results[1]:
            rec = self.resources[idx]
            recommendations.append(rec)
        return recommendations
