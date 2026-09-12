import pandas as pd

from intent.classifier import classify_message


INPUT_PATH = "data/processed/verizon_qa_pairs_final.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs_with_intent.csv"


def main():
    print("Loading final QA dataset...")

    df = pd.read_csv(INPUT_PATH)

    print("Rows loaded:", len(df))

    print("Classifying customer messages...")

    df["intent"] = df["customer_message"].apply(classify_message)

    df.to_csv(OUTPUT_PATH, index=False)

    print()
    print("Saved:", OUTPUT_PATH)
    print("Rows:", len(df))

    print("\nIntent distribution:")
    print(df["intent"].value_counts())


if __name__ == "__main__":
    main()