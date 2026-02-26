# ai_backend/note_generator.py

import subprocess

MODEL_NAME = "llama3:8b"

def generate_notes(transcript: str) -> str:

    prompt = f"""
You are an academic assistant.

Convert the following lecture transcript into READY-TO-STUDY notes.

STRICT FORMAT:
Title (1 line)

Definitions:
- Clear, exam-oriented definitions

Key Points:
- Bullet points
- Based ONLY on the transcript

Important Years / Facts (if any)

Conclusion (2 lines max)

TRANSCRIPT:
{transcript}
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