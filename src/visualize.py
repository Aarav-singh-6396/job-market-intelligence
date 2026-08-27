import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

# Load cleaned data
df = pd.read_csv("data/processed/jobs_cleaned.csv")

# Create charts folder
Path("data/charts").mkdir(parents=True, exist_ok=True)

# -----------------------------
# 1. Top Job Titles
# -----------------------------
top_jobs = df["title"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_jobs.sort_values().plot(kind="barh")
plt.title("Top 10 Job Titles")
plt.xlabel("Number of Jobs")
plt.tight_layout()
plt.savefig("data/charts/top_job_titles.png")
plt.close()

# -----------------------------
# 2. Top Locations
# -----------------------------
top_locations = df["location"].value_counts().head(10)

plt.figure(figsize=(10, 6))
top_locations.sort_values().plot(kind="barh")
plt.title("Top 10 Job Locations")
plt.xlabel("Number of Jobs")
plt.tight_layout()
plt.savefig("data/charts/top_locations.png")
plt.close()

# -----------------------------
# 3. Salary Distribution
# -----------------------------
salary_data = df["averageSalary"].dropna()

plt.figure(figsize=(10, 6))
sns.histplot(salary_data, bins=30)
plt.title("Salary Distribution")
plt.xlabel("Average Salary")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("data/charts/salary_distribution.png")
plt.close()

# -----------------------------
# 4. Experience Distribution
# -----------------------------
experience_data = df["averageExperience"].dropna()

plt.figure(figsize=(10, 6))
sns.histplot(experience_data, bins=20)
plt.title("Experience Distribution")
plt.xlabel("Average Experience")
plt.ylabel("Number of Jobs")
plt.tight_layout()
plt.savefig("data/charts/experience_distribution.png")
plt.close()

print("✅ VISUALIZATION COMPLETED")
print("Charts saved in: data/charts/")