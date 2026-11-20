
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

import pandas as pd
from rouge_score import rouge_scorer
from utils.summarizer import summarize_text

# Load processed dataset
df = pd.read_csv("dataset/processed_cnn_dailymail.csv")

# Select 30 records for evaluation
test_df = df.sample(n=30, random_state=42).reset_index(drop=True)

# Initialize ROUGE evaluator
scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)

results = []

print("Starting BART model evaluation...")

for index, row in test_df.iterrows():

    article = str(row["cleaned_article"])
    reference = str(row["cleaned_summary"])

    generated = summarize_text(article, "Medium")

    scores = scorer.score(reference, generated)

    results.append({
        "rouge1": scores["rouge1"].fmeasure,
        "rouge2": scores["rouge2"].fmeasure,
        "rougeL": scores["rougeL"].fmeasure
    })

    print(f"Evaluated {index + 1}/30")

# Calculate average scores
results_df = pd.DataFrame(results)

print("\n========== BART EVALUATION RESULTS ==========")
print("ROUGE-1:", round(results_df["rouge1"].mean(), 4))
print("ROUGE-2:", round(results_df["rouge2"].mean(), 4))
print("ROUGE-L:", round(results_df["rougeL"].mean(), 4))

# Save results
results_df.to_csv(
    "dataset/rouge_evaluation_results.csv",
    index=False
)

print("\nEvaluation completed successfully!")
