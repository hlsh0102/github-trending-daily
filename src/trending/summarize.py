"""Generate Chinese intros and English image prompts via Claude API."""
import json
import logging

from anthropic import Anthropic

from trending.config import (
    EnrichedRepo,
    SummarizedRepo,
    ANTHROPIC_API_KEY,
    PLACEHOLDER_IMAGE_PROMPT_TEMPLATE,
)

logger = logging.getLogger(__name__)

SYSTEM_PROMPT = """You are a technical writer who produces structured JSON output.
For each GitHub repository, write:
- intro_zh: 2-3 sentence Chinese introduction. Explain what this project is, what problem it solves, and who it is for.
- image_prompt_en: One English sentence prompt for DALL-E 3, isometric illustration style, no text/labels in the image.

Output ONLY valid JSON. No markdown fences, no extra text."""


def summarize(repos: list[EnrichedRepo]) -> list[SummarizedRepo]:
    """Generate intros and image prompts for each repo via Claude API.
    Individual failures fall back to description-based intro and generic prompt.
    """
    client = Anthropic(api_key=ANTHROPIC_API_KEY)
    results: list[SummarizedRepo] = []

    for repo in repos:
        try:
            sr = _summarize_one(client, repo)
            results.append(sr)
        except Exception as exc:
            logger.warning("Claude API failed for %s: %s. Using fallback.", repo.full_name, exc)
            results.append(_fallback(repo))

    return results


def _summarize_one(client: Anthropic, repo: EnrichedRepo) -> SummarizedRepo:
    context = _build_context(repo)
    message = client.messages.create(
        model="claude-sonnet-4-6-20250514",
        max_tokens=512,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": context}],
    )
    raw = message.content[0].text
    data = json.loads(raw)
    return SummarizedRepo(
        repo=repo,
        intro_zh=data.get("intro_zh", repo.description or ""),
        image_prompt_en=data.get(
            "image_prompt_en",
            PLACEHOLDER_IMAGE_PROMPT_TEMPLATE.format(full_name=repo.full_name),
        ),
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
        image_prompt_en=PLACEHOLDER_IMAGE_PROMPT_TEMPLATE.format(full_name=repo.full_name),
    )
