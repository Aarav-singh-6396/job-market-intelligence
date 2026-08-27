import pandas as pd
from pathlib import Path

# -----------------------------
# 1. Load raw dataset
# -----------------------------
input_file = Path("data/raw/indian-job-market-dataset.xlsx")
output_file = Path("data/processed/jobs_cleaned.csv")

df = pd.read_excel(input_file)

print("Original dataset:", df.shape)

# -----------------------------
# 2. Remove duplicate jobs
# -----------------------------
df = df.drop_duplicates(subset="jobId")

# -----------------------------
# 3. Clean text columns
# -----------------------------
text_columns = [
    "title",
    "companyName",
    "tagsAndSkills",
    "experience",
    "location",
    "jobDescription"
]

for col in text_columns:
    df[col] = df[col].fillna("Unknown").astype(str).str.strip()

# -----------------------------
# 4. Clean numeric columns
# -----------------------------
numeric_columns = [
    "jobId",
    "companyId",
    "ReviewsCount",
    "AggregateRating",
    "minimumSalary",
    "maximumSalary",
    "minimumExperience",
    "maximumExperience"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

# -----------------------------
# 5. Clean date column
# -----------------------------
df["jobUploaded"] = pd.to_datetime(
    df["jobUploaded"],
    errors="coerce"
)

# -----------------------------
# 6. Create useful salary column
# -----------------------------
df["averageSalary"] = (
    df["minimumSalary"] + df["maximumSalary"]
) / 2

# -----------------------------
# 7. Create useful experience column
# -----------------------------
df["averageExperience"] = (
    df["minimumExperience"] + df["maximumExperience"]
) / 2

# -----------------------------
# 8. Save cleaned dataset
# -----------------------------
output_file.parent.mkdir(parents=True, exist_ok=True)

df.to_csv(output_file, index=False)

# -----------------------------
# 9. Final report
# -----------------------------
print("\nCleaning completed!")
print("Final dataset:", df.shape)
print("Saved to:", output_file)

print("\nMissing values:")
print(df.isnull().sum().sort_values(ascending=False).head(10))