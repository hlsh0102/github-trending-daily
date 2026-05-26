"""Tests for summary generation."""

from trending.config import EnrichedRepo
from trending.summarize import SYSTEM_PROMPT, _summarize_one


class _FakeMessage:
    content = '{"intro_zh": "中文简介", "gpt_image_prompt": {"unused": true}}'


class _FakeChoice:
    message = _FakeMessage()


class _FakeResponse:
    choices = [_FakeChoice()]


class _FakeCompletions:
    def create(self, **kwargs):
        self.kwargs = kwargs
        return _FakeResponse()


class _FakeChat:
    def __init__(self):
        self.completions = _FakeCompletions()


class _FakeClient:
    def __init__(self):
        self.chat = _FakeChat()


def test_system_prompt_only_requests_text_summary():
    assert "gpt_image_prompt" not in SYSTEM_PROMPT
    assert "image prompt" not in SYSTEM_PROMPT.lower()


def test_summarize_one_ignores_image_prompt_fields():
    repo = EnrichedRepo(
        owner="owner",
        name="repo",
        full_name="owner/repo",
        description="A useful repo",
        language="Python",
        stars_total=100,
        stars_today=10,
        url="https://github.com/owner/repo",
    )

    result = _summarize_one(_FakeClient(), repo)

    assert result.intro_zh == "中文简介"
    assert result.image_prompt_en == ""
    assert result.gpt_image_prompt == ""
