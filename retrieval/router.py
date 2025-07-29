import yaml
import os
from .faiss_retriever import FAISSRetriever

def load_retrieval_config(path="config.yaml"):
    if os.path.exists(path):
        with open(path, "r") as f:
            config = yaml.safe_load(f)
        return config.get("retrieval", {})
    else:
        return {}

def get_retriever(config: dict = None, **kwargs):
    # Load config from file if not provided
    file_config = load_retrieval_config()
    config = config or {}
    # Merge: kwargs > config > file_config
    merged_config = {**file_config, **config, **kwargs}
    if merged_config.get("provider", "faiss") == "faiss":
        return FAISSRetriever(merged_config)
    else:
        raise ValueError(f"Unsupported retriever: {merged_config.get('provider')}")