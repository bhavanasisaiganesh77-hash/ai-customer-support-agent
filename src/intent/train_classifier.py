import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import classification_report, accuracy_score
import joblib

DATA_PATH = "data/hiver_verizon_golden_set_corrected.xlsx"
MODEL_PATH = "data/intent_classifier.joblib"

# Load dataset
df = pd.read_excel(DATA_PATH, sheet_name="golden_set")

# Remove rows without text or intent
df = df[["text", "intent"]].dropna()

X = df["text"].astype(str)
y = df["intent"].astype(str)

print(f"Total examples: {len(df)}")
print(f"Number of intents: {y.nunique()}")

# Show class distribution
print("\nIntent distribution:")
print(y.value_counts())

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

print(f"\nTraining examples: {len(X_train)}")
print(f"Testing examples: {len(X_test)}")

# Improved TF-IDF + Logistic Regression
model = Pipeline([
    (
        "tfidf",
        TfidfVectorizer(
            lowercase=True,
            strip_accents="unicode",
            sublinear_tf=True,
            ngram_range=(1, 2),
            min_df=1,
            max_df=0.95,
            max_features=5000
        )
    ),
    (
        "classifier",
        LogisticRegression(
            max_iter=2000,
            C=2.0,
            class_weight="balanced"
        )
    )
])

print("\nTraining improved model...")
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Evaluation
accuracy = accuracy_score(y_test, y_pred)

print("\n" + "=" * 60)
print("MODEL RESULTS")
print("=" * 60)

print(f"\nAccuracy: {accuracy:.4f}")
print(f"Accuracy percentage: {accuracy * 100:.2f}%")

print("\nClassification Report:")
print(classification_report(
    y_test,
    y_pred,
    zero_division=0
))

# Save model
joblib.dump(model, MODEL_PATH)

print(f"\nModel saved to: {MODEL_PATH}")