# Minimal Speech-to-Text Bridge for Hardware Demo
import whisper
# Import the local transcription engine
 
# 1. Setup Configuration
# Use the filename provided by your ESP32 or recording tool
FILE_NAME = "demo_recording.wav"
RESULT_FILE = "transcription.txt"
 
def run_demo():
    # 2. Initialize Model
    # 'base' is fast. 'small' or 'medium' are more accurate but slower.
    print("--- Loading AI Model (Whisper) ---")
    model = whisper.load_model("base")
 
    # 3. Transcribe Audio
    print(f"--- Processing: {FILE_NAME} ---")
    # This might take a few seconds depending on audio length
    result = model.transcribe(FILE_NAME)
    text_content = result["text"].strip()
 
    # 4. Display Results
    print("-" * 30)
    print("STT RESULT:")
    print(text_content)
    print("-" * 30)
 
    # 5. Export to File
    with open(RESULT_FILE, "w") as f:
        f.write(text_content)
    
    print(f"Success! Result saved to {RESULT_FILE}")
 
if __name__ == "__main__":
    run_demo()