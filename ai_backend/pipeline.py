# ai_backend/pipeline.py

from ai_backend.stt import speech_to_text
from ai_backend.note_generator import generate_notes
from ai_backend.confidence_checker import verify_notes


def process_audio(audio_path: str, output_path: str):
    print("🔹 Transcribing audio...")
    transcript = speech_to_text(audio_path)

    if not transcript.strip():
        print("Transcript empty.")
        return

    print("🔹 Generating notes...")
    notes = generate_notes(transcript)

    print("🔹 Running confidence checker...")
    verified_notes = verify_notes(notes)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(verified_notes)

    print("✅ Verified notes saved successfully.")