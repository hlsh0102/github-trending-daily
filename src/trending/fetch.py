"""Scrape GitHub Trending page for top 10 repos."""
import time
import logging
import re

import requests
from bs4 import BeautifulSoup, Tag

from trending.config import Repo, TRENDING_URL, USER_AGENT

logger = logging.getLogger(__name__)


def fetch_trending(period: str = "daily") -> list[Repo]:
    """Fetch and parse GitHub Trending top 10."""
    url = f"{TRENDING_URL}?since={period}"
    html = _fetch_html(url)
    repos = parse_trending_html(html)
    if len(repos) < 10:
        raise RuntimeError(f"Expected at least 10 trending repos, got {len(repos)}")
    return repos[:10]


def _fetch_html(url: str) -> str:
    """GET the URL with retry logic."""
    last_exc = None
    for attempt in range(3):
        try:
            resp = requests.get(url, headers={"User-Agent": USER_AGENT}, timeout=30)
            resp.raise_for_status()
            return resp.text
        except requests.RequestException as e:
            last_exc = e
            logger.warning("Attempt %d failed: %s", attempt + 1, e)
            if attempt < 2:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"Failed to fetch trending after 3 attempts: {last_exc}")


def parse_trending_html(html: str) -> list[Repo]:
    """Parse trending page HTML into Repo objects."""
    soup = BeautifulSoup(html, "html.parser")
    repos: list[Repo] = []
    for article in soup.find_all("article", class_="Box-row"):
        try:
            repo = _parse_one_article(article)
            if repo:
                repos.append(repo)
        except Exception as exc:
            logger.warning("Failed to parse one article: %s", exc)
            continue
    return repos


def _parse_one_article(article: Tag) -> Repo | None:
    """Parse a single article.Box-row into a Repo."""
    h2 = article.find("h2", class_="h3")
    if not h2:
        return None
    link = h2.find("a")
    if not link:
        return None

    href = (link.get("href") or "").strip().lstrip("/")
    if not href:
        return None
    parts = href.split("/")
    if len(parts) < 2:
        return None
    owner, name = parts[0], parts[1]
    full_name = f"{owner}/{name}"
    url = f"https://github.com/{full_name}"

    # Description
    desc_el = article.find("p", class_="col-9")
    description = desc_el.get_text(strip=True) if desc_el else None

    # Language
    lang_el = article.find("span", itemprop="programmingLanguage")
    language = lang_el.get_text(strip=True) if lang_el else None

    # Stars today
    stars_today = 0
    float_right = article.find("span", class_="float-sm-right")
    if float_right:
        nums = "".join(ch for ch in float_right.get_text(strip=True) if ch.isdigit())
        if nums:
            stars_today = int(nums)

    # Total stars
    stars_total = 0
    for a in article.find_all("a"):
        href_text = (a.get("href") or "").strip()
        if href_text.endswith("/stargazers"):
            nums = "".join(ch for ch in a.get_text(strip=True).replace(",", "") if ch.isdigit())
            if nums:
                stars_total = int(nums)
            break

    return Repo(
        owner=owner,
        name=name,
        full_name=full_name,
        description=description,
        language=language,
        stars_total=stars_total,
        stars_today=stars_today,
        url=url,
    )
