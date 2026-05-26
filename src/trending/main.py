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
    today_str,
)
from trending.dedupe import (
    load_state,
    save_state,
    split_repos,
    update_state_for_summarized,
)
from trending.enrich import enrich
from trending.fetch import fetch_trending
from trending.render import render_all
from trending.summarize import summarize
from trending.article import generate_articles

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
                sr.gpt_image_prompt = match.gpt_image_prompt
        state = update_state_for_summarized(llm_results, state)
        logger.info("  Summarized %d repos", len(llm_results))
    else:
        logger.info("Step 4/9: No new repos — skipping summarize")

    # 5. Merge summarized repos in original fetch order. The render layer still
    # consumes IllustratedRepo, but image_path is intentionally empty.
    logger.info("Step 5/8: Merging summarized repos in fetch order ...")
    summarized_by_name = {sr.repo.full_name: sr for sr in existing + new}

    all_illustrated: list[IllustratedRepo] = []
    for repo in repos:
        sr = summarized_by_name.get(repo.full_name)
        if sr:
            all_illustrated.append(IllustratedRepo(repo=sr, image_path=""))

    logger.info("  Merged %d repos", len(all_illustrated))

    # 6. Generate detailed Chinese articles
    logger.info("Step 6/8: Generating articles for %d repos ...", len(all_illustrated))
    articles = generate_articles(all_illustrated)
    logger.info("  Generated %d articles", len(articles))

    # 7. Render vault files
    logger.info("Step 7/8: Rendering vault files ...")
    render_all(all_illustrated, today, articles)

    # 8. Save state
    logger.info("Step 8/8: Saving state ...")
    save_state(state, state_path)
    logger.info("  State saved to %s", state_path)

    # 10. Git commit & push
    try:
        _git_commit_and_push(today)
    except subprocess.CalledProcessError as exc:
        logger.warning("Git commit/push failed (non-fatal): %s\nstderr: %s", exc, exc.stderr)
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

    # Ensure git identity is set (required in CI)
    for key, value in [
        ("user.name", "github-actions[bot]"),
        ("user.email", "github-actions[bot]@users.noreply.github.com"),
    ]:
        subprocess.run(
            ["git", "config", key, value],
            capture_output=True,
        )

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
