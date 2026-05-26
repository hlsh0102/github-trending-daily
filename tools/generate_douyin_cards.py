"""Generate Douyin-style vertical cards from daily GitHub Trending articles."""

from __future__ import annotations

import math
import re
import textwrap
from dataclasses import dataclass
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
DAY = "2026-05-26"
DAILY_DIR = ROOT / "vault" / "Inno" / "GithubTrending" / DAY
ARTICLES_DIR = DAILY_DIR / "articles"
OUT_DIR = DAILY_DIR / "douyin"

W, H = 1080, 1920
PINK = "#ff2bd6"
CYAN = "#23f7ff"
YELLOW = "#ffe45c"
WHITE = "#f7f7fb"
MUTED = "#a7a7b8"
BLACK = "#070710"


@dataclass
class RepoCard:
    index: int
    repo: str
    filename: str
    language: str
    stars_total: int
    stars_today: int
    overview: str
    bullets: list[str]
    scenarios: list[str]


def font(size: int) -> ImageFont.FreeTypeFont:
    candidates = [
        Path("C:/Windows/Fonts/simhei.ttf"),
        Path("C:/Windows/Fonts/simsun.ttc"),
        ROOT / "assets" / "Inter.ttf",
    ]
    for candidate in candidates:
        if candidate.exists():
            return ImageFont.truetype(str(candidate), size=size)
    return ImageFont.load_default()


F = {
    "mega": font(118),
    "title": font(68),
    "h1": font(54),
    "h2": font(40),
    "body": font(34),
    "small": font(26),
    "tiny": font(22),
}


def clean_markdown(text: str) -> str:
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    text = re.sub(r"!\[[^\]]*\]\([^)]+\)", "", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"[*_`>#-]", "", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def parse_frontmatter(text: str) -> dict[str, str]:
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1]
    data: dict[str, str] = {}
    for line in block.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            data[key.strip()] = value.strip()
    return data


def section(text: str, title: str) -> str:
    pattern = rf"## {re.escape(title)}\n(.*?)(?=\n## |\Z)"
    match = re.search(pattern, text, flags=re.S)
    return match.group(1).strip() if match else ""


def bullets_from(text: str, limit: int = 3) -> list[str]:
    items = []
    for line in text.splitlines():
        line = line.strip()
        if line.startswith(("- ", "* ")):
            items.append(clean_markdown(line[2:]))
    if not items:
        for part in re.split(r"[。；;]\s*", clean_markdown(text)):
            if len(part) > 10:
                items.append(part)
    return [shorten(item, 42) for item in items[:limit]]


def shorten(text: str, length: int) -> str:
    text = clean_markdown(text)
    return text if len(text) <= length else text[: length - 1].rstrip() + "…"


def load_cards() -> list[RepoCard]:
    cards: list[RepoCard] = []
    for idx, path in enumerate(sorted(ARTICLES_DIR.glob("*.md")), start=1):
        text = path.read_text(encoding="utf-8")
        meta = parse_frontmatter(text)
        overview = clean_markdown(section(text, "项目概述"))
        if not overview:
            overview = clean_markdown(text.split("---", 2)[-1])
        bullets = bullets_from(section(text, "核心功能"))
        scenarios = bullets_from(section(text, "适用场景"), limit=2)
        cards.append(
            RepoCard(
                index=idx,
                repo=meta.get("repo", path.stem.split("-", 1)[-1].replace("__", "/")),
                filename=path.stem,
                language=meta.get("language", "Unknown"),
                stars_total=int(meta.get("stars_total", "0") or 0),
                stars_today=int(meta.get("stars_today", "0") or 0),
                overview=shorten(overview, 108),
                bullets=bullets,
                scenarios=scenarios,
            )
        )
    return cards


def gradient_bg() -> Image.Image:
    img = Image.new("RGB", (W, H), BLACK)
    px = img.load()
    for y in range(H):
        for x in range(W):
            dx = x / W
            dy = y / H
            r = int(7 + 22 * dx + 20 * (1 - dy))
            g = int(7 + 12 * dy)
            b = int(16 + 35 * dy + 22 * math.sin(dx * math.pi))
            px[x, y] = (r, g, b)
    return img


def glow(draw: ImageDraw.ImageDraw, xy: tuple[int, int], color: str, radius: int) -> None:
    x, y = xy
    for r in range(radius, 0, -18):
        alpha = int(70 * r / radius)
        draw.ellipse([x - r, y - r, x + r, y + r], fill=color + f"{alpha:02x}")


def rounded_panel(draw: ImageDraw.ImageDraw, box: tuple[int, int, int, int], fill: str, outline: str) -> None:
    draw.rounded_rectangle(box, radius=34, fill=fill, outline=outline, width=2)


def text_lines(text: str, max_chars: int) -> list[str]:
    lines: list[str] = []
    current = ""
    for char in text:
        if len(current) >= max_chars and char not in "，。；、,. ":
            lines.append(current)
            current = ""
        current += char
    if current:
        lines.append(current)
    return lines


def draw_text_block(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    max_chars: int,
    line_gap: int,
    font_obj: ImageFont.FreeTypeFont,
    fill: str = WHITE,
    max_lines: int | None = None,
) -> int:
    x, y = xy
    lines = text_lines(text, max_chars)
    if max_lines is not None:
        lines = lines[:max_lines]
    for line in lines:
        draw.text((x, y), line, font=font_obj, fill=fill)
        y += line_gap
    return y


def draw_stroked(
    draw: ImageDraw.ImageDraw,
    xy: tuple[int, int],
    text: str,
    font_obj: ImageFont.FreeTypeFont,
    fill: str,
    stroke: str = BLACK,
    width: int = 3,
) -> None:
    draw.text(xy, text, font=font_obj, fill=fill, stroke_width=width, stroke_fill=stroke)


def chip(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, color: str) -> int:
    x, y = xy
    pad_x, pad_y = 20, 11
    bbox = draw.textbbox((0, 0), text, font=F["small"])
    width = bbox[2] - bbox[0] + pad_x * 2
    height = bbox[3] - bbox[1] + pad_y * 2
    draw.rounded_rectangle([x, y, x + width, y + height], radius=22, fill=color, outline="#ffffff55", width=1)
    draw.text((x + pad_x, y + pad_y - 2), text, font=F["small"], fill=BLACK)
    return x + width + 14


def save_card(img: Image.Image, path: Path) -> None:
    img = img.filter(ImageFilter.UnsharpMask(radius=1.1, percent=120, threshold=3))
    img.save(path, "PNG", optimize=True)


def cover(cards: list[RepoCard]) -> None:
    img = gradient_bg().convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    glow(draw, (120, 220), PINK, 260)
    glow(draw, (930, 1420), CYAN, 360)
    draw.text((64, 76), "GitHub Trending", font=F["h2"], fill=CYAN)
    draw.text((64, 136), DAY, font=F["small"], fill=MUTED)
    draw.text((64, 250), "今天这 10 个", font=F["title"], fill=WHITE)
    draw.text((64, 332), "开源项目值得看", font=F["title"], fill=YELLOW)
    draw.text((64, 454), "AI 编程 / 安全技能 / 免费工具 / 自托管媒体", font=F["body"], fill="#ffffffdd")
    rounded_panel(draw, (64, 610, 1016, 1570), "#101024dd", "#ffffff22")
    y = 664
    for item in cards[:10]:
        num = f"{item.index:02d}"
        draw.text((104, y - 4), num, font=F["h2"], fill=PINK if item.index % 2 else CYAN)
        draw.text((196, y), shorten(item.repo, 31), font=F["body"], fill=WHITE)
        draw.text((196, y + 44), f"+{item.stars_today:,} stars · {item.language}", font=F["small"], fill=MUTED)
        y += 86
    draw.rounded_rectangle([64, 1660, 1016, 1790], radius=34, fill="#ff2bd622", outline=PINK, width=2)
    draw.text((104, 1694), "收藏这组图，晚上慢慢看源码", font=F["h2"], fill=WHITE)
    save_card(img.convert("RGB"), OUT_DIR / "00-cover.png")


def repo_card(card: RepoCard) -> None:
    img = gradient_bg().convert("RGBA")
    draw = ImageDraw.Draw(img, "RGBA")
    accent = PINK if card.index % 2 else CYAN
    glow(draw, (160, 260), accent, 260)
    glow(draw, (900, 1260), YELLOW if card.index in (1, 5, 9) else CYAN, 260)
    draw_stroked(draw, (64, 70), f"TOP {card.index:02d}", F["mega"], WHITE, stroke=BLACK, width=4)
    draw.text((70, 202), "GitHub 今日热榜", font=F["small"], fill=MUTED)
    draw.line([64, 260, 1016, 260], fill="#ffffff22", width=2)
    draw_text_block(draw, (64, 332), card.repo, 19, 62, F["h1"], WHITE, max_lines=2)
    x = 64
    x = chip(draw, (x, 504), card.language, CYAN)
    x = chip(draw, (x, 504), f"+{card.stars_today:,} stars", YELLOW)
    chip(draw, (x, 504), f"总星 {card.stars_total:,}", PINK)
    rounded_panel(draw, (64, 620, 1016, 940), "#101024e8", "#ffffff22")
    draw.text((104, 666), "一句话看懂", font=F["h2"], fill=accent)
    draw_text_block(draw, (104, 728), card.overview, 22, 44, F["body"], "#fffffff0", max_lines=3)
    rounded_panel(draw, (64, 1000, 1016, 1374), "#101024d8", "#ffffff22")
    draw.text((104, 1044), "为什么值得点开", font=F["h2"], fill=YELLOW)
    y = 1110
    for bullet in card.bullets[:3]:
        draw.ellipse([104, y + 10, 122, y + 28], fill=accent)
        y = draw_text_block(draw, (142, y), bullet, 30, 36, F["small"], WHITE, max_lines=1) + 22
    rounded_panel(draw, (64, 1434, 1016, 1704), "#101024d8", "#ffffff22")
    draw.text((104, 1476), "适合谁", font=F["h2"], fill=CYAN)
    if card.scenarios:
        y = 1540
        for scene in card.scenarios[:2]:
            draw.text((104, y), "·", font=F["body"], fill=CYAN)
            y = draw_text_block(draw, (142, y), scene, 30, 36, F["small"], "#ffffffe8", max_lines=1) + 18
    else:
        draw_text_block(draw, (104, 1540), "适合想快速发现高价值开源项目的开发者。", 25, 40, F["small"], "#ffffffe8")
    draw.text((64, 1816), "完整介绍见文章 · daily.md", font=F["small"], fill=MUTED)
    draw.text((760, 1810), "开源雷达", font=F["h2"], fill=accent)
    save_card(img.convert("RGB"), OUT_DIR / f"{card.index:02d}-{card.filename}.png")


def intro_text(cards: list[RepoCard]) -> str:
    names = "、".join(card.repo.split("/")[-1] for card in cards[:5])
    return (
        f"今天 GitHub Trending 前 10 已整理：{names} 等项目上榜。"
        "这一期重点集中在 AI 编程工作流、AI 内容去味、网络安全技能、免费域名与自托管媒体服务。"
        "如果你想快速发现值得收藏、能马上试用的开源工具，这 10 个项目可以先看一遍。\n\n"
        "#GitHub #开源项目 #AI工具 #程序员 #效率工具 #技术分享 #每日开源"
    )


def main() -> None:
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    cards = load_cards()
    cover(cards)
    for card in cards:
        repo_card(card)
    (OUT_DIR / "douyin_intro.md").write_text(intro_text(cards) + "\n", encoding="utf-8")
    print(f"generated={len(cards) + 1}")
    print(f"out={OUT_DIR}")


if __name__ == "__main__":
    main()
