"""Tests for render module."""
import tempfile
from pathlib import Path
from trending.config import EnrichedRepo, SummarizedRepo, IllustratedRepo
from trending.render import render_daily_md, render_repo_md, render_index_md, render_bases


def make_illustrated(full_name: str, idx: int, today: str) -> IllustratedRepo:
    owner, name = full_name.split("/")
    repo = EnrichedRepo(
        owner=owner,
        name=name,
        full_name=full_name,
        description="A test repo",
        language="Python",
        stars_total=100,
        stars_today=20,
        url=f"https://github.com/{full_name}",
    )
    sr = SummarizedRepo(repo=repo, intro_zh="中文介绍测试。", image_prompt_en="test prompt")
    return IllustratedRepo(repo=sr, image_path=f"vault/{today}/assets/{idx:02d}-{full_name.replace('/', '__')}.png")


def test_render_daily_md():
    today = "2026-05-25"
    repos = [make_illustrated(f"owner{i}/repo{i}", i + 1, today) for i in range(10)]

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        assets_dir = daily_dir / "assets"
        assets_dir.mkdir(parents=True)
        (assets_dir / "overview.png").touch()

        render_daily_md(repos, today, daily_dir)

        content = (daily_dir / "daily.md").read_text("utf-8")
        assert "GitHub Trending — 2026-05-25" in content
        assert "![[2026-05-25/assets/overview.png]]" in content
        assert "owner0/repo0" in content
        assert "owner9/repo9" in content
        assert "tags:" in content


def test_render_repo_md_creates_new():
    today = "2026-05-25"
    repo = make_illustrated("test/example", 1, today)

    with tempfile.TemporaryDirectory() as tmp:
        repos_dir = Path(tmp) / "repos"
        repos_dir.mkdir(parents=True)

        render_repo_md(repo, today, repos_dir)
        content = (repos_dir / "test__example.md").read_text("utf-8")
        assert "test/example" in content
        assert "## 上榜历史" in content
        assert "appearances: 1" in content


def test_render_index_md_prepends():
    today = "2026-05-25"

    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        index = vault_dir / "_index.md"
        index.write_text("---\ntags: [moc]\n---\n\n# MOC\n\n## 历次\n\n- [[2026-05-24/daily|2026-05-24]]\n", encoding="utf-8")

        render_index_md(today, vault_dir)

        content = index.read_text("utf-8")
        assert "[[2026-05-25/daily|2026-05-25]]" in content
        assert content.index("2026-05-25") < content.index("2026-05-24")


def test_render_bases():
    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        render_bases(vault_dir)
        content = (vault_dir / "trending.base").read_text("utf-8")
        assert "github-trending" in content
        assert "appearances" in content


from trending.render import render_articles


def test_render_articles_writes_files_with_frontmatter():
    today = "2026-05-26"
    repos = [
        make_illustrated("alpha/one", 1, today),
        make_illustrated("beta/two", 2, today),
    ]
    articles = {
        "alpha/one": "## 项目概述\n\nAlpha 的内容。",
        "beta/two": "## 项目概述\n\nBeta 的内容。",
    }

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        daily_dir.mkdir(parents=True)

        render_articles(articles, repos, today, daily_dir)

        a = (daily_dir / "articles" / "01-alpha__one.md").read_text("utf-8")
        b = (daily_dir / "articles" / "02-beta__two.md").read_text("utf-8")

        assert "tags:\n  - trending\n  - article" in a
        assert "repo: alpha/one" in a
        assert f"date: {today}" in a
        assert "language: Python" in a
        assert "stars_total: 100" in a
        assert "stars_today: 20" in a
        assert "## 项目概述" in a
        assert "Alpha 的内容。" in a
        assert "Beta 的内容。" in b


def test_render_articles_skips_missing_entries():
    today = "2026-05-26"
    repos = [
        make_illustrated("alpha/one", 1, today),
        make_illustrated("beta/two", 2, today),
    ]
    articles = {"alpha/one": "## 项目概述\n\n仅 Alpha"}

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        daily_dir.mkdir(parents=True)

        render_articles(articles, repos, today, daily_dir)

        assert (daily_dir / "articles" / "01-alpha__one.md").exists()
        assert not (daily_dir / "articles" / "02-beta__two.md").exists()


def test_render_daily_md_includes_article_link():
    today = "2026-05-26"
    repos = [make_illustrated(f"owner{i}/repo{i}", i + 1, today) for i in range(10)]

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        assets_dir = daily_dir / "assets"
        assets_dir.mkdir(parents=True)
        (assets_dir / "overview.png").touch()

        render_daily_md(repos, today, daily_dir)

        content = (daily_dir / "daily.md").read_text("utf-8")
        assert "[详细介绍 →](2026-05-26/articles/01-owner0__repo0.md)" in content
        assert "[详细介绍 →](2026-05-26/articles/10-owner9__repo9.md)" in content


def test_render_repo_md_new_format_creates_index_page():
    today = "2026-05-26"
    repo = make_illustrated("test/example", 3, today)

    with tempfile.TemporaryDirectory() as tmp:
        repos_dir = Path(tmp) / "repos"
        repos_dir.mkdir(parents=True)

        render_repo_md(repo, today, repos_dir)
        content = (repos_dir / "test__example.md").read_text("utf-8")

        # Frontmatter
        assert "appearances: 1" in content
        assert "repo: test/example" in content
        # Body
        assert "# test/example" in content
        assert "> 中文介绍测试。" in content
        assert "## 详细介绍历史" in content
        assert "## 上榜历史" in content
        assert f"[[{today}/articles/03-test__example|{today}]]" in content
        assert f"[[{today}/daily|{today}]] — 20 stars" in content
        # Order: 详细介绍历史 must come before 上榜历史
        assert content.index("## 详细介绍历史") < content.index("## 上榜历史")


def test_render_repo_md_appends_to_existing_new_format():
    today = "2026-05-26"
    repo = make_illustrated("test/example", 5, today)

    with tempfile.TemporaryDirectory() as tmp:
        repos_dir = Path(tmp) / "repos"
        repos_dir.mkdir(parents=True)
        existing = """---
tags:
  - trending
  - repo
repo: test/example
language: Python
first_seen: 2026-05-20
appearances: 2
---

# test/example

> 旧介绍。

## 详细介绍历史

- [[2026-05-21/articles/02-test__example|2026-05-21]]
- [[2026-05-20/articles/01-test__example|2026-05-20]]

## 上榜历史

- [[2026-05-20/daily|2026-05-20]] — 50 stars
- [[2026-05-21/daily|2026-05-21]] — 75 stars
"""
        (repos_dir / "test__example.md").write_text(existing, encoding="utf-8")

        render_repo_md(repo, today, repos_dir)
        content = (repos_dir / "test__example.md").read_text("utf-8")

        assert "appearances: 3" in content
        # New article entry appears before the older one
        idx_new = content.index(f"[[{today}/articles/05-test__example|{today}]]")
        idx_old = content.index("[[2026-05-21/articles/02-test__example|2026-05-21]]")
        assert idx_new < idx_old
        # New daily entry appears before legacy entries
        idx_daily_new = content.index(f"[[{today}/daily|{today}]] — 20 stars")
        idx_daily_old = content.index("[[2026-05-20/daily|2026-05-20]] — 50 stars")
        assert idx_daily_new < idx_daily_old


def test_render_repo_md_migrates_legacy_file():
    today = "2026-05-26"
    repo = make_illustrated("test/example", 7, today)

    with tempfile.TemporaryDirectory() as tmp:
        repos_dir = Path(tmp) / "repos"
        repos_dir.mkdir(parents=True)
        legacy = """---
tags:
  - trending
  - repo
repo: test/example
language: Python
first_seen: 2026-05-20
appearances: 1
---

# test/example

旧式短简介。

## 上榜历史

- [[2026-05-20/daily|2026-05-20]] — 50 stars
"""
        (repos_dir / "test__example.md").write_text(legacy, encoding="utf-8")

        render_repo_md(repo, today, repos_dir)
        content = (repos_dir / "test__example.md").read_text("utf-8")

        assert "appearances: 2" in content
        assert "## 详细介绍历史" in content
        assert content.index("## 详细介绍历史") < content.index("## 上榜历史")
        assert f"[[{today}/articles/07-test__example|{today}]]" in content
        # Legacy daily entry still present
        assert "[[2026-05-20/daily|2026-05-20]] — 50 stars" in content
