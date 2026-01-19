import whisper
from datetime import datetime

AUDIO_FILE = "main_program/live_recording.wav"
OUTPUT_TEXT = "main_program/transcription.txt"

print("🧠 Loading Whisper model...")
model = whisper.load_model("base")   # use "small" if your system is slow

print("🎧 Transcribing audio...")
result = model.transcribe(
    AUDIO_FILE,
    language="en",
    fp16=False
)

text = result["text"]

with open(OUTPUT_TEXT, "w", encoding="utf-8") as f:
    f.write(text)

print("✅ Transcription saved to:", OUTPUT_TEXT)
print("\n--- TRANSCRIBED TEXT ---\n")
print(text)
#python main_program/transcribe.py


