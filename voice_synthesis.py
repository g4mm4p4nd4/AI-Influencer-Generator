import os
from pathlib import Path
from tempfile import NamedTemporaryFile


def generate_voice(text: str, voice_profile: str = None, engine: str = None) -> str:
    """Generate speech audio for the given text using the selected TTS engine.

    Parameters
    ----------
    text : str
        The text to synthesize.
    voice_profile : str, optional
        Name or path of a voice profile/model. Interpretation depends on the
        chosen engine.
    engine : str, optional
        Either ``"bark"`` or ``"coqui"``. When ``None``, the value of the
        ``TTS_ENGINE`` environment variable is used, defaulting to ``"bark"``.

    Returns
    -------
    str
        Path to the generated ``.wav`` file.
    """

    engine = (engine or os.getenv("TTS_ENGINE", "bark")).lower()

    temp_file = NamedTemporaryFile(delete=False, suffix=".wav")
    output_path = Path(temp_file.name)

    if engine == "coqui":
        from TTS.api import TTS

        model_name = voice_profile or "tts_models/en/ljspeech/tacotron2-DDC"
        tts = TTS(model_name=model_name)
        tts.tts_to_file(text, file_path=str(output_path))
    else:
        from bark import SAMPLE_RATE, generate_audio
        import numpy as np
        import soundfile as sf

        audio_array = generate_audio(text, history_prompt=voice_profile)
        sf.write(output_path, np.array(audio_array), SAMPLE_RATE)

    return str(output_path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Generate speech using Bark or Coqui")
    parser.add_argument("text", help="Text to convert to speech")
    parser.add_argument("--engine", default=None, help="Choose 'bark' or 'coqui'. Defaults to env TTS_ENGINE")
    parser.add_argument("--voice-profile", default=None, help="Voice profile or model name")
    args = parser.parse_args()

    path = generate_voice(args.text, voice_profile=args.voice_profile, engine=args.engine)
    print(path)
