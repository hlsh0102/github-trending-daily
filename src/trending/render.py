"""Obsidian vault file writer."""
import json
import re
from pathlib import Path
from trending.config import IllustratedRepo, VAULT_DIR
from trending.visual_hints import fallback_visual_hint


def render_all(
    repos: list[IllustratedRepo],
    today: str,
    articles: dict[str, str] | None = None,
    douyin_description: str | None = None,
    visual_hints: dict[str, str] | None = None,
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
    if douyin_description:
        render_douyin_description(douyin_description, daily_dir)
    render_douyin_prompts(repos, today, daily_dir, visual_hints)
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


def render_douyin_description(description: str, daily_dir: Path) -> None:
    """Write Douyin post copy to ``<daily_dir>/douyin-description.md``."""
    daily_dir.mkdir(parents=True, exist_ok=True)
    (daily_dir / "douyin-description.md").write_text(
        description.strip() + "\n",
        encoding="utf-8",
    )


def render_douyin_prompts(
    repos: list[IllustratedRepo],
    today: str,
    daily_dir: Path,
    visual_hints: dict[str, str] | None = None,
) -> None:
    """Write Douyin image prompt JSON files for summary and repo cards."""
    prompts_dir = daily_dir / "douyin-prompts"
    prompts_dir.mkdir(parents=True, exist_ok=True)
    previous_date, previous_repos = _load_previous_ranking(daily_dir.parent, today)
    new_entries = _find_new_entries(repos, previous_repos)

    summary = _build_summary_prompt(repos, today, previous_date, new_entries)
    _write_json(prompts_dir / "00-summary.json", summary)
    for i, illustrated in enumerate(repos, start=1):
        r = illustrated.repo.repo
        safe_name = r.full_name.replace("/", "__")
        prompt = _build_project_prompt(illustrated, today, i, visual_hints or {})
        _write_json(
            prompts_dir / f"{i:02d}-{safe_name}.json",
            prompt,
        )


def _write_json(path: Path, data: dict) -> None:
    path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )


def _build_summary_prompt(
    repos: list[IllustratedRepo],
    today: str,
    previous_date: str | None = None,
    new_entries: set[str] | None = None,
) -> dict:
    top_repo = max(repos, key=lambda item: item.repo.repo.stars_today, default=None)
    max_total = max((item.repo.repo.stars_total for item in repos), default=0)
    max_today = max((item.repo.repo.stars_today for item in repos), default=0)
    date_label = today.replace("-", ".")
    focus_name = top_repo.repo.repo.name if top_repo else "GitHub Trending"
    new_entries = new_entries or set()
    new_entry_labels = [
        f"{i:02d} {item.repo.repo.full_name}"
        for i, item in enumerate(repos, start=1)
        if item.repo.repo.full_name in new_entries
    ]

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
            "position": "从画面顶部约 220px 开始，居中偏上，但不要低于 250px 或贴近顶部边缘",
            "title_style": "白色超粗体(#FFFFFF)，字号极大，1米外清晰可辨，带绿色(#238636)下划线装饰",
            "subtitle": f"开源项目精选 · {focus_name} 暴涨{_format_stars(max_today)}⭐",
            "subtitle_style": "浅灰(#8B949E)，中号字，紧贴主标题下方，但不得进入顶部安全区",
            "hook_headline": "今日最值得看的开源项目",
            "hook_style": "副标题下方的大号粗体钩子，强调今日看点和榜单价值，必须完整可读",
        },
        "date_badge": {
            "text": date_label,
            "position": "标题上方或标题左上侧，仍然位于顶部安全区下方，作为日报日期身份强提示",
            "style": "醒目的绿色描边胶囊或金色小日历徽章，字号大于副标题但小于主标题，必须第一眼可见",
            "icon": "小日历图标",
        },
        "hero_module": {
            "position": "标题下方，画面中上部 40% 区域",
            "style": "大圆角卡片(24px)，半透明深色底(#1C2128)，绿色(#238636)左边框",
            "readability_rule": "必须直接展示今日焦点项目、单日增长和它解决的问题，不能只放抽象装饰图",
            "content": _summary_hero_content(top_repo),
        },
        "stats_row": {
            "position": "hero模块下方，三张关键数字卡片横排",
            "style": "3个等宽卡片，背景半透明黑，数字大号发光",
            "cards": [
                {"number": str(len(new_entries)), "label": "新上榜", "color": "#D4A574"},
                {"number": _format_stars(max_today), "label": "最高日增", "color": "#58A6FF"},
                {"number": _format_stars(max_total), "label": "最高星标", "color": "#D4A574"},
            ],
        },
        "comparison": {
            "baseline_date": previous_date,
            "rule": "与 vault 中早于今天的最近一个日期目录的 daily.md 排行榜对比；当前榜单里不存在于该历史榜单的项目标记为新上榜",
            "new_entries_count": len(new_entries),
            "new_entries": new_entry_labels,
            "visual_instruction": "在 ranking_strip 中所有新上榜条目右侧添加醒目的 🆕 新上榜 标签，使用绿色描边或金色小胶囊，但不要抢主标题",
        },
        "ranking_strip": {
            "position": "画面下半部，但避开底部160px安全区",
            "style": "5行×2列紧凑排列，每个条目一行：排名数字(01-10，绿色粗体) + 项目名(白色) + 星标数(金色小字)",
            "items": [
                _ranking_item_prompt(i, item, new_entries)
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


def _ranking_item_prompt(
    index: int,
    item: IllustratedRepo,
    new_entries: set[str],
) -> str:
    r = item.repo.repo
    label = f"{index:02d} {r.name} · {_format_stars(r.stars_total)}★"
    if r.full_name in new_entries:
        label += " · 🆕 新上榜"
    return label


def _load_previous_ranking(vault_dir: Path, today: str) -> tuple[str | None, set[str]]:
    previous_dirs = [
        path
        for path in vault_dir.iterdir()
        if path.is_dir() and re.fullmatch(r"\d{4}-\d{2}-\d{2}", path.name) and path.name < today
    ]
    if not previous_dirs:
        return None, set()

    previous_dir = max(previous_dirs, key=lambda path: path.name)
    daily_path = previous_dir / "daily.md"
    if not daily_path.exists():
        return previous_dir.name, set()
    return previous_dir.name, _parse_daily_repos(daily_path.read_text(encoding="utf-8"))


def _parse_daily_repos(content: str) -> set[str]:
    return set(re.findall(r"^##\s+\d+\.\s+\[\[repos/[^|]+?\|([^\]]+)\]\]", content, flags=re.MULTILINE))


def _find_new_entries(repos: list[IllustratedRepo], previous_repos: set[str]) -> set[str]:
    if not previous_repos:
        return set()
    return {
        item.repo.repo.full_name
        for item in repos
        if item.repo.repo.full_name not in previous_repos
    }


def _build_project_prompt(
    illustrated: IllustratedRepo,
    today: str,
    index: int,
    visual_hints: dict[str, str] | None = None,
) -> dict:
    r = illustrated.repo.repo
    intro = _clean_one_line(illustrated.repo.intro_zh, max_len=90, ellipsis=False)
    title = r.name
    language = r.language or "Unknown"
    tags = _project_tags(r, intro)
    intro_cards = _project_intro_cards(r, intro)
    hook_headline = _project_hook_headline(r, intro, intro_cards)
    workflow_nodes = _project_workflow_nodes(r, intro, intro_cards)
    visual_hint = (visual_hints or {}).get(r.full_name) or fallback_visual_hint(illustrated)
    prompt_cn = (
        "一张中文科技项目介绍卡，9:16竖屏(1080×1920)，暗色科技风。"
        "画面顶部保留约180px抖音安全区，不放标题、项目名、关键数字等重要文字；"
        "但顶部不要空，用低透明度git网格、代码线条、星标轨迹、霓虹绿节点和电路线填满科技氛围。"
        f"标题块从约220px处开始且不要低于250px：项目名「{title}」白色超粗体，"
        f"下方标签「#{index:02d} · {language} · {_format_stars(r.stars_total)}★」。"
        f"副标题下方立即放核心功能大字「{hook_headline}」，让用户1秒内知道项目用途。"
        "背景为深黑蓝渐变(#0D1117到#161B22)，带细微git网格和霓虹绿点缀。"
        "中央主视觉必须是功能流程图式主视觉，不要只放一个巨大装饰物："
        f"围绕「{hook_headline}」设计「输入/核心能力/输出结果」的清晰流程，"
        f"核心视觉参考：{visual_hint}；"
        f"至少出现这些短节点「{'」「'.join(workflow_nodes)}」，用绿色和蓝色光线连接，"
        "让观众一眼看懂项目如何工作。"
        f"插画下方三列关键数据：「{_format_stars(r.stars_total)} 总星标」"
        f"「+{_format_stars(r.stars_today)} 今日增长」「{language}」。"
        f"中下部不要放长段落简介，改放5个短信息卡：「{_cards_to_text(intro_cards)}」。"
        f"底部标签栏：「{' '.join(tags)}」。"
        "字体使用粗体无衬线，绿色#238636和金色#D4A574作为强调色，"
        "所有中文都必须完整显示，禁止省略号、截断号和半句话；"
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
            "position": "从画面顶部约 220px 开始，居中偏上，但不要低于 250px 或贴近顶部边缘",
            "title_style": "白色超粗体(#FFFFFF)，字号极大，带绿色(#238636)短下划线",
            "subtitle": f"#{index:02d} · {language} · {_format_stars(r.stars_total)}★",
            "subtitle_style": "浅灰(#8B949E)，中号字，紧贴主标题下方，但不得进入顶部安全区",
            "hook_headline": hook_headline,
            "hook_style": "副标题下方的大号粗体功能钩子，白色为主，关键词用绿色(#238636)强调，必须完整可读",
        },
        "content": {
            "repo": r.full_name,
            "date": today,
            "one_line_summary": intro,
            "intro_cards": intro_cards,
            "workflow_nodes": workflow_nodes,
            "visual_hint": visual_hint,
            "stats": [
                {"number": _format_stars(r.stars_total), "label": "总星标", "color": "#D4A574"},
                {"number": f"+{_format_stars(r.stars_today)}", "label": "今日增长", "color": "#238636"},
                {"number": language, "label": "主要语言", "color": "#58A6FF"},
            ],
            "tags": tags,
        },
        "layout_rules": [
            "不要把长段落简介放进画面",
            "用 intro_cards 的短标题和短说明替代正文段落",
            "每个中文说明控制在 10 个字以内",
            "主视觉必须表达项目用途和工作流，不能只是一张无信息量的大插画",
            "标题、副标题、功能钩子、主视觉流程、三列数据要形成清晰的第一眼阅读顺序",
            "所有可见文字必须完整显示，禁止出现省略号、省略半句或文字被裁切",
            "如果空间不足，减少装饰元素而不是截断文字",
        ],
        "prompt_cn": prompt_cn,
        "constraints": _douyin_constraints(),
    }


def _douyin_safe_area() -> dict:
    return {
        "top_reserved_area": "画面顶部约 180px 为抖音安全区，不放主标题、副标题、项目名、关键数字等重要信息",
        "title_position": "主标题块从画面约 220px 处开始，位于抖音刘海/状态栏下方，但不要低于 250px",
        "top_area_usage": "顶部安全区不要空，只放不可读的低透明度网格、星点、代码线、GitHub风格装饰线、霓虹绿节点和电路线",
        "bottom_reserved_area": "底部至少留出 160px，避免抖音文案、按钮或进度条遮挡核心信息",
    }


def _douyin_constraints() -> dict:
    return {
        "must_feel": "像真实抖音科技博主的高质量封面，不是PPT截图",
        "must_keep": [
            "主标题不能出现在画面顶部180px以内",
            "主标题在1米外清晰可辨",
            "副标题下方必须有一句大号功能钩子，让观众1秒内知道项目用途",
            "中央主视觉必须是功能流程或使用场景，不允许只是无信息量的大装饰图",
            "绿色(#238636)和金色(#D4A574)作为强调色贯穿全图",
            "至少3处出现大数字做视觉锚点",
            "排名区域清晰但不抢主标题",
            "整体暗色科技感+霓虹点缀",
        ],
        "avoid": [
            "标题贴近顶部边缘",
            "标题文字被手机刘海、摄像头、状态栏或任何元素遮挡",
            "顶部安全区大面积空白",
            "中间区域只有漂亮插画但看不出项目用途",
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


def _clean_one_line(text: str, max_len: int = 72, ellipsis: bool = True) -> str:
    clean = re.sub(r"\s+", " ", text).strip()
    if len(clean) <= max_len:
        return clean
    if not ellipsis:
        return clean[:max_len].rstrip("，。；、 ")
    return clean[: max_len - 1].rstrip("，。；、 ") + "…"


def _project_hook_headline(repo, intro: str, cards: list[dict[str, str]]) -> str:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if _is_short_video_generator(text):
        return "AI 一键生成短视频"
    if "knowledge-work-plugins" in text or "knowledge work" in text or "知识工作" in text:
        return "Claude 办公自动化插件"
    if "stop-slop" in text or "ai 痕迹" in text or "ai味" in text or "ai 味" in text:
        return "去掉 AI 写作痕迹"
    if "taste-skill" in text or "品味" in text or "审美" in text:
        return "提升 AI 输出审美"
    if "awesome-free-apps" in text or "free apps" in text or "免费应用" in text:
        return "免费应用精选清单"
    if "ai-engineering" in text or "ai engineering" in text or "人工智能工程" in text:
        return "从零构建 AI 系统"
    if "知识图谱" in text or "knowledge graph" in text or "graph" in text:
        return "看懂代码知识图谱"
    if "security" in text or "cyber" in text:
        return "AI 安全技能库"
    if "agent" in text or "claude" in text or "cursor" in text:
        return "强化 AI 编码代理"
    if "domain" in text or "域名" in text:
        return "免费域名资源库"
    if "media" in text or "媒体" in text:
        return "自托管影音中心"
    if "compiler" in text or "编译" in text or repo.language == "C":
        return "看懂代码编译过程"
    core = cards[0]["text"] if cards else "开源项目"
    ability = cards[1]["text"] if len(cards) > 1 else "提升效率"
    return f"{core} · {ability}"


def _project_workflow_nodes(repo, intro: str, cards: list[dict[str, str]]) -> list[str]:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if _is_short_video_generator(text):
        return ["输入主题", "写文案", "找素材", "加字幕", "配音乐", "高清成片"]
    if "knowledge graph" in text or "知识图谱" in text or "graph" in text:
        return ["导入仓库", "解析代码", "生成图谱", "搜索提问", "理解结构"]
    if "security" in text or "cyber" in text:
        return ["输入场景", "技能映射", "威胁分析", "生成建议", "安全报告"]
    if "agent" in text or "claude" in text or "cursor" in text:
        return ["接入工具", "记忆技能", "策略防护", "任务执行", "团队协作"]
    if "domain" in text or "域名" in text:
        return ["选择渠道", "查询域名", "提交申请", "DNS配置", "项目上线"]
    if "media" in text or "媒体" in text:
        return ["导入片库", "自托管", "转码整理", "多端播放", "家庭影音"]
    if "compiler" in text or "编译" in text or repo.language == "C":
        return ["输入代码", "词法解析", "语法分析", "生成字节码", "运行结果"]
    nodes = [card["text"] for card in cards[:5] if card.get("text")]
    return nodes or ["输入需求", "核心能力", "处理流程", "输出结果"]


def _is_short_video_generator(text: str) -> bool:
    return (
        "moneyprinterturbo" in text
        or ("short video" in text and ("generate" in text or "generator" in text or "create" in text))
        or ("短视频" in text and any(keyword in text for keyword in ["生成", "自动", "文案", "字幕", "配乐", "素材"]))
    )


def _project_intro_cards(repo, intro: str) -> list[dict[str, str]]:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if _is_short_video_generator(text):
        return [
            {"title": "核心用途", "text": "AI短视频"},
            {"title": "输入方式", "text": "主题关键词"},
            {"title": "自动能力", "text": "文案素材"},
            {"title": "成片能力", "text": "字幕配乐"},
            {"title": "项目特点", "text": "开源免费"},
        ]
    if "ai-engineering" in text or "ai engineering" in text or "人工智能工程" in text:
        return [
            {"title": "学习路径", "text": "从零到实践"},
            {"title": "核心内容", "text": "AI系统构建"},
            {"title": "项目训练", "text": "实战项目"},
            {"title": "部署能力", "text": "上线运维"},
            {"title": "适合人群", "text": "开发者进阶"},
        ]
    if "知识图谱" in text or "knowledge graph" in text or "graph" in text:
        return [
            {"title": "核心用途", "text": "理解代码库"},
            {"title": "交互方式", "text": "搜索与提问"},
            {"title": "可视结构", "text": "知识图谱"},
            {"title": "适配工具", "text": "AI编辑器"},
            {"title": "适合人群", "text": "开发者学习"},
        ]
    if "security" in text or "cyber" in text:
        return [
            {"title": "核心用途", "text": "安全技能库"},
            {"title": "覆盖范围", "text": "多框架映射"},
            {"title": "能力场景", "text": "安全分析"},
            {"title": "适配工具", "text": "AI代理"},
            {"title": "适合人群", "text": "安全工程师"},
        ]
    if "agent" in text or "claude" in text or "cursor" in text:
        return [
            {"title": "核心用途", "text": "优化AI代理"},
            {"title": "能力模块", "text": "记忆技能"},
            {"title": "安全机制", "text": "策略防护"},
            {"title": "适配工具", "text": "编码助手"},
            {"title": "适合人群", "text": "工程团队"},
        ]
    if "domain" in text or "域名" in text:
        return [
            {"title": "核心用途", "text": "免费域名"},
            {"title": "资源整理", "text": "渠道汇总"},
            {"title": "使用场景", "text": "个人项目"},
            {"title": "上手方式", "text": "按需申请"},
            {"title": "适合人群", "text": "独立开发者"},
        ]
    if "media" in text or "video" in text or "媒体" in text:
        return [
            {"title": "核心用途", "text": "媒体服务器"},
            {"title": "部署方式", "text": "自托管"},
            {"title": "播放体验", "text": "多端观看"},
            {"title": "项目特点", "text": "开源免费"},
            {"title": "适合人群", "text": "影音用户"},
        ]
    return [
        {"title": "核心用途", "text": "解决痛点"},
        {"title": "主要能力", "text": "提升效率"},
        {"title": "技术方向", "text": repo.language or "开源项目"},
        {"title": "使用场景", "text": "开发实践"},
        {"title": "适合人群", "text": "开发者"},
    ]


def _cards_to_text(cards: list[dict[str, str]]) -> str:
    return "；".join(f"{card['title']}：{card['text']}" for card in cards)


def _visual_hint(repo, intro: str) -> str:
    text = f"{repo.full_name} {repo.description or ''} {intro}".lower()
    if _is_short_video_generator(text):
        return "输入主题经过AI视频引擎变成文案、素材、字幕、配乐和竖屏成片的流程主视觉"
    if "ai-engineering" in text or "ai engineering" in text or "人工智能工程" in text:
        return "一个AI工程学习路线图从课程文件夹连接到模型训练、数据处理和云端部署模块的3D等距插画"
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
