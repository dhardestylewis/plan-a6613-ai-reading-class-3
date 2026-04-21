import re
from collections import Counter

with open('class_13_ai_reading_exercise.tex', 'r', encoding='utf-8') as f:
    text = f.read()

# Strip basic LaTeX commands and environments
text = re.sub(r'\\[a-zA-Z]+(?:\[[^\]]*\])?(?:\{[^\}]*\})?', ' ', text)
# Strip leftover braces and symbols
text = re.sub(r'[\{\}\$]', ' ', text)
# Strip comments
text = re.sub(r'%.*?\n', '\n', text)

words = re.findall(r'\b[a-z]{4,}\b', text.lower())

stopwords = {
    "that", "with", "this", "from", "which", "will", "have", "they", "their", "what", 
    "there", "would", "about", "could", "been", "also", "into", "than", "were", "when", 
    "more", "some", "only", "such", "these", "does", "over"
}

filtered = [w for w in words if w not in stopwords]
counter = Counter(filtered)

print("Top Word Frequencies (Excluding common stopwords and LaTeX commands):")
print("-" * 50)
for word, count in counter.most_common(25):
    print(f"{word:<15}: {count}")
