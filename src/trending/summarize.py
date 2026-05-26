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

2. gpt_image_prompt: A complete JSON object describing a "便当格 / Bento grid" infographic for gpt-image-2. This is a high-density modular information graphic. Use the schema below — fill EVERY module with real, repo-specific content (no TBD, no placeholders, no "..."):

{
  "type": "便当格 / Bento grid 高密度模块化信息图",
  "goal": "一张图说清这个 GitHub 项目是什么、为什么火、关键数据和卖点",
  "text_language": "zh-Hans",
  "canvas": {
    "aspect_ratio": "3:4 portrait",
    "background": "warm off-white #F5F2EC",
    "global_corner_radius": "24px",
    "module_gap": "16px"
  },
  "header": {
    "main_title": "owner/name",
    "subtitle": "一句中文定位（非英文），点出该项目核心价值",
    "title_position": "top-left, large bold sans-serif"
  },
  "palette": {
    "primary": "deep ink #1A1A1A",
    "accent": "warm gold #D4A574",
    "module_tints": ["#FFFFFF", "#F0EBE3", "#E8E2D8", "#FAF7F2"],
    "rule": "module backgrounds rotate among the tints; primary used for text; accent used at most twice across the whole image"
  },
  "layout": {
    "style": "asymmetric bento",
    "module_count": "choose 6 to 9 based on how much real content the repo offers",
    "grid": "irregular: 1 hero module (large, ~2x2 footprint) + 5-8 supporting modules of mixed 1x1 / 1x2 / 2x1 sizes",
    "alignment": "all modules share the same corner radius and gap; module edges align to an invisible grid"
  },
  "modules": [
    {
      "id": "M1-hero",
      "size": "large (2x2)",
      "role": "hero / 项目主推",
      "content": {
        "title": "项目名（中文化或保留 owner/name）",
        "subtitle": "一句中文核心价值",
        "metric": {"value": "实际 stars_total 数字", "label": "GitHub 星标"},
        "tags": ["实际语言", "实际许可证", "项目领域中文标签"],
        "visual": "isometric-illustration of the project's core concept"
      }
    },
    {
      "id": "M2",
      "size": "medium (1x2)",
      "role": "概览 / At a glance",
      "content": {
        "title": "概览",
        "items": [
          {"label": "编程语言", "value": "实际值"},
          {"label": "许可证", "value": "实际值"},
          {"label": "今日新增星标", "value": "+实际数字"}
        ]
      }
    },
    {
      "id": "M3",
      "size": "small (1x1)",
      "role": "关键数字 / 总星标",
      "content": {
        "title": "总星标数",
        "big_number": "实际 stars_total",
        "trend": "up"
      }
    },
    {
      "id": "M4",
      "size": "small (1x1)",
      "role": "关键数字 / 日增",
      "content": {
        "title": "日增星标",
        "big_number": "+实际 stars_today",
        "trend": "up"
      }
    },
    {
      "id": "M5",
      "size": "medium (1x2)",
      "role": "亮点 / 为何上榜",
      "content": {
        "title": "为何火热",
        "bullets": ["真实卖点 1", "真实卖点 2", "真实卖点 3"]
      }
    },
    {
      "id": "M6",
      "size": "medium (2x1)",
      "role": "描述 / About",
      "content": {
        "title": "关于",
        "text": "2-3 句中文总结：这个项目做什么 + 它最关键的差异化点。"
      }
    },
    {
      "id": "M7",
      "size": "medium (2x1)",
      "role": "对比 / 关键特性强度",
      "content": {
        "title": "关键特性",
        "bars": [
          {"label": "真实特性 1（中文标签）", "value": 90},
          {"label": "真实特性 2（中文标签）", "value": 80},
          {"label": "真实特性 3（中文标签）", "value": 70}
        ]
      }
    },
    {
      "id": "M8",
      "size": "small (1x1)",
      "role": "footer / 来源",
      "content": {
        "text": "github.com/owner/name",
        "icon": "github"
      }
    }
  ],
  "module_internal_style": {
    "padding": "16-24px inside each module",
    "typography": "sans-serif (Inter / Noto Sans SC); module micro-title in bold caps, body smaller",
    "imagery": "small product visuals / icons / micro-charts in every module — never a pure-text widget",
    "rule": "each module is self-contained and could stand alone"
  },
  "constraints": {
    "must_keep": [
      "所有模块统一 24px 圆角",
      "模块之间留固定 16px gap",
      "每个模块都有自己的 micro-title",
      "至少出现一个柱状对比图或一个超大数字",
      "整图配色不超过 5 种主色",
      "所有可见文字均为简体中文（除 owner/name、GitHub URL、icon 字段）",
      "header.subtitle 必须是中文一句定位"
    ],
    "avoid": [
      "所有模块尺寸一模一样（变成网格表）",
      "模块紧贴没有留白",
      "模块内只有文字（没有图标 / 数据可视化）",
      "模块边框使用粗描边 (>2px)",
      "渐变 / 玻璃质感模糊 bento 的极简感",
      "把英文标签留在最终图（如 'GitHub Stars' / 'At a Glance'）"
    ]
  }
}

CRITICAL RULES:
- ALL visible text in gpt_image_prompt MUST be in Chinese (简体中文). The ONLY exceptions are: repo full name (e.g. "owner/name"), the GitHub URL, the literal value "github" of the icon field, and color hex codes.
- header.subtitle must be a Chinese one-line positioning, NOT English.
- All module micro-titles, metric labels, bar labels, bullets, and descriptions must be Chinese (e.g. "GitHub 星标" not "GitHub Stars"; "概览" not "At a Glance").
- Fill EVERY module with real, specific content from the repo's README, description, and metadata. No "feature_1" / "reason 1" placeholders.
- big_number / metric.value must be the actual star counts provided in the context.
- bars and bullets must reflect real features/characteristics of the project.
- module_count: choose between 6 and 9 based on available real content; do NOT pad with empty modules.
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
