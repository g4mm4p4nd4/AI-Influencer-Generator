from diffusers import DiffusionPipeline


def generate_avatar_image(image_prompt: str) -> str:
    """Generate an avatar image using Stable Diffusion.

    Parameters
    ----------
    image_prompt : str
        Prompt describing the avatar.

    Returns
    -------
    str
        Path to the generated image.
    """
    pipe = DiffusionPipeline.from_pretrained(
        "stabilityai/stable-diffusion-2-1"
    ).to("cuda")
    image = pipe(image_prompt).images[0]
    image_path = "examples/source_image/generated_image.png"
    image.save(image_path)
    return image_path
