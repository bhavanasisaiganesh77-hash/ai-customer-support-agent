import pandas as pd

file_path = "data/raw/twcs.csv"
output_path = "data/processed/verizon_conversations.csv"

print("Loading dataset...")

df = pd.read_csv(file_path)

print("Total dataset rows:", len(df))

# VerizonSupport tweets
support = df[
    df["author_id"].astype(str).str.lower() == "verizonsupport"
].copy()

support_ids = set(support["tweet_id"].astype(str))

print("VerizonSupport tweets:", len(support))

# Customer tweets whose response_tweet_id points to VerizonSupport
customer = df[
    (df["inbound"] == True) &
    df["response_tweet_id"].fillna("").astype(str).apply(
        lambda x: any(
            tweet_id.strip() in support_ids
            for tweet_id in x.split(",")
            if tweet_id.strip()
        )
    )
].copy()

print("Customer messages connected to VerizonSupport:", len(customer))

# Combine both sides
result = pd.concat(
    [customer, support],
    ignore_index=True
)

result = result.drop_duplicates(subset=["tweet_id"])

result["created_at"] = pd.to_datetime(
    result["created_at"],
    format="mixed"
)

result = result.sort_values("created_at")

result.to_csv(output_path, index=False)

print("\nSaved:", output_path)
print("Final rows:", len(result))
print(
    "Customer messages:",
    (result["inbound"] == True).sum()
)
print(
    "VerizonSupport messages:",
    (result["author_id"].astype(str).str.lower() == "verizonsupport").sum()
)