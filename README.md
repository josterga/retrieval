# `retrieval` — FAISS-based Vector Retrieval

- **Description:**  
  Vector search over embeddings using FAISS, with metadata support.
- **Entrypoint:**  
  `from retrieval.faiss_retriever import FaissRetriever`
- **Configurable Arguments:**
  - `config_path`: Path to YAML config.
  - Or pass config dict directly (see below).

- **Configurable Options (YAML):**
  - `provider`, `index_path`, `metadata_path`, `top_k`, `normalize`, `metric`

- **Example:**
  ```python
  from retrieval.faiss_retriever import FaissRetriever
  retriever = FaissRetriever(config_path="config.yaml")
  results = retriever.query("your query here")
  ```

  - **Cache-Friendly:**
```from retrieval.faiss_retriever import FaissRetriever
import faiss, json

# Load once
index = faiss.read_index("data/index.faiss")
with open("data/metadata.json") as f:
    metadata = json.load(f)

# Reuse across retrievers
retriever = FaissRetriever.from_loaded(index=index, metadata=metadata, config=config)
results = retriever.query(query_embedding)
```