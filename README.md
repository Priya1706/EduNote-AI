# EduNote AI   
AI-Based Lecture-to-Notes System Using Local LLMs

---

##  Project Overview

EduNote AI is an AI-powered system that converts lecture audio into structured and summarized notes.

The current implementation processes both pre-recorded and live-recorded lecture audio and generates clean notes using:

-  **OpenAI Whisper** – Speech-to-Text  
-  **Ollama (Local LLM)** – Summarization  

This project explores the integration of Artificial Intelligence, Speech Processing, and Education Technology.

---

##  Current Working Features

- Lecture audio processing (pre-recorded + live recording)
- Speech-to-Text using OpenAI Whisper
- Summarization using Ollama (local LLM)
- Clean text output stored as `.txt` files
- Confidence score generator 
- Fully local AI pipeline (no cloud dependency for summarization)
- Wi-fi transmission of audio files from hardware

---

##  AI Processing Pipeline

1. Input lecture audio file (`.mp4` / `.wav`)
2. Convert speech → text using Whisper
3. Process and clean transcript
4. Summarize using Ollama LLM
5. Generate structured notes in text format

---

##  Tech Stack

| Component            | Technology Used        |
|---------------------|------------------------|
| Speech-to-Text     | OpenAI Whisper         |
| Summarization      | Ollama (Local LLM)     |
| Programming Language | Python               |
| Hardware Platform  | ESP32-S3              |
| Connectivity       | Wifi                  |
| Storage (Planned)  | SD Card               |

---

## Repository Structure

EduNote-AI/
│
├── live_recording/ # Audio recorded from ESP32
├── demo_recording/ # Pre-recorded lecture samples
├── notes.txt # Output from live recording
├── final_notes.txt # Output from demo recording
├── scripts/ # AI processing scripts
└── README.md

---

##  Research Direction

EduNote AI aims to evolve into a wearable AI-powered lecture assistant that:

- Records classroom audio using low-cost hardware
- Processes speech using local AI models
- Generates structured academic notes
- Integrates fact-verification mechanisms
- Optimizes for Indian classroom environments

The project explores the intersection of:

- Edge AI Systems  
- Speech Processing  
- Local LLM Deployment  
- AI for Education  
---

##  Author

**Priyamvadhaa**  
First-Year Engineering Student  
