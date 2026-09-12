import pandas as pd
import re

INPUT_PATH = "data/processed/verizon_qa_pairs.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs_clean.csv"

df = pd.read_csv(INPUT_PATH)

def clean_text(text):
    text = str(text)

    # Remove URLs
    text = re.sub(r"https?://\S+|www\.\S+", "", text)

    # Remove @mentions
    text = re.sub(r"@\w+", "", text)

    # Remove common Twitter caret/signature markers
    text = re.sub(r"\^[A-Za-z]+", "", text)

    # Normalize whitespace
    text = re.sub(r"\s+", " ", text).strip()

    return text

df["customer_message"] = df["customer_message"].apply(clean_text)
df["support_response"] = df["support_response"].apply(clean_text)

# Remove empty rows after cleaning
df = df[
    (df["customer_message"].str.len() > 0)
    & (df["support_response"].str.len() > 0)
]

# Remove exact duplicate pairs
df = df.drop_duplicates()

df.to_csv(OUTPUT_PATH, index=False)

print("Cleaned QA pairs:", len(df))
print("Saved:", OUTPUT_PATH)
print()
print(df.head(5).to_string(index=False))
