"""Obsidian vault file writer."""
import json
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
    repos_dir = vault / "repos"
    repos_dir.mkdir(parents=True, exist_ok=True)

    render_daily_md(repos, today, daily_dir)
    if articles:
        render_articles(articles, repos, today, daily_dir)
    render_douyin_prompts(repos, today, daily_dir)
    for i, repo in enumerate(repos, start=1):
        render_repo_md(repo, today, repos_dir, article_idx=i)
    render_index_md(today, vault)
    render_bases(vault)


def render_daily_md(repos: list[IllustratedRepo], today: str, daily_dir: Path) -> None:
    """Write daily.md with frontmatter and 10 numbered repo sections."""
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
    ]

    for i, illustrated in enumerate(repos, start=1):
        r = illustrated.repo.repo
        safe_name = r.full_name.replace("/", "__")
        idx_str = f"{i:02d}"
        lines.extend([
            f"## {i}. [[repos/{safe_name}|{r.full_name}]]",
            "",
            illustrated.repo.intro_zh,
            "",
            f"[GitHub]({r.url})",
            f"[详细介绍 →]({today}/articles/{idx_str}-{safe_name}.md)",
            "",
        ])

    daily_dir.mkdir(parents=True, exist_ok=True)
    (daily_dir / "daily.md").write_text("\n".join(lines), encoding="utf-8")


def render_repo_md(
    illustrated: IllustratedRepo,
    today: str,
    repos_dir: Path,
    article_idx: int | None = None,
) -> None:
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

    article_idx = article_idx or _article_index_for(illustrated)
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
    """Deprecated no-op: prompt JSON output is intentionally disabled."""
    return None


def render_douyin_prompts(
    repos: list[IllustratedRepo],
    today: str,
    daily_dir: Path,
) -> None:
    """Write Douyin image prompt JSON files for summary and repo cards."""
    prompts_dir = daily_dir / "douyin-prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)

    _write_json(prompts_dir / "00-summary.json", _build_summary_prompt(repos, today))
    for i, illustrated in enumerate(repos, start=1):
        r = illustrated.repo.repo
        safe_name = r.full_name.replace("/", "__")
        _write_json(
            prompts_dir / f"{i:02d}-{safe_name}.json",
            _build_project_prompt(illustrated, today, i),
        )


def _write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _build_summary_prompt(repos: list[IllustratedRepo], today: str) -> dict:
    top_repo = max(repos, key=lambda item: item.repo.repo.stars_today, default=None)
    max_total = max((item.repo.repo.stars_total for item in repos), default=0)
    max_today = max((item.repo.repo.stars_today for item in repos), default=0)
    date_label = today.replace("-", ".")
    focus_name = top_repo.repo.repo.name if top_repo else "GitHub Trending"

    return {
        "type": "短视频封面 + 便当格混合信息图",
        "goal": "生成一张抖音9:16竖屏封面，GitHub Trending TOP10汇总，标题抓眼球、数据震撼、便当格模块布局，同时适配手机刘海/摄像头遮挡区域",
        "aspect_ratio": "9:16 portrait (1080×1920)",
        "safe_area": _douyin_safe_area(),
        "background": {
            "color": "深黑蓝渐变 #0D1117 → #161B22 → #0D1117",
            "texture": "细微网格线(git风格) + 右下角一个巨大的半透明GitHub猫咪logo水印",
        },
        "title_block": {
            "main_title": "🔥 GitHub今日TOP10",
            "position": "从画面顶部约 260px 开始，居中偏上，但不要贴近顶部边缘",
            "title_style": "白色超粗体(#FFFFFF)，字号极大，1米外清晰可辨，带绿色(#238636)下划线装饰",
            "subtitle": f"{date_label} · 开源项目精选 · {focus_name} 暴涨{_format_stars(max_today)}⭐",
            "subtitle_style": "浅灰(#8B949E)，中号字，紧贴主标题下方，但不得进入顶部安全区",
        },
        "hero_module": {
            "position": "标题下方，画面中上部 40% 区域",
            "style": "大圆角卡片(24px)，半透明深色底(#1C2128)，绿色(#238636)左边框",
            "content": _summary_hero_content(top_repo),
        },
        "stats_row": {
            "position": "hero模块下方，三张关键数字卡片横排",
            "style": "3个等宽卡片，背景半透明黑，数字大号发光",
            "cards": [
                {"number": str(len(repos)), "label": "今日上榜", "color": "#238636"},
                {"number": _format_stars(max_total), "label": "最高星标", "color": "#D4A574"},
                {"number": _format_stars(max_today), "label": "最高日增", "color": "#58A6FF"},
            ],
        },
        "ranking_strip": {
            "position": "画面下半部，但避开底部160px安全区",
            "style": "5行×2列紧凑排列，每个条目一行：排名数字(01-10，绿色粗体) + 项目名(白色) + 星标数(金色小字)",
            "items": [
                f"{i:02d} {item.repo.repo.name} · {_format_stars(item.repo.repo.stars_total)}★"
                for i, item in enumerate(repos, start=1)
            ],
        },
        "bottom_bar": {
            "text": "每天一分钟，带你了解全球开发者都在关注什么 🔍",
            "position": "底部安全区上方，不贴底",
            "style": "底部白色细线分隔 + 灰色小字居中",
            "handle": "@GitHub精选日报",
        },
        "constraints": _douyin_constraints(),
    }


def _build_project_prompt(illustrated: IllustratedRepo, today: str, index: int) -> dict:
    r = illustrated.repo.repo
    intro = _clean_one_line(illustrated.repo.intro_zh)
    title = r.name
    language = r.language or "Unknown"
    tags = _project_tags(r, intro)
    prompt_cn = (
        "一张中文科技项目介绍卡，9:16竖屏(1080×1920)，暗色科技风。"
        "画面顶部至少留出220px安全区，不放标题和重要文字；"
        f"标题块从约260px处开始：项目名「{title}」白色超粗体，"
        f"下方标签「#{index:02d} · {language} · {_format_stars(r.stars_total)}★」。"
        "背景为深黑蓝渐变(#0D1117到#161B22)，带细微git网格和霓虹绿点缀。"
        f"中央主视觉：{_visual_hint(r, intro)}。"
        f"插画下方三列关键数据：「{_format_stars(r.stars_total)} 总星标」"
        f"「+{_format_stars(r.stars_today)} 今日增长」「{language}」。"
        f"中下部中文简介：「{intro}」"
        f"底部标签栏：「{' '.join(tags)}」。"
        "字体使用粗体无衬线，绿色#238636和金色#D4A574作为强调色，"
        "整体像真实抖音科技博主的高质量封面，不要PPT截图，不要卡通可爱风。"
    )

    return {
        "type": "短视频项目介绍卡",
        "goal": "生成一张抖音9:16竖屏项目介绍封面，突出项目名、核心用途、星标数据和科技感主视觉",
        "aspect_ratio": "9:16 portrait (1080×1920)",
        "safe_area": _douyin_safe_area(),
        "background": {
            "color": "深黑蓝渐变 #0D1117 → #161B22 → #0D1117",
            "texture": "细微网格线(git风格) + 低透明度代码线条 + 霓虹绿节点点缀",
        },
        "title_block": {
            "main_title": title,
            "position": "从画面顶部约 260px 开始，居中偏上，但不要贴近顶部边缘",
            "title_style": "白色超粗体(#FFFFFF)，字号极大，带绿色(#238636)短下划线",
            "subtitle": f"#{index:02d} · {language} · {_format_stars(r.stars_total)}★",
            "subtitle_style": "浅灰(#8B949E)，中号字，紧贴主标题下方，但不得进入顶部安全区",
        },
        "content": {
            "repo": r.full_name,
            "date": today,
            "tagline": intro,
            "visual_hint": _visual_hint(r, intro),
            "stats": [
                {"number": _format_stars(r.stars_total), "label": "总星标", "color": "#D4A574"},
                {"number": f"+{_format_stars(r.stars_today)}", "label": "今日增长", "color": "#238636"},
                {"number": language, "label": "主要语言", "color": "#58A6FF"},
            ],
            "tags": tags,
        },
        "prompt_cn": prompt_cn,
        "constraints": _douyin_constraints(),
    }


def _douyin_safe_area() -> dict:
    return {
        "top_reserved_area": "画面顶部至少留出 220px 安全区，不放主标题、副标题、项目名、关键数字等重要信息",
        "title_position": "主标题整体下移，标题块顶部从画面约 260px 处开始，位于抖音刘海/状态栏下方",
        "top_area_usage": "顶部安全区只允许放非常淡的网格、星点、GitHub风格装饰线，不放任何可读文字",
        "bottom_reserved_area": "底部至少留出 160px，避免抖音文案、按钮或进度条遮挡核心信息",
    }


def _douyin_constraints() -> dict:
    return {
        "must_feel": "像真实抖音科技博主的高质量封面，不是PPT截图",
        "must_keep": [
            "主标题不能出现在画面顶部220px以内",
            "主标题在1米外清晰可辨",
            "绿色(#238636)和金色(#D4A574)作为强调色贯穿全图",
            "至少3处出现大数字做视觉锚点",
            "排名区域清晰但不抢主标题",
            "整体暗色科技感+霓虹点缀",
        ],
        "avoid": [
            "标题贴近顶部边缘",
            "标题文字被手机刘海、摄像头、状态栏或任何元素遮挡",
            "纯黑背景(要有层次)",
            "信息堆砌到看不清",
            "超过5种颜色",
            "卡通/可爱/手账风格",
        ],
    }


def _summary_hero_content(top_repo: IllustratedRepo | None) -> dict:
    if top_repo is None:
        return {
            "title": "🏆 今日焦点",
            "project": "GitHub Trending",
            "tagline": "今日开源项目精选",
            "big_number": "+0 ⭐",
            "big_number_label": "单日增长",
            "visual_hint": "右侧一个3D发光节点网络小图标",
        }

    r = top_repo.repo.repo
    return {
        "title": "🏆 今日焦点",
        "project": r.full_name,
        "tagline": _clean_one_line(top_repo.repo.intro_zh),
        "big_number": f"+{_format_stars(r.stars_today)} ⭐",
        "big_number_label": "单日暴涨",
        "visual_hint": _visual_hint(r, top_repo.repo.intro_zh),
    }


def _format_stars(stars: int) -> str:
    if stars >= 100_000:
        return f"{stars // 1000}K"
    if stars >= 10_000:
        return f"{stars / 1000:.1f}K"
    if stars >= 1_000:
        return f"{stars / 1000:.1f}K"
    return str(stars)


def _clean_one_line(text: str, max_len: int = 72) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= max_len:
        return clean
    return clean[: max_len - 1].rstrip("，。；、 ") + "…"


def _visual_hint(repo, intro: str) -> str:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if "知识图谱" in text or "knowledge graph" in text or "graph" in text:
        return "一个从代码文件中生长出来的发光节点网络知识图谱3D等距插画"
    if "security" in text or "cyber" in text:
        return "一个发光盾牌连接代码终端和告警节点的3D等距插画"
    if "agent" in text or "claude" in text or "cursor" in text:
        return "一个AI代理核心连接多个工具模块的3D等距插画"
    if "domain" in text or "域名" in text:
        return "一个发光地球和域名标签漂浮在代码网格上的3D等距插画"
    if "media" in text or "video" in text or "媒体" in text:
        return "一个自托管媒体服务器连接多块播放屏幕的3D等距插画"
    if "compiler" in text or "编译" in text or repo.language == "C":
        return "一个代码文件进入编译器芯片并输出二进制光流的3D等距插画"
    return "一个发光代码仓库向外连接知识节点和星标粒子的3D等距插画"


def _project_tags(repo, intro: str) -> list[str]:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    tags = ["#开源"]
    if "ai" in text or "agent" in text or "claude" in text:
        tags.append("#AI工具")
    if "security" in text or "cyber" in text:
        tags.append("#安全")
    if "compiler" in text or "编译" in text:
        tags.append("#编程学习")
    if "self-host" in text or "media" in text or "自托管" in text:
        tags.append("#自托管")
    if len(tags) < 4:
        tags.extend(["#开发者工具", "#GitHub热榜"])
    return tags[:4]


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
