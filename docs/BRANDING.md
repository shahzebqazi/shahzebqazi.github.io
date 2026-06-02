# Personal branding — canonical map

**Owner:** Willy Worst · **Primary domain:** [sqazi.sh](https://sqazi.sh) · **Contact:** code@sqazi.sh

This document is the **source of truth** for how personal surfaces relate. When anything disagrees, fix the canonical source first, then sync dependents.

---

## Hierarchy (what each surface is for)

| Priority | Surface | Repo | URL | Role |
|----------|---------|------|-----|------|
| 1 | **CV (human)** | `shahzebqazi.github.io` | [sqazi.sh/content.html?page=cv](https://sqazi.sh/content.html?page=cv) | **Main résumé page** — share in applications, email sig, Featured |
| 1 | **CV (machine)** | same | [sqazi.sh/content/cv.txt](https://sqazi.sh/content/cv.txt) | Live CV (plain text at `?page=cv`); facts from `~/Git/private/my-linkedin` |
| 2 | **Portfolio home** | same | [sqazi.sh](https://sqazi.sh/) | About, narrative, nav to Projects / CV / Blog |
| 2 | **Projects** | same | [sqazi.sh/content.html?page=projects](https://sqazi.sh/content.html?page=projects) | Curated shipped work |
| 3 | **GitHub profile** | `shahzebqazi` | [github.com/shahzebqazi](https://github.com/shahzebqazi) | Code identity; README mirrors **home** story, links to CV |
| 4 | **Link hub** | `links` | [shahzeb.me](https://shahzeb.me/) | Family / friends / clients — social + ventures table |
| 4 | **Links redirect** | same | [sqazi.sh/links.html](https://sqazi.sh/links.html) | Redirect to **shahzeb.me** (do not duplicate link tables here) |
| 5 | **LinkedIn** | `social/linkedin` (copy only) | [linkedin.com/in/lambdaqazi](https://www.linkedin.com/in/lambdaqazi) | Recruiter search — **derived** from CV + `profile/*.md` |
| — | **Tailored CVs** | `social/linkedin` | `applications/resumes/tailored/*` | Per-job variants — never overwrite `content/cv.txt` |

**Rule:** Facts (employers, dates, projects, contact) live in **`content/cv.txt`**. LinkedIn and PDFs are **projections** of that file plus lane-specific emphasis (`social/linkedin`).

---

## Canonical identity block

Use this block everywhere (CV header, cover letters, email footer, link hub email row):

```
Willy Worst
Toronto, Ontario, Canada
code@sqazi.sh · https://sqazi.sh
CV: https://sqazi.sh/content.html?page=cv
```

| Field | Canonical | Notes |
|-------|-----------|--------|
| Display name | **Willy Worst** | Professional / portfolio / LinkedIn |
| Legal / forms | Willy S. Qazi | Government, payroll, contracts only |
| Email | **code@sqazi.sh** | Not gmail for professional applies |
| Portfolio | **https://sqazi.sh** | Never `shahzebqazi.github.io` in outward copy |
| Legacy host | **https://shahzebqazi.github.io** | Redirects to sqazi.sh (same path/query); not a second site |
| GitHub | **https://github.com/shahzebqazi** | |
| CV (share link) | **https://sqazi.sh/content.html?page=cv** | Primary CTA for recruiters |
| CV (fetch) | **https://sqazi.sh/content/cv.txt** | For agents and scripts |
| LinkedIn | **/in/lambdaqazi** | Public profile URL |
| Link hub | **https://shahzeb.me** | Personal network; footer may link sqazi.sh |
| Venture (agents) | **Mystic Agents** | Not “Mystic Labs” |
| mystic-ai | Product / design repo name | Distinct from Mystic Agents venture |

---

## Positioning

**sqazi.sh CV is SWE-only** (`content/cv.txt`): software engineering, agents, backends, and shipped code. Audio mastering, Reverb shop, and client-service ventures stay on [shahzeb.me](https://shahzeb.me/) and LinkedIn—not on the public CV page.

Job-specific emphasis (e.g. backend-heavy vs. agent-heavy) happens in:

- `social/linkedin/profile/*.md` → LinkedIn paste
- `social/linkedin/applications/resumes/tailored/*` → per application

Do not maintain two competing master CV files.

---

## Sync checklist (after editing `content/cv.txt`)

1. Push `shahzebqazi.github.io` → verify [CV page](https://sqazi.sh/content.html?page=cv) and [cv.txt](https://sqazi.sh/content/cv.txt).
2. If **summary** or **ventures** changed, scan **shahzeb.me** link table (`links/index.html`) for matching labels (Mystic Agents, CV link).
3. If **bio story** changed on home, sync `index.html` ↔ `shahzebqazi/README.md` per `SYNC.md`.
4. Run `social/linkedin` diff: `profile/experience.md`, `about.md` — no invented facts.
5. Regenerate tailored PDFs only when applying (not on every CV tweak).

---

## Repo map (for agents)

| Path | Edit when |
|------|-----------|
| `shahzebqazi.github.io/content/cv.txt` | Live CV facts — sync from `my-linkedin` (`CANDIDATE.md`, `profile/*.md`) |
| `my-linkedin/assets/` | LinkedIn post / company art (private; not deployed to sqazi.sh) |
| `shahzebqazi.github.io/assets/cv-heroes/` | Project hero art for **projects page** only |
| `shahzebqazi.github.io/index.html` | Home / About narrative |
| `shahzebqazi.github.io/content/projects.html` | Project cards |
| `shahzebqazi.github.io/links.html` | Redirect target for link hub only |
| `shahzebqazi/README.md` | GitHub profile README |
| `links/index.html` | shahzeb.me link table + socials |
| `social/linkedin/profile/*.md` | LinkedIn copy |
| `social/linkedin/applications/**` | Covers, tailored CVs, applies |

---

## Known gaps (operator)

- [x] LinkedIn public URL: `lambdaqazi` (sqazi.sh, shahzeb.me, GitHub profile)
- [ ] Lane-A master PDF for Easy Apply (`PRE_APPLICATION_CHECKLIST.md`)
- [x] Home page + GitHub README pinned repos differ — aligned around featured GitHub pins
- [x] Home page (`index.html`) still audio-forward—aligned to SWE / AI / developer tooling first

---

*Last updated: 2026-05-28*
