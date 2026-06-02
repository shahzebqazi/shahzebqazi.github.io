"""Unit checks: repo layout and workflow YAML."""
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_index_html_exists_and_has_markers():
    index = (REPO_ROOT / "index.html").read_text(encoding="utf-8")
    assert "<!DOCTYPE html>" in index
    assert "sqazi.sh" in index
    assert "Willy Worst" in index
    assert "assets/css/catppuccin.css" in index


def test_content_shell_exists():
    assert (REPO_ROOT / "content.html").is_file()
    assert (REPO_ROOT / "content" / "projects.html").is_file()
    assert (REPO_ROOT / "content" / "cv.html").is_file()


def test_cv_hero_assets_exist():
    heroes = REPO_ROOT / "assets" / "cv-heroes"
    for name in (
        "dotfiles-horde.jpg",
        "mastodon-agent.webp",
        "power-ampache2-android-auto.png",
        "mystic-ai.png",
    ):
        path = heroes / name
        assert path.is_file(), name
        assert path.stat().st_size > 1000, name


DEPLOYED_COPY = (
    "index.html",
    "content.html",
    "links.html",
    "content/projects.html",
    "content/cv.html",
    "content/cv.txt",
)


def test_deployed_copy_has_no_github_io_urls():
    for rel in DEPLOYED_COPY:
        text = (REPO_ROOT / rel).read_text(encoding="utf-8")
        assert "shahzebqazi.github.io" not in text, rel


def test_pages_redirect_stubs():
    index = (REPO_ROOT / "pages" / "index.html").read_text(encoding="utf-8")
    assert "https://sqazi.sh/" in index
    not_found = (REPO_ROOT / "pages" / "404.html").read_text(encoding="utf-8")
    assert "location.pathname" in not_found


def test_deploy_workflow_yaml_valid():
    workflow_path = REPO_ROOT / ".github" / "workflows" / "deploy.yml"
    data = yaml.safe_load(workflow_path.read_text(encoding="utf-8"))
    assert data["name"]
    on = data.get(True) or data.get("on")
    assert on and "push" in on
    assert data["permissions"]["id-token"] == "write"
    steps = data["jobs"]["deploy"]["steps"]
    step_names = [s.get("name", s.get("uses", "")) for s in steps]
    assert any("S3" in n for n in step_names)
    assert any("CloudFront" in n for n in step_names)
    sync_step = next(s for s in steps if s.get("name") == "Sync static files to S3")
    run = sync_step["run"]
    assert "--guess-mime-type" not in run
    assert "--exclude \"pages/*\"" in run


def test_pages_redirect_workflow_yaml_valid():
    workflow_path = REPO_ROOT / ".github" / "workflows" / "pages-redirect.yml"
    data = yaml.safe_load(workflow_path.read_text(encoding="utf-8"))
    assert data["permissions"]["pages"] == "write"
    steps = data["jobs"]["deploy"]["steps"]
    upload = next(s for s in steps if "upload-pages-artifact" in s.get("uses", ""))
    assert upload["with"]["path"] == "pages"
