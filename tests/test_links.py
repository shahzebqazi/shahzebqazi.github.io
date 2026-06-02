"""Link hygiene for deployed copy (static parse; optional live probe)."""
import re
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parents[1]

DEPLOYED_GLOB = (
    "index.html",
    "content.html",
    "links.html",
    "content/projects.html",
    "content/cv.txt",
    "assets/js/plain-content.js",
)

URL_RE = re.compile(r"https?://[^\s\"'<>)\]]+")

# sqazi.sh demo prefixes still blocked on S3 (no public artifact yet)
FORBIDDEN_SQAZI_DEMO_PREFIXES = (
    "https://sqazi.sh/iconoclast-vst-ui/",
)

# Known-bad GitHub paths cited in past audits
FORBIDDEN_GITHUB_PATHS = (
    "https://github.com/shahzebqazi/benchmark-euterpea/tree/main/report",
)


def _deployed_texts():
    for rel in DEPLOYED_GLOB:
        yield rel, (REPO_ROOT / rel).read_text(encoding="utf-8")


def test_deployed_copy_has_no_forbidden_sqazi_demo_hrefs():
    for rel, text in _deployed_texts():
        for bad in FORBIDDEN_SQAZI_DEMO_PREFIXES:
            assert bad not in text, f"{rel} still links {bad}"


def test_deployed_copy_has_no_known_bad_github_paths():
    for rel, text in _deployed_texts():
        for bad in FORBIDDEN_GITHUB_PATHS:
            assert bad not in text, f"{rel} still links {bad}"


def test_cv_txt_github_repos_have_plain_content_anchor():
    """Every shahzebqazi repo URL in cv.txt must be in GITHUB_REPO_ANCHOR (if rewrite re-enabled)."""
    import re

    cv = (REPO_ROOT / "content" / "cv.txt").read_text(encoding="utf-8")
    js = (REPO_ROOT / "assets/js/plain-content.js").read_text(encoding="utf-8")
    anchors = set(re.findall(r'"([^"]+)":\s*"project-', js)) | set(
        re.findall(r"(\w+):\s*\"project-", js)
    )
    repos = re.findall(
        r"https://github\.com/shahzebqazi/([^/#?\s]+)", cv, flags=re.IGNORECASE
    )
    missing = sorted({r for r in repos if r not in anchors})
    assert not missing, f"cv.txt repos missing from GITHUB_REPO_ANCHOR: {missing}"


def test_projects_html_urls_are_https_or_internal():
    projects = (REPO_ROOT / "content" / "projects.html").read_text(encoding="utf-8")
    for url in URL_RE.findall(projects):
        url = url.rstrip(".,;)")
        assert url.startswith("https://") or url.startswith("content.html"), url


@pytest.mark.live
def test_sqazi_demo_prefixes_return_200():
    """Run with: pytest tests/test_links.py -m live (needs network + infra)."""
    import subprocess

    for prefix in (
        "lambda-terminal",
        "pa2-car-plugin",
        "neck-diagram-studio",
        "mhn-ai-agent-memory",
        "mystic-ai",
        "benchmark-euterpea",
    ):
        url = f"https://sqazi.sh/{prefix}/"
        code = subprocess.check_output(
            ["curl", "-sI", "-L", "-o", "/dev/null", "-w", "%{http_code}", url],
            text=True,
        ).strip()
        assert code == "200", f"{url} -> {code}"
