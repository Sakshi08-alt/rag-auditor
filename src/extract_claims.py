import json
import ollama

MODEL = "llama3.2:3b"

def extract_claims(answer):

    prompt = f"""
Split the answer into small factual claims.

Rules:
- Each claim must contain only one fact.
- Each claim must make sense on its own.
- Replace pronouns like it, they, and this with the actual subject.
- Keep numbers exactly the same.
- Do not invent information.

Answer:
{answer}

Return only JSON:
{{"claims": ["claim 1", "claim 2"]}}
"""

    response = ollama.chat(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        format="json",
        options={"temperature": 0}
    )

    text = response["message"]["content"]

    try:
        data = json.loads(text)
    except json.JSONDecodeError:
        return []

    claims = data.get("claims", [])

    return [
        claim.strip()
        for claim in claims
        if isinstance(claim, str) and claim.strip()
    ]


if __name__ == "__main__":

    sample = "The penalty is 2% of the outstanding amount, and it applies only in the first year."

    claims = extract_claims(sample)

    for claim in claims:
        print("-", claim)