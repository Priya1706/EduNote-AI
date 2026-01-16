# ai_backend/text_cleaner.py
import re

def clean_text(text):
    text = re.sub(r'\b(um|uh|you know)\b', '', text, flags=re.IGNORECASE)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('.', '.\n')
    return text.strip()
