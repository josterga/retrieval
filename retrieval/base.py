class BaseRetriever:
    def index(self, embeddings: list[list[float]], metadata: list[dict]):
        raise NotImplementedError

    def query(self, query_embedding: list[float], top_k=5) -> list[dict]:
        raise NotImplementedError
