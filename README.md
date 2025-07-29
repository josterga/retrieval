# Retrieval System

This project implements a retrieval system using FAISS for efficient similarity search over vector embeddings.

## Features

- Vector search using FAISS (supports cosine and L2 metrics)
- Configurable via `config.yaml`
- Metadata support

## Configuration

Edit `config.yaml` to set parameters such as:
- `provider`: Retrieval backend (default: `faiss`)
- `index_path`: Path to the FAISS index file
- `metadata_path`: Path to the metadata JSON file
- `top_k`: Number of top results to return
- `normalize`: Whether to normalize vectors
- `metric`: Similarity metric (`cosine` or `l2`)

Example:
```yaml
retrieval:
  provider: faiss
  index_path: index/faiss.index
  metadata_path: index/metadata.json
  top_k: 5
  normalize: true
  metric: cosine
```

## Usage

Import and use the retriever in your Python code:

```python
from retrieval.faiss_retriever import FaissRetriever

retriever = FaissRetriever(config_path="config.yaml")
results = retriever.query("your query here")
```

## License

MIT License