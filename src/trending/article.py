"""Generate detailed Chinese articles via DeepSeek API (OpenAI-compatible)."""
import logging

from openai import OpenAI

from trending.config import (
    DEEPSEEK_API_KEY,
    DEEPSEEK_BASE_URL,
    DEEPSEEK_MODEL,
    EnrichedRepo,
    IllustratedRepo,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """你是一名中文技术写作者，需要为 GitHub 仓库撰写一篇 800–1500 字的详细中文介绍文章。

严格按照以下 Markdown 结构输出，且**只输出正文 Markdown**（不要包含 frontmatter、不要用代码围栏包裹整篇文章、不要添加最外层一级标题）：

## 项目概述
说明这是什么项目、解决了什么问题、目标用户。

## 核心功能
列出 3–6 项主要功能，使用无序列表。

## 技术架构
描述项目使用的关键技术、设计思路或架构特点。

## 安装与使用
给出基本的安装步骤和最小可用示例。如果上下文信息不足，可基于常见做法概述。

## 适用场景
列出 2–4 个典型使用场景。

## 项目亮点
强调与同类项目相比的差异化优势。

## 相关链接
- [GitHub 仓库](https://github.com/{owner}/{name})
- 如有官网/文档/演示，再列出相应链接

要求：
- 全文使用简体中文。
- 客观、准确、避免营销化修辞。
- 不要重复段落标题以外的内容。
- 字数控制在 800–1500 字之间。"""


def generate_articles(repos: list[IllustratedRepo]) -> dict[str, str]:
    """Generate detailed Chinese articles for each repo via DeepSeek.

    Returns dict mapping ``full_name`` → markdown body string.
    Body contains no frontmatter; the render layer injects it.
    On per-repo failure, falls back to ``intro_zh``.
    """
    client = OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)
    results: dict[str, str] = {}

    for ir in repos:
        full_name = ir.repo.repo.full_name
        try:
            results[full_name] = _generate_one(client, ir.repo.repo)
        except Exception as exc:
            logger.warning(
                "Article generation failed for %s: %s. Using fallback.",
                full_name,
                exc,
            )
            results[full_name] = ir.repo.intro_zh

    return results


def _generate_one(client: OpenAI, repo: EnrichedRepo) -> str:
    context = _build_context(repo)
    response = client.chat.completions.create(
        model=DEEPSEEK_MODEL,
        max_tokens=4096,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context},
        ],
    )
    body = response.choices[0].message.content or ""
    return body.strip()


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
