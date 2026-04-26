from sentence_transformers import SentenceTransformer
import pandas as pd
import os

from scripts.utils import vector_to_str


def main():

    model = SentenceTransformer("all-MiniLM-L6-v2")

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    input_path = os.path.join(BASE_DIR, "data", "complaints_db.csv")

    df = pd.read_csv(input_path)

    texts = df["review"].tolist()

    embeddings = model.encode(texts)

    embedding_strings = [vector_to_str(e) for e in embeddings]

    vector_df = pd.DataFrame({
        "complaint": texts,
        "embedding": embedding_strings
    })

    vector_df.to_csv(input_path, index=False)

    print("Vector DB created.")


if __name__ == "__main__":
    main()