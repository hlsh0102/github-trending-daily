"""Pipeline orchestrator: fetch → enrich → dedupe → summarize → illustrate → compose → render → git-commit."""

import logging
import os
import subprocess
import sys
from pathlib import Path

from trending.config import (
    IllustratedRepo,
    PROJECT_ROOT,
    STATE_FILE,
    VAULT_DIR,
    today_str,
)
from trending.compose import compose
from trending.dedupe import (
    load_state,
    reuse_images,
    save_state,
    split_repos,
    update_state_for_illustrated,
    update_state_for_summarized,
)
from trending.enrich import enrich
from trending.fetch import fetch_trending
from trending.illustrate import illustrate
from trending.render import render_all
from trending.summarize import summarize

logger = logging.getLogger(__name__)


def main() -> None:
    """Run the full trending pipeline for today."""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
        stream=sys.stderr,
    )

    today = today_str()
    logger.info("=== Trending pipeline START for %s ===", today)

    # 1. Fetch trending repos
    logger.info("Step 1/9: Fetching trending repos ...")
    repos = fetch_trending("daily")
    logger.info("  Fetched %d repos", len(repos))

    # 2. Enrich via GitHub REST API
    logger.info("Step 2/9: Enriching via GitHub REST ...")
    enriched = enrich(repos)
    logger.info("  Enriched %d repos", len(enriched))

    # 3. Dedupe — split into existing (reuse) and new (need LLM)
    logger.info("Step 3/9: Deduplicating against state ...")
    state_path = Path(STATE_FILE)
    state = load_state(state_path)
    existing, new, state = split_repos(enriched, state, today)
    logger.info("  Existing: %d, New: %d", len(existing), len(new))

    # 4. Summarize new repos via Claude API
    if new:
        logger.info("Step 4/9: Summarizing %d new repos via Claude ...", len(new))
        # summarize() takes list[EnrichedRepo], so extract from SummarizedRepo
        enriched_for_new = [sr.repo for sr in new]
        llm_results = summarize(enriched_for_new)
        # Merge LLM-generated intros & prompts back into the 'new' list
        llm_map: dict[str, any] = {sr.repo.full_name: sr for sr in llm_results}
        for sr in new:
            match = llm_map.get(sr.repo.full_name)
            if match:
                sr.intro_zh = match.intro_zh
                sr.image_prompt_en = match.image_prompt_en
        state = update_state_for_summarized(llm_results, state)
        logger.info("  Summarized %d repos", len(llm_results))
    else:
        logger.info("Step 4/9: No new repos — skipping summarize")

    # 5. Illustrate
    today_dir = Path(VAULT_DIR) / today
    today_assets_dir = today_dir / "assets"
    today_assets_dir.mkdir(parents=True, exist_ok=True)

    # 5a. Reuse old images for existing repos
    existing_illustrated = reuse_images(existing, state, today, today_assets_dir)
    logger.info("  Reused images for %d existing repos", len(existing_illustrated))

    # 5b. Generate new images for new repos
    new_illustrated: list[IllustratedRepo] = []
    if new:
        logger.info("Step 5/9: Illustrating %d new repos via DALL-E ...", len(new))
        new_illustrated = illustrate(new, today_assets_dir)
        state = update_state_for_illustrated(new_illustrated, state)
        logger.info("  Illustrated %d new repos", len(new_illustrated))

    # 6. Merge all IllustratedRepo in original fetch order
    logger.info("Step 6/9: Merging illustrated repos in fetch order ...")
    illustrated_by_name: dict[str, IllustratedRepo] = {}
    for ir in existing_illustrated + new_illustrated:
        illustrated_by_name[ir.repo.repo.full_name] = ir

    all_illustrated: list[IllustratedRepo] = []
    for repo in repos:
        ir = illustrated_by_name.get(repo.full_name)
        if ir:
            all_illustrated.append(ir)

    logger.info("  Merged %d illustrated repos", len(all_illustrated))

    # Re-number image files to match merged order so markdown embeds resolve
    _rename_images(all_illustrated, today_assets_dir)

    # 7. Compose overview.png
    logger.info("Step 7/9: Compositing overview image ...")
    overview_path = today_assets_dir / "overview.png"
    compose(all_illustrated, overview_path)

    # 8. Render vault files
    logger.info("Step 8/9: Rendering vault files ...")
    render_all(all_illustrated, today)

    # 9. Save state
    logger.info("Step 9/9: Saving state ...")
    save_state(state, state_path)
    logger.info("  State saved to %s", state_path)

    # 10. Git commit & push
    try:
        _git_commit_and_push(today)
    except Exception as exc:
        logger.warning("Git commit/push failed (non-fatal): %s", exc)

    logger.info("=== Trending pipeline DONE for %s ===", today)


def _rename_images(all_illustrated: list[IllustratedRepo], assets_dir: Path) -> None:
    """Rename image files to ``{idx:02d}-{owner}__{name}.png`` so that
    markdown embeds (which use the merged positional index) resolve correctly.

    After ``reuse_images`` and ``illustrate`` the files may have wrong indices
    because each function uses its own positional counter.  This function
    normalises every file to its position in the final merged list.
    """
    for i, ir in enumerate(all_illustrated):
        if not ir.image_path:
            continue
        old_path = Path(ir.image_path)
        if not old_path.exists():
            continue

        expected_name = f"{i + 1:02d}-{ir.repo.repo.owner}__{ir.repo.repo.name}.png"
        expected_path = assets_dir / expected_name

        if old_path.resolve() != expected_path.resolve():
            old_path.rename(expected_path)
            ir.image_path = str(expected_path.resolve())
            logger.debug("  Renamed %s → %s", old_path.name, expected_name)


def _git_commit_and_push(today: str) -> None:
    """Stage ``vault/`` and ``state/``, commit if dirty, push to remote."""
    os.chdir(PROJECT_ROOT)

    subprocess.run(
        ["git", "add", "vault/", "state/"],
        check=True,
        capture_output=True,
        text=True,
    )
    logger.info("  Staged vault/ and state/")

    # Check whether any changes are staged
    result = subprocess.run(
        ["git", "diff", "--quiet", "--cached"],
        capture_output=True,
    )
    if result.returncode == 0:
        logger.info("  No staged changes — skipping commit")
        return

    subprocess.run(
        ["git", "commit", "-m", f"chore(trending): {today}"],
        check=True,
        capture_output=True,
        text=True,
    )
    logger.info("  Committed: chore(trending): %s", today)

    subprocess.run(
        ["git", "push"],
        check=True,
        capture_output=True,
        text=True,
    )
    logger.info("  Pushed to remote")


if __name__ == "__main__":
    main()
