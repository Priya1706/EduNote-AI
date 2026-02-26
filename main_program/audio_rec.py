import socket
import wave
import time
import os

ESP_IP = "192.168.137.151"
PORT = 5000
SAMPLE_RATE = 16000
OUTPUT_FILE = "main_program/live_recording.wav"

def record_audio(duration):

    print("Connecting to ESP...")
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((ESP_IP, PORT))

    # VERY IMPORTANT
    sock.settimeout(0.2)

    print("Sending START")
    sock.sendall(b"START\n")

    print(f"Recording for {duration} seconds...")
    start_time = time.time()
    audio_data = bytearray()

    while True:
        if time.time() - start_time >= duration:
            break

        try:
            data = sock.recv(4096)
            if data:
                audio_data.extend(data)
        except socket.timeout:
            pass

    print("Sending STOP")
    sock.sendall(b"STOP\n")
    sock.close()

    print("Bytes captured:", len(audio_data))
    return audio_data


def save_wav(audio_data):
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with wave.open(OUTPUT_FILE, "w") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(SAMPLE_RATE)
        wf.writeframes(audio_data)

    print("Saved:", OUTPUT_FILE)


if __name__ == "__main__":
    duration = int(input("Enter recording duration (seconds): "))
    data = record_audio(duration)
    save_wav(data)
#python main_program/audio_rec.py