---
tags:
  - inno
  - prompt
  - github-trending
status: ready-to-implement
created: 2026-05-25
project: github-trending-daily
---

# GitHub Trending Daily — Implementation Prompt

> [!abstract] 你的任务
> 实现一个每日自动化工具:抓取 GitHub Trending 前 10 项目 → 用 Claude API 生成中文介绍 + 英文图像 prompt → 调 OpenAI Images 生成 10 张配图 → Pillow 拼一张 iPhone 竖屏比例的 2×5 总览图 → 写成 Obsidian 笔记 commit 回本仓库。

---

## 1. 目标与范围

### 1.1 最终交付
- 一个 **Python 项目 + GitHub Actions workflow**
- 每天 UTC 02:00 (北京 10:00) 自动运行
- 产物 commit 推到 `main` 分支
- Obsidian vault 通过 **obsidian-git 插件** 自动 pull 拿到产物

### 1.2 不在范围
- 不做前端 / Web UI
- 不做用户登录、多 vault 支持
- 不做历史回填(只从部署日开始)

---

## 2. 技术栈(已确定,不要变)

| 维度 | 选择 |
|------|------|
| 语言 | Python 3.11+ |
| 调度 | GitHub Actions `schedule: cron` |
| Trending 源 | 抓取 `https://github.com/trending` HTML(`requests` + `beautifulsoup4`) |
| 文本 LLM | Anthropic Claude API(`claude-sonnet-4-6`) |
| 文生图 | OpenAI Images API(`dall-e-3`,1024×1792 portrait) |
| 图像合成 | Pillow |
| Secret 管理 | GitHub Actions Repository Secrets |
| 同步 | vault 即 git repo,obsidian-git 拉取 |

---

## 3. 目录结构(必须这样建)

```
.
├── .github/workflows/daily.yml
├── pyproject.toml                 # uv / pip 都能用
├── README.md                      # 部署说明
├── src/trending/
│   ├── __init__.py
│   ├── config.py                  # 读 env / 常量
│   ├── fetch.py                   # 抓 trending 页
│   ├── enrich.py                  # 调 GitHub REST 拿 README/avatar/license
│   ├── summarize.py               # Claude API 产中文介绍 + 英文 image prompt
│   ├── illustrate.py              # OpenAI Images 生 10 张单图
│   ├── compose.py                 # Pillow 拼总图
│   ├── render.py                  # 生成 daily.md / repo notes / 更新 index 与 base
│   ├── dedupe.py                  # 跨日复用已生成的图与介绍
│   └── main.py                    # 编排
├── tests/                         # pytest, 至少覆盖 fetch / dedupe / render
├── vault/Inno/GithubTrending/     # Obsidian 子目录(直接写这里)
│   ├── _index.md                  # MOC 页(每天追加一行)
│   ├── trending.base              # Bases 视图
│   ├── repos/                     # 每个 repo 一个独立笔记
│   └── YYYY-MM-DD/
│       ├── daily.md
│       └── assets/
│           ├── overview.png       # 2×5 iPhone 竖屏总图
│           └── 01-<owner>__<name>.png ... 10-...png
└── state/
    └── repos.json                 # dedupe 的状态:已生成过的 repo 元数据
```

---

## 4. 模块详细规格

### 4.1 `fetch.py` — 抓 trending
```python
def fetch_trending(period: str = "daily") -> list[Repo]:
    """
    GET https://github.com/trending?since={period}
    解析 article.Box-row。返回前 10 条。
    Repo dataclass 字段:
        owner: str
        name: str        # 不含 owner
        full_name: str   # owner/name
        description: str | None
        language: str | None
        stars_total: int
        stars_today: int
        url: str
    """
```
- **必须**用真实浏览器 User-Agent
- 失败重试 3 次,指数退避
- 如果只解析到 < 10 条,raise(不要静默截断)

### 4.2 `enrich.py` — GitHub API 富化
```python
def enrich(repos: list[Repo]) -> list[EnrichedRepo]:
    """
    每个 repo 用 GitHub REST 取:
    - README.md 头部(去掉徽章/HTML,前 1500 字符)
    - owner avatar URL
    - license.spdx_id
    - default_branch
    使用 GITHUB_TOKEN 提高 rate limit。
    """
```
- 用 `gh` CLI 不可用,直接 `requests`
- 任一 repo 失败 → 留空字段继续,不要让整轮挂掉

### 4.3 `summarize.py` — Claude API
对每个 repo 发一次请求,**严格 JSON 输出**:
```json
{
  "intro_zh": "2-3 句中文介绍。说清楚:这是什么 / 解决什么问题 / 为谁。",
  "image_prompt_en": "One sentence English prompt for DALL-E 3, isometric illustration style, no text in image."
}
```
- 用 `claude-sonnet-4-6`,system prompt 明确要 JSON
- 提供 README 摘要 + 项目元信息作为上下文
- 失败回退:`intro_zh = description`,`image_prompt_en = "isometric illustration of {full_name}, minimalist, soft colors"`

### 4.4 `illustrate.py` — OpenAI Images
- 模型 `dall-e-3`,size `1024x1792`,quality `standard`
- 每张失败回退占位图(本地 `assets/placeholder.png`)
- **并发限制**:OpenAI 这条 API 串行调即可(避免 rate limit)
- 在 `dedupe.py` 已确认要重画时才调

### 4.5 `compose.py` — 总图
- 画布:**1080×2340**(iPhone 14 Pro 竖屏分辨率)
- 布局:2 列 × 5 行,每格留 24px gutter,16px 圆角
- 每格内容(从上到下):repo 缩略生图(圆角裁切)、`owner/name`(粗体 18pt)、语言色块 + `★今日 +N`
- 字体:打包 Inter Variable(`assets/Inter.ttf`),不要依赖系统字体
- 输出 `overview.png` 到当日 assets 目录

### 4.6 `dedupe.py` — 跨日复用
状态文件 `state/repos.json`:
```json
{
  "microsoft/autogen": {
    "first_seen": "2026-05-20",
    "appearances": ["2026-05-20", "2026-05-21", "2026-05-25"],
    "intro_zh": "...",
    "image_path": "vault/Inno/GithubTrending/2026-05-20/assets/03-microsoft__autogen.png"
  }
}
```
- 复用规则:`intro_zh` 和单图永久复用;**当日 stars_today 必须重新写**
- 单图被复用时,在当日 assets 用 git ln(或 Python `Path.symlink_to`)指过去;若 cross-platform 不便,直接 copy

### 4.7 `render.py` — 写 Obsidian 文件

#### `daily.md` 模板
```markdown
---
tags: [github-trending, daily]
date: 2026-05-25
type: trending-daily
count: 10
---

# GitHub Trending — 2026-05-25

![[2026-05-25/assets/overview.png]]

## 今日 Top 10

### 1. [[microsoft__autogen|microsoft/autogen]] · Python · ★今日 +1234
![[2026-05-25/assets/01-microsoft__autogen.png|400]]

> Claude 生成的中文介绍。

[GitHub →](https://github.com/microsoft/autogen)

### 2. ...
```

#### `repos/<owner>__<name>.md`(每个 repo 独立笔记)
```markdown
---
tags: [github-trending, repo]
repo: microsoft/autogen
language: Python
first_seen: 2026-05-20
appearances: 4
---

# microsoft/autogen

> Claude 生成的中文介绍。

## 上榜历史
- [[2026-05-25/daily#microsoft__autogen]]
- [[2026-05-21/daily#microsoft__autogen]]
- [[2026-05-20/daily#microsoft__autogen]]
```
**注意**:每天追加,不要重写整个文件;`appearances` 字段 +1。

#### `_index.md`(MOC)
- 文件已存在则在 `## 历次` 段落顶部插入 `- [[2026-05-25/daily|2026-05-25]]`(倒序)

#### `trending.base`
```yaml
filters:
  - type: tag
    value: github-trending
    op: contains
properties:
  - repo
  - language
  - appearances
  - first_seen
views:
  - name: All Repos
    type: table
    sort: appearances desc
```

### 4.8 `main.py` — 编排
顺序:`fetch → enrich → dedupe(分流出 need_summarize / need_illustrate 子集) → summarize → illustrate → compose → render → git commit & push`。

---

## 5. GitHub Actions workflow

`.github/workflows/daily.yml`:
- `on: schedule: cron: '0 2 * * *'` + `workflow_dispatch`(手动可触发)
- runs-on: `ubuntu-latest`
- steps:
  1. checkout(`fetch-depth: 0`,需要 push)
  2. setup-python 3.11
  3. install deps(`pip install -e .` 或 `uv sync`)
  4. run `python -m trending.main`(env 注入 secrets)
  5. `git config` + `git add vault/ state/` + commit(消息 `chore(trending): YYYY-MM-DD`)+ `git push`
- env / secrets:
  - `ANTHROPIC_API_KEY`
  - `OPENAI_API_KEY`
  - `GITHUB_TOKEN`(Actions 自带,用于 push 和 enrich)

如果当日内容没变(很少见,但要处理):commit 步骤检测 `git diff --quiet`,无变化跳过 push。

---

## 6. 验收标准(Definition of Done)

- [ ] 本地 `python -m trending.main` 跑通,产物落到 `vault/Inno/GithubTrending/<today>/`
- [ ] `overview.png` 是 1080×2340,2×5 排版,**没有文字溢出**
- [ ] 10 张单图都生成,失败回退到 placeholder
- [ ] `daily.md` 在 Obsidian 中渲染:总图正常嵌入、wikilink 可跳、frontmatter 被识别
- [ ] `_index.md` 顶部新增了今日条目
- [ ] `trending.base` 在 Obsidian 中能打开为表格视图
- [ ] 同一 repo 第二天上榜时,`intro_zh` 与单图被复用,LLM/生图调用次数 < 10
- [ ] Actions 在 `workflow_dispatch` 手动触发能跑完并 push
- [ ] `tests/` 通过:`pytest tests/`(至少 fetch 解析、dedupe 决策、render 输出三处)
- [ ] `README.md` 写明:本地运行 / Secrets 配置 / Vault 接入步骤

---

## 7. 注意事项

- **不要** 把 API key 写进任何文件,只走 env
- **不要** 每天产生新的 repo note,而是 append 到已有的
- **图片复用** 优先 copy 而非 symlink,跨平台稳
- DALL-E 3 不能控制图中文字,prompt 里加 `no text, no labels` 减少破图概率
- Trending 页面 HTML 结构可能变,parser 要写得宽松,缺字段 → 留空,不要崩
- Actions 的时区是 UTC,不要在代码里写死时区,用 `datetime.now(timezone.utc).date()` 决定 `today`

---

## 8. 给执行 agent 的建议工作流

1. 先建仓库骨架 + `README.md` + `pyproject.toml`
2. 分模块实现,每模块写完立即写 unit test
3. **先用 mock fixture 跑通整条 pipeline**(不调任何外部 API)
4. 再依次接入真 GitHub trending → Claude → DALL-E
5. 最后接 Actions,先用 `workflow_dispatch` 手动触发验证
6. 调通后再启 schedule

> [!tip] 调试小技巧
> `compose.py` 的 layout 调试可以单独跑,用 placeholder 图;不需要每次重新调 DALL-E。
