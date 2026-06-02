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

CV_MARKERS = (
    "Willy Worst",
    "FEATURED GITHUB PINS",
    "https://github.com/shahzebqazi",
    "Authorized to work in Canada",
    "mailto:code@sqazi.sh",
)


@pytest.mark.parametrize("base", BASE_URLS)
def test_homepage_returns_200_and_markers(base: str):
    r = requests.get(f"{base}/", timeout=30)
    r.raise_for_status()
    text = r.text
    for marker in MARKERS:
        assert marker in text, f"missing {marker!r} on {base}"


@pytest.mark.github_io
@pytest.mark.parametrize("base", BASE_URLS)
def test_cv_page_returns_200_and_markers(base: str):
    r = requests.get(f"{base}/content.html?page=cv", timeout=30)
    r.raise_for_status()
    text = r.text
    for marker in CV_MARKERS:
        assert marker in text, f"missing {marker!r} on {base} CV"


@pytest.mark.github_io
def test_github_io_root_is_redirect_stub():
    r = requests.get("https://shahzebqazi.github.io/", timeout=30)
    r.raise_for_status()
    text = r.text
    assert "sqazi.sh" in text
    assert "Willy Worst" not in text


@pytest.mark.github_io
def test_github_io_preserves_path_on_missing_page():
    r = requests.get(
        "https://shahzebqazi.github.io/content.html?page=cv", timeout=30
    )
    r.raise_for_status()
    assert "sqazi.sh/content.html" in r.text
