from ai_backend.pipeline import process_audio

AUDIO_FILE = "main_program/demo_recording.wav"
OUTPUT_FILE = "main_program/final_notes.txt"

process_audio(AUDIO_FILE, OUTPUT_FILE)

# Run using:
# python -m main_program.main
