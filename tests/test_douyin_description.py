"""Tests for Douyin description generation."""

from unittest.mock import MagicMock, patch

from trending.config import EnrichedRepo, IllustratedRepo, SummarizedRepo
from trending.douyin_description import generate_douyin_description


def _make_illustrated(idx: int) -> IllustratedRepo:
    full_name = f"owner{idx}/repo{idx}"
    repo = EnrichedRepo(
        owner=f"owner{idx}",
        name=f"repo{idx}",
        full_name=full_name,
        description=f"Description {idx}",
        language="Python",
        stars_total=1000 + idx,
        stars_today=10 + idx,
        url=f"https://github.com/{full_name}",
    )
    summary = SummarizedRepo(
        repo=repo,
        intro_zh=f"repo{idx} 是一个用于测试的开源项目。",
        image_prompt_en="",
    )
    return IllustratedRepo(repo=summary, image_path="")


def test_generate_douyin_description_success_path():
    repos = [_make_illustrated(i) for i in range(10)]
    fake_resp = MagicMock()
    fake_resp.choices = [MagicMock()]
    fake_resp.choices[0].message.content = "今日开源速览：10 个项目都值得看看。\n#GitHub #开源"

    with patch("trending.douyin_description.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.return_value = fake_resp
        mock_openai.return_value = client

        result = generate_douyin_description(repos, {"owner0/repo0": "article"})

    assert "今日开源速览" in result
    assert len(result) <= 1000
    messages = client.chat.completions.create.call_args.kwargs["messages"]
    assert "owner0/repo0" in messages[1]["content"]
    assert "Article excerpt" in messages[1]["content"]


def test_generate_douyin_description_fallback_on_exception():
    repos = [_make_illustrated(i) for i in range(10)]

    with patch("trending.douyin_description.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.side_effect = RuntimeError("boom")
        mock_openai.return_value = client

        result = generate_douyin_description(repos)

    assert "今天 GitHub Trending TOP10 速览" in result
    assert "repo0" in result
    assert "repo9" in result
    assert "#GitHub" in result
    assert len(result) <= 1000
