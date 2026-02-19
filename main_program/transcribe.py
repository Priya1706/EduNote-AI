from ai_backend.pipeline import process_audio

AUDIO_FILE = "main_program/live_recording.wav"
OUTPUT_FILE = "main_program/notes.txt"

process_audio(AUDIO_FILE, OUTPUT_FILE)
#python -m main_program.transcribe