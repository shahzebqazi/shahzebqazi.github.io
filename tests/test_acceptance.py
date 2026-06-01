"""Acceptance checks against production (sqazi.sh)."""
import os

import pytest
import requests

BASE_URLS = (
    os.environ.get("SITE_URL", "https://sqazi.sh").rstrip("/"),
    os.environ.get("SITE_WWW_URL", "https://www.sqazi.sh").rstrip("/"),
)

MARKERS = (
    "Willy Worst",
    "sqazi-theme",
    "assets/css/catppuccin.css",
    "content.html?page=projects",
)


@pytest.mark.parametrize("base", BASE_URLS)
def test_homepage_returns_200_and_markers(base: str):
    r = requests.get(f"{base}/", timeout=30)
    r.raise_for_status()
    text = r.text
    for marker in MARKERS:
        assert marker in text, f"missing {marker!r} on {base}"
