import serial
import wave
import time
import os

PORT = "COM10"
BAUD_RATE = 921600
SAMPLE_RATE = 16000
OUTPUT_FILE = "main_program/live_recording.wav"

def record_audio(duration):
    print("🎙 Opening serial port...")
    ser = serial.Serial(PORT, BAUD_RATE, timeout=0.1)
    time.sleep(2)

    print("▶ Sending start signal to ESP...")
    ser.write(b'1')

    print(f"🎙 Recording for {duration} seconds...")

    start_time = time.time()
    audio_data = bytearray()

    while time.time() - start_time < duration:
        chunk = ser.read(4096)
        if chunk:
            audio_data.extend(chunk)

    ser.close()

    print("Recording finished")
    print("Bytes captured:", len(audio_data))

    return bytes(audio_data)


def save_wav(audio_data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with wave.open(OUTPUT_FILE, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data)

    print("✅ Audio saved as:", OUTPUT_FILE)


if __name__ == "__main__":
    duration = int(input("Enter recording duration (seconds): "))
    data = record_audio(duration)
    save_wav(data)
#python main_program/audio_rec.py