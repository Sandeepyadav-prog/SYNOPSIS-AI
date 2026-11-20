
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

print("Loading BART tokenizer...")

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading BART model...")

model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model.eval()

print("BART model loaded successfully!")

text = """
Artificial Intelligence is transforming the modern world.
It is used in healthcare, education, transportation and
business. Machine learning allows computers to learn from
data and make predictions. Deep learning uses neural
networks to solve complex problems. Natural Language
Processing helps computers understand human language.
"""

inputs = tokenizer(
    text,
    return_tensors="pt",
    max_length=1024,
    truncation=True
)

with torch.no_grad():
    summary_ids = model.generate(
        inputs["input_ids"],
        max_length=80,
        min_length=25,
        num_beams=4,
        early_stopping=True
    )

summary = tokenizer.decode(
    summary_ids[0],
    skip_special_tokens=True
)

print("\nORIGINAL TEXT:")
print(text)

print("\nGENERATED SUMMARY:")
print(summary)
