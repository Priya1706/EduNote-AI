import os
from ai_backend.stt import speech_to_text
from ai_backend.note_generator import generate_notes

AUDIO_FILE = os.path.join("main_program", "demo_recording.wav")

print("🎙 Transcribing audio...")
transcript = speech_to_text(AUDIO_FILE)

print("📝 Generating study notes using LLaMA 3...")
notes = generate_notes(transcript)

with open("main_program/transcription.txt", "w", encoding="utf-8") as f:
    f.write(notes)

print("✅ Ready-to-study notes saved to transcription.txt")
