import json
from extract_claims import extract_claims

with open("data/tricky_answers.json") as f:
    answers = json.load(f)

for answer in answers:

    print("\nOriginal answer:")
    print(answer)

    print("\nExtracted claims:")

    claims = extract_claims(answer)

    for claim in claims:
        print("-", claim)

    print("-" * 40)