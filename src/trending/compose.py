"""Composite 10 repo thumbnails into a 1080×2340 iPhone-ratio overview image."""
import logging
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from trending.config import (
    IllustratedRepo,
    CANVAS_W,
    CANVAS_H,
    COLS,
    ROWS,
    GUTTER,
    CELL_RADIUS,
    FONT_SIZE_TITLE,
    FONT_SIZE_STARS,
    FONT_PATH,
)

logger = logging.getLogger(__name__)

LANGUAGE_COLORS = {
    "Python": "#3572A5", "JavaScript": "#f1e05a", "TypeScript": "#3178c6",
    "Go": "#00ADD8", "Rust": "#dea584", "Java": "#b07219",
    "C++": "#f34b7d", "C": "#555555", "C#": "#178600", "Ruby": "#701516",
    "Swift": "#F05138", "Kotlin": "#A97BFF", "Zig": "#ec915c",
    "R": "#198CE7", "Shell": "#89e051", "HTML": "#e34c26",
    "CSS": "#563d7c", "Vue": "#41b883", "Jupyter Notebook": "#DA5B0B",
}


def compose(repos: list[IllustratedRepo], output_path: Path) -> None:
    """Create 2x5 overview grid from 10 illustrated repos."""
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), "#0d0d0d")
    draw = ImageDraw.Draw(canvas)

    cell_w = (CANVAS_W - GUTTER * (COLS + 1)) // COLS
    cell_h = (CANVAS_H - GUTTER * (ROWS + 1)) // ROWS

    try:
        font_title = ImageFont.truetype(FONT_PATH, size=FONT_SIZE_TITLE)
        font_stars = ImageFont.truetype(FONT_PATH, size=FONT_SIZE_STARS)
    except Exception:
        font_title = ImageFont.load_default()
        font_stars = font_title

    for i, illustrated in enumerate(repos[:10]):
        row = i // COLS
        col = i % COLS
        x = GUTTER + col * (cell_w + GUTTER)
        y = GUTTER + row * (cell_h + GUTTER)
        _draw_cell(canvas, draw, x, y, cell_w, cell_h, illustrated, font_title, font_stars)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, "PNG")
    logger.info("Overview saved to %s", output_path)


def _draw_cell(
    canvas: Image.Image,
    draw: ImageDraw.Draw,
    x: int, y: int, w: int, h: int,
    illustrated: IllustratedRepo,
    font_title: ImageFont.FreeTypeFont,
    font_stars: ImageFont.FreeTypeFont,
) -> None:
    repo = illustrated.repo
    thumb_h = h - 70

    # Cell background
    draw.rounded_rectangle([x, y, x + w, y + h], radius=CELL_RADIUS, fill="#1a1a2e")

    # Thumbnail image
    if illustrated.image_path and Path(illustrated.image_path).exists():
        try:
            thumb = Image.open(illustrated.image_path)
            thumb = thumb.resize((w, thumb_h), Image.LANCZOS)
            mask = Image.new("L", (w, thumb_h), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle([0, 0, w, thumb_h], radius=CELL_RADIUS, fill=255)
            canvas.paste(thumb, (x, y), mask)
        except Exception as exc:
            logger.warning("Failed to paste thumbnail: %s", exc)
            draw.rectangle([x, y, x + w, y + thumb_h], fill="#333355")
    else:
        draw.rectangle([x, y, x + w, y + thumb_h], fill="#333355")

    # Repo name
    name = repo.repo.full_name
    if len(name) > 25:
        name = name[:23] + ".."
    draw.text((x + 10, y + thumb_h + 6), name, fill="white", font=font_title)

    # Language color dot + stars today
    lang_color = LANGUAGE_COLORS.get(repo.repo.language or "", "#888888")
    dot_y = y + thumb_h + 30
    draw.ellipse([x + 10, dot_y, x + 20, dot_y + 10], fill=lang_color)
    draw.text((x + 26, y + thumb_h + 28), f"+{repo.repo.stars_today}", fill="#aaaaaa", font=font_stars)
