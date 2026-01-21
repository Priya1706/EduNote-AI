import whisper
import subprocess

AUDIO_FILE = "main_program/live_recording.wav"
NOTES_FILE = "main_program/notes.txt"

print("🎧 Loading Whisper model...")
model = whisper.load_model("base")

print("📝 Transcribing audio...")
result = model.transcribe(AUDIO_FILE)

transcript = result["text"].strip()

print("\n--- TRANSCRIPTION ---\n")
print(transcript)

# =========================
# OLLAMA NOTES GENERATION
# =========================

print("\n🤖 Generating notes using Ollama...")

prompt = f"""
You are an AI note-taking assistant for students.

Convert the following lecture transcript into clear, well-structured study notes.

Rules:
- Use headings
- Use bullet points
- Add short definitions or formulas if present
- Keep it concise and accurate
- Do NOT invent new topics
- Student-friendly language

Lecture transcript:
{transcript}
"""

ollama_process = subprocess.run(
    ["ollama", "run", "llama3"],
    input=prompt,
    text=True,
    capture_output=True
)

notes = ollama_process.stdout.strip()

# Save notes
with open(NOTES_FILE, "w", encoding="utf-8") as f:
    f.write(notes)

print("\n✅ NOTES GENERATED SUCCESSFULLY\n")
print("--- NOTES ---\n")
print(notes)
#python main_program/transcribe.py