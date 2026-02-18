# EduNote AI 

AI-Based Lecture-to-Notes System Using Local LLMs

---

##  Project Overview

EduNote AI is an AI-powered system that converts lecture audio into clean, structured notes.

Currently, the system processes pre-recorded lecture audio and generates summarized notes using:

- OpenAI Whisper (Speech-to-Text)
- Ollama (Local LLM for Summarization)

This project explores the integration of AI + Speech Processing + Education Technology.

---

##  Current Working Features

-  Lecture audio processing (pre-recorded files + live recording)
-  Speech-to-Text using OpenAI Whisper
-  Summarization using Ollama (local LLM)
-  Clean text output stored as `.txt` files
-  Fully local AI pipeline (runs without cloud dependency) 

---

##  Current AI Pipeline

1. Input lecture audio file (.mp4 / .wav)
2. Convert speech → text using Whisper
3. Process transcript
4. Summarize using Ollama LLM
5. Generate structured notes in text format

---

##  Tech Stack

| Component | Technology |
|------------|------------|
| Speech-to-Text | OpenAI Whisper |
| Summarization | Ollama (Local LLM) |
| Programming Language | Python |
| Hardware | ESP32-S3 |
| Connectivity (Planned) | Bluetooth |
| Storage (Planned) | SD Card |

---

## Features Under Development

The following features are part of the full EduNote AI Smartwatch vision but are not yet implemented:

- ⌚ ESP32-based smartwatch prototype
- 📡 Bluetooth audio transfer
- 💾 SD card storage on device
- ✅ Confidence Checker (Fact verification module)
- 📱 Mobile app integration

---

## Repository Structure

EduNote-AI/
│
├── live_recording/        # Audio recorded from ESP32
├── demo_recording/        # Pre-recorded lecture
├── notes.txt              # Output from live recording
├── final_notes.txt        # Output from demo recording
├── scripts/               # AI processing scripts
└── README.md

---

## Research Direction

This project aims to evolve into a wearable AI-powered lecture assistant that:

- Records classroom audio
- Processes it locally or on companion device
- Generates structured, verified academic notes
- Optimizes for Indian classroom environments

---

## Future Work

- Integrate Bluetooth file transfer
- Implement SD card audio storage
- Add AI-based confidence checker
- Build companion mobile app
- On-device summarization optimization

---

## Author

Priyamvadhaa  
First-Year Engineering Student  
