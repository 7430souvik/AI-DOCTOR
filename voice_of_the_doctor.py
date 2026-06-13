#step-1a

from dotenv import load_dotenv
import os

load_dotenv()
from gtts import gTTS

def text_to_speech_with_gtts_old(input_text, output_filepath):
    language = 'en'


    audioobj= gTTS(
        text=input_text, 
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)

input_text="Hello, I am your AI doctor. How can I assist you today?"
# text_to_speech_with_gtts_old(input_text=input_text, output_filepath="gtts_testing.mp3")

#step-1b
import elevenlabs
from elevenlabs.client import ElevenLabs

ELEVENLABS_API_KEY=os.environ.get("ELEVENLABS_API_KEY")

def text_to_speech_with_elevenlabs_old(input_text,output_filepath): 
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        
        model_id="eleven_turbo_v2",
        output_format="mp3_44100_128"
    )
    elevenlabs.save(audio, output_filepath)

# text_to_speech_with_elevenlabs_old(input_text=input_text, output_filepath="elevenlabs_testing.mp3")

#step-2
import subprocess
import platform

def text_to_speech_with_gtts(input_text, output_filepath):
    language = 'en'


    audioobj= gTTS(
        text=input_text, 
        lang=language,
        slow=False
    )
    audioobj.save(output_filepath)
    return output_filepath
    # os_name=platform.system()
    # try:
    #     if os_name== "Darwin":
    #         subprocess.run(["open", output_filepath])
    #     elif os_name=="Windows":
    #         subprocess.run(["powerShell", "-Command", f"Start-Process '{output_filepath}'"])
    #     elif os_name=="Linux":
    #         subprocess.run(["aplay", output_filepath])
    #     else:
    #         raise OSError("Unsupported operating system")
    # except Exception as e:
    #     print(f"An error occurred while trying to play the audio: {e}")

# input_text="Hello, I am your AI doctor.new version testing!"
# text_to_speech_with_gtts(input_text=input_text, output_filepath="gtts_testing_autoplay.mp3")

def text_to_speech_with_elevenlabs(input_text,output_filepath): 
    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)
    audio=client.text_to_speech.convert(
        text=input_text,
        voice_id="EXAVITQu4vr4xnSDxMaL",
        
        model_id="eleven_turbo_v2",
        output_format="mp3_44100_128"
    )
    elevenlabs.save(audio, output_filepath)
    os_name=platform.system()
    try:
        if os_name== "Darwin":
            subprocess.run(["open", output_filepath])
        elif os_name=="Windows":
            subprocess.run(["powerShell", "-Command", f"Start-Process '{output_filepath}'"])
        elif os_name=="Linux":
            subprocess.run(["aplay", output_filepath])
        else:
            raise OSError("Unsupported operating system")
    except Exception as e:
        print(f"An error occurred while trying to play the audio: {e}")


# text_to_speech_with_elevenlabs(input_text=input_text, output_filepath="elevenlabs_testing_autoplay.mp3")
