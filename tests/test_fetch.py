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
