import numpy as np

# Convert CSV string → vector
def str_to_vector(s):
    return np.array(list(map(float, s.split(","))))



# Convert vector → CSV string
def vector_to_str(vector):
    return ",".join(map(str, vector))


# Cosine similarity calculation
def cosine_similarity(vec1, vec2):
    return np.dot(vec1, vec2) / (
        np.linalg.norm(vec1) * np.linalg.norm(vec2)
    )