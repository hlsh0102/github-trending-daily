"""Tests for visual hint generation."""

import json
from unittest.mock import MagicMock, patch

from trending.config import EnrichedRepo, IllustratedRepo, SummarizedRepo
from trending.visual_hints import fallback_visual_hint, generate_visual_hints


def _make_illustrated(full_name: str, intro: str = "测试项目。") -> IllustratedRepo:
    owner, name = full_name.split("/")
    repo = EnrichedRepo(
        owner=owner,
        name=name,
        full_name=full_name,
        description=intro,
        language="Python",
        stars_total=1000,
        stars_today=50,
        url=f"https://github.com/{full_name}",
    )
    return IllustratedRepo(
        repo=SummarizedRepo(repo=repo, intro_zh=intro, image_prompt_en=""),
        image_path="",
    )


def test_generate_visual_hints_success_path():
    repos = [
        _make_illustrated("owner/one"),
        _make_illustrated("owner/two"),
    ]
    fake_resp = MagicMock()
    fake_resp.choices = [MagicMock()]
    fake_resp.choices[0].message.content = (
        "```json\n"
        + json.dumps({
            "owner/one": "一个代码审计工作台展示差异化模块",
            "owner/two": "一个数据管线实验室连接训练和部署",
        }, ensure_ascii=False)
        + "\n```"
    )

    with patch("trending.visual_hints.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.return_value = fake_resp
        mock_openai.return_value = client

        result = generate_visual_hints(repos, {"owner/one": "article"})

    assert result == {
        "owner/one": "一个代码审计工作台展示差异化模块",
        "owner/two": "一个数据管线实验室连接训练和部署",
    }
    messages = client.chat.completions.create.call_args.kwargs["messages"]
    assert "一眼看懂" in messages[0]["content"]
    assert "输入、核心能力、输出结果" in messages[0]["content"]
    assert "owner/one" in messages[1]["content"]
    assert "Article excerpt" in messages[1]["content"]


def test_generate_visual_hints_fallback_on_exception():
    repos = [
        _make_illustrated(
            "rohitg00/ai-engineering-from-scratch",
            "从零开始学习人工智能工程实践。",
        )
    ]

    with patch("trending.visual_hints.OpenAI") as mock_openai:
        client = MagicMock()
        client.chat.completions.create.side_effect = RuntimeError("boom")
        mock_openai.return_value = client

        result = generate_visual_hints(repos)

    assert "rohitg00/ai-engineering-from-scratch" in result
    assert "AI工程学习路线图" in result["rohitg00/ai-engineering-from-scratch"]


def test_short_video_fallback_hint_prioritizes_generation_workflow():
    item = _make_illustrated(
        "harry0703/MoneyPrinterTurbo",
        "AI 大模型短视频自动生成工具，自动完成文案、素材、字幕、配乐并输出高清短视频。",
    )

    hint = fallback_visual_hint(item)

    assert "AI视频引擎" in hint
    assert "文案" in hint
    assert "竖屏高清成片" in hint
    assert "媒体服务器" not in hint
