
import requests
import pandas as pd
import time

DATASET = "abisee/cnn_dailymail"
CONFIG = "3.0.0"
SPLIT = "train"

all_rows = []

print("Downloading CNN/DailyMail dataset...")

for offset in range(0, 500, 100):
    url = "https://datasets-server.huggingface.co/rows"

    params = {
        "dataset": DATASET,
        "config": CONFIG,
        "split": SPLIT,
        "offset": offset,
        "length": 100
    }

    response = requests.get(url, params=params, timeout=120)
    response.raise_for_status()

    data = response.json()

    for item in data["rows"]:
        row = item["row"]

        all_rows.append({
            "article": row["article"],
            "highlights": row["highlights"]
        })

    print(f"Downloaded {len(all_rows)} records")
    time.sleep(1)

df = pd.DataFrame(all_rows)

df.to_csv(
    "dataset/cnn_dailymail_sample.csv",
    index=False,
    encoding="utf-8"
)

print("\nDataset downloaded successfully!")
print("Total records:", len(df))
print(df.head())
