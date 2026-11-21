import json
import ollama

MODEL = "llama3.2:3b"

with open("data/examples.json", "r", encoding="utf-8") as file:
    examples = json.load(file)


def judge_claim(claim, sources):
    prompt = f"""
You are a strict fact-checker.

Decide whether the claim is supported by the sources.

Sources:
{sources}

Claim:
{claim}

Reply with exactly one word:
SUPPORTED, CONTRADICTED, or NOT_MENTIONED.
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}]
    )

    return response["message"]["content"].strip()


for example in examples:

    print("\nQuestion:", example.get("question", "No question"))

    sources = example.get("sources", "")

    if not sources:
        print("WARNING: This example has no sources!")
        continue

    for claim in example.get("claims", []):

        verdict = judge_claim(claim, sources)

        print(f"{verdict:15} <- {claim}")

    print()