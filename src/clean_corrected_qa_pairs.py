import pandas as pd
import re

INPUT_PATH = "data/processed/verizon_qa_pairs_corrected.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs_clean.csv"

df = pd.read_csv(INPUT_PATH)

def clean_text(text):
    text = str(text)

    # Remove Twitter mentions only when they are clearly @username tokens
    text = re.sub(r'(?<!\w)@\d{3,}', '', text)

    # Remove agent signatures such as ^DFM, ^TXA
    text = re.sub(r'\^[A-Za-z]{2,5}\b', '', text)

    # Convert escaped newlines to spaces
    text = text.replace("\\n", " ")

    # Normalize repeated whitespace
    text = re.sub(r'\s+', ' ', text).strip()

    return text

df["customer_message"] = df["customer_message"].apply(clean_text)
df["support_response"] = df["support_response"].apply(clean_text)

# Remove rows that became empty
df = df[
    (df["customer_message"].str.strip() != "") &
    (df["support_response"].str.strip() != "")
].copy()

df.to_csv(OUTPUT_PATH, index=False)

print("Clean QA pairs:", len(df))
print("Saved:", OUTPUT_PATH)
print()
print("First 5 pairs:")
for i, row in df.head(5).iterrows():
    print(f"\nPAIR {i + 1}")
    print("CUSTOMER:", repr(row["customer_message"]))
    print("SUPPORT:", repr(row["support_response"]))
