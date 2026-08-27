import pandas as pd

# Load cleaned dataset
df = pd.read_csv("data/processed/jobs_cleaned.csv")

print("=" * 50)
print("JOB MARKET INTELLIGENCE - EDA")
print("=" * 50)

# 1. Total jobs
print("\n📊 TOTAL JOBS")
print(len(df))

# 2. Top job titles
print("\n💼 TOP 15 JOB TITLES")
print(df["title"].value_counts().head(15))

# 3. Top companies
print("\n🏢 TOP 15 COMPANIES")
print(df["companyName"].value_counts().head(15))

# 4. Top locations
print("\n📍 TOP 15 LOCATIONS")
print(df["location"].value_counts().head(15))

# 5. Salary statistics
print("\n💰 SALARY STATISTICS")
print(df["averageSalary"].describe())

# 6. Experience statistics
print("\n🎓 EXPERIENCE STATISTICS")
print(df["averageExperience"].describe())

# 7. Most common skills
print("\n🛠️ TOP SKILLS")

skills = (
    df["tagsAndSkills"]
    .dropna()
    .astype(str)
    .str.lower()
    .str.replace(",", ";")
    .str.split(";")
    .explode()
    .str.strip()
)

skills = skills[skills != ""]

print(skills.value_counts().head(20))

print("\n" + "=" * 50)
print("EDA COMPLETED")
print("=" * 50)