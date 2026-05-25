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
For each GitHub repository, write:
- intro_zh: 2-3 sentence Chinese introduction. Explain what this project is, what problem it solves, and who it is for.

Output ONLY valid JSON. No markdown fences, no extra text."""


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
        max_tokens=512,
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": context},
        ],
    )
    raw = response.choices[0].message.content
    data = json.loads(raw)
    return SummarizedRepo(
        repo=repo,
        intro_zh=data.get("intro_zh", repo.description or ""),
        image_prompt_en="",
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
    )
