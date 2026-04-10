# Agents guide — sqazi.sh (`shahzebqazi.github.io`)

This file is for **human and AI collaborators** who edit this repository. Follow it so changes stay consistent with how the site is built and deployed.

## Planning and tasks (source of truth)

**All ideas, backlog items, and tasks for this site should live in this GitHub Project:**

[https://github.com/users/shahzebqazi/projects/14](https://github.com/users/shahzebqazi/projects/14)

Before starting non-trivial work:

1. Check the project for existing items (avoid duplicating tasks).
2. Add or update cards there when you discover new follow-ups.
3. If an agent cannot access the project in a given environment, ask the user to paste the relevant card text or confirm priorities.

Treat the project board as the **canonical task list**; this repo’s issues and PRs should **reference** project items when useful (e.g. “Tracked in Project #14”).

## What this site is

- **Static GitHub Pages** site: plain HTML files at the repo root, no bundler.
- **Custom domain:** `sqazi.sh` (see `CNAME`). Live site is deployed from the **`main`** branch.
- **“Dynamic” pages:** `content.html?page=…` loads content via `fetch`. **Projects** uses `content/projects.html` (HTML + scoped CSS injected by script); **Papers, CV, Blog** use `content/*.txt` as plain text in a monospace block. There is no server-side rendering.

## Repo map

| Path | Role |
|------|------|
| `index.html` | Home / About |
| `links.html` | Redirect to the **links** site (separate repo; see `SYNC.md`) |
| `content.html` | Shell for Projects, Papers, CV, Blog (`?page=` → `content/projects.html` or `content/<name>.txt`) |
| `content/projects.html` | Projects portfolio (HTML cards; styles injected once) |
| `content/*.txt` | Papers, CV, Blog bodies (plain text; monospace block) |
| `README.md` | Plain-text mirror of bio/links for **GitHub profile** sync (see `SYNC.md`) |
| `SYNC.md` | How to keep profile README, home page, and links aligned |
| `.github/workflows/deploy.yml` | Deploy to GitHub Pages on push to `main` |

## Editing rules

- **Prefer minimal HTML** unless the user asks for richer structure or styling. Do not add CSS or heavy layout changes unless requested.
- **Bio / “About” copy:** If you change the story on the home page, update **`README.md`** here in plain text and remind the user to sync **`shahzebqazi/shahzebqazi`** if their profile should match (`SYNC.md`).
- **Projects list:** Edit **`content/projects.html`** (grouped sections, live URLs). Refresh periodically against GitHub (`has_pages` on repos) and spot-check URLs.
- **Links:** Maintain the standalone **links** repository (not this repo); navigation here points to **`links.html`** (redirect). Mirror to profile **`README.md`** when you want parity.

## Git and deploy

- Work on **feature branches**; merge to **`main`** to publish (workflow deploys on push to `main`).
- Commit messages should describe **what** changed and **why** when it is not obvious.

## Checklist before finishing a change

- [ ] Any new copy that belongs in the profile README is noted or updated per `SYNC.md`.
- [ ] `content/projects.html` and any `content/*.txt` used by navigation are up to date.
- [ ] New tasks or discoveries are reflected on [Project #14](https://github.com/users/shahzebqazi/projects/14) when appropriate.
