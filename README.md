# EduNote-AI  
Smartwatch-based AI Note Generation System  

EduNote-AI is a wearable device + mobile app system that records lectures, transfers compressed audio to a phone, and generates structured, summarized notes using an AI backend.

---

## Features
- ESP32-S3 based smartwatch prototype  
- I2S microphone audio capture  
- MicroSD-based audio storage  
- BLE file transfer to Android app  
- AI-powered transcription using Whisper  
- Structured summary generation  
- Confidence-based verification  

---

## System Architecture

**Watch (ESP32-S3):**  
- I2S Recording  
- WAV/Opus compression  
- BLE GATT Server  
- Audio Chunk Transfer  

**Mobile App (Android):**  
- BLE Client  
- File Sync  
- Displays summarized notes  

**AI Backend:**  
- Speech-to-Text  
- Summarization  
- Confidence scoring  

---

## Project Structure
ai_backend/ → Whisper, summarizer scripts
mobile_app/ → Android Studio project
hardware/ → ESP32 I2S + BLE firmware
docs/ → Technical documents, protocols
.github/ → Repo automation



---

## Team Roles

- **Integrator (P6)** — Hardware + software integration  
- **P1** — AI Backend  
- **P2** — Android App  
- **P3** — ESP32 I2S + Storage  
- **P4** — ESP32 BLE Server  
- **P5** — Testing + Documentation  

---

## Week 1 Deliverables
- BLE Handshake Protocol  
- Pinout Definition  
- I2S Audio Standard  
- Repo Setup + Branch Rules  
- Initial sample test audio file  

---

## Next Goals  
- I2S Audio Logging  
- BLE File Transfer  
- App UI Screens  
- Whisper integration  

---

## License  
MIT License.
