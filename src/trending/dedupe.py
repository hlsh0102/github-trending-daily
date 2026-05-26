"""Cross-day deduplication via state/repos.json."""
import json
import logging
import shutil
from pathlib import Path

from trending.config import EnrichedRepo, SummarizedRepo, IllustratedRepo

logger = logging.getLogger(__name__)

DEFAULT_IMAGE_PROMPT = ""


def load_state(path: Path) -> dict:
    """Load dedupe state from JSON, returning {} if missing or corrupt."""
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        return {}


def save_state(state: dict, path: Path) -> None:
    """Write dedupe state to JSON file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(state, ensure_ascii=False, indent=2), encoding="utf-8")


def split_repos(
    repos: list[EnrichedRepo],
    state: dict,
    today: str,
) -> tuple[list[SummarizedRepo], list[SummarizedRepo], dict]:
    """Split repos into existing (reuse intro) and new (need LLM).

    Returns:
        (existing_repos, new_repos, updated_state)
    """
    existing: list[SummarizedRepo] = []
    new: list[SummarizedRepo] = []

    for repo in repos:
        entry = state.get(repo.full_name)
        if entry:
            entry.setdefault("appearances", [])
            if today not in entry["appearances"]:
                entry["appearances"].append(today)

            sr = SummarizedRepo(
                repo=repo,
                intro_zh=entry.get("intro_zh", repo.description or ""),
                image_prompt_en=entry.get("image_prompt_en", ""),
                gpt_image_prompt=entry.get("gpt_image_prompt", ""),
            )
            existing.append(sr)
        else:
            fallback_intro = repo.description or f"{repo.full_name}"
            sr = SummarizedRepo(
                repo=repo,
                intro_zh=fallback_intro,
                image_prompt_en=DEFAULT_IMAGE_PROMPT,
            )
            new.append(sr)

            state[repo.full_name] = {
                "first_seen": today,
                "appearances": [today],
                "intro_zh": fallback_intro,
                "image_prompt_en": DEFAULT_IMAGE_PROMPT,
                "image_path": "",
            }

    return existing, new, state


def reuse_images(
    existing: list[SummarizedRepo],
    state: dict,
    today: str,
    today_assets_dir: Path,
) -> list[IllustratedRepo]:
    """Copy reused images into today's assets directory."""
    results: list[IllustratedRepo] = []
    for sr in existing:
        entry = state.get(sr.repo.full_name, {})
        old_path = entry.get("image_path", "")
        new_path = ""

        if old_path:
            src = Path(old_path)
            if src.exists():
                idx = len(list(today_assets_dir.glob("*.png"))) + 1
                dst_name = f"{idx:02d}-{sr.repo.owner}__{sr.repo.name}.png"
                dst = today_assets_dir / dst_name
                shutil.copy2(src, dst)
                new_path = str(dst.resolve())
                entry["image_path"] = new_path

        results.append(IllustratedRepo(repo=sr, image_path=new_path))
    return results


def update_state_for_summarized(results: list, state: dict) -> dict:
    """Write intro_zh, image_prompt_en, and gpt_image_prompt from LLM results back into state."""
    for sr in results:
        entry = state.get(sr.repo.full_name)
        if entry:
            entry["intro_zh"] = sr.intro_zh
            entry["image_prompt_en"] = sr.image_prompt_en
            if sr.gpt_image_prompt:
                entry["gpt_image_prompt"] = sr.gpt_image_prompt
    return state


def update_state_for_illustrated(results: list[IllustratedRepo], state: dict) -> dict:
    """Write image_path from illustration results back into state."""
    for ir in results:
        entry = state.get(ir.repo.repo.full_name)
        if entry and ir.image_path:
            entry["image_path"] = ir.image_path
    return state
