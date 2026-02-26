# ai_backend/pipeline.py

from ai_backend.stt import speech_to_text
from ai_backend.note_generator import generate_notes
from ai_backend.confidence_checker import verify_notes


def process_audio(audio_path: str, output_path: str):

    print("🔹 Transcribing audio...")
    transcript = speech_to_text(audio_path)

    if not transcript.strip():
        print("❌ Transcript empty.")
        return

    print("Transcript length:", len(transcript))

    print("🔹 Generating notes...")
    notes = generate_notes(transcript)

    if not notes.strip():
        print("❌ Note generator returned empty output.")
        return

    print("Notes length:", len(notes))

    print("🔹 Running confidence checker...")
    verified_notes = verify_notes(notes)

    if not verified_notes.strip():
        print("⚠ Confidence checker returned empty. Saving unverified notes instead.")
        verified_notes = notes

    print("Verified length:", len(verified_notes))

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(verified_notes)

    print("✅ Notes saved successfully.")