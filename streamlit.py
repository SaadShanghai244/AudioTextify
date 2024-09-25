# streamlit_app.py (Streamlit Application)
import streamlit as st
import requests

st.title("Audio to Text Transcription App")

# Allow the user to upload an audio file (MP3, WAV)
uploaded_file = st.file_uploader("Choose an audio file...", type=["mp3", "wav"])

if uploaded_file is not None:
    # Display the uploaded file name
    st.audio(uploaded_file, format='audio/mp3')
    st.write(f"Uploaded file: {uploaded_file.name}")

    # Call the FastAPI service
    if st.button('Transcribe'):
        files = {'file': uploaded_file.getvalue()}
        # Ensure the FastAPI app is running at this address
        response = requests.post("http://localhost:8000/transcribe/", files=files)
        result = response.json()

        if response.status_code == 200:
            st.write(f"Transcription: {result['transcription']}")
        else:
            st.write(f"Error: {result.get('error', 'Unknown error occurred')}")
