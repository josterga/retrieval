import numpy as np

def normalize_embeddings(arr):
    norms = np.linalg.norm(arr, axis=1, keepdims=True)
    return arr / (norms + 1e-10)
