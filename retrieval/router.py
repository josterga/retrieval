import yaml
from .faiss_retriever import FAISSRetriever

def load_retrieval_config(path="config.yaml"):
    with open(path, "r") as f:
        config = yaml.safe_load(f)
    return config["retrieval"]

def get_retriever():
    config = load_retrieval_config()
    if config["provider"] == "faiss":
        return FAISSRetriever(config)
    else:
        raise ValueError(f"Unsupported retriever: {config['provider']}")
