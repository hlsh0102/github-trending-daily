"""Generate 1024×1792 DALL-E 3 thumbnails, with dynamic placeholder fallback."""
import io
import logging
from pathlib import Path

from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont

from trending.config import (
    SummarizedRepo,
    IllustratedRepo,
    OPENAI_API_KEY,
)

logger = logging.getLogger(__name__)

PLACEHOLDER_COLORS = [
    "#6366f1", "#8b5cf6", "#a855f7", "#d946ef",
    "#ec4899", "#f43f5e", "#ef4444", "#f97316",
    "#eab308", "#22c55e",
]


def illustrate(
    repos: list[SummarizedRepo],
    output_dir: Path,
) -> list[IllustratedRepo]:
    """Generate DALL-E 3 images for each repo (serial, to respect rate limits)."""
    client = OpenAI(api_key=OPENAI_API_KEY)
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[IllustratedRepo] = []

    for i, repo in enumerate(repos):
        path = output_dir / f"{i + 1:02d}-{repo.repo.owner}__{repo.repo.name}.png"
        try:
            _generate_image(client, repo.image_prompt_en, path)
        except Exception as exc:
            logger.warning("DALL-E failed for %s: %s. Using placeholder.", repo.repo.full_name, exc)
            _generate_placeholder(repo.repo.full_name, path, color=PLACEHOLDER_COLORS[i % len(PLACEHOLDER_COLORS)])

        results.append(IllustratedRepo(repo=repo, image_path=str(path.resolve())))

    return results


def _generate_image(client: OpenAI, prompt: str, path: Path) -> None:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{prompt}. No text, no labels, no words.",
        size="1024x1792",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    import requests
    img_data = requests.get(image_url, timeout=60).content
    path.write_bytes(img_data)


def _generate_placeholder(text: str, path: Path, color: str = "#6366f1") -> None:
    """Generate a 1024×1792 placeholder with solid color and repo name."""
    img = Image.new("RGB", (1024, 1792), color)
    draw = ImageDraw.Draw(img)

    try:
        from trending.config import FONT_PATH
        font = ImageFont.truetype(FONT_PATH, size=48)
    except Exception:
        font = ImageFont.load_default()

    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (1024 - tw) // 2
    y = (1792 - th) // 2
    draw.text((x, y), text, fill="white", font=font)
    img.save(path, "PNG")
