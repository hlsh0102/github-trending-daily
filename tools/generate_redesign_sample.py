"""Generate one redesigned Douyin-style sample card."""

from __future__ import annotations

import math
import random
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "vault" / "Inno" / "GithubTrending" / "2026-05-26" / "douyin" / "redesign-sample-01.png"
W, H = 1080, 1920
FONT_BOLD = "C:/Windows/Fonts/msyhbd.ttc"
FONT_MED = "C:/Windows/Fonts/msyh.ttc"


def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size=size)


F = {
    "kicker": font(FONT_MED, 34),
    "mega": font(FONT_BOLD, 118),
    "title": font(FONT_BOLD, 86),
    "h": font(FONT_BOLD, 40),
    "body": font(FONT_MED, 32),
    "small": font(FONT_MED, 27),
}


def blur_ellipse(cx: int, cy: int, rx: int, ry: int, color: str, alpha: int, blur: int = 70) -> Image.Image:
    layer = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer, "RGBA")
    draw.ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=color + f"{alpha:02x}")
    return layer.filter(ImageFilter.GaussianBlur(blur))


def main() -> None:
    img = Image.new("RGB", (W, H), "#07070b")
    px = img.load()
    for y in range(H):
        for x in range(W):
            dx, dy = x / W, y / H
            r = int(6 + 16 * dy + 12 * math.sin(dx * math.pi))
            g = int(7 + 10 * dx)
            b = int(14 + 24 * (1 - dy) + 12 * math.sin((dx + dy) * math.pi))
            px[x, y] = (r, g, b)

    img = img.convert("RGBA")
    img.alpha_composite(blur_ellipse(840, 250, 430, 220, "#00f5ff", 86, 90))
    img.alpha_composite(blur_ellipse(190, 1450, 360, 300, "#ff2bd6", 78, 100))
    img.alpha_composite(blur_ellipse(1000, 1580, 250, 360, "#a6ff00", 44, 90))
    draw = ImageDraw.Draw(img, "RGBA")

    for off, col, alpha in [(0, "#00f5ff", 42), (42, "#ff2bd6", 34), (86, "#ffffff", 18)]:
        draw.polygon([(W - 70 + off, 0), (W + 90 + off, 0), (610 + off, H), (450 + off, H)], fill=col + f"{alpha:02x}")
    for x in range(64, W - 64, 16):
        color = "#00f5ff" if (x // 16) % 2 else "#ff2bd6"
        draw.rounded_rectangle([x, 62, x + 8, 70], radius=4, fill=color)

    def stroked(x: int, y: int, text: str, font_obj: ImageFont.FreeTypeFont, fill: str, width: int = 3) -> None:
        draw.text((x, y), text, font=font_obj, fill=fill, stroke_width=width, stroke_fill="#000000")

    stroked(64, 104, "GitHub 今日热榜 · TOP 01", F["kicker"], "#8cf7ff", 1)
    draw.text((64, 154), "2026.05.26", font=F["small"], fill="#ffffff99")
    for dx, color in [(-5, "#00f5ff"), (5, "#ff2bd6"), (0, "#ffffff")]:
        draw.text((690 + dx, 92), "01", font=F["mega"], fill=color + "ee")

    y = 326
    for i, line in enumerate(["把代码库", "变成一张", "可提问地图"]):
        stroked(64, y, line, F["title"], "#ccff00" if i == 2 else "#ffffff", 3)
        y += 106

    draw.rounded_rectangle([64, 690, 770, 752], radius=31, fill="#11151ee8", outline="#8cf7ff88", width=2)
    draw.text((92, 706), "Lum1104 / Understand-Anything", font=F["small"], fill="#ffffff")

    random.seed(2)
    nodes = [(760, 610), (910, 690), (820, 790), (960, 875), (730, 915), (880, 1010), (990, 1120)]
    for i, (x1, y1) in enumerate(nodes):
        for j, (x2, y2) in enumerate(nodes):
            if j > i and (j - i in (1, 2) or random.random() < 0.18):
                draw.line([x1, y1, x2, y2], fill="#8cf7ff55", width=3)
    for i, (x, y) in enumerate(nodes):
        color = "#ccff00" if i == 0 else ("#00f5ff" if i % 2 else "#ff2bd6")
        draw.ellipse([x - 18, y - 18, x + 18, y + 18], fill=color, outline="#ffffff", width=2)
        draw.ellipse([x - 38, y - 38, x + 38, y + 38], outline=color + "40", width=2)

    draw.rounded_rectangle([64, 865, 660, 1126], radius=42, fill="#10131bcc", outline="#ffffff33", width=2)
    draw.text((102, 914), "为什么火？", font=F["h"], fill="#ffffff")
    draw.text((102, 980), "AI 写的代码越来越多，", font=F["body"], fill="#ffffffe8")
    draw.text((102, 1026), "但理解成本也越来越高。", font=F["body"], fill="#ffffffe8")

    for x, val, label in [(64, "+5,604", "今日新增"), (382, "33,820", "总 Star"), (700, "TS", "语言")]:
        draw.rounded_rectangle([x, 1196, x + 290, 1328], radius=34, fill="#11151ee8", outline="#ffffff30", width=2)
        draw.text((x + 28, 1222), val, font=F["h"], fill="#ccff00" if val.startswith("+") else "#ffffff")
        draw.text((x + 30, 1276), label, font=F["small"], fill="#9ca3af")

    draw.rounded_rectangle([64, 1408, 1016, 1736], radius=52, fill="#f3f5ff", outline="#ffffff", width=2)
    draw.text((104, 1454), "一句话总结", font=F["h"], fill="#111114")
    for y, line in [
        (1524, "它把陌生代码仓库解析成可视化知识图谱，"),
        (1572, "让你像问 ChatGPT 一样追问函数、依赖"),
        (1620, "和模块关系。"),
    ]:
        draw.text((104, y), line, font=F["body"], fill="#17171f")

    draw.rounded_rectangle([64, 1788, 1016, 1858], radius=35, fill="#ff2bd6")
    draw.text((112, 1804), "适合：接手旧项目 / AI代码审查 / 技术讲解", font=F["small"], fill="#ffffff")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    img.convert("RGB").save(OUT, quality=95)
    print(OUT)


if __name__ == "__main__":
    main()
