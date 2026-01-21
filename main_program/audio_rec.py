import serial
import wave
import struct
import time
import math
from scipy.signal import butter, lfilter

# ================= CONFIG =================
PORT = "COM10"
BAUD_RATE = 115200
SAMPLE_RATE = 16000
DURATION = 30                          # seconds
OUTPUT_FILE = "main_program/live_recording.wav"

# Audio tuning
TARGET_RMS = 12000                     # speech sweet spot
MAX_GAIN = 6.0
MIN_GAIN = 1.0

# Band-pass (speech range)
LOWCUT = 300
HIGHCUT = 3400
FILTER_ORDER = 3
# =========================================


def bandpass_filter(data, lowcut, highcut, fs, order=3):
    nyq = 0.5 * fs
    low = lowcut / nyq
    high = highcut / nyq
    b, a = butter(order, [low, high], btype='band')
    return lfilter(b, a, data)


print("🎙 Opening serial port...")
ser = serial.Serial(PORT, BAUD_RATE, timeout=0.1)
time.sleep(2)

samples = []
print(f"🎙 Recording for {DURATION} seconds. Speak normally...")

start = time.time()
while time.time() - start < DURATION:
    line = ser.readline().decode(errors="ignore").strip()
    if not line:
        continue
    try:
        samples.append(int(line))
    except:
        pass

ser.close()
print("Recording finished")
print("Samples captured:", len(samples))

# 🔍 DEBUG: check real audio duration
duration = len(samples) / 16000
print("Audio duration (seconds):", duration)


# ================= SAFETY CHECK =================
if len(samples) < 2000:
    print("❌ Not enough audio captured")
    exit()

# ================= DC OFFSET REMOVAL =================
mean = sum(samples) / len(samples)
samples = [s - mean for s in samples]

# ================= RMS AUTO GAIN =================
rms = math.sqrt(sum(s * s for s in samples) / len(samples))
if rms < 100:
    print("❌ Audio too quiet")
    exit()

gain = TARGET_RMS / rms
gain = max(MIN_GAIN, min(MAX_GAIN, gain))
print("🎚 Applied RMS gain:", round(gain, 2))

samples = [s * gain for s in samples]

# ================= BAND-PASS FILTER =================
samples = bandpass_filter(
    samples,
    lowcut=LOWCUT,
    highcut=HIGHCUT,
    fs=SAMPLE_RATE,
    order=FILTER_ORDER
)

# ================= WRITE WAV =================
with wave.open(OUTPUT_FILE, "w") as wf:
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(12000)

    for s in samples:
        # 1️⃣ Convert to int
        v = int(s)

        # 2️⃣ Soft limiter / clamp
        if v > 32767:
            v = 32767
        elif v < -32768:
            v = -32768

        # 3️⃣ Write clean int16
        wf.writeframes(struct.pack("<h", v))


print("✅ Audio saved as:", OUTPUT_FILE)


#python main_program/audio_rec.py
