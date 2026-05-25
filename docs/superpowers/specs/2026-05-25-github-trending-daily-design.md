# GitHub Trending Daily — Design Spec

> Status: approved | Date: 2026-05-25 | Project: `github-trending-daily`

## 1. Goal

A Python project + GitHub Actions workflow that runs daily at UTC 02:00 (Beijing 10:00), scrapes GitHub Trending top 10, enriches each repo with README/metadata via GitHub REST, generates Chinese intros + English image prompts via Claude API, creates 10 DALL-E 3 illustrations, composes a 1080×2340 iPhone-ratio overview image, and writes Obsidian vault files committed back to the repo. The vault is synced to Obsidian via the obsidian-git plugin.

### Out of scope

No frontend/Web UI, no user auth, no multi-vault support, no backfilling history.

---

## 2. Tech Stack (fixed)

| Concern | Choice |
|---------|--------|
| Language | Python 3.11+ |
| Package manager | `uv` |
| Scheduler | GitHub Actions `schedule: cron` |
| Trending source | Scrape `https://github.com/trending` HTML (`requests` + `beautifulsoup4`) |
| Text LLM | Anthropic Claude API (`claude-sonnet-4-6`), strict JSON output |
| Image gen | OpenAI Images API (`dall-e-3`, 1024×1792 portrait) |
| Image compositing | Pillow |
| Font | Inter Variable, committed as `assets/Inter.ttf` (OFL license) |
| Placeholder image | Generated dynamically by Pillow (no static file) |
| Secret management | GitHub Actions Repository Secrets |
| Sync | Vault is the git repo; obsidian-git pulls |

---

## 3. Directory Structure

```
.
├── .github/workflows/daily.yml
├── pyproject.toml
├── README.md
├── assets/
│   ├── Inter.ttf
│   └── placeholder.png          # dynamically generated, not committed
├── src/trending/
│   ├── __init__.py
│   ├── config.py
│   ├── fetch.py
│   ├── enrich.py
│   ├── summarize.py
│   ├── illustrate.py
│   ├── compose.py
│   ├── render.py
│   ├── dedupe.py
│   └── main.py
├── tests/                       # pytest
├── vault/Inno/GithubTrending/
│   ├── _index.md                # MOC, one line appended per day
│   ├── trending.base            # Obsidian Bases view definition
│   ├── repos/                   # per-repo notes
│   └── YYYY-MM-DD/
│       ├── daily.md
│       └── assets/
│           ├── overview.png     # 1080×2340 2×5 composite
│           └── NN-<owner>__<name>.png ...
└── state/
    └── repos.json               # dedupe state
```

---

## 4. Architecture & Data Flow

```
GitHub Actions (UTC 02:00)
       │
       ▼
  main.py ── orchestrator, linear pipeline
       │
  ┌────┼────┬────┬────┬────┬────┬────┐
  ▼    ▼    ▼    ▼    ▼    ▼    ▼    ▼
fetch enrich dedupe summarize illustrate compose render → git push
```

### Data types flow

```
Repo (fetch) → EnrichedRepo (enrich) → dedupe split:
  ├── existing repo → reuse intro_zh + image_path
  └── new repo → summarize → SummarizedRepo → illustrate → IllustratedRepo
                                                                      │
                                                    compose ←─────────┘
                                                       │
                                                    render → vault files
```

### Module responsibilities

| Module | Input | Output | Key behavior |
|--------|-------|--------|-------------|
| `fetch.py` | trending HTML | `list[Repo]` (top 10) | Parse `article.Box-row`, real UA, 3 retries with exponential backoff, raise if < 10 parsed |
| `enrich.py` | `list[Repo]` + GitHub REST | `list[EnrichedRepo]` | Fetch README head / avatar / license / default_branch per repo; individual failure → empty fields, continue |
| `dedupe.py` | `list[EnrichedRepo]` + `state/repos.json` | `(need_summarize, need_illustrate)` subsets | Match by `full_name`; reuse intro + image for known repos, always rewrite `stars_today` |
| `summarize.py` | subset of `EnrichedRepo` + Claude API | `list[SummarizedRepo]` | Strict JSON: `intro_zh` + `image_prompt_en`. Fallback: `intro_zh = description`, generic prompt |
| `illustrate.py` | `list[SummarizedRepo]` + DALL-E 3 | `list[IllustratedRepo]` | Serial calls (rate limit), fallback to dynamic placeholder |
| `compose.py` | `list[IllustratedRepo]` | `overview.png` | 1080×2340 canvas, 2×5 grid, 24px gutter, 16px radius, Inter font 18pt, language color + stars |
| `render.py` | all data | vault files on disk | `daily.md`, `repos/<owner>__<name>.md` (append), `_index.md` (prepend), `trending.base` |
| `main.py` | (orchestrator) | — | Sequential pipeline, then `git add vault/ state/` + commit + push |

---

## 5. Error Handling Strategy

Principle: single failure must not cascade; produce as complete a daily note as possible.

| Layer | Failure scenario | Behavior |
|-------|-----------------|----------|
| fetch | Page unreachable / HTML changed | Retry 3× exponential backoff; last failure → exit |
| fetch | Individual field missing (language, desc) | Leave empty, continue |
| enrich | Single repo API call fails | README/avatar/etc. empty for that repo; others proceed |
| summarize | Claude API error | Fallback: `intro_zh = description`, generic `image_prompt_en` |
| illustrate | DALL-E error | Dynamic Pillow placeholder (solid color + repo name) |
| compose | A single thumbnail missing | Use placeholder in that cell; layout proceeds |
| render | Disk I/O error | Raise immediately (unrecoverable) |
| git push | `git diff --quiet` no changes | Skip push, no error |

---

## 6. Deduplication (`state/repos.json`)

```json
{
  "microsoft/autogen": {
    "first_seen": "2026-05-20",
    "appearances": ["2026-05-20", "2026-05-21"],
    "intro_zh": "...",
    "image_path": "vault/.../03-microsoft__autogen.png"
  }
}
```

- `intro_zh` and single images are reused forever
- `stars_today` is always rewritten for the current day
- Reused images are **copied** (not symlinked) into today's assets directory for cross-platform stability
- State is read at pipeline start, written back after render

---

## 7. GitHub Actions

- `on: schedule: cron: '0 2 * * *'` + `workflow_dispatch` for manual trigger
- `runs-on: ubuntu-latest`
- Steps: checkout → setup-python 3.11 → `uv sync` → `python -m trending.main` → git commit + push
- Secrets: `ANTHROPIC_API_KEY`, `OPENAI_API_KEY`, `GITHUB_TOKEN` (built-in)

---

## 8. Acceptance Criteria (DoD)

- [ ] `python -m trending.main` completes locally, outputs land in `vault/Inno/GithubTrending/<today>/`
- [ ] `overview.png` is 1080×2340, 2×5 layout, no text overflow
- [ ] All 10 single images generated; failures fall back to placeholder
- [ ] `daily.md` renders correctly in Obsidian (image embeds, wikilinks, frontmatter)
- [ ] `_index.md` has today's entry prepended
- [ ] `trending.base` opens as table view in Obsidian
- [ ] Same repo on consecutive days reuses `intro_zh` and image; LLM/image calls < 10
- [ ] `workflow_dispatch` manual trigger runs and pushes successfully
- [ ] `pytest tests/` passes (at minimum: fetch parsing, dedupe logic, render output)
- [ ] `README.md` documents local run / secrets config / vault setup
