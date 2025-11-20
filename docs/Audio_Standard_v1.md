# Audio Standard Specification – v1

This document defines the audio format used across the hardware and AI team.

---

## 🎧 Audio Format (Finalized)

- Format: WAV (PCM)
- Sample Rate: **16,000 Hz**
- Bit Depth: **16-bit**
- Channels: **Mono**
- Target Size: 90 sec = <2 MB (compressed Opus version for BLE test)

---

## 📌 Why 16kHz?  
Ideal for speech recognition:  
- Lower size  
- Whisper accuracy remains >90%  

---

## 🎤 Usage  
- P3 uses this spec to configure I2S  
- P1 uses this spec to run Whisper tests  
- P6 uses this file for BLE transfer protocol testing  
