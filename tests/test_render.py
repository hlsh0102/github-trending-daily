"""Tests for render module."""
import json
import tempfile
from pathlib import Path
from trending.config import EnrichedRepo, SummarizedRepo, IllustratedRepo
from trending.render import (
    render_daily_md,
    render_repo_md,
    render_index_md,
    render_bases,
    render_all,
    render_gpt_prompts,
    render_douyin_prompts,
    render_douyin_description,
)


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
        render_daily_md(repos, today, daily_dir)

        content = (daily_dir / "daily.md").read_text("utf-8")
        assert "GitHub Trending — 2026-05-25" in content
        assert "assets/" not in content
        assert "overview.png" not in content
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
        render_daily_md(repos, today, daily_dir)

        content = (daily_dir / "daily.md").read_text("utf-8")
        assert "[详细介绍 →](2026-05-26/articles/01-owner0__repo0.md)" in content
        assert "[详细介绍 →](2026-05-26/articles/10-owner9__repo9.md)" in content


def test_render_all_does_not_create_image_or_prompt_dirs(monkeypatch):
    today = "2026-05-26"
    repos = [make_illustrated(f"owner{i}/repo{i}", i + 1, today) for i in range(10)]
    for repo in repos:
        repo.image_path = ""
    articles = {repo.repo.repo.full_name: "## Intro\n\nBody" for repo in repos}

    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        monkeypatch.setattr("trending.render.VAULT_DIR", str(vault_dir))

        render_all(repos, today, articles)

        daily_dir = vault_dir / today
        assert (daily_dir / "daily.md").exists()
        assert len(list((daily_dir / "articles").glob("*.md"))) == 10
        assert len(list((daily_dir / "douyin-prompts").glob("*.json"))) == 11
        assert not (daily_dir / "assets").exists()
        assert not (daily_dir / "prompts").exists()
        repo_index = (vault_dir / "repos" / "owner9__repo9.md").read_text("utf-8")
        assert f"[[{today}/articles/10-owner9__repo9|{today}]]" in repo_index


def test_render_douyin_prompts_writes_summary_and_project_json():
    today = "2026-05-27"
    repos = [
        make_illustrated("alpha/one", 1, today),
        make_illustrated("beta/two", 2, today),
    ]

    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        previous_dir = vault_dir / "2026-05-25"
        previous_dir.mkdir(parents=True)
        previous_dir.joinpath("daily.md").write_text(
            "\n".join([
                "# GitHub Trending — 2026-05-25",
                "",
                "## 1. [[repos/alpha__one|alpha/one]]",
                "",
            ]),
            encoding="utf-8",
        )
        daily_dir = vault_dir / today

        render_douyin_prompts(
            repos,
            today,
            daily_dir,
            {"alpha/one": "一个专属视觉实验室展示独特项目能力"},
        )

        prompts_dir = daily_dir / "douyin-prompts"
        files = sorted(path.name for path in prompts_dir.glob("*.json"))
        assert files == [
            "00-summary.json",
            "01-alpha__one.json",
            "02-beta__two.json",
        ]

        summary = json.loads((prompts_dir / "00-summary.json").read_text("utf-8"))
        assert summary["aspect_ratio"] == "9:16 portrait (1080×1920)"
        assert summary["safe_area"]["top_reserved_area"].startswith("画面顶部约 180px")
        assert summary["title_block"]["position"].startswith("从画面顶部约 220px")
        assert summary["title_block"]["hook_headline"] == "今日最值得看的开源项目"
        assert summary["date_badge"]["text"] == "2026.05.27"
        assert "醒目" in summary["date_badge"]["style"]
        assert "标题贴近顶部边缘" in summary["constraints"]["avoid"]
        assert "顶部安全区大面积空白" in summary["constraints"]["avoid"]
        assert summary["comparison"]["baseline_date"] == "2026-05-25"
        assert summary["comparison"]["new_entries"] == ["02 beta/two"]
        stat_labels = [card["label"] for card in summary["stats_row"]["cards"]]
        assert "今日上榜" not in stat_labels
        assert stat_labels == ["新上榜", "最高日增", "最高星标"]
        assert summary["ranking_strip"]["items"] == [
            "01 one · 100★",
            "02 two · 100★ · 🆕 新上榜",
        ]

        project = json.loads((prompts_dir / "01-alpha__one.json").read_text("utf-8"))
        assert project["type"] == "短视频项目介绍卡"
        assert project["safe_area"]["top_reserved_area"].startswith("画面顶部约 180px")
        assert project["title_block"]["main_title"] == "one"
        assert project["title_block"]["position"].startswith("从画面顶部约 220px")
        assert "hook_headline" in project["title_block"]
        assert project["content"]["repo"] == "alpha/one"
        assert "tagline" not in project["content"]
        assert "intro_cards" in project["content"]
        assert "workflow_nodes" in project["content"]
        assert project["content"]["visual_hint"] == "一个专属视觉实验室展示独特项目能力"
        assert "不要把长段落简介放进画面" in project["layout_rules"]
        assert "主视觉必须表达项目用途和工作流，不能只是一张无信息量的大插画" in project["layout_rules"]
        assert "..." not in project["prompt_cn"]
        assert "…" not in project["prompt_cn"]
        assert "核心功能大字" in project["prompt_cn"]
        assert "功能流程图式主视觉" in project["prompt_cn"]

        assert not (prompts_dir / "all-prompts.md").exists()


def test_render_douyin_prompt_for_short_video_generator_is_workflow_first():
    today = "2026-05-28"
    repo = EnrichedRepo(
        owner="harry0703",
        name="MoneyPrinterTurbo",
        full_name="harry0703/MoneyPrinterTurbo",
        description="AI-powered short video generator",
        language="Python",
        stars_total=63500,
        stars_today=1700,
        url="https://github.com/harry0703/MoneyPrinterTurbo",
    )
    summarized = SummarizedRepo(
        repo=repo,
        intro_zh="MoneyPrinterTurbo 是一个基于 AI 大模型的短视频自动生成工具。用户只需提供视频主题或关键词，即可自动完成文案撰写、素材匹配、字幕添加和背景音乐合成，最终输出高清短视频。",
        image_prompt_en="",
    )
    repos = [IllustratedRepo(repo=summarized, image_path="")]

    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / today
        render_douyin_prompts(repos, today, daily_dir)

        project = json.loads(
            (daily_dir / "douyin-prompts" / "01-harry0703__MoneyPrinterTurbo.json").read_text("utf-8")
        )

    assert project["title_block"]["hook_headline"] == "AI 一键生成短视频"
    assert project["content"]["workflow_nodes"] == ["输入主题", "写文案", "找素材", "加字幕", "配音乐", "高清成片"]
    assert [card["text"] for card in project["content"]["intro_cards"]] == [
        "AI短视频",
        "主题关键词",
        "文案素材",
        "字幕配乐",
        "开源免费",
    ]
    assert "媒体服务器" not in project["prompt_cn"]
    assert "输入/核心能力/输出结果" in project["prompt_cn"]
    assert "AI 一键生成短视频" in project["prompt_cn"]


def test_render_douyin_description_writes_md_file():
    with tempfile.TemporaryDirectory() as tmp:
        daily_dir = Path(tmp) / "2026-05-27"

        render_douyin_description("今天的抖音文案", daily_dir)

        assert (daily_dir / "douyin-description.md").read_text("utf-8") == "今天的抖音文案\n"


def test_render_gpt_prompts_is_noop(monkeypatch):
    today = "2026-05-26"
    repos = [make_illustrated("owner/repo", 1, today)]
    repos[0].repo.gpt_image_prompt = '{"prompt": "unused"}'

    with tempfile.TemporaryDirectory() as tmp:
        vault_dir = Path(tmp)
        monkeypatch.setattr("trending.render.VAULT_DIR", str(vault_dir))

        render_gpt_prompts(repos, today)

        assert not (vault_dir / today / "prompts").exists()


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
