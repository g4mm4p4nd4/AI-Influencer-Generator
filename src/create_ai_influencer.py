import os


def create_ai_influencer(image_path: str, audio_path: str):
    """Run SadTalker inference to generate an AI influencer video.

    Parameters
    ----------
    image_path : str
        Path to the avatar image.
    audio_path : str
        Path to the voiceover audio.

    Returns
    -------
    list[str]
        List of files generated under ``./results``.
    """
    os.system(
        f"python3.8 inference.py --driven_audio {audio_path} --source_image {image_path} "
        "--result_dir ./results --still --preprocess full --enhancer gfpgan"
    )
    return sorted(os.listdir("./results/"))
