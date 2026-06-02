# Agents guide — sqazi.sh (`my-website`)

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

- **Static site** on **AWS**: S3 + CloudFront — infra in **`my-servers`** moon Sol ([`infra/README.md`](infra/README.md)).
- **Custom domain:** `sqazi.sh` (DNS via DigitalOcean by default; see [`docs/AWS_MIGRATION.md`](docs/AWS_MIGRATION.md)).
- **Deploy (sqazi.sh):** push to **`main`** → `deploy.yml` → S3 sync + CloudFront invalidation.
- **Deploy (github.io):** same push → `pages-redirect.yml` → `pages/` only (redirect stubs to sqazi.sh). Repo **Settings → Pages → Source: GitHub Actions** must be enabled once.
- **CV:** [sqazi.sh/content.html?page=cv](https://sqazi.sh/content.html?page=cv) — edit `content/cv.html` (human, with hero art) and `content/cv.txt` (machine); see [`docs/BRANDING.md`](docs/BRANDING.md).
- **CV hero art:** vendored under `assets/cv-heroes/` from source repos (do not replace with `assets/projects/*` placeholders).
- **“Dynamic” pages:** `content.html?page=…` loads HTML fragments or plain text. **Projects** → `content/projects.html`; **CV** → `content/cv.html`; **Papers, Blog** → `content/*.txt`.

## Repo map

| Path | Role |
|------|------|
| `index.html` | Home / About |
| `links.html` | Redirect to the **links** site (separate repo; see `SYNC.md`) |
| `content.html` | Shell for Projects, Papers, CV, Blog (`?page=` → `content/projects.html`, `content/cv.html`, or `content/<name>.txt`) |
| `content/cv.html` | Human CV with linked copy and `assets/cv-heroes/` art |
| `content/projects.html` | Projects portfolio (HTML cards) |
| `content/*.txt` | Papers, CV, Blog bodies |
| `README.md` | Plain-text mirror for **GitHub profile** sync (`SYNC.md`) — not deployed to S3 |
| `SYNC.md` | Profile README, home page, and links alignment |
| `infra/README.md` | Pointer to `my-servers/moons/sol/` |
| `docs/AWS_MIGRATION.md` | Short pointer to moon Sol setup |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | Planned work: CV/projects, employability, SEO |
| `pages/` | GitHub Pages redirect stubs (not deployed to S3) |
| `.github/workflows/deploy.yml` | Deploy site to S3 + invalidate CloudFront |
| `.github/workflows/pages-redirect.yml` | Deploy `pages/` to GitHub Pages |

## Editing rules

- **Prefer minimal HTML** unless the user asks for richer structure or styling.
- **Bio / “About” copy:** If you change the story on the home page, update **`README.md`** and remind the user to sync **`shahzebqazi/shahzebqazi`** per `SYNC.md`.
- **Projects list:** Edit **`content/projects.html`**; spot-check live URLs.
- **Links:** Maintain the standalone **links** repository; **`links.html`** only holds the redirect.

## Git and deploy

- Work on **feature branches**; merge to **`main`** to publish.
- **Do not** re-add a root `CNAME` file (custom domain on Pages removed 2026-06-01).
- **Do not** put `shahzebqazi.github.io` in deployed HTML or `content/*` — use `https://sqazi.sh/…` paths.
- Per-repo project sites under `github.io/<project>/` are separate repos; migrate or redirect those individually if needed.
- Infra changes: in `~/Git/Machines/my-servers/moons/sol/terraform` — not this repo.
- Commit messages should describe **what** changed and **why** when it is not obvious.

## Checklist before finishing a change

- [ ] Profile README sync noted per `SYNC.md` when bio/links changed.
- [ ] `content/projects.html` and relevant `content/*.txt` updated.
- [ ] New tasks on [Project #14](https://github.com/users/shahzebqazi/projects/14) when appropriate.
- [ ] No secrets in git (GitHub Actions secrets; `terraform.tfvars` in my-servers, gitignored there).
