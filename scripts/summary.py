import pandas as pd
import os


def load_data():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "complaints_db.csv")

    df = pd.read_csv(file_path)

    return df


def generate_summary(df):

    counts = df["category"].value_counts()

    top_category = counts.idxmax()
    top_count = counts.max()
    total = len(df)

    percentage = (top_count / total) * 100

    # Sample complaints
    samples = df[df["category"] == top_category]["complaint"].head(3)

    print("\n🧠 AI Summary:\n")

    print(f"Out of {total} records, most complaints fall under '{top_category}' category.")
    print(f"This represents approximately {percentage:.2f}% of the data.\n")

    print("Common patterns observed:\n")

    for s in samples:
        print(f"- {s}")

    print("\nOverall Insight:")
    print(f"The dataset is heavily dominated by '{top_category}' related issues.")


def main():

    df = load_data()
    generate_summary(df)


if __name__ == "__main__":
    main()