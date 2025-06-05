import os
from pathlib import Path


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

    output_path = Path("output.wav")

    if engine == "coqui":
        from TTS.api import TTS

        model_name = voice_profile or "tts_models/en/ljspeech/tacotron2-DDC"
        tts = TTS(model_name)
        tts.tts_to_file(text, file_path=str(output_path))
    else:
        from bark import SAMPLE_RATE, generate_audio
        import numpy as np
        import soundfile as sf

        audio_array = generate_audio(text, history_prompt=voice_profile)
        sf.write(output_path, np.array(audio_array), SAMPLE_RATE)

    return str(output_path)
