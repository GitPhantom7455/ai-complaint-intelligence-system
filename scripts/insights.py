import pandas as pd
import os


def load_data():

    BASE_DIR = os.path.dirname(os.path.dirname(__file__))
    file_path = os.path.join(BASE_DIR, "data", "complaints_db.csv")

    df = pd.read_csv(file_path)

    return df


def category_distribution(df):

    print("\n📊 Category Distribution:\n")

    counts = df["category"].value_counts()

    for category, count in counts.items():
        print(f"{category}: {count}")


def sample_per_category(df):

    print("\n📌 Sample Complaints per Category:\n")

    grouped = df.groupby("category")

    for category, group in grouped:

        print(f"\n--- {category.upper()} ---")

        samples = group["complaint"].head(2)

        for s in samples:
            print(f"- {s}")


def main():

    df = load_data()

    category_distribution(df)
    sample_per_category(df)


if __name__ == "__main__":
    main()