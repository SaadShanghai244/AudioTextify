# main.py (FastAPI Application)
from fastapi import FastAPI, File, UploadFile
from typing import List
# from .utils.audio_logic import check_exists
import whisper
import os
from tempfile import NamedTemporaryFile

app = FastAPI()
model = whisper.load_model("small", device="cpu") 

app.route('/', methods=['GET'])
async def main():
    try:
        return "HELLO THIS APP IS FUNCTIONAL"
    except Exception as e:
        return {"error": str(e)}

app.route('/home', methods=['GET'])
async def home():
    try:
        return "HELLO THIS APP IS FUNCTIONAL"
    except Exception as e:
        return {"error": str(e)}

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        with NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio_file:
            temp_audio_file.write(await file.read())
            temp_audio_file_path = temp_audio_file.name
            print("temp_audio_file_path", temp_audio_file_path)
        
        if not os.path.isfile(temp_audio_file_path):
            return {"error": "Failed to save the uploaded file."}

        result = model.transcribe(temp_audio_file_path)
        transcription = result['text']

        os.remove(temp_audio_file_path)

        return {"transcription": transcription}

    except Exception as e:
        return {"error": str(e)}
