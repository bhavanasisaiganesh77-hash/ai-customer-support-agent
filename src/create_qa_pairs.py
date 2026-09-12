import pandas as pd

INPUT_PATH = "data/processed/verizon_conversations.csv"
OUTPUT_PATH = "data/processed/verizon_qa_pairs.csv"

df = pd.read_csv(INPUT_PATH)

support = df[df["inbound"] == False].copy()

support["tweet_id"] = support["tweet_id"].astype(str)

support_lookup = dict(
    zip(
        support["tweet_id"],
        support["text"].fillna("")
    )
)

customer = df[df["inbound"] == True].copy()

def get_response(response_ids):
    responses = []

    for response_id in str(response_ids).split(","):
        response_id = response_id.strip()

        if response_id in support_lookup:
            responses.append(support_lookup[response_id])

    return " ".join(responses)

customer["response"] = customer["response_tweet_id"].apply(get_response)

qa = customer[["text", "response"]].copy()

qa.columns = ["customer_message", "support_response"]

qa = qa[
    (qa["customer_message"].str.strip() != "")
    & (qa["support_response"].str.strip() != "")
]

qa = qa.drop_duplicates()

qa.to_csv(OUTPUT_PATH, index=False)

print("Customer-support pairs:", len(qa))
print("Saved:", OUTPUT_PATH)
print()
print(qa.head(5).to_string(index=False))
