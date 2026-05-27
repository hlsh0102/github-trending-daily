"""Generate differentiated visual hints for Douyin project cards."""

import json
import logging
import re

from openai import OpenAI

from trending.config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    IllustratedRepo,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """你是短视频科技封面的视觉创意总监。

请为每个 GitHub Trending 项目生成一个差异化的中文主视觉描述，用于 9:16 抖音项目介绍图。

要求：
- 每个 visual_hint 必须明显不同，不要都写成“发光代码仓库、节点网络、AI核心”。
- 结合项目用途、目标用户、技术场景来设计主视觉。
- 每条 25-60 个汉字，具体可画，不要抽象口号。
- 保持暗色科技风、3D等距/高级科技封面感。
- 不要要求画长段落文字。
- 只输出 JSON 对象，key 是 full_name，value 是 visual_hint。"""


def generate_visual_hints(
    repos: list[IllustratedRepo],
    articles: dict[str, str] | None = None,
) -> dict[str, str]:
    """Generate per-repo visual hints with rule-based fallback."""
    fallback = {
        item.repo.repo.full_name: fallback_visual_hint(item)
        for item in repos
    }
    try:
        client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
        generated = _generate_one(client, repos, articles or {})
    except Exception as exc:
        logger.warning("Visual hint generation failed: %s. Using fallback.", exc)
        return fallback

    return {
        key: _clean_hint(generated.get(key)) or fallback[key]
        for key in fallback
    }


def fallback_visual_hint(item: IllustratedRepo) -> str:
    """Rule-based visual hint used when LLM output is unavailable."""
    repo = item.repo.repo
    intro = item.repo.intro_zh
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if "knowledge-work-plugins" in text or "knowledge work" in text or "知识工作" in text:
        return "知识工作桌面同时展开文档、日历、邮件和检索面板，Claude插件在中心调度"
    if "stop-slop" in text or "ai 痕迹" in text or "ai味" in text or "ai 味" in text:
        return "文本清洗工作台把AI模板化句子送入过滤器，输出更自然的人类表达"
    if "taste-skill" in text or "品味" in text or "审美" in text:
        return "设计评审仪对比粗糙稿和精修稿，审美刻度盘点亮关键改进点"
    if "awesome-free-apps" in text or "free apps" in text or "免费应用" in text:
        return "多平台免费应用陈列墙展示电脑和手机图标，下载清单像应用商店看板"
    if "ai-engineering" in text or "ai engineering" in text or "人工智能工程" in text:
        return "AI工程学习路线图连接课程文件夹、模型训练、数据处理和云端部署模块"
    if "知识图谱" in text or "knowledge graph" in text or "graph" in text:
        return "代码文件中生长出可交互知识图谱，节点连线展示仓库结构和提问路径"
    if "security" in text or "cyber" in text:
        return "安全作战台连接盾牌、漏洞告警、攻击矩阵和终端审计面板"
    if "agent" in text or "claude" in text or "cursor" in text:
        return "AI编码助手控制台连接记忆、技能、安全策略和工具调用模块"
    if "domain" in text or "域名" in text:
        return "域名雷达地图上漂浮免费域名卡片，连接个人网站和DNS节点"
    if "media" in text or "video" in text or "媒体" in text:
        return "家庭媒体服务器向电视、平板、手机推送影片库的多屏播放网络"
    if "compiler" in text or "编译" in text or repo.language == "C":
        return "代码文件进入编译器芯片，输出二进制光流和极简语法树"
    return "项目控制台展示核心功能模块、星标增长曲线和开发者工作流"


def _generate_one(
    client: OpenAI,
    repos: list[IllustratedRepo],
    articles: dict[str, str],
) -> dict[str, str]:
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        max_tokens=2500,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": _build_context(repos, articles)},
        ],
    )
    raw = response.choices[0].message.content or "{}"
    data = _parse_json_object(raw)
    if not isinstance(data, dict):
        return {}
    return {str(key): str(value) for key, value in data.items()}


def _build_context(repos: list[IllustratedRepo], articles: dict[str, str]) -> str:
    lines = ["请为以下项目分别生成 visual_hint："]
    for i, item in enumerate(repos, start=1):
        repo = item.repo.repo
        lines.extend([
            "",
            f"{i}. {repo.full_name}",
            f"Language: {repo.language or 'Unknown'}",
            f"Stars: {repo.stars_total} total, +{repo.stars_today} today",
            f"Intro: {item.repo.intro_zh}",
        ])
        article = articles.get(repo.full_name)
        if article:
            lines.append(f"Article excerpt: {article[:700]}")
    return "\n".join(lines)


def _parse_json_object(raw: str) -> dict:
    try:
        data = json.loads(raw)
    except json.JSONDecodeError:
        match = json.loads(_extract_json(raw))
        data = match
    if not isinstance(data, dict):
        return {}
    return data


def _extract_json(raw: str) -> str:
    text = raw.strip()
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?\s*", "", text)
        text = re.sub(r"\s*```$", "", text)
    start = text.find("{")
    end = text.rfind("}")
    if start == -1 or end == -1 or end <= start:
        return "{}"
    return text[start : end + 1]


def _clean_hint(value: str | None) -> str:
    if not value:
        return ""
    clean = " ".join(str(value).split()).strip()
    if len(clean) <= 180:
        return clean
    punct_positions = [
        clean.rfind(mark, 0, 180)
        for mark in ["。", "；", "，", ","]
    ]
    cut = max(punct_positions)
    if cut >= 50:
        return clean[: cut + 1]
    return clean[:180].rstrip("，。；、 ")
