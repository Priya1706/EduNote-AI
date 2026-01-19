from ai_backend.stt import speech_to_text
from ai_backend.note_generator import generate_notes

# ===== DEMO AUDIO FILE =====
AUDIO_FILE = "main_program/demo_recording.wav"

# ===== OUTPUT FILE =====
OUTPUT_FILE = "main_program/final_notes.txt"

print("Transcribing audio...")
transcript = speech_to_text(AUDIO_FILE)

if not transcript.strip():
    print("Transcript empty. Check demo audio.")
    exit()

print("Generating notes...")
notes = generate_notes(transcript)

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write(notes)

print("Notes saved successfully to final_notes.txt")

#python -m main_program.main
