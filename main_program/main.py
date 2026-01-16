from ai_backend.stt import speech_to_text
from ai_backend.text_cleaner import clean_text
from ai_backend.study_notes import generate_study_notes
from ai_backend.confidence_checker import confidence_check
import os

AUDIO_FILE = os.path.join("main_program", "demo_recording.wav")

print("Loading AI Model...")

# 1. Speech to Text
raw_text = speech_to_text(AUDIO_FILE)

# 2. Clean Text
cleaned_text = clean_text(raw_text)

# 3. Generate Study Notes
study_notes = generate_study_notes(cleaned_text)

# 4. Confidence Check
confidence_report = confidence_check(cleaned_text)

final_output = f"""
{study_notes}

{confidence_report}

🧠 Generated using EduNote AI
"""

# 5. Save Final Output
with open(os.path.join("main_program", "transcription.txt"), "w", encoding="utf-8") as f:
    f.write(final_output)

print("Success! Ready-to-study notes saved.")
