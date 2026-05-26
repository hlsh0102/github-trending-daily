# Daily Articles — Design Spec

**Date:** 2026-05-26
**Status:** Approved, ready for plan
**Project:** github-trending-daily

---

## 1. 目标

在每日 trending pipeline 中，为每个上榜 repo 生成一篇 800–1500 字的中文详细介绍文章（综合性：项目概述、核心功能、技术架构、安装/使用、适用场景、亮点、相关链接），存放在当日子目录的新 `articles/` 文件夹下。

`repos/<owner>__<name>.md` 由"短简介 + 上榜历史"升级为"短简介 + 详细介绍历史 + 上榜历史"的索引页。

## 2. 范围

**In scope**
- 新增独立模块 `src/trending/article.py`，调用 DeepSeek 生成详细 markdown
- 在每日子目录下新增 `articles/` 文件夹，每个 repo 一个 `NN-<owner>__<name>.md` 文件
- 在 `daily.md` 每个 repo 段落追加详细介绍链接
- 改造 `repos/<owner>__<name>.md` 为含"详细介绍历史"段的索引页
- 自动迁移旧版 `repos/*.md`（缺"详细介绍历史"段时插入空段）
- 测试覆盖新增 render 行为
- pipeline 编排：每天对全部 10 个 repo 都重新生成详细文章（不复用）

**Out of scope**
- 不修改 `summarize.py`、`illustrate.py`、`compose.py`、`fetch.py`、`enrich.py`、`dedupe.py`
- 不修改 `state/repos.json` schema
- 不修改 bento prompt JSON / overview.png / 单图生成
- 不做跨日复用、不做缓存（明确选 A：每天全量重新生成）

## 3. 架构

### 3.1 新增模块 `src/trending/article.py`

**职责**：对每个 `IllustratedRepo` 调一次 DeepSeek，产出详细中文 markdown 正文。

**接口**
```python
def generate_articles(repos: list[IllustratedRepo]) -> dict[str, str]:
    """Generate detailed Chinese articles for each repo via DeepSeek.

    Returns: dict mapping ``full_name`` → markdown body string.
            The body does NOT include frontmatter; render layer injects it.

    Failure fallback: on LLM failure for a single repo, returns
    ``intro_zh`` as the body (never raises; never blocks pipeline).
    """
```

**Prompt 结构**
- system prompt：要求输出纯 markdown（无 frontmatter，无代码围栏包裹整体），按以下小节顺序：
  - `## 项目概述`
  - `## 核心功能`
  - `## 技术架构`
  - `## 安装与使用`
  - `## 适用场景`
  - `## 项目亮点`
  - `## 相关链接`
- 全文中文（简体），800–1500 字
- 链接段落由 LLM 给出 GitHub 仓库链接和（如有）官网/文档链接
- user message：复用 `summarize._build_context` 同款上下文（README 摘要 + 元信息 + stars）

**实现要点**
- 复用 `summarize.py` 中的 OpenAI client 构造方式（`OpenAI(api_key=DEEPSEEK_API_KEY, base_url=DEEPSEEK_BASE_URL)`）
- 串行调用，与现有 `summarize` 调用方式一致
- `max_tokens` 设到足够覆盖长文（4096+）
- 单 repo 异常 → log warning + fallback 到 `intro_zh`，不抛
- 不写 state/不持久化（每天全量重生成）

### 3.2 改动 `src/trending/render.py`

新增/改动函数：

**新增 `render_articles(articles: dict[str, str], repos: list[IllustratedRepo], today: str) -> None`**
- 路径：`vault/Inno/GithubTrending/<today>/articles/`
- 每个 repo 写一个 `{idx:02d}-{owner}__{name}.md`
- 文件内容 = frontmatter + LLM 正文，frontmatter 字段：
  - `tags: [trending, article]`
  - `repo: owner/name`
  - `date: YYYY-MM-DD`
  - `language: ...`
  - `stars_total: N`
  - `stars_today: N`

**修改 `render_daily_md`**
- 在现有每个 repo 段落的 `[GitHub]({url})` 行之后，追加：
  ```
  [详细介绍 →]({today}/articles/{idx:02d}-{safe_name}.md)
  ```
- 链接采用相对路径，与现有 `[GitHub →]` 风格一致

**重写 `render_repo_md` → 索引页**
- 新文件结构：
  ```markdown
  ---
  tags:
    - trending
    - repo
  repo: owner/name
  language: ...
  first_seen: YYYY-MM-DD
  appearances: N
  ---

  # owner/name

  > {intro_zh}

  ## 详细介绍历史

  - [[YYYY-MM-DD/articles/NN-owner__name|YYYY-MM-DD]]

  ## 上榜历史

  - [[YYYY-MM-DD/daily|YYYY-MM-DD]] — N stars
  ```
- 已有文件迁移：
  1. 增量 `appearances` 计数（保留现有行为）
  2. 检查文件是否包含 `## 详细介绍历史`：
     - 不包含 → 在 `## 上榜历史` 之前插入 `## 详细介绍历史\n\n` 空段
     - 已包含 → 跳过插入步骤
  3. 在 `## 详细介绍历史` 段落顶部插入今日条目 `- [[YYYY-MM-DD/articles/NN-owner__name|YYYY-MM-DD]]`（最新在顶部）
  4. 在 `## 上榜历史` 段落顶部插入今日条目（最新在顶部）— **变更**：现有实现是 append 到末尾，新版改为 prepend 到段落顶部以保持时间倒序一致

> 备注：旧 `## 上榜历史` 是按 append 顺序（旧→新）。迁移时不重排既有条目，只保证新条目从今天起插在段落顶部。视觉上会出现"新条目在顶 + 旧条目按旧顺序"的混合排序，可接受。

**保留不变**
- `render_index_md`、`render_bases`、`render_gpt_prompts` 不动

### 3.3 改动 `src/trending/main.py`

在 `render_all` 调用之前插入新步骤：

```python
# 7b. Generate detailed articles
logger.info("Step 7b: Generating articles for %d repos ...", len(all_illustrated))
articles = generate_articles(all_illustrated)
logger.info("  Generated %d articles", len(articles))
```

将 `articles` dict 传入 `render_all`：

```python
render_all(all_illustrated, today, articles)
```

`render_all` 签名扩展为：
```python
def render_all(repos: list[IllustratedRepo], today: str, articles: dict[str, str]) -> None
```
内部新增对 `render_articles(articles, repos, today)` 的调用。

步骤编号顺延（"Step 8/9" → "Step 9/10" 等）或重新编号，由实现选择，不影响行为。

## 4. 数据流

```
illustrate()
  → all_illustrated: list[IllustratedRepo]
       │
       ├──► article.generate_articles(all_illustrated)
       │      → articles: dict[full_name → md_body]
       │
       └──► compose() → overview.png

render_all(all_illustrated, today, articles)
  ├── render_daily_md      (含详细介绍链接)
  ├── render_articles      (写 articles/NN-xxx.md)
  ├── render_repo_md       (索引页：自动迁移 + 双段插入)
  ├── render_index_md      (不变)
  └── render_bases         (不变)
```

## 5. 错误处理

| 情形 | 行为 |
|-----|------|
| 某 repo LLM 调用失败 | log warning，body 回退为 `intro_zh`，pipeline 继续 |
| 全部 repo LLM 失败 | 所有 article 都用 `intro_zh` 作为回退，pipeline 继续 |
| `articles` dict 缺某 repo | 该 repo 跳过 `render_articles` 写文件、daily.md 不追加链接、索引页不追加该日条目 |
| `articles/` 目录已存在 | `mkdir(exist_ok=True)`，覆盖同名文件 |
| 旧索引页缺"详细介绍历史"段 | 自动插入空段（迁移逻辑） |

## 6. 测试

`tests/` 新增/更新：

1. **`test_render_articles`**
   - 输入：mock 2 个 `IllustratedRepo` + articles dict
   - 验证：`articles/01-xxx.md` 与 `articles/02-yyy.md` 存在；frontmatter 字段齐全；正文匹配输入

2. **`test_render_daily_md_with_article_link`**
   - 验证 daily.md 中每个 repo 段落包含 `[详细介绍 →]` 链接

3. **`test_render_repo_md_new_format`**
   - 新建索引页：含"详细介绍历史"和"上榜历史"两段，且新条目在顶部

4. **`test_render_repo_md_migration`**
   - 输入：旧版文件（无"详细介绍历史"段）
   - 验证：迁移后文件含新段，今日条目插在段顶；`appearances` 增 1

5. **`test_article_generate_fallback`**
   - mock DeepSeek client 抛异常 → 验证返回 dict 中该 repo body 等于 `intro_zh`

## 7. 验收标准

- [ ] `vault/Inno/GithubTrending/<today>/articles/01-...md ... 10-...md` 全部生成
- [ ] 每个 article 包含完整 frontmatter + 7 个标准小节
- [ ] `daily.md` 每个 repo 段落含 `[详细介绍 →]` 链接，且 Obsidian 可跳
- [ ] `repos/<owner>__<name>.md` 含"详细介绍历史"段，今日条目在段顶
- [ ] 旧索引页被自动迁移（新增"详细介绍历史"段，保留原有内容）
- [ ] 单个 repo LLM 失败时 pipeline 不中断，fallback 内容写入
- [ ] `pytest tests/` 全绿
- [ ] Actions workflow 无需改动即可正常跑（DEEPSEEK_API_KEY 已存在）

## 8. 不做的事（YAGNI）

- 不复用昨天/历史的文章内容
- 不缓存 article 到 state
- 不做文章长度自动校验/重试
- 不做多模型 fallback（继续用 DeepSeek）
- 不为旧索引页的"上榜历史"段重排现有条目
- 不修改 `trending.base` schema
