# Audio to Text Converter with FastAPI and Whisper

This project provides an API that allows users to upload an audio file and receive its transcription using OpenAI's Whisper model. The API is built using **FastAPI** and processes audio files like MP3 using Whisper.

## Features

- Users can upload an audio file through the FastAPI endpoint.
- Transcription is performed using OpenAI's Whisper model.
- The API supports transcription of audio in formats like MP3.
- Temporary files are created for processing and deleted after use.

## Prerequisites

Before you can run the project, make sure you have the following installed:

- Python 3.7+
- Pip (Python package installer)

Additionally, you will need the following Python libraries:

- **FastAPI**: A modern web framework for building APIs with Python.
- **Uvicorn**: ASGI server for running FastAPI apps.
- **Whisper**: OpenAI’s model for speech-to-text transcription.
- **FFmpeg**: A multimedia framework required for audio file processing.

### Install FFmpeg

1. Download FFmpeg from [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html).
2. Extract and add FFmpeg to your system's PATH variable.
3. Verify installation by running:
   ```bash
   ffmpeg -version
   ```
