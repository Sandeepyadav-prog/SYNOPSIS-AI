
import pandas as pd
import re

# Load dataset
df = pd.read_csv("dataset/cnn_dailymail_sample.csv")

# Handle missing values
df = df.dropna(subset=["article", "highlights"]).copy()

# Text cleaning function
def clean_text(text):
    text = str(text)
    text = re.sub(r"\s+", " ", text)
    text = text.strip()
    return text

# Clean article and summary
df["cleaned_article"] = df["article"].apply(clean_text)
df["cleaned_summary"] = df["highlights"].apply(clean_text)

# Remove empty records
df = df[
    (df["cleaned_article"].str.len() > 0) &
    (df["cleaned_summary"].str.len() > 0)
].copy()

# Save processed dataset
df.to_csv(
    "dataset/processed_cnn_dailymail.csv",
    index=False,
    encoding="utf-8"
)

print("TEXT PREPROCESSING COMPLETED!")
print("Total processed records:", len(df))

print("\nOriginal article:")
print(df["article"].iloc[0][:300])

print("\nCleaned article:")
print(df["cleaned_article"].iloc[0][:300])

print("\nCleaned summary:")
print(df["cleaned_summary"].iloc[0][:300])
