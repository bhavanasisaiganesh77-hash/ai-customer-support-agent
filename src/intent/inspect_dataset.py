import pandas as pd

file_path = "data/hiver_verizon_golden_set_corrected.xlsx"

print("Starting dataset inspection...")

excel_file = pd.ExcelFile(file_path)

print("\nAvailable sheets:")
print(excel_file.sheet_names)

df = pd.read_excel(file_path, sheet_name="golden_set")

print("\nDataset shape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nFirst 5 rows:")
print(df.head())

print("\nIntent distribution:")
print(df["intent"].value_counts())

print("\nMissing values:")
print(df.isnull().sum())

print("\nInspection completed.")