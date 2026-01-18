import subprocess

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

    result = subprocess.run(
        ["ollama", "run", "llama3:8b"],
        input=prompt,
        capture_output=True,
        text=True,
        encoding="utf-8"
    )

    return result.stdout.strip()
