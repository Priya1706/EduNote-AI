# ai_backend/confidence_checker.py

import subprocess


MODEL_NAME = "llama3:8b"


def verify_notes(summary_text: str) -> str:
    """
    Sends the entire generated notes to Ollama for factual verification.
    Returns verified notes with confidence score.
    """

    prompt = f"""
Fact-check the notes below.

Rules:
- Do NOT rewrite everything.
- Only correct clearly wrong facts.
- Keep structure unchanged.
- If correct, leave as is.
- Add: Overall Confidence Score: XX%

NOTES:
{summary_text}
"""


    result = subprocess.run(
        ["ollama", "run", MODEL_NAME],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    return result.stdout.strip()