# Daily Articles Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Generate a detailed Chinese article (800–1500 字, 7 sections) per trending repo each day, store under `vault/Inno/GithubTrending/<today>/articles/`, link from `daily.md`, and upgrade `repos/<owner>__<name>.md` to an index page that lists every day's article.

**Architecture:** A new module `src/trending/article.py` calls DeepSeek (one call per repo) to produce markdown bodies. `render.py` gains an `render_articles` function and is updated so `render_daily_md` adds a `[详细介绍 →]` link and `render_repo_md` becomes a two-history index page with auto-migration for legacy files. `main.py` inserts a `generate_articles` step before `render_all`.

**Tech Stack:** Python 3.11+, OpenAI SDK (DeepSeek-compatible), pytest, existing dataclasses (`IllustratedRepo`, `EnrichedRepo`, `SummarizedRepo`).

**Spec:** `docs/superpowers/specs/2026-05-26-daily-articles-design.md`

---

## File Structure

| Path | Action | Purpose |
|------|--------|---------|
| `src/trending/article.py` | **Create** | DeepSeek call + fallback; `generate_articles()` |
| `src/trending/render.py` | Modify | New `render_articles`; updated `render_daily_md`, `render_repo_md`, `render_all` |
| `src/trending/main.py` | Modify | Insert article-generation step; pass `articles` into `render_all` |
| `tests/test_article.py` | **Create** | Unit tests for `generate_articles` (mocked client) |
| `tests/test_render.py` | Modify | Tests for new render functions and migration |

---

## Task 1: Create article module skeleton with fallback

**Files:**
- Create: `src/trending/article.py`
- Create: `tests/test_article.py`

- [ ] **Step 1: Write the failing test for fallback path**

Create `tests/test_article.py`:

```python
"""Tests for article module."""
from unittest.mock import MagicMock, patch

from trending.article import generate_articles
from trending.config import EnrichedRepo, IllustratedRepo, SummarizedRepo


def _make_illustrated(full_name: str, intro: str = "短简介。") -> IllustratedRepo:
    owner, name = full_name.split("/")
    er = EnrichedRepo(
        owner=owner,
        name=name,
        full_name=full_name,
        description="desc",
        language="Python",
        stars_total=1000,
        stars_today=42,
        url=f"https://github.com/{full_name}",
    )
    sr = SummarizedRepo(repo=er, intro_zh=intro, image_prompt_en="")
    return IllustratedRepo(repo=sr, image_path="x.png")


def test_generate_articles_fallback_on_exception():
    repo = _make_illustrated("owner/name", intro="回退中文简介")

    with patch("trending.article.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.side_effect = RuntimeError("boom")
        mock_openai.return_value = client

        result = generate_articles([repo])

    assert result == {"owner/name": "回退中文简介"}
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_article.py::test_generate_articles_fallback_on_exception -v`
Expected: FAIL with `ModuleNotFoundError: No module named 'trending.article'`

- [ ] **Step 3: Implement minimal `article.py`**

Create `src/trending/article.py`:

```python
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
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_article.py::test_generate_articles_fallback_on_exception -v`
Expected: PASS

- [ ] **Step 5: Stage new files**

```bash
git add src/trending/article.py tests/test_article.py
```

---

## Task 2: Add success-path test for `generate_articles`

**Files:**
- Modify: `tests/test_article.py`

- [ ] **Step 1: Add the success test**

Append to `tests/test_article.py`:

```python
def test_generate_articles_success_path():
    repo = _make_illustrated("owner/name")

    fake_resp = MagicMock()
    fake_resp.choices = [MagicMock()]
    fake_resp.choices[0].message.content = "## 项目概述\n\n这是一个项目。"

    with patch("trending.article.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.return_value = fake_resp
        mock_openai.return_value = client

        result = generate_articles([repo])

    assert "owner/name" in result
    assert result["owner/name"].startswith("## 项目概述")
```

- [ ] **Step 2: Run the new test**

Run: `pytest tests/test_article.py::test_generate_articles_success_path -v`
Expected: PASS

---

## Task 3: Implement `render_articles`

**Files:**
- Modify: `src/trending/render.py`
- Modify: `tests/test_render.py`

- [ ] **Step 1: Write failing test**

Append to `tests/test_render.py`:

```python
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
```

- [ ] **Step 2: Run tests to verify they fail**

Run: `pytest tests/test_render.py::test_render_articles_writes_files_with_frontmatter -v`
Expected: FAIL with `ImportError: cannot import name 'render_articles'`

- [ ] **Step 3: Implement `render_articles`**

Append to `src/trending/render.py`:

```python
def render_articles(
    articles: dict[str, str],
    repos: list[IllustratedRepo],
    today: str,
    daily_dir: Path,
) -> None:
    """Write detailed article markdown files to ``<daily_dir>/articles/``.

    For each repo whose ``full_name`` is present in ``articles``, write
    ``{idx:02d}-{owner}__{name}.md`` with a frontmatter block plus the
    LLM-generated body. Repos absent from ``articles`` are skipped silently.
    """
    articles_dir = daily_dir / "articles"
    articles_dir.mkdir(parents=True, exist_ok=True)

    for i, illustrated in enumerate(repos, start=1):
        r = illustrated.repo.repo
        body = articles.get(r.full_name)
        if body is None:
            continue

        safe_name = r.full_name.replace("/", "__")
        filename = f"{i:02d}-{safe_name}.md"
        frontmatter = "\n".join([
            "---",
            "tags:",
            "  - trending",
            "  - article",
            f"repo: {r.full_name}",
            f"date: {today}",
            f"language: {r.language or 'Unknown'}",
            f"stars_total: {r.stars_total}",
            f"stars_today: {r.stars_today}",
            "---",
            "",
        ])
        content = frontmatter + body.strip() + "\n"
        (articles_dir / filename).write_text(content, encoding="utf-8")
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `pytest tests/test_render.py::test_render_articles_writes_files_with_frontmatter tests/test_render.py::test_render_articles_skips_missing_entries -v`
Expected: PASS

---

## Task 4: Add `[详细介绍 →]` link to `render_daily_md`

**Files:**
- Modify: `src/trending/render.py:23-57`
- Modify: `tests/test_render.py`

- [ ] **Step 1: Write failing test**

Append to `tests/test_render.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py::test_render_daily_md_includes_article_link -v`
Expected: FAIL — `[详细介绍 →]` not in content.

- [ ] **Step 3: Modify `render_daily_md`**

In `src/trending/render.py`, replace the loop body (current lines 41–54):

```python
    for i, illustrated in enumerate(repos, start=1):
        r = illustrated.repo.repo
        safe_name = r.full_name.replace("/", "__")
        idx_str = f"{i:02d}"
        lines.extend([
            f"## {i}. [[repos/{safe_name}|{r.full_name}]]",
            "",
            f"![[{today}/assets/{idx_str}-{safe_name}.png]]",
            "",
            illustrated.repo.intro_zh,
            "",
            f"[GitHub]({r.url})",
            f"[详细介绍 →]({today}/articles/{idx_str}-{safe_name}.md)",
            "",
        ])
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py::test_render_daily_md_includes_article_link -v`
Expected: PASS

- [ ] **Step 5: Run full render test suite to make sure nothing else broke**

Run: `pytest tests/test_render.py -v`
Expected: ALL PASS (including pre-existing `test_render_daily_md`).

---

## Task 5: Rewrite `render_repo_md` as index page (new-file branch)

**Files:**
- Modify: `src/trending/render.py:60-107`
- Modify: `tests/test_render.py`

- [ ] **Step 1: Write failing test for new file**

Append to `tests/test_render.py`:

```python
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
```

- [ ] **Step 2: Run test to verify it fails**

Run: `pytest tests/test_render.py::test_render_repo_md_new_format_creates_index_page -v`
Expected: FAIL — `## 详细介绍历史` not in content.

- [ ] **Step 3: Replace `render_repo_md` in `src/trending/render.py`**

Replace the entire current `render_repo_md` function (lines 60–107) with:

```python
def render_repo_md(illustrated: IllustratedRepo, today: str, repos_dir: Path) -> None:
    """Write or update ``repos/<owner>__<name>.md`` index page.

    Sections (in order):
      1. Frontmatter (tags, repo, language, first_seen, appearances)
      2. Title (``# owner/name``)
      3. Quote-style ``intro_zh``
      4. ``## 详细介绍历史`` — newest entries on top
      5. ``## 上榜历史`` — new entries inserted on top; legacy entries kept as-is

    On update:
      * Increment ``appearances``
      * Auto-migrate legacy files missing ``## 详细介绍历史`` by inserting
        an empty section before ``## 上榜历史``
      * Prepend today's article link to ``## 详细介绍历史``
      * Prepend today's daily link to ``## 上榜历史``
    """
    r = illustrated.repo.repo
    safe_name = r.full_name.replace("/", "__")
    file_path = repos_dir / f"{safe_name}.md"

    article_idx = _article_index_for(illustrated)
    article_entry = (
        f"- [[{today}/articles/{article_idx:02d}-{safe_name}|{today}]]"
    )
    daily_entry = f"- [[{today}/daily|{today}]] — {r.stars_today} stars"

    if file_path.exists():
        content = file_path.read_text("utf-8")
        content = re.sub(
            r"^appearances: (\d+)$",
            lambda m: f"appearances: {int(m.group(1)) + 1}",
            content,
            flags=re.MULTILINE,
        )
        content = _ensure_articles_section(content)
        content = _prepend_to_section(content, "## 详细介绍历史", article_entry)
        content = _prepend_to_section(content, "## 上榜历史", daily_entry)
        file_path.write_text(content, encoding="utf-8")
    else:
        lines = [
            "---",
            "tags:",
            "  - trending",
            "  - repo",
            f"repo: {r.full_name}",
            f"language: {r.language or 'Unknown'}",
            f"first_seen: {today}",
            "appearances: 1",
            "---",
            "",
            f"# {r.full_name}",
            "",
            f"> {illustrated.repo.intro_zh}",
            "",
            "## 详细介绍历史",
            "",
            article_entry,
            "",
            "## 上榜历史",
            "",
            daily_entry,
            "",
        ]
        repos_dir.mkdir(parents=True, exist_ok=True)
        file_path.write_text("\n".join(lines), encoding="utf-8")


def _article_index_for(illustrated: IllustratedRepo) -> int:
    """Extract the article index from the image_path's filename prefix.

    The image was renamed to ``{idx:02d}-{owner}__{name}.png`` by main.py;
    the article uses the same index. Falls back to 1 if parsing fails.
    """
    try:
        stem = Path(illustrated.image_path).stem
        prefix = stem.split("-", 1)[0]
        return int(prefix)
    except (ValueError, IndexError):
        return 1


def _ensure_articles_section(content: str) -> str:
    """Insert an empty ``## 详细介绍历史`` section before ``## 上榜历史``
    if the file does not yet contain it (legacy migration)."""
    if "## 详细介绍历史" in content:
        return content
    if "## 上榜历史" in content:
        return content.replace(
            "## 上榜历史",
            "## 详细介绍历史\n\n## 上榜历史",
            1,
        )
    return content.rstrip() + "\n\n## 详细介绍历史\n\n## 上榜历史\n"


def _prepend_to_section(content: str, heading: str, entry: str) -> str:
    """Insert ``entry`` immediately after ``heading`` (with a blank line),
    so the newest item appears first within that section."""
    pattern = rf"^({re.escape(heading)}\s*\n)"
    if re.search(pattern, content, flags=re.MULTILINE):
        return re.sub(
            pattern,
            rf"\g<1>\n{entry}\n",
            content,
            count=1,
            flags=re.MULTILINE,
        )
    return content.rstrip() + f"\n\n{heading}\n\n{entry}\n"
```

- [ ] **Step 4: Run test to verify it passes**

Run: `pytest tests/test_render.py::test_render_repo_md_new_format_creates_index_page -v`
Expected: PASS

- [ ] **Step 5: Verify pre-existing test still passes (it expects `## 上榜历史` and `appearances: 1`)**

Run: `pytest tests/test_render.py::test_render_repo_md_creates_new -v`
Expected: PASS

---

## Task 6: Add update + migration tests for `render_repo_md`

**Files:**
- Modify: `tests/test_render.py`

- [ ] **Step 1: Write update test**

Append to `tests/test_render.py`:

```python
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
```

- [ ] **Step 2: Run new tests**

Run: `pytest tests/test_render.py::test_render_repo_md_appends_to_existing_new_format tests/test_render.py::test_render_repo_md_migrates_legacy_file -v`
Expected: PASS (the implementation in Task 5 already covers these paths).

---

## Task 7: Wire `render_articles` into `render_all`

**Files:**
- Modify: `src/trending/render.py:7-20`
- Modify: `tests/test_main_pipeline.py` (if it calls `render_all`)

- [ ] **Step 1: Check whether existing tests call `render_all`**

Run: `grep -n "render_all" tests/`
If `render_all` is called with the old 2-arg signature, those tests will need updating in this task. Otherwise skip the test edits.

- [ ] **Step 2: Update `render_all` signature and body**

In `src/trending/render.py`, replace the current `render_all`:

```python
def render_all(
    repos: list[IllustratedRepo],
    today: str,
    articles: dict[str, str] | None = None,
) -> None:
    """Orchestrate writing all vault files. Creates directories as needed.

    ``articles`` maps ``full_name`` → markdown body. When provided,
    ``render_articles`` writes one file per repo under ``<today>/articles/``.
    When omitted, the articles step is skipped (preserves backward
    compatibility for tests that don't exercise this path).
    """
    vault = Path(VAULT_DIR)
    daily_dir = vault / today
    assets_dir = daily_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    repos_dir = vault / "repos"
    repos_dir.mkdir(parents=True, exist_ok=True)

    render_daily_md(repos, today, daily_dir)
    if articles:
        render_articles(articles, repos, today, daily_dir)
    for repo in repos:
        render_repo_md(repo, today, repos_dir)
    render_index_md(today, vault)
    render_bases(vault)
```

- [ ] **Step 3: If existing tests passed `render_all(repos, today)` with no articles, leave them alone — the optional kwarg keeps them green.**

- [ ] **Step 4: Run full render test file**

Run: `pytest tests/test_render.py -v`
Expected: ALL PASS.

---

## Task 8: Hook article generation into `main.py`

**Files:**
- Modify: `src/trending/main.py:28` (import) and pipeline body

- [ ] **Step 1: Add import**

In `src/trending/main.py`, add to imports:

```python
from trending.article import generate_articles
```

- [ ] **Step 2: Insert article-generation step before `render_all`**

Locate the section labelled `# 8. Render vault files` (around line 121). Insert immediately before it:

```python
    # 7c. Generate detailed Chinese articles
    logger.info("Step 7c: Generating articles for %d repos ...", len(all_illustrated))
    articles = generate_articles(all_illustrated)
    logger.info("  Generated %d articles", len(articles))
```

- [ ] **Step 3: Update the `render_all` call to pass articles**

Change:
```python
    render_all(all_illustrated, today)
```
to:
```python
    render_all(all_illustrated, today, articles)
```

- [ ] **Step 4: Run main pipeline tests**

Run: `pytest tests/test_main_pipeline.py -v`
Expected: PASS. If a test mocks `render_all` or pipeline steps, ensure it doesn't break on the new `generate_articles` call (mock it if needed — see Step 5).

- [ ] **Step 5: If a pipeline test fails because `generate_articles` is hit unexpectedly, mock it**

Open `tests/test_main_pipeline.py`, find the existing patches block, and add:

```python
@patch("trending.main.generate_articles", return_value={})
```

to the decorator stack of any test that calls `main()`. Ensure the new mock parameter is added to the test signature in the correct order (decorators are applied bottom-up; the outermost decorator's mock is the last argument).

Re-run: `pytest tests/test_main_pipeline.py -v`
Expected: PASS.

---

## Task 9: Full test suite + lint sanity

**Files:** none

- [ ] **Step 1: Run full test suite**

Run: `pytest tests/ -v`
Expected: ALL PASS.

- [ ] **Step 2: Quick smoke check — import every module**

Run: `python -c "from trending import article, render, main; print('ok')"`
Expected: prints `ok`.

- [ ] **Step 3: Stage all modified/new files**

```bash
git add src/trending/article.py src/trending/render.py src/trending/main.py tests/test_article.py tests/test_render.py
# Also stage tests/test_main_pipeline.py if Task 8 Step 5 modified it.
git add -u tests/test_main_pipeline.py
```

---

## Self-Review Notes

- **Spec coverage:** every numbered section in the spec maps to a task —
  - §3.1 article module → Tasks 1–2
  - §3.2 render changes → Tasks 3–7 (`render_articles`, daily.md link, repo_md rewrite, migration, render_all signature)
  - §3.3 main.py wiring → Task 8
  - §6 testing → tests are colocated with each implementation task (TDD)
  - §7 acceptance criteria → covered by Task 9 full-suite run
- **Type consistency:** `render_articles(articles, repos, today, daily_dir)` signature is identical across Task 3 (definition) and Task 7 (caller). `render_all` keeps `articles` optional so old call sites don't break.
- **No placeholders:** every code step shows full code; commands are exact; expected outputs are stated.
- **Article index source:** Task 5 derives the article index from `illustrated.image_path` (already renamed by `main._rename_images` before render). This avoids threading an explicit index through every render call.
