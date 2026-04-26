from sentence_transformers import SentenceTransformer
import pandas as pd
import os

from scripts.utils import str_to_vector, cosine_similarity


def load_data():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "complaints_db.csv")

    df = pd.read_csv(file_path)

    df["embedding"] = df["embedding"].apply(str_to_vector)

    return df


def search(query, model, df, top_k=5, category=None):

    query_embedding = model.encode(query)

    results = []

    for _, row in df.iterrows():

        # Apply category filter if given
        if category and row["category"] != category:
            continue

        text = row["complaint"]
        embedding = row["embedding"]

        similarity = cosine_similarity(query_embedding, embedding)

        results.append((text, row["category"], float(similarity)))

    results.sort(key=lambda x: x[2], reverse=True)

    return results[:top_k]


def run_search():

    print("\nLoading search system...")

    model = SentenceTransformer("all-MiniLM-L6-v2")
    df = load_data()

    query = input("\nEnter your query: ")

    category = input("Filter by category (or press Enter to skip): ")

    top_k = input("How many results? (default 5): ")

    # Handle inputs
    if category == "":
        category = None

    if top_k == "":
        top_k = 5
    else:
        top_k = int(top_k)

    results = search(query, model, df, top_k=top_k, category=category)

    print("\n🔍 Results:\n")

    for i, (text, cat, score) in enumerate(results, 1):
        print(f"{i}. {text}")
        print(f"   Category: {cat}")
        print(f"   Score: {score:.4f}\n")