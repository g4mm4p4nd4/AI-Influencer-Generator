#!/usr/bin/env python3
"""Command line driver for generating an AI influencer video."""

import argparse
from src.generate_avatar_image import generate_avatar_image
from src.generate_voiceover import generate_voiceover
from src.create_ai_influencer import create_ai_influencer


def main():
    parser = argparse.ArgumentParser(description="Generate an AI influencer video")
    parser.add_argument("--characteristics", required=True, help="Avatar characteristics")
    parser.add_argument("--script", required=True, help="Text script for the voiceover")
    parser.add_argument("--output", default="./results", help="Output directory")
    args = parser.parse_args()

    prompt = args.characteristics
    image_path = generate_avatar_image(prompt)
    audio_path = "examples/driven_audio/audio.wav"
    generate_voiceover(args.script, audio_path)

    results = create_ai_influencer(image_path, audio_path)
    print("Generated files:", results)


if __name__ == "__main__":
    main()
