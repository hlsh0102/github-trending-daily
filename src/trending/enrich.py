"""Enrich repos with GitHub REST API data."""
import logging
import re

import requests

from trending.config import EnrichedRepo, Repo, GITHUB_TOKEN

logger = logging.getLogger(__name__)

API_BASE = "https://api.github.com/repos"
HEADERS = {
    "Accept": "application/vnd.github+json",
    "X-GitHub-Api-Version": "2022-11-28",
}
if GITHUB_TOKEN:
    HEADERS["Authorization"] = f"Bearer {GITHUB_TOKEN}"


def enrich(repos: list[Repo]) -> list[EnrichedRepo]:
    """Enrich each repo with README, avatar, license, default_branch.
    Individual failures leave fields empty; other repos proceed.
    """
    enriched: list[EnrichedRepo] = []
    for repo in repos:
        enriched.append(_enrich_one(repo))
    return enriched


def _enrich_one(repo: Repo) -> EnrichedRepo:
    enriched = EnrichedRepo(
        owner=repo.owner, name=repo.name, full_name=repo.full_name,
        description=repo.description, language=repo.language,
        stars_total=repo.stars_total, stars_today=repo.stars_today,
        url=repo.url,
    )
    try:
        data = _fetch_repo_data(repo.full_name)
        enriched.readme_head = data.get("readme_head")
        enriched.avatar_url = data.get("avatar_url")
        enriched.license_spdx = data.get("license_spdx")
        enriched.default_branch = data.get("default_branch")
    except Exception as exc:
        logger.warning("Failed to enrich %s: %s", repo.full_name, exc)
    return enriched


def _fetch_repo_data(full_name: str) -> dict:
    """Fetch repo metadata from GitHub REST API."""
    resp = requests.get(f"{API_BASE}/{full_name}", headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    readme_head = _fetch_readme_head(full_name, data.get("default_branch", "main"))
    license_spdx = data.get("license", {}).get("spdx_id") if data.get("license") else None

    return {
        "readme_head": readme_head,
        "avatar_url": data.get("owner", {}).get("avatar_url"),
        "license_spdx": license_spdx,
        "default_branch": data.get("default_branch"),
    }


def _fetch_readme_head(full_name: str, default_branch: str) -> str | None:
    """Fetch first ~1500 chars of README, stripping badges/HTML comments."""
    try:
        resp = requests.get(
            f"{API_BASE}/{full_name}/readme",
            headers={**HEADERS, "Accept": "application/vnd.github.raw+json"},
            timeout=15,
        )
        resp.raise_for_status()
        text = resp.text
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text[:1500].strip()
    except Exception:
        return None
