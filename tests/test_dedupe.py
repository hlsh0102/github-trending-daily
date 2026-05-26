"""Tests for dedupe module."""
import json
import tempfile
from pathlib import Path
from trending.config import EnrichedRepo
from trending.dedupe import load_state, save_state, split_repos


def make_repo(full_name: str) -> EnrichedRepo:
    return EnrichedRepo(
        owner=full_name.split("/")[0],
        name=full_name.split("/")[1],
        full_name=full_name,
        description=None,
        language=None,
        stars_total=100,
        stars_today=50,
        url=f"https://github.com/{full_name}",
    )


def test_split_repos_new_and_existing():
    state = {
        "a/b": {
            "first_seen": "2026-05-20",
            "appearances": ["2026-05-20"],
            "intro_zh": "old intro",
            "image_path": "vault/path/old.png",
        }
    }
    repos = [make_repo("a/b"), make_repo("c/d")]

    existing, new, updated_state = split_repos(repos, state, "2026-05-25")

    assert len(existing) == 1
    assert len(new) == 1
    assert existing[0].repo.full_name == "a/b"
    assert new[0].repo.full_name == "c/d"
    assert "intro_zh" in updated_state["a/b"]
    assert updated_state["c/d"]["image_prompt_en"] == ""
    assert "2026-05-25" in updated_state["a/b"]["appearances"]


def test_save_and_load_state():
    state = {"x/y": {"first_seen": "2026-05-20", "appearances": [], "intro_zh": "hi", "image_path": "p"}}
    with tempfile.NamedTemporaryFile(suffix=".json", mode="w", delete=False) as f:
        save_state(state, Path(f.name))
        loaded = load_state(Path(f.name))
    assert loaded == state


def test_load_state_missing_file():
    state = load_state(Path("/nonexistent/repos.json"))
    assert state == {}
