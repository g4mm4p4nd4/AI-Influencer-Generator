from gtts import gTTS
import os


def generate_voiceover(text: str, filename: str) -> None:
    """Generate a voiceover using gTTS.

    Parameters
    ----------
    text : str
        Text to convert to speech.
    filename : str
        Output filename for the WAV file.
    """
    tts = gTTS(text)
    tts.save("temp.mp3")
    os.system(f"ffmpeg -i temp.mp3 -ar 16000 -ac 1 {filename}")
    os.remove("temp.mp3")
