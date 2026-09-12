import pandas as pd

DATA_PATH = "data/hiver_verizon_golden_set_corrected.xlsx"

df = pd.read_excel(DATA_PATH, sheet_name="golden_set")

print("=" * 70)
print("INTENT EXAMPLES")
print("=" * 70)

for intent in sorted(df["intent"].unique()):
    examples = df[df["intent"] == intent]

    print(f"\n{'=' * 70}")
    print(f"INTENT: {intent}")
    print(f"EXAMPLES: {len(examples)}")
    print("=" * 70)

    for i, text in enumerate(examples["text"].tolist(), 1):
        print(f"{i}. {text}")