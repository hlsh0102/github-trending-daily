"""Obsidian vault file writer."""
import re
from pathlib import Path
from trending.config import IllustratedRepo, VAULT_DIR


def render_all(repos: list[IllustratedRepo], today: str) -> None:
    """Orchestrate writing all vault files. Creates directories as needed."""
    vault = Path(VAULT_DIR)
    daily_dir = vault / today
    assets_dir = daily_dir / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    repos_dir = vault / "repos"
    repos_dir.mkdir(parents=True, exist_ok=True)

    render_daily_md(repos, today, daily_dir)
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
            "",
        ])

    daily_dir.mkdir(parents=True, exist_ok=True)
    (daily_dir / "daily.md").write_text("\n".join(lines), encoding="utf-8")


def render_repo_md(illustrated: IllustratedRepo, today: str, repos_dir: Path) -> None:
    """Write or update repos/<owner>__<name>.md.

    If the file already exists, append today's appearance to the history list
    and increment the appearances counter. Otherwise, create a new file with
    frontmatter, intro, and history section.
    """
    r = illustrated.repo.repo
    safe_name = r.full_name.replace("/", "__")
    file_path = repos_dir / f"{safe_name}.md"

    history_entry = f"- [[{today}/daily|{today}]] — {r.stars_today} stars"

    if file_path.exists():
        content = file_path.read_text("utf-8")
        # Increment appearances counter in frontmatter
        content = re.sub(
            r"^appearances: (\d+)$",
            lambda m: f"appearances: {int(m.group(1)) + 1}",
            content,
            flags=re.MULTILINE,
        )
        # Append today's history entry
        content = content.rstrip() + f"\n{history_entry}\n"
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
            illustrated.repo.intro_zh,
            "",
            "## 上榜历史",
            "",
            history_entry,
            "",
        ]
        repos_dir.mkdir(parents=True, exist_ok=True)
        file_path.write_text("\n".join(lines), encoding="utf-8")


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
