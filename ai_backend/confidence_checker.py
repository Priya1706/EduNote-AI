# ai_backend/confidence_checker.py

import subprocess

MODEL_NAME = "llama3:8b"

def verify_notes(summary_text: str) -> str:

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

    process = subprocess.Popen(
        ["ollama", "run", MODEL_NAME],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    output, error = process.communicate(prompt)

    if error:
        print("Ollama error:", error)

    return output.strip()