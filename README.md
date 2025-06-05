# AI Influencer

Create your virtual AI influencer for free with open-source technologies

Link to medium tutorial :- https://medium.com/@anilmatcha/ai-influencer-automation-to-earn-10k-month-for-free-b8936212bcb9 

### Demo Video

https://github.com/user-attachments/assets/c5c27c58-7f3d-450e-a1dc-26984a0d2c05

🌟 Show Support

If you enjoy using AI Influencer, we'd appreciate your support with a star ⭐ on our repository. Your encouragement is invaluable and inspires us to continually improve and expand AI Influencer. Thank you, and happy content creation! 🎉

[![GitHub star chart](https://img.shields.io/github/stars/SamurAIGPT/AI-Influencer?style=social)](https://github.com/SamurAIGPT/AI-Influencer/stargazers)

### Steps to run

Open the colab notebook from [here](https://github.com/SamurAIGPT/AI-Influencer/blob/main/AI_Influencer.ipynb) and run all the steps one-by-one

### Technologies used

gTTS for simple text-to-speech

Bark or [Coqui TTS](https://github.com/coqui-ai/TTS) for high-quality voice synthesis

Sad-Talker for lip-sync

OpenAI for generating prompt for AI image generation

Stable diffusion for image generation

### Voice Synthesis

The repository ships with a small utility [`voice_synthesis.py`](./voice_synthesis.py)
that can generate speech either with [Bark](https://github.com/suno-ai/bark) or
[Coqui TTS](https://github.com/coqui-ai/TTS). Select the engine with the
`TTS_ENGINE` environment variable or pass `--engine` when calling the script.
The default engine is `bark`.

Set the environment variable:

```bash
export TTS_ENGINE=coqui  # or "bark"
```

```python
from voice_synthesis import generate_voice
audio_file = generate_voice("Hello world!", voice_profile=None)

# Or from the command line
python voice_synthesis.py "Hello world!" --engine coqui
```

Specify a voice profile when using Bark (e.g. `"en_speaker_6"`) or a model name
when using Coqui TTS (e.g. `"tts_models/en/ljspeech/tacotron2-DDC"`). The
function returns the path to a generated `wav` file.

## 💁 Contribution

As an open-source project we are extremely open to contributions. To get started raise an issue in Github or create a pull request

### Other useful AI Projects

[AI Youtube Shorts generator](https://github.com/SamurAIGPT/AI-Youtube-Shorts-Generator/)

[Faceless Video Generator](https://github.com/SamurAIGPT/Faceless-Video-Generator)

[Text to Video AI](https://www.vadoo.tv/text-to-video-ai)
