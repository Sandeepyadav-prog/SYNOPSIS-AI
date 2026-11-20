
import torch
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

MODEL_NAME = "sshleifer/distilbart-cnn-12-6"

print("Loading BART tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

print("Loading BART model...")
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)

model.eval()


def summarize_text(text, length="Medium"):

    if not text or not text.strip():
        return "Please enter some text to summarize."

    length_settings = {
        "Short": {"min_length": 25, "max_length": 60},
        "Medium": {"min_length": 50, "max_length": 120},
        "Long": {"min_length": 80, "max_length": 180}
    }

    settings = length_settings.get(
        length, length_settings["Medium"]
    )

    inputs = tokenizer(
        text,
        return_tensors="pt",
        max_length=1024,
        truncation=True
    )

    with torch.no_grad():
        summary_ids = model.generate(
            inputs["input_ids"],
            attention_mask=inputs["attention_mask"],
            max_length=settings["max_length"],
            min_length=settings["min_length"],
            num_beams=4,
            early_stopping=True
        )

    summary = tokenizer.decode(
        summary_ids[0],
        skip_special_tokens=True
    )

    return summary
