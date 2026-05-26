"""Obsidian vault file writer."""
import re
from pathlib import Path
from trending.config import IllustratedRepo, VAULT_DIR


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


def render_daily_md(repos: list[IllustratedRepo], today: str, daily_dir: Path) -> None:
    """Write daily.md with frontmatter, overview embed, and 10 numbered repo sections."""
    lines = [
        "---",
        "tags:",
        "  - trending",
        "  - daily",
        f"date: {today}",
        "type: daily",
        f"count: {len(repos)}",
        "---",
        "",
        f"# GitHub Trending — {today}",
        "",
        f"![[{today}/assets/overview.png]]",
        "",
    ]

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

    daily_dir.mkdir(parents=True, exist_ok=True)
    (daily_dir / "daily.md").write_text("\n".join(lines), encoding="utf-8")


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
    so the newest item appears first within that section.

    The pattern consumes the heading line plus an optional trailing blank
    line so we can rebuild the section with exactly one blank line between
    heading and entries — preventing accumulation across daily updates.
    """
    pattern = rf"^({re.escape(heading)})\n(\n)?"
    if re.search(pattern, content, flags=re.MULTILINE):
        return re.sub(
            pattern,
            rf"\g<1>\n\n{entry}\n",
            content,
            count=1,
            flags=re.MULTILINE,
        )
    return content.rstrip() + f"\n\n{heading}\n\n{entry}\n"


def render_index_md(today: str, vault_dir: Path) -> None:
    """Prepend today's link to _index.md MOC page.

    If _index.md exists, the link is inserted right after the ``## 历次``
    heading so the most recent day appears first.  If the file does not exist,
    a full MOC template is created.
    """
    index_path = vault_dir / "_index.md"
    today_link = f"- [[{today}/daily|{today}]]"

    if index_path.exists():
        content = index_path.read_text("utf-8")
        # Insert after the "## 历次" heading (most-recent-first)
        pattern = r"^(## 历次\s*\n)"
        if re.search(pattern, content, flags=re.MULTILINE):
            content = re.sub(
                pattern,
                rf"\g<1>\n{today_link}\n",
                content,
                flags=re.MULTILINE,
            )
        else:
            content = content.rstrip() + f"\n\n{today_link}\n"
        index_path.write_text(content, encoding="utf-8")
    else:
        lines = [
            "---",
            "tags: [moc]",
            "---",
            "",
            "# MOC",
            "",
            "## 历次",
            "",
            today_link,
            "",
        ]
        vault_dir.mkdir(parents=True, exist_ok=True)
        index_path.write_text("\n".join(lines), encoding="utf-8")


def render_bases(vault_dir: Path) -> None:
    """Write ``trending.base`` if it does not already exist (idempotent).

    Defines filters, properties, and views for Obsidian Bases so the vault
    can present a structured table of all trending repositories.
    """
    base_path = vault_dir / "trending.base"
    if base_path.exists():
        return

    lines = [
        "---",
        "filters:",
        "  - field: tags",
        "    value: github-trending",
        "properties:",
        "  - name: repo",
        "    type: text",
        "  - name: language",
        "    type: text",
        "  - name: first_seen",
        "    type: date",
        "  - name: appearances",
        "    type: number",
        "  - name: tags",
        "    type: multitext",
        "views:",
        "  - type: table",
        "    name: All Repos",
        "    columns:",
        "      - repo",
        "      - language",
        "      - appearances",
        "      - first_seen",
        "---",
        "",
    ]

    vault_dir.mkdir(parents=True, exist_ok=True)
    base_path.write_text("\n".join(lines), encoding="utf-8")


def render_gpt_prompts(repos: list[IllustratedRepo], today: str) -> None:
    """Save gpt-image-2 bento-grid prompt JSON files per repo.

    Each file is written to ``vault/Inno/GithubTrending/<today>/prompts/``
    as ``{idx:02d}-{owner}__{name}.json``.  Repos with an empty prompt are
    skipped.
    """
    vault = Path(VAULT_DIR)
    prompts_dir = vault / today / "prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    for i, illustrated in enumerate(repos, start=1):
        prompt = illustrated.repo.gpt_image_prompt
        if not prompt:
            continue

        r = illustrated.repo.repo
        safe_name = r.full_name.replace("/", "__")
        filename = f"{i:02d}-{safe_name}.json"
        file_path = prompts_dir / filename
        file_path.write_text(prompt, encoding="utf-8")


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
