import argparse
import json
import os
from openai import OpenAI
from diffusers import DiffusionPipeline
from gtts import gTTS


def get_prompt_for_image(characteristics: str, api_key: str) -> str:
    """Use OpenAI to create an image prompt based on characteristics."""
    client = OpenAI(api_key=api_key)
    prompt = f"""Given below are some characteristics of a person for a single scene in a video, give output a prompt for an image generating model to generate an image of the person.\n\nStrictly give output in JSON format as: {{\"prompt\": <text>}}\n\nCharacteristics:\n{characteristics}\n"""
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        temperature=0.5,
        messages=[{"role": "user", "content": prompt}],
    )
    data = response.choices[0].message.content
    try:
        return json.loads(data)["prompt"]
    except Exception:
        data = data.split('```json')[-1].split('```')[0]
        return json.loads(data)["prompt"]


def generate_avatar_image(image_prompt: str, model: str = "hf-internal-testing/tiny-stable-diffusion-xl-pipe") -> str:
    """Generate an avatar image using a lightweight diffusion model."""
    pipe = DiffusionPipeline.from_pretrained(model)
    image = pipe(image_prompt).images[0]
    out_path = os.path.join("examples", "source_image", "generated_image.png")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    image.save(out_path)
    return out_path


def generate_voiceover(text: str, filename: str) -> None:
    """Generate voiceover using gTTS."""
    tts = gTTS(text)
    tts.save("temp.mp3")
    os.system(f"ffmpeg -y -i temp.mp3 -ar 16000 -ac 1 {filename}")
    os.remove("temp.mp3")


def main():
    parser = argparse.ArgumentParser(description="Generate a simple AI influencer clip")
    parser.add_argument("characteristics", help="Description of the avatar")
    parser.add_argument("script", help="Text to speak")
    args = parser.parse_args()
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise SystemExit("OPENAI_API_KEY environment variable not set")

    prompt = get_prompt_for_image(args.characteristics, api_key)
    print("Image prompt:", prompt)
    image_path = generate_avatar_image(prompt)
    print("Image saved to:", image_path)
    audio_path = os.path.join("examples", "driven_audio", "audio.wav")
    os.makedirs(os.path.dirname(audio_path), exist_ok=True)
    generate_voiceover(args.script, audio_path)
    print("Voiceover saved to:", audio_path)
    print("Generation complete. Lip-sync step omitted in this environment.")


if __name__ == "__main__":
    main()
