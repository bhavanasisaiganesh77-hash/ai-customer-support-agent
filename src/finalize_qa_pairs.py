import pandas as pd
import re

INPUT_PATH = "data/processed/verizon_qa_pairs_clean.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs_final.csv"

df = pd.read_csv(INPUT_PATH)

def clean_remaining(text):
    text = str(text)
    text = re.sub(r'(?<!\w)@\d+', '', text)
    text = re.sub(r'\s+', ' ', text).strip()
    return text

df["customer_message"] = df["customer_message"].apply(clean_remaining)
df["support_response"] = df["support_response"].apply(clean_remaining)

before = len(df)

df = df[
    (df["customer_message"] != "") &
    (df["support_response"] != "")
].copy()

df = df.drop_duplicates(
    subset=["customer_message", "support_response"]
).reset_index(drop=True)

df.to_csv(OUTPUT_PATH, index=False)

print("Original cleaned pairs:", before)
print("Final QA pairs:", len(df))
print("Exact duplicates removed:", before - len(df))
print("Empty rows:", ((df["customer_message"] == "") | (df["support_response"] == "")).sum())
print("Remaining @mentions:", df.astype(str).apply(lambda c: c.str.contains(r'@\d+', regex=True)).sum().sum())
print("Saved:", OUTPUT_PATH)
