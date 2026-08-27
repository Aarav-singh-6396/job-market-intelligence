import pandas as pd
from pathlib import Path

data_folder = Path("data/raw")

excel_files = list(data_folder.glob("*.xlsx"))

if not excel_files:
    print("❌ Excel file nahi mili!")
else:
    file = excel_files[0]
    print(f"✅ Dataset found: {file.name}")

    df = pd.read_excel(file)

    print("\n--- DATASET SHAPE ---")
    print(df.shape)

    print("\n--- COLUMNS ---")
    print(df.columns.tolist())

    print("\n--- FIRST 5 ROWS ---")
    print(df.head())

    print("\n--- MISSING VALUES ---")
    print(df.isnull().sum())