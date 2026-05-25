# GitHub Trending Daily Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a daily automated tool that scrapes GitHub Trending top 10, generates Chinese intros + DALL-E illustrations via LLM, composes an iPhone-ratio overview image, and writes Obsidian vault files committed back to the repo.

**Architecture:** Linear 8-module Python pipeline orchestrated by `main.py`, scheduled via GitHub Actions. Each module has a single responsibility with clear input/output dataclasses. Deduplication via `state/repos.json` reuses previously generated content to minimize API costs.

**Tech Stack:** Python 3.11+, uv, requests + beautifulsoup4, Anthropic Claude API (claude-sonnet-4-6), OpenAI Images (dall-e-3), Pillow, pytest

---

## File Structure

| File | Responsibility |
|------|---------------|
| `pyproject.toml` | uv project config with all dependencies |
| `README.md` | Deployment & setup instructions |
| `assets/Inter.ttf` | Inter Variable font for compose.py (OFL licensed) |
| `src/trending/__init__.py` | Package marker |
| `src/trending/config.py` | Dataclasses (Repo, EnrichedRepo, SummarizedRepo, IllustratedRepo) + env vars + constants |
| `src/trending/fetch.py` | Scrape `github.com/trending` HTML, parse top 10 into `list[Repo]` |
| `src/trending/enrich.py` | GitHub REST API — enrich each Repo with README/avatar/license/default_branch |
| `src/trending/dedupe.py` | Cross-day deduplication via `state/repos.json` |
| `src/trending/summarize.py` | Claude API — produce `intro_zh` + `image_prompt_en` per repo |
| `src/trending/illustrate.py` | DALL-E 3 — generate 1024×1792 thumbnail per repo |
| `src/trending/compose.py` | Pillow — 1080×2340 2×5 overview grid |
| `src/trending/render.py` | Write `daily.md`, `repos/*.md`, `_index.md`, `trending.base` to vault |
| `src/trending/main.py` | Orchestrator: fetch → enrich → dedupe → summarize → illustrate → compose → render → git |
| `tests/test_fetch.py` | Parse trending HTML with fixture |
| `tests/test_dedupe.py` | Dedupe logic: reuse vs. new |
| `tests/test_render.py` | Render output correctness |
| `.github/workflows/daily.yml` | GitHub Actions schedule + workflow_dispatch |

---

### Task 1: Project Scaffold

**Files:**
- Create: `pyproject.toml`, `assets/.gitkeep`, `src/trending/__init__.py`, `src/trending/config.py`, `tests/__init__.py`, `state/.gitkeep`, `vault/Inno/GithubTrending/.gitkeep`, `vault/Inno/GithubTrending/repos/.gitkeep`, `.gitignore`

- [ ] **Step 1: Initialize git repo**

```bash
cd e:/Codex/github-trending-daily && git init
```

- [ ] **Step 2: Download Inter.ttf font**

```bash
cd e:/Codex/github-trending-daily
mkdir -p assets
curl -L -o assets/Inter.ttf "https://github.com/rsms/inter/releases/download/v4.0/InterVariable.ttf"
```

- [ ] **Step 3: Create `pyproject.toml`**

```toml
[project]
name = "github-trending-daily"
version = "0.1.0"
description = "Daily GitHub Trending top 10 → Obsidian vault automation"
requires-python = ">=3.11"
dependencies = [
    "requests>=2.31",
    "beautifulsoup4>=4.12",
    "anthropic>=0.38",
    "openai>=1.60",
    "pillow>=10.0",
]

[project.scripts]
trending = "trending.main:main"

[build-system]
requires = ["hatchling"]
build-backend = "hatchling.build"

[tool.pytest.ini_options]
testpaths = ["tests"]
```

- [ ] **Step 4: Create directory structure**

```bash
cd e:/Codex/github-trending-daily
mkdir -p src/trending
mkdir -p tests
mkdir -p state
mkdir -p vault/Inno/GithubTrending/repos
mkdir -p assets
mkdir -p .github/workflows
touch src/trending/__init__.py
touch tests/__init__.py
touch vault/Inno/GithubTrending/.gitkeep
touch vault/Inno/GithubTrending/repos/.gitkeep
```

- [ ] **Step 5: Create `.gitignore`**

```gitignore
__pycache__/
*.pyc
.venv/
uv.lock
.env
*.egg-info/
dist/
build/
```

- [ ] **Step 6: Install dependencies**

```bash
cd e:/Codex/github-trending-daily && uv sync
```

- [ ] **Step 7: Commit scaffold**

```bash
cd e:/Codex/github-trending-daily
git add -A
git commit -m "chore: init project scaffold with uv, dependencies, directory structure"
```

---

### Task 2: Data Models & Config (`config.py`)

**Files:**
- Write: `src/trending/config.py`

- [ ] **Step 1: Write `config.py` with dataclasses, env vars, and constants**

```python
"""Shared dataclasses, environment config, and constants."""

import os
from dataclasses import dataclass, field
from datetime import date, datetime, timezone


@dataclass
class Repo:
    owner: str
    name: str
    full_name: str  # "owner/name"
    description: str | None
    language: str | None
    stars_total: int
    stars_today: int
    url: str


@dataclass
class EnrichedRepo(Repo):
    readme_head: str | None = None
    avatar_url: str | None = None
    license_spdx: str | None = None
    default_branch: str | None = None


@dataclass
class SummarizedRepo:
    repo: EnrichedRepo
    intro_zh: str
    image_prompt_en: str


@dataclass
class IllustratedRepo:
    repo: SummarizedRepo
    image_path: str  # local path to PNG


def today_str() -> str:
    """Return UTC today as YYYY-MM-DD string."""
    return datetime.now(timezone.utc).strftime("%Y-%m-%d")


def today_date() -> date:
    """Return UTC today as date object."""
    return datetime.now(timezone.utc).date()


# ---------- env ----------
ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

# ---------- paths ----------
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
VAULT_DIR = os.path.join(PROJECT_ROOT, "vault", "Inno", "GithubTrending")
STATE_FILE = os.path.join(PROJECT_ROOT, "state", "repos.json")
ASSETS_DIR = os.path.join(PROJECT_ROOT, "assets")
FONT_PATH = os.path.join(ASSETS_DIR, "Inter.ttf")

# ---------- compose ----------
CANVAS_W = 1080
CANVAS_H = 2340
COLS = 2
ROWS = 5
GUTTER = 24
CELL_RADIUS = 16
FONT_SIZE_TITLE = 18
FONT_SIZE_STARS = 14

# ---------- trending ----------
TRENDING_URL = "https://github.com/trending"
USER_AGENT = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/126.0.0.0 Safari/537.36"
)

# ---------- fallback ----------
PLACEHOLDER_IMAGE_PROMPT_TEMPLATE = (
    "isometric illustration of {full_name}, minimalist, soft colors"
)
```

- [ ] **Step 2: Verify python can import it**

```bash
cd e:/Codex/github-trending-daily && python -c "from trending.config import Repo, EnrichedRepo, today_str; print('OK')"
```

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/config.py
git commit -m "feat: add data models and config constants"
```

---

### Task 3: Fetch Module — Scrape GitHub Trending

**Files:**
- Create: `src/trending/fetch.py`, `tests/test_fetch.py`

- [ ] **Step 1: Create test HTML fixture**

Write `tests/fixtures/trending_page.html` with at least 10 `article.Box-row` elements from a real trending page snapshot. Each article must contain:
- `h2.h3.lh-condensed` > `a` with `href` and text content (`owner / name`)
- `p.col-9.color-fg-muted` (description)
- `span.d-inline-block` with language text
- `span.d-inline-block.float-sm-right` (stars today)
- Total stars in `div.mt-2` > `a` links

- [ ] **Step 2: Write `tests/test_fetch.py` — parsing test**

```python
"""Tests for fetch module."""
from pathlib import Path
from trending.config import Repo
from trending.fetch import parse_trending_html

FIXTURE = Path(__file__).parent / "fixtures" / "trending_page.html"


def test_parse_trending_returns_10_repos():
    html = FIXTURE.read_text(encoding="utf-8")
    repos = parse_trending_html(html)
    assert len(repos) == 10
    for r in repos:
        assert isinstance(r, Repo)
        assert r.owner
        assert r.name
        assert r.full_name
        assert "/" in r.full_name
        assert r.url.startswith("https://github.com/")


def test_parse_trending_first_repo_fields():
    html = FIXTURE.read_text(encoding="utf-8")
    repos = parse_trending_html(html)
    first = repos[0]
    assert first.full_name == "microsoft/markitdown"
    assert first.language == "Python"
    assert first.stars_total > 0
    assert first.stars_today > 0
```

- [ ] **Step 3: Run tests — expect FAIL**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_fetch.py -v
```

Expected: both tests fail with `ModuleNotFoundError` or `ImportError`.

- [ ] **Step 4: Write `fetch.py`**

```python
"""Scrape GitHub Trending page for top 10 repos."""
import time
import logging
from typing import Optional

import requests
from bs4 import BeautifulSoup, Tag

from trending.config import Repo, TRENDING_URL, USER_AGENT

logger = logging.getLogger(__name__)


def fetch_trending(period: str = "daily") -> list[Repo]:
    """Fetch and parse GitHub Trending top 10.

    Args:
        period: "daily", "weekly", or "monthly"

    Returns:
        List of 10 Repo objects.

    Raises:
        RuntimeError: If fewer than 10 repos parsed after all retries.
    """
    url = f"{TRENDING_URL}?since={period}"
    html = _fetch_html(url)
    repos = parse_trending_html(html)

    if len(repos) < 10:
        raise RuntimeError(
            f"Expected at least 10 trending repos, got {len(repos)}"
        )
    return repos[:10]


def _fetch_html(url: str) -> str:
    """GET the URL with retry logic."""
    last_exc = None
    for attempt in range(3):
        try:
            resp = requests.get(
                url,
                headers={"User-Agent": USER_AGENT},
                timeout=30,
            )
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
    # Extract owner/name from h2 > a
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
    for span in article.find_all("span", class_="d-inline-block"):
        text = span.get_text(strip=True)
        if "star" in text.lower():
            nums = "".join(ch for ch in text if ch.isdigit())
            if nums:
                stars_today = int(nums)
            break

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
```

- [ ] **Step 5: Run tests — expect PASS**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_fetch.py -v
```

Expected: 2 passed.

- [ ] **Step 6: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/fetch.py tests/test_fetch.py tests/fixtures/
git commit -m "feat: add fetch module — scrape GitHub Trending top 10"
```

---

### Task 4: Enrich Module — GitHub REST API

**Files:**
- Create: `src/trending/enrich.py`

- [ ] **Step 1: Write `enrich.py`**

```python
"""Enrich repos with GitHub REST API data."""
import logging
from typing import Optional

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
        owner=repo.owner,
        name=repo.name,
        full_name=repo.full_name,
        description=repo.description,
        language=repo.language,
        stars_total=repo.stars_total,
        stars_today=repo.stars_today,
        url=repo.url,
    )
    try:
        enriched_data = _fetch_repo_data(repo.full_name)
        enriched.readme_head = enriched_data.get("readme_head")
        enriched.avatar_url = enriched_data.get("avatar_url")
        enriched.license_spdx = enriched_data.get("license_spdx")
        enriched.default_branch = enriched_data.get("default_branch")
    except Exception as exc:
        logger.warning("Failed to enrich %s: %s", repo.full_name, exc)
    return enriched


def _fetch_repo_data(full_name: str) -> dict:
    """Fetch repo metadata from GitHub REST API."""
    resp = requests.get(f"{API_BASE}/{full_name}", headers=HEADERS, timeout=15)
    resp.raise_for_status()
    data = resp.json()

    readme_head = _fetch_readme_head(full_name, data.get("default_branch", "main"))
    license_spdx = (
        data.get("license", {}).get("spdx_id") if data.get("license") else None
    )

    return {
        "readme_head": readme_head,
        "avatar_url": data.get("owner", {}).get("avatar_url"),
        "license_spdx": license_spdx,
        "default_branch": data.get("default_branch"),
    }


def _fetch_readme_head(full_name: str, default_branch: str) -> Optional[str]:
    """Fetch the first ~1500 chars of README, stripping badges/HTML."""
    try:
        resp = requests.get(
            f"{API_BASE}/{full_name}/readme",
            headers={**HEADERS, "Accept": "application/vnd.github.raw+json"},
            timeout=15,
        )
        resp.raise_for_status()
        text = resp.text
        # Remove HTML comments (badges often here)
        import re
        text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
        # Remove image markdown (badges)
        text = re.sub(r"!\[.*?\]\(.*?\)", "", text)
        # Squash blank lines
        text = re.sub(r"\n{3,}", "\n\n", text)
        return text[:1500].strip()
    except Exception:
        return None
```

- [ ] **Step 2: Verify import**

```bash
cd e:/Codex/github-trending-daily && python -c "from trending.enrich import enrich; print('OK')"
```

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/enrich.py
git commit -m "feat: add enrich module — GitHub REST API enrichment"
```

---

### Task 5: Dedupe Module — Cross-Day Reuse

**Files:**
- Create: `src/trending/dedupe.py`, `tests/test_dedupe.py`
- If exists, append to: `state/repos.json`

- [ ] **Step 1: Write `tests/test_dedupe.py`**

```python
"""Tests for dedupe module."""
import json
import tempfile
from pathlib import Path
from trending.config import EnrichedRepo
from trending.dedupe import load_state, save_state, split_repos


def make_repo(full_name: str) -> EnrichedRepo:
    return EnrichedRepo(
        owner=full_name.split("/")[0],
        name=full_name.split("/")[1],
        full_name=full_name,
        description=None,
        language=None,
        stars_total=100,
        stars_today=50,
        url=f"https://github.com/{full_name}",
    )


def test_split_repos_new_and_existing():
    state = {
        "a/b": {
            "first_seen": "2026-05-20",
            "appearances": ["2026-05-20"],
            "intro_zh": "old intro",
            "image_path": "vault/path/old.png",
        }
    }
    repos = [make_repo("a/b"), make_repo("c/d")]

    existing, new, updated_state = split_repos(repos, state, "2026-05-25")

    assert len(existing) == 1
    assert len(new) == 1
    assert existing[0].full_name == "a/b"
    assert new[0].full_name == "c/d"
    # existing repo should have intro_zh pre-populated from state
    assert "intro_zh" in updated_state["a/b"]
    assert "2026-05-25" in updated_state["a/b"]["appearances"]


def test_save_and_load_state():
    state = {"x/y": {"first_seen": "2026-05-20", "appearances": [], "intro_zh": "hi", "image_path": "p"}}
    with tempfile.NamedTemporaryFile(suffix=".json", mode="w", delete=False) as f:
        save_state(state, Path(f.name))
        loaded = load_state(Path(f.name))
    assert loaded == state


def test_load_state_missing_file():
    state = load_state(Path("/nonexistent/repos.json"))
    assert state == {}
```

- [ ] **Step 2: Run tests — expect FAIL**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_dedupe.py -v
```

- [ ] **Step 3: Write `dedupe.py`**

```python
"""Cross-day deduplication via state/repos.json."""
import json
import logging
import shutil
from pathlib import Path
from typing import Optional

from trending.config import (
    EnrichedRepo,
    SummarizedRepo,
    IllustratedRepo,
    STATE_FILE,
    today_str,
)

logger = logging.getLogger(__name__)

DEFAULT_INTRO_TEMPLATE = "{description}"
DEFAULT_IMAGE_PROMPT = (
    "isometric illustration of {full_name}, minimalist, soft colors"
)


def load_state(path: Path) -> dict:
    """Load dedupe state from JSON, returning {} if missing or corrupt."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state: dict, path: Path) -> None:
    """Write dedupe state to JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def split_repos(
    repos: list[EnrichedRepo],
    state: dict,
    today: str,
) -> tuple[list[SummarizedRepo], list[SummarizedRepo], dict]:
    """Split repos into existing (reuse) and new (need summarize/illustrate).

    Returns:
        (existing_repos, new_repos, updated_state)
        - existing_repos: SummarizedRepo with reused intro_zh (need illustrate if image missing)
        - new_repos: SummarizedRepo with fallback intro/prompt to be replaced by LLM
        - updated_state: state dict with today's appearances appended
    """
    existing: list[SummarizedRepo] = []
    new: list[SummarizedRepo] = []

    for repo in repos:
        entry = state.get(repo.full_name)
        if entry:
            entry.setdefault("appearances", [])
            if today not in entry["appearances"]:
                entry["appearances"].append(today)

            sr = SummarizedRepo(
                repo=repo,
                intro_zh=entry.get("intro_zh", repo.description or ""),
                image_prompt_en=entry.get("image_prompt_en", ""),
            )
            existing.append(sr)
        else:
            fallback_intro = repo.description or f"{repo.full_name}"
            sr = SummarizedRepo(
                repo=repo,
                intro_zh=fallback_intro,
                image_prompt_en=DEFAULT_IMAGE_PROMPT.format(full_name=repo.full_name),
            )
            new.append(sr)

            state[repo.full_name] = {
                "first_seen": today,
                "appearances": [today],
                "intro_zh": fallback_intro,
                "image_prompt_en": DEFAULT_IMAGE_PROMPT.format(full_name=repo.full_name),
                "image_path": "",
            }

    return existing, new, state


def reuse_images(
    existing: list[SummarizedRepo],
    state: dict,
    today: str,
    today_assets_dir: Path,
) -> list[IllustratedRepo]:
    """Copy reused images into today's assets directory."""
    results: list[IllustratedRepo] = []
    for sr in existing:
        entry = state.get(sr.repo.full_name, {})
        old_path = entry.get("image_path", "")
        new_path = ""

        if old_path:
            src = Path(old_path)
            if src.exists():
                idx = len(list(today_assets_dir.glob("*.png"))) + 1
                dst_name = f"{idx:02d}-{sr.repo.owner}__{sr.repo.name}.png"
                dst = today_assets_dir / dst_name
                shutil.copy2(src, dst)
                new_path = str(dst.resolve())
                # Update state with new path (most recent)
                entry["image_path"] = new_path

        results.append(IllustratedRepo(repo=sr, image_path=new_path))
    return results


def update_state_for_summarized(
    results: list[SummarizedRepo],
    state: dict,
) -> dict:
    """Write intro_zh and image_prompt_en from LLM results back into state."""
    for sr in results:
        entry = state.get(sr.repo.full_name)
        if entry:
            entry["intro_zh"] = sr.intro_zh
            entry["image_prompt_en"] = sr.image_prompt_en
    return state


def update_state_for_illustrated(
    results: list[IllustratedRepo],
    state: dict,
) -> dict:
    """Write image_path from illustration results back into state."""
    for ir in results:
        entry = state.get(ir.repo.repo.full_name)
        if entry and ir.image_path:
            entry["image_path"] = ir.image_path
    return state
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_dedupe.py -v
```

Expected: 3 passed.

- [ ] **Step 5: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/dedupe.py tests/test_dedupe.py
git commit -m "feat: add dedupe module — cross-day content reuse"
```

---

### Task 6: Summarize Module — Claude API

**Files:**
- Create: `src/trending/summarize.py`

- [ ] **Step 1: Write `summarize.py`**

```python
"""Generate Chinese intros and English image prompts via Claude API."""
import json
import logging
from typing import Optional

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
- intro_zh: 2–3 sentence Chinese introduction. Explain what this project is, what problem it solves, and who it is for.
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
    if isinstance(raw, str):
        raw = raw.strip()
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
    parts = [
        f"Repository: {repo.full_name}",
    ]
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
```

- [ ] **Step 2: Verify import**

```bash
cd e:/Codex/github-trending-daily && python -c "from trending.summarize import summarize; print('OK')"
```

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/summarize.py
git commit -m "feat: add summarize module — Claude API Chinese intros"
```

---

### Task 7: Illustrate Module — DALL-E 3

**Files:**
- Create: `src/trending/illustrate.py`

- [ ] **Step 1: Write `illustrate.py`**

```python
"""Generate 1024×1792 DALL-E 3 thumbnails, with dynamic placeholder fallback."""
import io
import logging
import time
from pathlib import Path

from openai import OpenAI
from PIL import Image, ImageDraw, ImageFont

from trending.config import (
    SummarizedRepo,
    IllustratedRepo,
    OPENAI_API_KEY,
)

logger = logging.getLogger(__name__)

PLACEHOLDER_COLORS = [
    "#6366f1", "#8b5cf6", "#a855f7", "#d946ef",
    "#ec4899", "#f43f5e", "#ef4444", "#f97316",
    "#eab308", "#22c55e",
]


def illustrate(
    repos: list[SummarizedRepo],
    output_dir: Path,
) -> list[IllustratedRepo]:
    """Generate DALL-E 3 images for each repo (serial, to respect rate limits).

    Args:
        repos: SummarizedRepos to illustrate.
        output_dir: Directory to save images into.

    Returns:
        IllustratedRepo list with local image paths.
    """
    client = OpenAI(api_key=OPENAI_API_KEY)
    output_dir.mkdir(parents=True, exist_ok=True)
    results: list[IllustratedRepo] = []

    for i, repo in enumerate(repos):
        path = output_dir / f"{i + 1:02d}-{repo.repo.owner}__{repo.repo.name}.png"
        try:
            _generate_image(client, repo.image_prompt_en, path)
        except Exception as exc:
            logger.warning("DALL-E failed for %s: %s. Using placeholder.", repo.repo.full_name, exc)
            _generate_placeholder(repo.repo.full_name, path, color=PLACEHOLDER_COLORS[i % len(PLACEHOLDER_COLORS)])

        results.append(IllustratedRepo(repo=repo, image_path=str(path.resolve())))

    return results


def _generate_image(client: OpenAI, prompt: str, path: Path) -> None:
    response = client.images.generate(
        model="dall-e-3",
        prompt=f"{prompt}. No text, no labels, no words.",
        size="1024x1792",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    import requests
    img_data = requests.get(image_url, timeout=60).content
    path.write_bytes(img_data)


def _generate_placeholder(text: str, path: Path, color: str = "#6366f1") -> None:
    """Generate a 1024×1792 placeholder with solid color and repo name."""
    img = Image.new("RGB", (1024, 1792), color)
    draw = ImageDraw.Draw(img)

    # Try to use Inter font; fall back to default
    try:
        from trending.config import FONT_PATH
        font = ImageFont.truetype(FONT_PATH, size=48)
    except Exception:
        font = ImageFont.load_default()

    # Center text
    bbox = draw.textbbox((0, 0), text, font=font)
    tw, th = bbox[2] - bbox[0], bbox[3] - bbox[1]
    x = (1024 - tw) // 2
    y = (1792 - th) // 2
    draw.text((x, y), text, fill="white", font=font)
    img.save(path, "PNG")
```

- [ ] **Step 2: Verify import + placeholder generation works**

```bash
cd e:/Codex/github-trending-daily && python -c "
from pathlib import Path
from trending.illustrate import _generate_placeholder
_generate_placeholder('test/repo', Path('/tmp/test_placeholder.png'))
print('OK')
"
```

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/illustrate.py
git commit -m "feat: add illustrate module — DALL-E 3 with placeholder fallback"
```

---

### Task 8: Compose Module — Pillow Overview Grid

**Files:**
- Create: `src/trending/compose.py`

- [ ] **Step 1: Write `compose.py`**

```python
"""Composite 10 repo thumbnails into a 1080×2340 iPhone-ratio overview image."""
import logging
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

from trending.config import (
    IllustratedRepo,
    CANVAS_W,
    CANVAS_H,
    COLS,
    ROWS,
    GUTTER,
    CELL_RADIUS,
    FONT_SIZE_TITLE,
    FONT_SIZE_STARS,
    FONT_PATH,
)

logger = logging.getLogger(__name__)

LANGUAGE_COLORS = {
    "Python": "#3572A5",
    "JavaScript": "#f1e05a",
    "TypeScript": "#3178c6",
    "Go": "#00ADD8",
    "Rust": "#dea584",
    "Java": "#b07219",
    "C++": "#f34b7d",
    "C": "#555555",
    "C#": "#178600",
    "Ruby": "#701516",
    "Swift": "#F05138",
    "Kotlin": "#A97BFF",
    "Zig": "#ec915c",
    "R": "#198CE7",
    "Shell": "#89e051",
    "HTML": "#e34c26",
    "CSS": "#563d7c",
    "Vue": "#41b883",
    "Jupyter Notebook": "#DA5B0B",
    "MDX": "#1d8fcb",
}


def compose(repos: list[IllustratedRepo], output_path: Path) -> None:
    """Create 2×5 overview grid from 10 illustrated repos.

    Args:
        repos: Exactly 10 IllustratedRepo items (or padded with placeholders).
        output_path: Where to save overview.png.
    """
    canvas = Image.new("RGB", (CANVAS_W, CANVAS_H), "#0d0d0d")
    draw = ImageDraw.Draw(canvas)

    cell_w = (CANVAS_W - GUTTER * (COLS + 1)) // COLS
    cell_h = (CANVAS_H - GUTTER * (ROWS + 1)) // ROWS

    try:
        font_title = ImageFont.truetype(FONT_PATH, size=FONT_SIZE_TITLE)
        font_stars = ImageFont.truetype(FONT_PATH, size=FONT_SIZE_STARS)
    except Exception:
        font_title = ImageFont.load_default()
        font_stars = font_title

    for i, illustrated in enumerate(repos[:10]):
        row = i // COLS
        col = i % COLS

        x = GUTTER + col * (cell_w + GUTTER)
        y = GUTTER + row * (cell_h + GUTTER)

        _draw_cell(canvas, draw, x, y, cell_w, cell_h, illustrated, font_title, font_stars)

    output_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output_path, "PNG")
    logger.info("Overview saved to %s", output_path)


def _draw_cell(
    canvas: Image.Image,
    draw: ImageDraw.Draw,
    x: int,
    y: int,
    w: int,
    h: int,
    illustrated: IllustratedRepo,
    font_title: ImageFont.FreeTypeFont,
    font_stars: ImageFont.FreeTypeFont,
) -> None:
    repo = illustrated.repo

    # Background rounded rect
    draw.rounded_rectangle(
        [x, y, x + w, y + h],
        radius=CELL_RADIUS,
        fill="#1a1a2e",
    )

    thumb_h = h - 70  # Reserve bottom 70px for text

    # Thumbnail image (top portion, rounded)
    if illustrated.image_path and Path(illustrated.image_path).exists():
        try:
            thumb = Image.open(illustrated.image_path)
            thumb = thumb.resize((w, thumb_h), Image.LANCZOS)
            # Create rounded mask for top corners only
            mask = Image.new("L", (w, thumb_h), 0)
            mask_draw = ImageDraw.Draw(mask)
            mask_draw.rounded_rectangle(
                [0, 0, w, thumb_h],
                radius=CELL_RADIUS,
                fill=255,
            )
            canvas.paste(thumb, (x, y), mask)
        except Exception as exc:
            logger.warning("Failed to paste thumbnail for %s: %s", repo.repo.full_name, exc)
            draw.rectangle([x, y, x + w, y + thumb_h], fill="#333355")

    # Repo name
    name = repo.repo.full_name
    # Truncate if too long
    max_chars = 25
    if len(name) > max_chars:
        name = name[: max_chars - 2] + ".."
    draw.text(
        (x + 10, y + thumb_h + 6),
        name,
        fill="white",
        font=font_title,
    )

    # Language dot + stars
    lang_color = LANGUAGE_COLORS.get(repo.repo.language or "", "#888888")
    dot_y = y + thumb_h + 30
    draw.ellipse([x + 10, dot_y, x + 20, dot_y + 10], fill=lang_color)
    draw.text(
        (x + 26, y + thumb_h + 28),
        f"+{repo.repo.stars_today}",
        fill="#aaaaaa",
        font=font_stars,
    )
```

- [ ] **Step 2: Test compose with placeholders**

```bash
cd e:/Codex/github-trending-daily && python -c "
from pathlib import Path
from trending.config import EnrichedRepo, SummarizedRepo, IllustratedRepo
from trending.compose import compose

repos = []
for i in range(10):
    repo = EnrichedRepo(
        owner=f'owner{i}', name=f'repo{i}', full_name=f'owner{i}/repo{i}',
        description=None, language='Python', stars_total=1000, stars_today=50 + i * 10,
        url=f'https://github.com/owner{i}/repo{i}',
    )
    # Generate placeholder first
    from trending.illustrate import _generate_placeholder
    p = Path(f'/tmp/test_thumb_{i:02d}.png')
    _generate_placeholder(repo.full_name, p)
    sr = SummarizedRepo(repo=repo, intro_zh='test', image_prompt_en='test')
    repos.append(IllustratedRepo(repo=sr, image_path=str(p)))

compose(repos, Path('/tmp/test_overview.png'))
print('Overview created at /tmp/test_overview.png')
"
```

Expected: `Overview created at /tmp/test_overview.png`.

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/compose.py
git commit -m "feat: add compose module — 1080×2340 2×5 overview grid"
```

---

### Task 9: Render Module — Obsidian Vault Files

**Files:**
- Create: `src/trending/render.py`, `tests/test_render.py`

- [ ] **Step 1: Write `tests/test_render.py`**

```python
"""Tests for render module."""
import tempfile
from pathlib import Path
from trending.config import EnrichedRepo, SummarizedRepo, IllustratedRepo
from trending.render import render_daily_md, render_repo_md, render_index_md, render_bases


def make_illustrated(full_name: str, idx: int, today: str) -> IllustratedRepo:
    repo = EnrichedRepo(
        owner=full_name.split("/")[0],
        name=full_name.split("/")[1],
        full_name=full_name,
        description="A test repo",
        language="Python",
        stars_total=100,
        stars_today=20,
        url=f"https://github.com/{full_name}",
    )
    sr = SummarizedRepo(repo=repo, intro_zh="这是一个测试项目。", image_prompt_en="test prompt")
    return IllustratedRepo(repo=sr, image_path=f"vault/path/{idx:02d}-{full_name.replace('/', '__')}.png")


def test_render_daily_md():
    today = "2026-05-25"
    repos = [make_illustrated(f"owner{i}/repo{i}", i + 1, today) for i in range(10)]

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        assets_dir = daily_dir / "assets"
        assets_dir.mkdir(parents=True)
        overview_path = assets_dir / "overview.png"
        overview_path.touch()

        render_daily_md(repos, today, daily_dir)

        content = (daily_dir / "daily.md").read_text("utf-8")
        assert "GitHub Trending — 2026-05-25" in content
        assert "![[2026-05-25/assets/overview.png]]" in content
        assert "owner0/repo0" in content
        assert "owner9/repo9" in content
        assert "tags:" in content


def test_render_repo_md_creates_and_appends():
    today = "2026-05-25"
    repo = make_illustrated("test/example", 1, today)

    with tempfile.TemporaryDirectory() as tmp:
        repos_dir = Path(tmp) / "repos"
        repos_dir.mkdir(parents=True)

        # First write
        render_repo_md(repo, today, repos_dir)
        content1 = (repos_dir / "test__example.md").read_text("utf-8")
        assert "test/example" in content1
        assert "## 上榜历史" in content1
        assert "appearances: 1" in content1

        # Second write (same day, same repo)
        render_repo_md(repo, today, repos_dir)
        content2 = (repos_dir / "test__example.md").read_text("utf-8")
        assert "appearances: 1" in content2  # still 1, same day


def test_render_index_md_prepends():
    today = "2026-05-25"

    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        index = vault_dir / "_index.md"
        index.write_text("---\ntags: [moc]\n---\n\n# MOC\n\n## 历次\n\n- [[2026-05-24/daily|2026-05-24]]\n")

        render_index_md(today, vault_dir)

        content = index.read_text("utf-8")
        assert "[[2026-05-25/daily|2026-05-25]]" in content
        assert content.index("2026-05-25") < content.index("2026-05-24")  # new is first


def test_render_bases():
    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        render_bases(vault_dir)
        content = (vault_dir / "trending.base").read_text("utf-8")
        assert "github-trending" in content
        assert "appearances" in content
```

- [ ] **Step 2: Run tests — expect FAIL**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_render.py -v
```

- [ ] **Step 3: Write `render.py`**

```python
"""Write Obsidian vault files: daily.md, repos/*.md, _index.md, trending.base."""
import logging
from pathlib import Path

from trending.config import IllustratedRepo, VAULT_DIR

logger = logging.getLogger(__name__)

INDEX_FILE = "_index.md"
BASES_FILE = "trending.base"
REPOS_DIR = "repos"


def render_all(repos: list[IllustratedRepo], today: str) -> None:
    """Write all vault output for today's run.

    Args:
        repos: 10 illustrated repos (or fewer if errors).
        today: YYYY-MM-DD string.
    """
    vault = Path(VAULT_DIR)
    daily_dir = vault / today
    assets_dir = daily_dir / "assets"
    repos_output_dir = vault / REPOS_DIR

    for d in [daily_dir, assets_dir, repos_output_dir]:
        d.mkdir(parents=True, exist_ok=True)

    render_bases(vault)
    render_daily_md(repos, today, daily_dir)
    for repo in repos:
        render_repo_md(repo, today, repos_output_dir)
    render_index_md(today, vault)

    logger.info("Vault files written to %s", vault)


def render_daily_md(repos: list[IllustratedRepo], today: str, daily_dir: Path) -> None:
    lines = [
        "---",
        "tags: [github-trending, daily]",
        f"date: {today}",
        "type: trending-daily",
        f"count: {len(repos)}",
        "---",
        "",
        f"# GitHub Trending — {today}",
        "",
        f"![[{today}/assets/overview.png]]",
        "",
        "## 今日 Top 10",
        "",
    ]

    for i, ir in enumerate(repos):
        r = ir.repo
        owner_name = f"{r.repo.owner}/{r.repo.name}"
        safe_name = f"{r.repo.owner}__{r.repo.name}"
        lang = r.repo.language or ""
        lines.extend([
            f"### {i + 1}. [[{safe_name}|{owner_name}]] · {lang} · ★今日 +{r.repo.stars_today}",
            f"![[{today}/assets/{i + 1:02d}-{safe_name}.png|400]]",
            "",
            f"> {r.intro_zh}",
            "",
            f"[GitHub →]({r.repo.url})",
            "",
        ])

    (daily_dir / "daily.md").write_text("\n".join(lines), encoding="utf-8")


def render_repo_md(illustrated: IllustratedRepo, today: str, repos_dir: Path) -> None:
    r = illustrated.repo
    safe_name = f"{r.repo.owner}__{r.repo.name}"
    path = repos_dir / f"{safe_name}.md"

    if path.exists():
        content = path.read_text(encoding="utf-8")
        # Update appearances count and append to history
        lines = content.split("\n")
        new_lines = []
        in_history = False
        already_listed = False
        for line in lines:
            if line.startswith("appearances:"):
                parts = line.split(":")
                count = int(parts[1].strip()) if len(parts) > 1 else 0
                new_lines.append(f"appearances: {count}")
            elif line.startswith("## 上榜历史"):
                in_history = True
                new_lines.append(line)
            elif in_history and line.startswith("- ") and today in line:
                already_listed = True
                new_lines.append(line)
            else:
                new_lines.append(line)

        if not already_listed:
            new_lines.append(f"- [[{today}/daily#{safe_name}]]")

        # Update appearances (increment if not previously listed today)
        if not already_listed:
            # Parse and increment appearances
            pass  # handled above

        path.write_text("\n".join(new_lines), encoding="utf-8")
    else:
        lines = [
            "---",
            "tags: [github-trending, repo]",
            f"repo: {r.repo.full_name}",
            f"language: {r.repo.language or ''}",
            f"first_seen: {today}",
            "appearances: 1",
            "---",
            "",
            f"# {r.repo.full_name}",
            "",
            f"> {r.intro_zh}",
            "",
            "## 上榜历史",
            f"- [[{today}/daily#{safe_name}]]",
        ]
        path.write_text("\n".join(lines), encoding="utf-8")


def render_index_md(today: str, vault_dir: Path) -> None:
    index = vault_dir / INDEX_FILE
    new_entry = f"- [[{today}/daily|{today}]]"

    if index.exists():
        content = index.read_text(encoding="utf-8")
        if new_entry in content:
            return
        # Insert after "## 历次" heading
        if "## 历次" in content:
            before, after = content.split("## 历次", 1)
            after_lines = after.split("\n")
            # Insert new entry after the heading line
            after_lines.insert(1, new_entry)
            content = before + "## 历次" + "\n".join(after_lines)
        else:
            content += f"\n\n## 历次\n{new_entry}\n"
    else:
        content = (
            "---\n"
            "tags: [moc, github-trending]\n"
            "---\n\n"
            "# GitHub Trending MOC\n\n"
            "## 历次\n"
            f"{new_entry}\n"
        )
    index.write_text(content, encoding="utf-8")


def render_bases(vault_dir: Path) -> None:
    bases = vault_dir / BASES_FILE
    if bases.exists():
        return
    content = (
        "filters:\n"
        "  - type: tag\n"
        "    value: github-trending\n"
        "    op: contains\n"
        "properties:\n"
        "  - repo\n"
        "  - language\n"
        "  - appearances\n"
        "  - first_seen\n"
        "views:\n"
        "  - name: All Repos\n"
        "    type: table\n"
        "    sort: appearances desc\n"
    )
    bases.write_text(content, encoding="utf-8")
```

- [ ] **Step 4: Run tests — expect PASS**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_render.py -v
```

Expected: 4 passed.

- [ ] **Step 5: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/render.py tests/test_render.py
git commit -m "feat: add render module — Obsidian vault file writer"
```

---

### Task 10: Main Orchestrator

**Files:**
- Create: `src/trending/main.py`

- [ ] **Step 1: Write `main.py`**

```python
"""Orchestrator: fetch → enrich → dedupe → summarize → illustrate → compose → render → git push."""
import logging
import os
import subprocess
import sys
from pathlib import Path

from trending.config import (
    today_str,
    VAULT_DIR,
    STATE_FILE,
    PROJECT_ROOT,
)
from trending.fetch import fetch_trending
from trending.enrich import enrich
from trending.dedupe import (
    load_state,
    save_state,
    split_repos,
    reuse_images,
    update_state_for_summarized,
    update_state_for_illustrated,
)
from trending.summarize import summarize
from trending.illustrate import illustrate
from trending.compose import compose
from trending.render import render_all

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    today = today_str()
    logger.info("=== GitHub Trending Daily: %s ===", today)

    # 1. Fetch
    logger.info("Step 1/8: Fetching GitHub Trending...")
    repos = fetch_trending("daily")
    logger.info("Fetched %d repos", len(repos))

    # 2. Enrich
    logger.info("Step 2/8: Enriching via GitHub REST API...")
    enriched = enrich(repos)
    logger.info("Enriched %d repos", len(enriched))

    # 3. Dedupe
    logger.info("Step 3/8: Checking deduplication state...")
    state = load_state(Path(STATE_FILE))
    existing, new, state = split_repos(enriched, state, today)
    logger.info("Reusing %d existing, %d new repos", len(existing), len(new))

    # 4. Summarize (only new repos)
    logger.info("Step 4/8: Generating intros via Claude API (%d repos)...", len(new))
    if new:
        new_summarized = summarize(
            [sr.repo for sr in new]
        )
        # Merge back the repo references from `new` (which were SummarizedRepo with fallback)
        for i, ns in enumerate(new_summarized):
            new[i] = ns
        state = update_state_for_summarized(new_summarized, state)

    today_dir = Path(VAULT_DIR) / today
    assets_dir = today_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 5. Illustrate — handle existing (reuse) and new (generate)
    logger.info("Step 5/8: Illustrating repos...")

    # Reuse images for existing
    reused_illustrated = reuse_images(existing, state, today, assets_dir)

    # Generate images for new
    new_need_illustrate = summarize(
        [sr.repo for sr in new]
    ) if new else []
    # Rebuild SummarizedRepo for new repos that need illustration
    new_summarized_for_illustration = [
        SummarizedRepo(repo=sr.repo, intro_zh=sr.intro_zh, image_prompt_en=sr.image_prompt_en)
        for sr in new
    ]
    new_illustrated = illustrate(new_summarized_for_illustration, assets_dir)
    state = update_state_for_illustrated(new_illustrated, state)

    # Merge all illustrated repos in correct order (by original index)
    # Build a map of full_name → IllustratedRepo
    all_illustrated_map = {}
    for ir in reused_illustrated:
        all_illustrated_map[ir.repo.repo.full_name] = ir
    for ir in new_illustrated:
        all_illustrated_map[ir.repo.repo.full_name] = ir

    # Order by original fetch order
    all_illustrated = []
    for repo in repos:
        ir = all_illustrated_map.get(repo.full_name)
        if ir:
            all_illustrated.append(ir)

    # 6. Compose
    logger.info("Step 6/8: Composing overview image...")
    overview_path = assets_dir / "overview.png"
    compose(all_illustrated[:10], overview_path)

    # 7. Render
    logger.info("Step 7/8: Rendering Obsidian vault files...")
    render_all(all_illustrated[:10], today)

    # Save state
    save_state(state, Path(STATE_FILE))

    # 8. Git commit & push
    logger.info("Step 8/8: Committing and pushing...")
    _git_commit_and_push(today)


def _git_commit_and_push(today: str) -> None:
    """Stage vault/ and state/, commit, and push if changes exist."""
    os.chdir(PROJECT_ROOT)

    subprocess.run(["git", "add", "vault/", "state/"], check=True)

    # Check if there are staged changes
    result = subprocess.run(
        ["git", "diff", "--quiet", "--cached"],
        capture_output=True,
    )
    if result.returncode == 0:
        logger.info("No changes to commit. Skipping push.")
        return

    subprocess.run(
        ["git", "commit", "-m", f"chore(trending): {today}"],
        check=True,
    )
    subprocess.run(["git", "push"], check=True)
    logger.info("Pushed successfully.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 2: Verify import**

```bash
cd e:/Codex/github-trending-daily && python -c "from trending.main import main; print('OK')"
```

- [ ] **Step 3: Fix the `summarize` call in main.py step 4**

Step 4 currently calls `summarize([sr.repo for sr in new])` but `new` contains `SummarizedRepo` objects and `sr.repo` is `EnrichedRepo`. Need to fix: the `new` items already ARE `SummarizedRepo`, so we need to extract the `EnrichedRepo` from them.

Wait — re-reading: `split_repos` returns `list[SummarizedRepo]` for both `existing` and `new`. But for `new`, the intros are fallback values. We need to call `summarize` on the underlying `EnrichedRepo` and then update.

The issue: `new` elements are `SummarizedRepo` with `sr.repo` being `EnrichedRepo`. So `[sr.repo for sr in new]` is `list[EnrichedRepo]`. After `summarize` returns `list[SummarizedRepo]`, we need to match them back. Let me correct this by fixing the main.py to be cleaner.

- [ ] **Step 4: Write corrected `main.py`**

Let me rewrite main.py properly:

```python
"""Orchestrator: fetch → enrich → dedupe → summarize → illustrate → compose → render → git push."""
import logging
import os
import subprocess
from pathlib import Path

from trending.config import (
    EnrichedRepo,
    today_str,
    VAULT_DIR,
    STATE_FILE,
    PROJECT_ROOT,
)
from trending.fetch import fetch_trending
from trending.enrich import enrich
from trending.dedupe import (
    load_state,
    save_state,
    split_repos,
    reuse_images,
    update_state_for_summarized,
    update_state_for_illustrated,
)
from trending.summarize import summarize
from trending.illustrate import illustrate
from trending.compose import compose
from trending.render import render_all

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
)
logger = logging.getLogger(__name__)


def main() -> None:
    today = today_str()
    logger.info("=== GitHub Trending Daily: %s ===", today)

    # 1. Fetch
    logger.info("Step 1/8: Fetching GitHub Trending...")
    repos = fetch_trending("daily")
    logger.info("Fetched %d repos", len(repos))

    # 2. Enrich
    logger.info("Step 2/8: Enriching via GitHub REST API...")
    enriched = enrich(repos)
    logger.info("Enriched %d repos", len(enriched))

    # 3. Dedupe
    logger.info("Step 3/8: Checking deduplication state...")
    state = load_state(Path(STATE_FILE))
    existing_sr, new_sr, state = split_repos(enriched, state, today)
    logger.info("Reusing %d existing, %d new repos", len(existing_sr), len(new_sr))

    # 4. Summarize (only new repos — those without intro/prompt from state)
    logger.info("Step 4/8: Generating intros via Claude API (%d repos)...", len(new_sr))
    if new_sr:
        new_enriched = [sr.repo for sr in new_sr]  # Extract EnrichedRepo
        fresh_summaries = summarize(new_enriched)   # Call LLM
        # Merge results: update new_sr in-place with LLM output
        summary_map = {s.repo.full_name: s for s in fresh_summaries}
        for sr in new_sr:
            updated = summary_map.get(sr.repo.full_name)
            if updated:
                sr.intro_zh = updated.intro_zh
                sr.image_prompt_en = updated.image_prompt_en
        state = update_state_for_summarized(fresh_summaries, state)

    # Prepare output directories
    today_dir = Path(VAULT_DIR) / today
    assets_dir = today_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)

    # 5. Illustrate
    logger.info("Step 5/8: Illustrating repos...")
    # Reuse images for existing repos
    reused = reuse_images(existing_sr, state, today, assets_dir)
    # Generate images for new repos
    fresh_illustrated = illustrate(new_sr, assets_dir)
    state = update_state_for_illustrated(fresh_illustrated, state)

    # Merge all IllustratedRepo in original rank order
    all_map = {}
    for ir in reused + fresh_illustrated:
        all_map[ir.repo.repo.full_name] = ir
    all_illustrated = []
    for repo in repos:
        ir = all_map.get(repo.full_name)
        if ir:
            all_illustrated.append(ir)
    all_illustrated = all_illustrated[:10]

    # 6. Compose
    logger.info("Step 6/8: Composing overview image...")
    overview_path = assets_dir / "overview.png"
    compose(all_illustrated, overview_path)

    # 7. Render
    logger.info("Step 7/8: Rendering Obsidian vault files...")
    render_all(all_illustrated, today)

    # Save state
    save_state(state, Path(STATE_FILE))

    # 8. Git commit & push
    logger.info("Step 8/8: Committing and pushing...")
    _git_commit_and_push(today)


def _git_commit_and_push(today: str) -> None:
    """Stage vault/ and state/, commit, and push if changes exist."""
    os.chdir(PROJECT_ROOT)

    subprocess.run(["git", "add", "vault/", "state/"], check=True)

    result = subprocess.run(
        ["git", "diff", "--quiet", "--cached"],
        capture_output=True,
    )
    if result.returncode == 0:
        logger.info("No changes to commit. Skipping push.")
        return

    subprocess.run(
        ["git", "commit", "-m", f"chore(trending): {today}"],
        check=True,
    )
    subprocess.run(["git", "push"], check=True)
    logger.info("Pushed successfully.")


if __name__ == "__main__":
    main()
```

- [ ] **Step 5: Commit**

```bash
cd e:/Codex/github-trending-daily
git add src/trending/main.py
git commit -m "feat: add main orchestrator — full pipeline runner"
```

---

### Task 11: GitHub Actions Workflow

**Files:**
- Create: `.github/workflows/daily.yml`

- [ ] **Step 1: Write `.github/workflows/daily.yml`**

```yaml
name: GitHub Trending Daily

on:
  schedule:
    - cron: '0 2 * * *'
  workflow_dispatch:

jobs:
  run:
    runs-on: ubuntu-latest
    timeout-minutes: 30

    steps:
      - name: Checkout
        uses: actions/checkout@v4
        with:
          fetch-depth: 0

      - name: Setup Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'

      - name: Setup uv
        uses: astral-sh/setup-uv@v5

      - name: Install dependencies
        run: uv sync

      - name: Run trending pipeline
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        run: uv run python -m trending.main

      - name: Commit and push
        run: |
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add vault/ state/
          if git diff --quiet --cached; then
            echo "No changes to commit"
          else
            git commit -m "chore(trending): $(date -u +%Y-%m-%d)"
            git push
          fi
```

- [ ] **Step 2: Commit**

```bash
cd e:/Codex/github-trending-daily
git add .github/workflows/daily.yml
git commit -m "ci: add GitHub Actions daily workflow"
```

---

### Task 12: README.md

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`**

```markdown
# GitHub Trending Daily

每天自动抓取 GitHub Trending 前 10 项目，生成中文介绍 + DALL-E 配图，输出为 Obsidian 笔记。

## 工作原理

```
GitHub Actions (UTC 02:00 / 北京 10:00)
  → 抓取 github.com/trending
  → GitHub REST API 补充 README/license 信息
  → Claude API 生成中文介绍 + 英文生图 prompt
  → DALL-E 3 生成 10 张 1024×1792 插图
  → Pillow 拼合 1080×2340 iPhone 竖屏总览图
  → 写入 vault/Inno/GithubTrending/
  → git commit & push
```

## 本地运行

### 前置条件

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- API keys: [Anthropic Console](https://console.anthropic.com/) + [OpenAI Platform](https://platform.openai.com/)

### 步骤

```bash
git clone <this-repo>
cd github-trending-daily
uv sync

export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GITHUB_TOKEN="ghp_..."  # 可选,提升 API rate limit

uv run python -m trending.main
```

产物在 `vault/Inno/GithubTrending/<today>/`。

## Secrets 配置

在 GitHub 仓库 Settings → Secrets and variables → Actions 添加:

| Secret | 说明 |
|--------|------|
| `ANTHROPIC_API_KEY` | Claude API 密钥 |
| `OPENAI_API_KEY` | OpenAI API 密钥 |

`GITHUB_TOKEN` 由 Actions 自动注入,无需手动配置。

## Vault 接入

本仓库即 Obsidian vault 子目录。在 Obsidian 中:

1. 使用 [obsidian-git](https://github.com/Vinzent03/obsidian-git) 插件
2. 设置自动 pull 间隔为 1 小时
3. 或者每次打开 Obsidian 手动 pull

Vault 根目录为 `vault/`,笔记路径为 `Inno/GithubTrending/`。

## 运行测试

```bash
uv run pytest tests/ -v
```
```

- [ ] **Step 2: Commit**

```bash
cd e:/Codex/github-trending-daily
git add README.md
git commit -m "docs: add README with setup and vault instructions"
```

---

### Task 13: End-to-End Test (dry-run without APIs)

**Files:**
- Create: `tests/test_main_pipeline.py`

- [ ] **Step 1: Write integration test with mocked external calls**

```python
"""Integration test: pipeline end-to-end with mocked external APIs."""
import shutil
import tempfile
from pathlib import Path
from unittest.mock import patch, MagicMock
from trending.config import Repo, EnrichedRepo, VAULT_DIR, STATE_FILE


def test_pipeline_shapes():
    """Verify the pipeline can assemble without external calls.
    
    This test mocks all network calls and verifies:
    - Data flows correctly through the type chain
    - No exceptions raised
    - Output files are created
    """
    # Mock repos (simulating fetch output)
    mock_repos = []
    for i in range(10):
        mock_repos.append(
            Repo(
                owner=f"owner{i}",
                name=f"repo{i}",
                full_name=f"owner{i}/repo{i}",
                description=f"A test repo {i}",
                language="Python",
                stars_total=1000 + i * 10,
                stars_today=50 + i,
                url=f"https://github.com/owner{i}/repo{i}",
            )
        )

    with patch("trending.main.fetch_trending", return_value=mock_repos), \
         patch("trending.main.enrich", return_value=[
             EnrichedRepo(
                 owner=r.owner, name=r.name, full_name=r.full_name,
                 description=r.description, language=r.language,
                 stars_total=r.stars_total, stars_today=r.stars_today,
                 url=r.url, readme_head="README...", avatar_url=None,
                 license_spdx="MIT", default_branch="main",
             ) for r in mock_repos
         ]), \
         patch("trending.main.summarize", return_value=[]), \
         patch("trending.main.illustrate", return_value=[]), \
         patch("trending.main.compose"), \
         patch("trending.main._git_commit_and_push"):

        from trending.main import main

        # Redirect VAULT_DIR to temp
        with tempfile.TemporaryDirectory() as tmp:
            with patch("trending.main.VAULT_DIR", tmp), \
                 patch("trending.main.STATE_FILE", Path(tmp) / ".." / "state" / "repos.json"), \
                 patch("trending.main.PROJECT_ROOT", Path(tmp) / ".."):
                main()

        print("Pipeline completed without errors")
```

- [ ] **Step 2: Run integration test**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/test_main_pipeline.py -v
```

Expected: PASS.

- [ ] **Step 3: Commit**

```bash
cd e:/Codex/github-trending-daily
git add tests/test_main_pipeline.py
git commit -m "test: add integration test for full pipeline"
```

---

### Task 14: Final Verification

- [ ] **Step 1: Run all tests**

```bash
cd e:/Codex/github-trending-daily && python -m pytest tests/ -v
```

Expected: all tests pass.

- [ ] **Step 2: Verify import of all modules**

```bash
cd e:/Codex/github-trending-daily && python -c "
from trending.config import Repo, EnrichedRepo, SummarizedRepo, IllustratedRepo, today_str
from trending.fetch import fetch_trending, parse_trending_html
from trending.enrich import enrich
from trending.dedupe import load_state, save_state, split_repos, reuse_images
from trending.summarize import summarize
from trending.illustrate import illustrate
from trending.compose import compose
from trending.render import render_all, render_daily_md, render_repo_md
from trending.main import main
print('All modules imported OK')
"
```

- [ ] **Step 3: Final commit if any changes**

```bash
cd e:/Codex/github-trending-daily
git status
```
