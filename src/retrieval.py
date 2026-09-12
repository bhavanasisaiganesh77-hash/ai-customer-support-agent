import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from src.intent.classifier import classify_message


DATA_PATH = "data/processed/verizon_qa_pairs_with_intent.csv"


class SupportRetriever:

    def __init__(self, data_path=DATA_PATH):

        self.df = pd.read_csv(data_path)

        self.df["customer_message"] = (
            self.df["customer_message"]
            .fillna("")
            .astype(str)
        )

        self.df["support_response"] = (
            self.df["support_response"]
            .fillna("")
            .astype(str)
        )

        self.df["intent"] = (
            self.df["intent"]
            .fillna("")
            .astype(str)
        )

        self.vectorizer = TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.95
        )

        self.customer_vectors = self.vectorizer.fit_transform(
            self.df["customer_message"]
        )

    def search(self, query, top_k=5):

        predicted_intent = classify_message(query)

        intent_mask = self.df["intent"] == predicted_intent

        candidate_indices = self.df.index[intent_mask].tolist()

        if not candidate_indices:
            candidate_indices = self.df.index.tolist()

        candidate_vectors = self.customer_vectors[candidate_indices]

        query_vector = self.vectorizer.transform([query])

        scores = cosine_similarity(
            query_vector,
            candidate_vectors
        ).flatten()

        top_count = min(top_k, len(candidate_indices))

        top_positions = scores.argsort()[::-1][:top_count]

        results = []

        for position in top_positions:

            original_index = candidate_indices[position]

            results.append({
                "customer_message": self.df.iloc[original_index]["customer_message"],
                "support_response": self.df.iloc[original_index]["support_response"],
                "intent": self.df.iloc[original_index]["intent"],
                "score": float(scores[position])
            })

        return pd.DataFrame(results)


if __name__ == "__main__":

    retriever = SupportRetriever()

    query = input("Customer message: ")

    predicted_intent = classify_message(query)

    print(f"\nDetected intent: {predicted_intent}")

    results = retriever.search(query, top_k=5)

    print("\nTop matching support responses:\n")

    for _, row in results.iterrows():

        print(f"Score: {row['score']:.4f}")
        print(f"Intent: {row['intent']}")
        print(f"Customer: {row['customer_message']}")
        print(f"Support: {row['support_response']}")
        print("-" * 60)
