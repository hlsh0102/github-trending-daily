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
