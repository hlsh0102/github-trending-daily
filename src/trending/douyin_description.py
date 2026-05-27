"""Generate Douyin copy for the daily GitHub Trending list."""

import logging

from openai import OpenAI

from trending.config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    IllustratedRepo,
)

logger = logging.getLogger(__name__)

MAX_DESCRIPTION_CHARS = 1000

SYSTEM_PROMPT = """你是一个中文短视频科技账号文案编辑。

请为当天 GitHub Trending TOP10 生成一段抖音发布文案，要求：
- 1000 字以内。
- 必须覆盖全部 10 个项目，不要遗漏。
- 中文为主，保留英文项目名。
- 语气像科技资讯/开源日报，清楚、有节奏，但不要夸张营销。
- 可以用编号、短句和少量 emoji。
- 结尾带 4-8 个相关话题标签。
- 不要编造项目功能，不要写投资建议。
- 只输出可直接复制到抖音简介/文案区的正文，不要解释。"""


def generate_douyin_description(
    repos: list[IllustratedRepo],
    articles: dict[str, str] | None = None,
) -> str:
    """Generate <=1000 chars of Douyin copy via DeepSeek, with fallback."""
    try:
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
        text = _generate_one(client, repos, articles or {})
    except Exception as exc:
        logger.warning("Douyin description generation failed: %s. Using fallback.", exc)
        text = _fallback_description(repos)
    return _limit_text(text)


def _generate_one(
    client: OpenAI,
    repos: list[IllustratedRepo],
    articles: dict[str, str],
) -> str:
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        max_tokens=1800,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_context(repos, articles)},
        ],
    )
    return (response.choices[0].message.content or "").strip()


def _build_context(repos: list[IllustratedRepo], articles: dict[str, str]) -> str:
    lines = ["今日 GitHub Trending TOP10："]
    for i, item in enumerate(repos, start=1):
        repo = item.repo.repo
        article = articles.get(repo.full_name, "")
        lines.extend([
            "",
            f"{i}. {repo.full_name}",
            f"Language: {repo.language or 'Unknown'}",
            f"Stars: {repo.stars_total} total, +{repo.stars_today} today",
            f"Intro: {item.repo.intro_zh}",
        ])
        if article:
            lines.append(f"Article excerpt: {_limit_text(article, 500)}")
    return "\n".join(lines)


def _fallback_description(repos: list[IllustratedRepo]) -> str:
    lines = ["今天 GitHub Trending TOP10 速览："]
    for i, item in enumerate(repos, start=1):
        repo = item.repo.repo
        intro = _single_line(item.repo.intro_zh)
        lines.append(
            f"{i}. {repo.name}：{intro}（{repo.language or 'Unknown'}，"
            f"{_format_stars(repo.stars_total)}★，今日 +{_format_stars(repo.stars_today)}）"
        )
    lines.append("关注我，每天一分钟看懂全球开发者都在关注什么。")
    lines.append("#GitHub #开源项目 #AI工具 #程序员 #GitHubTrending #科技资讯")
    return _limit_text("\n".join(lines))


def _single_line(text: str, max_len: int = 46) -> str:
    clean = " ".join(text.split())
    if len(clean) <= max_len:
        return clean
    return clean[: max_len - 1].rstrip("，。；、 ") + "…"


def _limit_text(text: str, max_chars: int = MAX_DESCRIPTION_CHARS) -> str:
    clean = text.strip()
    if len(clean) <= max_chars:
        return clean
    return clean[: max_chars - 1].rstrip("，。；、 \n") + "…"


def _format_stars(stars: int) -> str:
    if stars >= 100_000:
        return f"{stars // 1000}K"
    if stars >= 1_000:
        return f"{stars / 1000:.1f}K"
    return str(stars)
