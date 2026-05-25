"""Generate placeholder thumbnails — always colorful, never API-dependent."""
import logging
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from trending.config import (
    SummarizedRepo,
    IllustratedRepo,
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
    """Generate placeholder thumbnails for each repo (no external API)."""
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[IllustratedRepo] = []

    for i, repo in enumerate(repos):
        path = output_dir / f"{i + 1:02d}-{repo.repo.owner}__{repo.repo.name}.png"
        color = PLACEHOLDER_COLORS[i % len(PLACEHOLDER_COLORS)]
        _generate_placeholder(repo.repo.full_name, path, color=color)
        results.append(IllustratedRepo(repo=repo, image_path=str(path.resolve())))

    return results


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
