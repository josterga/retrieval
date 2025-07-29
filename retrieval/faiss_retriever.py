import faiss
import json
import numpy as np
from .base import BaseRetriever
from .utils import normalize_embeddings

class FAISSRetriever(BaseRetriever):
    def __init__(self, config):
        self.index_path = config["index_path"]
        self.metadata_path = config["metadata_path"]
        self.top_k = config.get("top_k", 5)
        self.metric = config.get("metric", "cosine")
        self.normalize = config.get("normalize", True)

        self.index = faiss.read_index(self.index_path)
        with open(self.metadata_path) as f:
            self.metadata = json.load(f)

    def query(self, query_embedding, top_k=None):
        top_k = top_k or self.top_k
        q = np.array([query_embedding]).astype("float32")
        if self.normalize:
            q = normalize_embeddings(q)
        distances, indices = self.index.search(q, top_k)

        results = []
        for i, idx in enumerate(indices[0]):
            if idx < 0 or idx >= len(self.metadata):
                continue
            result = {
                "score": float(distances[0][i]),
                "metadata": self.metadata[idx]
            }
            results.append(result)
        return results
