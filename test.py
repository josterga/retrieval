# test.py
"""
Example usage of the retrieval system from an external module.
This script demonstrates how to load a retriever and perform a query.
"""

import numpy as np
from retrieval.router import get_retriever

def main():
    # Get a retriever instance (configured via config.yaml)
    retriever = get_retriever()

    # Example: Create a random query embedding (replace with your actual embedding)
    # Make sure the dimension matches your FAISS index (e.g., 768)
    embedding_dim = retriever.index.d  # FAISS index dimension
    query_embedding = np.random.rand(embedding_dim).astype("float32")

    # Perform the query
    results = retriever.query(query_embedding)

    # Print the results
    print("Top results:")
    for i, result in enumerate(results, 1):
        print(f"Result {i}:")
        print("  Score:", result["score"])
        print("  Metadata:", result["metadata"])
        print()

if __name__ == "__main__":
    main()