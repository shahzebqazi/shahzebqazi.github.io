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
