import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from utils.summarizer import summarize_text

article = """
Artificial Intelligence has become an important part of modern
technology. It is transforming industries such as healthcare,
education, banking and transportation. Machine learning enables
computers to learn from data and make predictions. Deep learning
uses artificial neural networks to solve complex problems.
Natural Language Processing allows computers to understand,
interpret and generate human language. AI-powered applications
are increasingly helping businesses improve efficiency,
automate tasks and make better decisions.
"""

print("\n========== SHORT SUMMARY ==========")
print(summarize_text(article, "Short"))

print("\n========== MEDIUM SUMMARY ==========")
print(summarize_text(article, "Medium"))

print("\n========== LONG SUMMARY ==========")
print(summarize_text(article, "Long"))

print("\nAll summarization tests completed!")
