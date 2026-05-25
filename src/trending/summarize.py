"""Generate Chinese intros via DeepSeek API (OpenAI-compatible)."""
import json
import logging

from openai import OpenAI

from trending.config import (
    EnrichedRepo,
    SummarizedRepo,
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a technical writer who produces structured JSON output.

For each GitHub repository, write TWO things:

1. intro_zh: 2-3 sentence Chinese introduction. Explain what this project is, what problem it solves, and who it is for.

2. gpt_image_prompt: A complete JSON object describing a "便当格 / Bento grid" infographic for gpt-image-2. This is a high-density modular information graphic in 3:4 portrait. Follow this exact schema and fill EVERY module with real content derived from the repo — no TBD, no placeholders:

{
  "type": "便当格 / Bento grid 高密度模块化信息图",
  "canvas": {
    "width": 1080,
    "height": 1440,
    "ratio": "3:4",
    "background": "#F5F2EC",
    "corner_radius": 24,
    "module_gap": 16,
    "padding": 24
  },
  "header": {
    "main_title": "owner/name",
    "subtitle": "one-line positioning in English",
    "position": "top-left"
  },
  "palette": {
    "primary_ink": "#1A1A1A",
    "accent": "#D4A574",
    "module_tints": ["#FFFFFF", "#F0EBE3", "#E8E2D8", "#FAF7F2"]
  },
  "layout": "asymmetric-bento",
  "modules": [
    {
      "id": "M1",
      "position": {"row": 1, "col": 1, "row_span": 2, "col_span": 2},
      "size": "2x2",
      "content_type": "hero",
      "content": {
        "title": "Project name",
        "subtitle": "One-line pitch",
        "metric": {"value": "stars_count", "label": "GitHub Stars"},
        "tags": ["language", "license", "domain"],
        "visual": "isometric-illustration"
      }
    },
    {
      "id": "M2",
      "position": {"row": 1, "col": 3, "row_span": 2, "col_span": 1},
      "size": "1x2",
      "content_type": "stats",
      "content": {
        "title": "At a Glance",
        "items": [
          {"label": "Language", "value": "..."},
          {"label": "License", "value": "..."},
          {"label": "Stars Today", "value": "+N"}
        ]
      }
    },
    {
      "id": "M3",
      "position": {"row": 3, "col": 1, "row_span": 1, "col_span": 1},
      "size": "1x1",
      "content_type": "metric",
      "content": {
        "title": "Total Stars",
        "big_number": "stars_total",
        "trend": "up"
      }
    },
    {
      "id": "M4",
      "position": {"row": 3, "col": 2, "row_span": 1, "col_span": 1},
      "size": "1x1",
      "content_type": "metric",
      "content": {
        "title": "Daily Gain",
        "big_number": "+stars_today",
        "trend": "up"
      }
    },
    {
      "id": "M5",
      "position": {"row": 3, "col": 3, "row_span": 2, "col_span": 1},
      "size": "1x2",
      "content_type": "highlight",
      "content": {
        "title": "Why Trending",
        "bullets": ["reason 1", "reason 2", "reason 3"]
      }
    },
    {
      "id": "M6",
      "position": {"row": 4, "col": 1, "row_span": 1, "col_span": 2},
      "size": "2x1",
      "content_type": "description",
      "content": {
        "title": "About",
        "text": "2-3 sentence English summary of what this project does and its key differentiator."
      }
    },
    {
      "id": "M7",
      "position": {"row": 5, "col": 1, "row_span": 1, "col_span": 2},
      "size": "2x1",
      "content_type": "comparison",
      "content": {
        "title": "Key Features",
        "bars": [
          {"label": "feature_1", "value": 95},
          {"label": "feature_2", "value": 80},
          {"label": "feature_3", "value": 70}
        ]
      }
    },
    {
      "id": "M8",
      "position": {"row": 5, "col": 3, "row_span": 1, "col_span": 1},
      "size": "1x1",
      "content_type": "footer",
      "content": {
        "text": "github.com/owner/name",
        "icon": "github"
      }
    }
  ],
  "module_internal_style": {
    "padding": 20,
    "font_family": "Inter, Noto Sans SC",
    "micro_title": {"size": 11, "color": "#8C8C8C", "text_transform": "uppercase"}
  },
  "constraints": [
    "统一 24px 圆角",
    "每个模块必须填充内容，禁止留空或写 TBD",
    "至少出现一个柱状对比图或大数字",
    "8 个模块全部填满"
  ]
}

CRITICAL RULES:
- Fill EVERY module with real, specific content from the repo's README, description, and metadata.
- big_number values must be the actual star counts provided in the context.
- bars and bullets must reflect real features/characteristics of the project.
- The JSON must be complete and valid — no truncation, no ellipsis, no "..." as placeholder.

Output ONLY a single JSON object with two keys: intro_zh (string) and gpt_image_prompt (object). No markdown fences, no extra text."""


def summarize(repos: list[EnrichedRepo]) -> list[SummarizedRepo]:
    """Generate Chinese intros for each repo via DeepSeek API.
    Individual failures fall back to description-based intro.
    """
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    results: list[SummarizedRepo] = []

    for repo in repos:
        try:
            sr = _summarize_one(client, repo)
            results.append(sr)
        except Exception as exc:
            logger.warning("DeepSeek API failed for %s: %s. Using fallback.", repo.full_name, exc)
            results.append(_fallback(repo))

    return results


def _summarize_one(client: OpenAI, repo: EnrichedRepo) -> SummarizedRepo:
    context = _build_context(repo)
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        max_tokens=4096,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context},
        ],
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    gpt_prompt = data.get("gpt_image_prompt", {})
    return SummarizedRepo(
        repo=repo,
        intro_zh=data.get("intro_zh", repo.description or ""),
        image_prompt_en="",
        gpt_image_prompt=json.dumps(gpt_prompt, ensure_ascii=False) if gpt_prompt else "",
    )


def _build_context(repo: EnrichedRepo) -> str:
    parts = [f"Repository: {repo.full_name}"]
    if repo.description:
        parts.append(f"Description: {repo.description}")
    if repo.language:
        parts.append(f"Language: {repo.language}")
    if repo.readme_head:
        parts.append(f"README excerpt:\n{repo.readme_head}")
    if repo.license_spdx:
        parts.append(f"License: {repo.license_spdx}")
    parts.append(f"Stars: {repo.stars_total} total, +{repo.stars_today} today")
    return "\n\n".join(parts)


def _fallback(repo: EnrichedRepo) -> SummarizedRepo:
    return SummarizedRepo(
        repo=repo,
        intro_zh=repo.description or f"{repo.full_name} — GitHub Trending 项目。",
        image_prompt_en="",
        gpt_image_prompt="",
    )
