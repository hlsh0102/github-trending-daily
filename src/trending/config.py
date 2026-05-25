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
    gpt_image_prompt: str = ""  # JSON string — bento-grid prompt for gpt-image-2


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
DEEPSEEK_API_KEY = os.environ.get("DEEPSEEK_API_KEY", "")
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

# ---------- deepseek ----------
DEEPSEEK_BASE_URL = "https://api.deepseek.com"
DEEPSEEK_MODEL = "deepseek-chat"
