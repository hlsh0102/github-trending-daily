"""Integration test for the full trending pipeline — all external calls mocked."""

import tempfile
from pathlib import Path
from unittest.mock import patch

from trending.config import EnrichedRepo, Repo, SummarizedRepo
from trending.main import main


def _make_repo(idx: int) -> Repo:
    """Build a realistic-looking Repo for test use."""
    return Repo(
        owner=f"owner{idx}",
        name=f"repo{idx}",
        full_name=f"owner{idx}/repo{idx}",
        description=f"Test repo {idx}",
        language="Python",
        stars_total=1000 + idx * 100,
        stars_today=50 + idx,
        url=f"https://github.com/owner{idx}/repo{idx}",
    )


def _make_enriched(r: Repo) -> EnrichedRepo:
    """Upgrade a Repo to an EnrichedRepo with fake API data."""
    return EnrichedRepo(
        owner=r.owner,
        name=r.name,
        full_name=r.full_name,
        description=r.description,
        language=r.language,
        stars_total=r.stars_total,
        stars_today=r.stars_today,
        url=r.url,
        readme_head="# README",
        avatar_url=f"https://avatars.example.com/{r.owner}.png",
        license_spdx="MIT",
        default_branch="main",
    )


def test_main_pipeline_all_existing():
    """Full pipeline assembles correctly when every repo is already known.

    All repos come back as "existing" so the LLM summarisation and DALL-E
    illustration steps are skipped entirely.  Every external boundary is
    mocked so the test passes without API keys and in under 2 seconds.
    """
    # ------------------------------------------------------------------
    # 1.  Create 10 mock Repo objects
    # ------------------------------------------------------------------
    repos = [_make_repo(i) for i in range(10)]

    # 2.  Enriched versions (as if GitHub REST API had been called)
    enriched = [_make_enriched(r) for r in repos]

    # 3.  Summarised repos — already known from previous days
    summarized = [
        SummarizedRepo(
            repo=e,
            intro_zh=f"intro zh for {e.full_name}",
            image_prompt_en=f"isometric illustration of {e.full_name}",
        )
        for e in enriched
    ]

    # ------------------------------------------------------------------
    # Temporary directory to isolate filesystem operations
    # ------------------------------------------------------------------
    with tempfile.TemporaryDirectory() as tmpdir:
        tmp = Path(tmpdir)
        state_file = tmp / "state" / "repos.json"

        with (
            # -- pipeline steps -------------------------------------------------
            patch("trending.main.fetch_trending", return_value=repos),
            patch("trending.main.enrich", return_value=enriched),
            patch(
                "trending.main.split_repos",
                return_value=(summarized, [], {}),  # all existing, no new
            ),
            patch("trending.main.summarize") as mock_summarize,
            patch("trending.main.render_all") as mock_render_all,
            patch("trending.main.generate_articles", return_value={}),
            # -- state I/O -------------------------------------------------------
            patch("trending.main.load_state", return_value={}),
            patch("trending.main.save_state"),
            patch("trending.main.update_state_for_summarized", return_value={}),
            # -- git ------------------------------------------------------------
            patch("trending.main._git_commit_and_push"),
            # -- paths (so real vault / state files are never touched) -----------
            patch("trending.main.STATE_FILE", str(state_file)),
        ):
            main()

        # ------------------------------------------------------------------
        # Assertions: no API calls were made
        # ------------------------------------------------------------------
        mock_summarize.assert_not_called()
        rendered_repos = mock_render_all.call_args.args[0]
        assert len(rendered_repos) == 10
        assert all(repo.image_path == "" for repo in rendered_repos)
