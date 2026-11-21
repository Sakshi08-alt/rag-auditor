import json
from extract_claims import extract_claims

with open("data/examples.json") as f:
    examples = json.load(f)

for i, ex in enumerate(examples):

    extracted = extract_claims(ex["answer"])
    expected = ex["claims"]

    print(f"\nExample {i + 1}")

    print("Expected claims:")
    for claim in expected:
        print("-", claim)

    print("\nAI extracted claims:")
    for claim in extracted:
        print("-", claim)

    print("-" * 40)