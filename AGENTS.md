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
- **Content sections:** `projects.html`, `papers.html`, `cv.html`, and `blog.html` are the canonical URLs. They are generated (or assembled) so crawlers see full HTML in the first response. Run `node scripts/generate-content-pages.mjs` after changing section bodies.
- **Projects body:** **`content/projects.html`** holds the portfolio markup (grouped cards + scoped CSS). The generator inlines it into root **`projects.html`** with shared nav and SEO tags.
- **Papers, CV, Blog:** Plain text in **`content/*.txt`**, inlined inside `<pre>` in the generated pages.
- **Legacy URL:** `content.html?page=…` redirects to the matching static page (deprecated; `noindex`).
- **Outbound links:** Maintained in a **separate** repository (its own GitHub Pages site). This repo’s **`links.html`** redirects there; see **`SYNC.md`**.

## Repo map

| Path | Role |
|------|------|
| `index.html` | Home / About |
| `links.html` | Redirect to the **links** site (separate repo; see `SYNC.md`) |
| `projects.html`, `papers.html`, `cv.html`, `blog.html` | Section pages (regenerate with `node scripts/generate-content-pages.mjs`) |
| `content.html` | Redirects `?page=` to the static pages above (deprecated; `noindex`) |
| `content/projects.html` | Projects portfolio (HTML + scoped style; source for `projects.html`) |
| `content/*.txt` | Papers, CV, Blog bodies; `content/projects.txt` is a plain-text mirror / legacy list |
| `scripts/generate-content-pages.mjs` | Builds root section HTML from `content/projects.html` and `content/*.txt` |
| `robots.txt`, `sitemap.xml` | Crawling and discovery |
| `README.md` | Plain-text mirror of bio/links for **GitHub profile** sync (see `SYNC.md`) |
| `SYNC.md` | How to keep profile README, home page, and links aligned |
| `.github/workflows/deploy.yml` | Deploy to GitHub Pages on push to `main` |

## Editing rules

- **Prefer minimal HTML** unless the user asks for richer structure or styling. Do not add CSS or heavy layout changes unless requested.
- **Bio / “About” copy:** If you change the story on the home page, update **`README.md`** here in plain text and remind the user to sync **`shahzebqazi/shahzebqazi`** if their profile should match (`SYNC.md`).
- **Projects list:** Edit **`content/projects.html`** (grouped sections, live URLs), then run **`node scripts/generate-content-pages.mjs`**. Refresh periodically against GitHub (`has_pages` on repos) and spot-check URLs.
- **Links:** Maintain the standalone **links** repository (not this repo); **`links.html`** here only redirects if the published URL changes. Mirror to profile **`README.md`** when you want parity.

## Git and deploy

- Work on **feature branches**; merge to **`main`** to publish (workflow deploys on push to `main`).
- Commit messages should describe **what** changed and **why** when it is not obvious.

## Checklist before finishing a change

- [ ] Any new copy that belongs in the profile README is noted or updated per `SYNC.md`.
- [ ] `content/projects.html` and any `content/*.txt` used by navigation are up to date; run `node scripts/generate-content-pages.mjs` when those bodies change.
- [ ] New tasks or discoveries are reflected on [Project #14](https://github.com/users/shahzebqazi/projects/14) when appropriate.
