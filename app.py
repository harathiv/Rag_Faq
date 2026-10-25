
import json
from pathlib import Path

import ollama
from minsearch import Index

# 1. Configuration
MODEL = "llama3.2:3b"  # Change to your installed model name
DATA_FILE = Path("data/faqs.json")


# 2. Load the cleaned FAQ dataset
if not DATA_FILE.exists():
    raise FileNotFoundError(
        "data/faqs.json not found. "
        "Run the notebook steps to extract and save FAQs first."
    )

with DATA_FILE.open("r", encoding="utf-8") as f:
    documents = json.load(f)

if not documents:
    raise ValueError("The FAQ dataset is empty.")

print(f"Loaded {len(documents)} FAQ documents.")


# 3. Build the search index
index = Index(text_fields=["question", "answer"])
index.fit(documents)

print("FAQ search index is ready.")


# 4. Retrieve context and generate an answer
def ask_faq(question, top_k=3):
    results = index.search(question, num_results=top_k)

    if not results:
        return "I couldn't find a relevant FAQ."

    context = "\n\n".join(
        f"Question: {doc['question']}\n"
        f"Answer: {doc['answer']}"
        for doc in results
    )

    response = ollama.chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": (
                    "Answer the user using only the supplied FAQ context. "
                    "If the context doesn't answer the question, say so. "
                    "Do not invent facts."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"FAQ context:\n{context}\n\n"
                    f"Question: {question}"
                ),
            },
        ],
    )

    return response.message.content


# 5. Interactive question-and-answer loop
print("\nPython FAQ Assistant")
print("Type 'exit' to quit.\n")

while True:
    question = input("You: ").strip()

    if question.lower() in {"exit", "quit"}:
        print("Goodbye!")
        break

    if not question:
        continue

    try:
        answer = ask_faq(question)
        print(f"\nAssistant: {answer}\n")
    except Exception as error:
        print(f"\nSomething went wrong: {error}\n")
