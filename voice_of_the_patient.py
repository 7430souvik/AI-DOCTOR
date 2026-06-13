# setup audio recorder(ffmpeg & portaudio)
import os
import logging
import speech_recognition as sr
from pydub import AudioSegment
from io import BytesIO

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def record_audio(file_path, timeout=20, phrase_time_linit=None):
    """
    Simplified function to record audio from the microphone and save it as an mp3 file.

    Args:
    file_path (str): path to save the recorded audio file (should end with .mp3)
    timeout (int): maximum time to wait for a phrase to start (in seconds).
    phrase_time_linit (int): maximum duration of a single phrase (in seconds).
    """
    recognizer = sr.Recognizer()
    try:
            with sr.Microphone() as source:

                logging.info("Calibrating microphone...")
                recognizer.adjust_for_ambient_noise(source, duration=2)

                logging.info("Speak now...")

                audio_data = recognizer.listen(
                    source,
                    timeout=20,
                    phrase_time_limit=15
                )

                logging.info("Recording complete.")
                #convert the audio data to an MP3 file
                wav_data = audio_data.get_wav_data()
                audio_segment = AudioSegment.from_wav(BytesIO(wav_data))
                with open(file_path, "wb") as f:
                    f.write(audio_data.get_wav_data())
                logging.info(f"Audio saved to {file_path}")
    except Exception as e:
        logging.error(f"An error occurred while recording audio: {e}")

# audio_file_path = "patient_voice.wav" 

# record_audio(file_path=audio_file_path)

#setup speech to text-STT-model for transcription
from dotenv import load_dotenv
import os
load_dotenv()
from groq import Groq

GROQ_API_KEY =os.environ.get("GROQ_API_KEY")

def transcribe_with_groq(stt_model, audio_file_path,GROQ_API_KEY):
    if audio_file_path is None:
        return ""
    client= Groq(api_key=GROQ_API_KEY)
    stt_model="whisper-large-v3-turbo"
    audio_file=open(audio_file_path, "rb")

    transcription=client.audio.transcriptions.create(
        model=stt_model,
        file=audio_file,
        language="en",
    )

    return transcription.text




