
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/cnn_dailymail_sample.csv")

# Basic information
print("DATASET OVERVIEW")
print("-------------------------")
print("Total records:", len(df))
print("\nMissing values:")
print(df.isnull().sum())

# Remove missing records
df = df.dropna(subset=["article", "highlights"]).copy()

# Calculate word counts
df["article_words"] = df["article"].apply(
    lambda x: len(str(x).split())
)

df["summary_words"] = df["highlights"].apply(
    lambda x: len(str(x).split())
)

print("\nARTICLE STATISTICS")
print(df["article_words"].describe())

print("\nSUMMARY STATISTICS")
print(df["summary_words"].describe())

print("\nAverage article words:",
      round(df["article_words"].mean(), 2))

print("Average summary words:",
      round(df["summary_words"].mean(), 2))

# Visualizations
plt.figure(figsize=(10, 5))
sns.histplot(df["article_words"], bins=30, kde=True)
plt.title("Distribution of Article Lengths")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("dataset/article_length_distribution.png")
plt.show()

plt.figure(figsize=(10, 5))
sns.histplot(df["summary_words"], bins=30, kde=True)
plt.title("Distribution of Summary Lengths")
plt.xlabel("Number of Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("dataset/summary_length_distribution.png")
plt.show()

# Save updated dataset
df.to_csv("dataset/cnn_dailymail_sample.csv", index=False)

print("\nEDA completed successfully!")
