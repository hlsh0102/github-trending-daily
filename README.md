# GitHub Trending Daily

GitHub Actions + Python, auto-generate daily GitHub Trending top 10 into an Obsidian vault.

## How It Works

```
GitHub Actions (UTC 02:00 / Beijing 10:00)
  -> Scrape github.com/trending
  -> GitHub REST API for README/license metadata
  -> DeepSeek API for Chinese summaries and detailed articles
  -> Write one daily summary md and ten article md files
  -> Write to vault/Inno/GithubTrending/
  -> git commit & push
```

## Local Setup

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- API key: DeepSeek API key

### Quick Start

```bash
git clone <this-repo>
cd github-trending-daily
uv sync

export DEEPSEEK_API_KEY="sk-..."
export GITHUB_TOKEN="ghp_..."  # optional, avoids API rate limits on repo metadata

uv run python -m trending.main
```

### Secrets Configuration

Add these secrets in your GitHub repo under Settings -> Secrets and variables -> Actions:

| Secret | Purpose |
|--------|---------|
| `DEEPSEEK_API_KEY` | DeepSeek API for Chinese summaries and detailed articles |

`GITHUB_TOKEN` is automatically provided by Actions. No manual setup needed unless you run locally and want repo metadata enrichment.

## Vault Integration

The output is an Obsidian vault folder. To use it in Obsidian:

1. Install [obsidian-git](https://github.com/Vinzent03/obsidian-git) community plugin
2. Configure auto-pull interval (suggested: 1 hour)
3. Open the vault folder in Obsidian and let the plugin pull updates

Vault root is `vault/`. Daily content lands in `Inno/GithubTrending/`.

## Running Tests

```bash
uv run pytest tests/ -v
```
