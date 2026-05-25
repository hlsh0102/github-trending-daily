# GitHub Trending Daily

GitHub Actions + Python, auto-generate daily GitHub Trending top 10 into an Obsidian vault.

## How It Works

```
GitHub Actions (UTC 02:00 / Beijing 10:00)
  -> Scrape github.com/trending
  -> GitHub REST API for README/license metadata
  -> Claude API for Chinese summary + scoring prompt
  -> DALL-E 3 banner image at 1024x1792
  -> Pillow compose into 1080x2340 iPhone wallpaper grid (2x5)
  -> Write to vault/Inno/GithubTrending/
  -> git commit & push
```

## Local Setup

### Prerequisites

- Python 3.11+
- [uv](https://docs.astral.sh/uv/)
- API keys: [Anthropic Console](https://console.anthropic.com/) + [OpenAI Platform](https://platform.openai.com/)

### Quick Start

```bash
git clone <this-repo>
cd github-trending-daily
uv sync

export ANTHROPIC_API_KEY="sk-ant-..."
export OPENAI_API_KEY="sk-..."
export GITHUB_TOKEN="ghp_..."  # optional, avoids API rate limits on repo metadata

uv run python -m trending.main
```

### Secrets Configuration

Add these secrets in your GitHub repo under Settings -> Secrets and variables -> Actions:

| Secret | Purpose |
|--------|---------|
| `ANTHROPIC_API_KEY` | Claude API for Chinese summaries |
| `OPENAI_API_KEY` | OpenAI API for DALL-E 3 images |

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
