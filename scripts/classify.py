from sentence_transformers import SentenceTransformer, util
import pandas as pd
import os


def main():

    model = SentenceTransformer("all-MiniLM-L6-v2")

    labels = ["motivation", "love", "life", "sadness", "inspiration"]
    label_embeddings = model.encode(labels)

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "complaints_db.csv")

    df = pd.read_csv(file_path)

    predicted_labels = []

    for text in df["complaint"]:

        text_embedding = model.encode(text)

        scores = util.cos_sim(text_embedding, label_embeddings)[0]

        best_label_index = scores.argmax()
        best_label = labels[best_label_index]

        predicted_labels.append(best_label)

    df["category"] = predicted_labels

    df.to_csv(file_path, index=False)

    print("Classification completed.")


if __name__ == "__main__":
    main()