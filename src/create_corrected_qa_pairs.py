import pandas as pd

INPUT_PATH = "data/processed/verizon_conversations.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs_corrected.csv"

df = pd.read_csv(INPUT_PATH)

# Normalize IDs
df["tweet_id"] = df["tweet_id"].astype(str)
df["response_tweet_id"] = (
    df["response_tweet_id"]
    .fillna("")
    .astype(str)
    .str.replace(r"\.0$", "", regex=True)
)

df["in_response_to_tweet_id"] = (
    df["in_response_to_tweet_id"]
    .fillna("")
    .astype(str)
    .str.replace(r"\.0$", "", regex=True)
)

# Customer messages
customers = df[df["inbound"] == True][
    ["tweet_id", "text", "response_tweet_id"]
].copy()

# VerizonSupport messages
support = df[df["inbound"] == False][
    ["tweet_id", "text", "in_response_to_tweet_id"]
].copy()

# Keep ONLY direct two-way relationships:
# customer.response_tweet_id == support.tweet_id
# AND support.in_response_to_tweet_id == customer.tweet_id
pairs = customers.merge(
    support,
    left_on=["tweet_id", "response_tweet_id"],
    right_on=["in_response_to_tweet_id", "tweet_id"],
    how="inner",
    suffixes=("_customer", "_support")
)

qa = pairs[["text_customer", "text_support"]].copy()
qa.columns = ["customer_message", "support_response"]

# Remove empty messages and exact duplicates
qa["customer_message"] = qa["customer_message"].fillna("").astype(str).str.strip()
qa["support_response"] = qa["support_response"].fillna("").astype(str).str.strip()

qa = qa[
    (qa["customer_message"] != "") &
    (qa["support_response"] != "")
]

qa = qa.drop_duplicates()

qa.to_csv(OUTPUT_PATH, index=False)

print("Corrected QA pairs:", len(qa))
print("Saved:", OUTPUT_PATH)
print()
print("First 5 pairs:")
print(qa.head(5).to_string(index=False))
