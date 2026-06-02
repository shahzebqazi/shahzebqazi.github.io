# Handoff — CV, projects page, employability & SEO

**Status:** In progress (2026-06-02) — Phases 1–3 implemented locally; deploy + Phase 4 infra pending  
**Repo:** `shahzebqazi.github.io` (site source; deploys to **sqazi.sh** via AWS)  
**Canon:** [`docs/BRANDING.md`](../BRANDING.md) · [`AGENTS.md`](../../AGENTS.md) · [`SYNC.md`](../../SYNC.md)  
**Task board:** [GitHub Project #14](https://github.com/users/shahzebqazi/projects/14)

---

## Mission

Improve the **human CV** and **projects** pages so they read clearly to recruiters and hiring managers in under 30 seconds, strengthen **employability signals** (scope, dates, outcomes, links that work), and fix **SEO / discoverability** without keyword stuffing or duplicating audio-studio positioning on the SWE CV.

**Out of scope unless operator approves:** LinkedIn paste (`social/linkedin`), tailored PDFs, private `my-mac-config` content, Terraform/Sol infra except S3 prefix sync for broken demo URLs.

---

## Current state (baseline)

### Hosting

| URL | Host | Notes |
|-----|------|--------|
| `https://sqazi.sh` | S3 + CloudFront (Sol) | Production; push `main` → `deploy.yml` |
| `https://shahzebqazi.github.io` | GitHub Pages (`pages/` redirect only) | Must redirect to sqazi.sh; not a second site |

### CV (recent)

- **Human:** `content/cv.html` — HTML with links, dates on roles, **Highlighted work** cards.
- **Machine:** `content/cv.txt` — ATS/agent source; must stay in sync with facts in `cv.html`.
- **Hero art (vendored):** `assets/cv-heroes/` — canonical art copied from source repos (not `assets/projects/*` placeholders).

| File | Source repo / path |
|------|---------------------|
| `dotfiles-horde.jpg` | `my-mac-config/docs/assets/hero-horde-peons.jpg` (devops-for-the-horde lineage; private repo — already vendored) |
| `mastodon-agent.png` | `mastodon-agent/docs/images/hero.png` (~1.9 MB — consider compressing) |
| `power-ampache2-android-auto.png` | Recovered from `PowerAmpache2PluginTemplate` git: `docs/images/hero-android-auto.png` |
| `mystic-ai.png` | `mystic-ai/Assets/output/heroes/hero-landing.png` |

### Projects (needs work)

- `content/projects.html` still uses **`assets/projects/*-hero.svg`** — Catppuccin template banners added 2026-05-28 (`52f78a2`, Cursor). **Not** the same as repo demo art or `assets/cv-heroes/`.
- **Featured pins on page ≠ canon:** Page lists mystic-ai + zinwa in featured; canon (home, `BRANDING_AUDIT_TASKS.md`) is: **lambda-terminal · benchmark-euterpea · cursor-agents · mhn-ai-agent-memory · dotfiles · Power Ampache 2**.
- **uxui card** reuses `mystic-ai-hero.svg`; copy is weak; `uxui.sqazi.sh` may not resolve.
- Many `https://sqazi.sh/<project>/` demo paths return **403** (S3 prefix never synced) — see [`my-servers` handoff](https://github.com/shahzebqazi/my-servers/blob/main/docs/handoff/alerts/2026-06-01-lambda-terminal-down.md).

### Tests

- `tests/test_unit.py` — layout, no `shahzebqazi.github.io` in deployed copy, cv-heroes exist.
- `tests/test_acceptance.py` — live sqazi.sh homepage + CV markers (post-deploy).
- Run: `python3 -m pytest tests/ -q -m "not github_io"`

---

## Employability signals review

Use this rubric when editing. Score each area **Pass / Weak / Fail** in PR description.

### Above the fold (CV + home)

| Signal | Current | Target |
|--------|---------|--------|
| Name + role clarity | Pass | Keep “Software engineer · AI agents” lead on home; CV `<h1>` is still page title “CV” only — consider `Willy Worst — Software Engineer` in `<title>` and visible `<h1>` |
| Location + work auth | Pass (Toronto) | Add work authorization only if operator confirms (not in repo today) |
| Primary CTA | Weak | One obvious “CV” / “Contact” above fold on CV; `mailto:code@sqazi.sh` present |
| Scan time | Weak | Recruiter should grasp fit in **&lt;10 s** — reduce repeated stack keywords between summary and strengths |

### Experience

| Signal | Current | Target |
|--------|---------|--------|
| Dates | Partial | PA2 + Iconoclast dated; **education has no year**; pin projects have no dates |
| Outcomes | Weak | Bullets are tasks, not results (metrics, scale, users, latency, shipped version) |
| SWE vs audio | Mixed | Iconoclast bullets are studio-heavy — OK as founder role but keep **SWE CV** framing per BRANDING |
| Duplication | Fail | Power Ampache appears in highlights, experience, and featured pins — consolidate |

### Projects & proof

| Signal | Current | Target |
|--------|---------|--------|
| GitHub pins alignment | Fail | Match six pins exactly in featured section |
| Demo links | Fail | Fix 403s or link to working URLs (github.io demos, raw Pages) until S3 synced |
| Visual proof | Partial | CV has real heroes; projects page does not |
| mastodon-agent | Pass on CV | Not a GitHub pin — OK in highlights; don’t imply pin unless pinned |

### Trust & hygiene

| Signal | Current | Target |
|--------|---------|--------|
| Broken encoding | Fail | `assets/projects/lambda-terminal-hero.svg` has U+FFFD mojibake — fix or replace with repo `lambda-terminal/docs/assets/hero.svg` |
| Consistency | Weak | `cv.html` vs `cv.txt` vs `index.html` vs `projects.html` — single fact source (`cv.txt` first, then propagate) |
| Private lineage | Pass | dotfiles ↔ horde called out honestly (public layer vs private bootstrap) |

---

## SEO review

### Page-level (technical)

| Page | Issue | Recommendation |
|------|--------|----------------|
| `content.html` (all `?page=`) | Generic `<title>Content — sqazi.sh</title>` in shell; JS sets title late | Static or per-page meta in shell: CV, Projects, Papers, Blog |
| CV / Projects | No `<meta name="description">` | Unique descriptions (155–160 chars), SWE-focused |
| CV / Projects | No canonical link | `<link rel="canonical" href="https://sqazi.sh/content.html?page=cv">` |
| CV / Projects | Content loaded via JS `fetch` | Acceptable for portfolio; ensure **cv.txt** and **semantic HTML in fragment** exist for crawlers; consider lightweight `<noscript>` fallback links |
| `index.html` | Has description | Good — mirror tone on subpages |
| Headings | CV fragment uses `<h2>` sections | Good; ensure one logical `<h1>` per rendered page (either in fragment or shell) |
| Images | Heroes need descriptive `alt` | CV alts are good; audit projects after art swap |
| Performance | `mastodon-agent.png` ~1.9 MB | Compress (WebP or optimized PNG); `loading="lazy"` already set |

### Content SEO (avoid over-optimization)

**Problems observed:**

- Repeated keywords: “software engineer”, “AI”, “agent”, “Kotlin”, “MCP” across summary, strengths, and project blurbs.
- Open-role line stacks synonyms (“Software Engineer, AI Engineer, platform/backend”) — pick **2 target titles** max for human CV.
- mystic-ai + uxui duplicate “design / UX showcase” story.

**Target:**

- One **primary keyword cluster** in summary (e.g. software engineer, AI agents, backends).
- Strengths = capability buckets, not repeat of summary adjectives.
- Each project card = **unique** proof line (what shipped, stack, link).
- Do **not** add hidden text or meta keyword lists.

### Structured data (optional P2)

- `Person` JSON-LD on CV or home: name, url, sameAs (GitHub, LinkedIn), jobTitle.
- Only if operator wants rich results; keep facts identical to BRANDING block.

---

## Planned work (phases)

### Phase 0 — Read & verify (no code)

- [ ] Read `docs/BRANDING.md`, `AGENTS.md`, this handoff.
- [ ] Open live: `https://sqazi.sh/content.html?page=cv`, `?page=projects`, `https://sqazi.sh/content/cv.txt`.
- [ ] `diff <(curl -sL https://sqazi.sh/content/cv.txt) content/cv.txt` after any deploy (empty = in sync).
- [ ] Curl demo paths from projects page; log 200 vs 403.

### Phase 1 — CV employability (P0)

**Files:** `content/cv.html`, `content/cv.txt`, `assets/css/site.css`, `content.html` (title/meta only if needed).

1. **Deduplicate** — One mention of Power Ampache / dotfiles / mystic in highlights; slim featured list or merge sections.
2. **Education** — Add graduation year or expected date (operator fact).
3. **Outcomes** — Rewrite 2–4 bullets with shipped results (no invented metrics; ask operator if unknown).
4. **Summary** — Tighten to 2 sentences; move stack list to strengths once.
5. **Sync** — `cv.txt` facts ↔ `cv.html` (machine file remains ATS source).
6. **Compress** — `assets/cv-heroes/mastodon-agent.png` if &gt;500 KB after optimization.

**Acceptance:**

- [ ] All URLs in CV click (mailto, LinkedIn, GitHub, sqazi.sh).
- [ ] No `shahzebqazi.github.io` in deployed `content/*` or `index.html`.
- [ ] `pytest tests/test_unit.py -q` passes.
- [ ] Human read: SWE story clear in 10 s; audio deferred to iconoclast link only.

### Phase 2 — Projects page alignment (P0)

**Files:** `content/projects.html`, `assets/projects/` (deprecate or replace), optionally share `assets/cv-heroes/`.

1. **Reorder featured** to canon six pins (remove mystic-ai + zinwa from featured; move to broader portfolio per `BRANDING_AUDIT_TASKS.md`).
2. **Replace hero art** — Per project, use **canonical** asset:
   - Copy from repo `docs/assets/hero.svg` **or** `assets/cv-heroes/*` **or** demo PNG paths (see table in §Baseline).
   - **Delete or stop referencing** generic `assets/projects/*-hero.svg` template set when replaced.
   - Fix lambda-terminal encoding from repo source.
3. **Remove or fix uxui card** — Drop until `uxui` repo/subdomain exists; or link to real `uxui` / miverna mockups with own art.
4. **Demo URLs** — Prefer URLs that return 200 today; document fallbacks in card meta.

**Acceptance:**

- [ ] Featured section = six GitHub pins (names match home `index.html`).
- [ ] No Catppuccin-template duplicate art unless repo has no art (then ask operator).
- [ ] `curl -sI` spot-check every `href` demo link on projects page.

### Phase 3 — SEO & shell (P1)

**Files:** `content.html`, `index.html`, maybe `assets/js/meta.js` (minimal).

- [ ] Per-page `<title>` and meta description (cv, projects, papers, blog).
- [ ] `<link rel="canonical">` for `content.html?page=*`.
- [ ] Optional: JSON-LD on CV.
- [ ] Open Graph tags (`og:title`, `og:description`, `og:image` — use one cv-hero or site default).

**Acceptance:**

- [ ] View source / curl shows meta without executing JS (shell-level tags).
- [ ] Titles include “Willy Worst” or role where appropriate.

### Phase 4 — Infra follow-up (P2, separate repo)

**Repo:** `my-servers` moon Sol — not blocking copy edits.

- [ ] S3 sync missing prefixes: `mystic-ai/`, `mhn-ai-agent-memory/`, `neck-diagram-studio/`, `pa2-car-plugin/`, etc.
- [ ] CloudFront subpath rewrite already exists for directory indexes.
- [ ] After sync, re-test all `sqazi.sh/<project>/` links from projects/CV.

### Phase 5 — Cross-surface sync (P1)

- [ ] `index.html` ↔ `README.md` ↔ featured pins (per `SYNC.md`).
- [ ] `docs/BRANDING.md` repo map: add `content/cv.html`, `assets/cv-heroes/`.
- [ ] Close or update `docs/BRANDING_AUDIT_TASKS.md` checkboxes when done.
- [ ] Card on Project #14 for any new follow-ups.

---

## Canonical six GitHub pins (do not drift)

1. lambda-terminal  
2. benchmark-euterpea  
3. cursor-agents  
4. mhn-ai-agent-memory  
5. dotfiles  
6. Power Ampache 2 Plugin Template  

**Broader portfolio (not featured):** Iconoclast Audio, Neck Diagram Studio, mystic-ai, zinwa-q25-keyboard, mastodon-agent (CV highlight OK).

---

## Hero art source map (for projects page fix)

| Project | Prefer this asset | Notes |
|---------|-------------------|--------|
| mystic-ai | `mystic-ai/Assets/output/heroes/hero-landing.png` or `banner-readme.png` | Already on CV as `assets/cv-heroes/mystic-ai.png` |
| dotfiles | `assets/cv-heroes/dotfiles-horde.jpg` or repo `docs/assets/hero.svg` | Horde art = devops-for-the-horde lineage |
| Power Ampache 2 | `assets/cv-heroes/power-ampache2-android-auto.png` | Restore to plugin repo `docs/images/` if missing |
| lambda-terminal | `lambda-terminal/docs/assets/hero.svg` | Do not use corrupted site copy |
| benchmark-euterpea | Generated report site or repo README art | No `docs/assets/hero.svg` in repo |
| cursor-agents | `cursor-agents/docs/assets/hero.svg` | |
| mhn-ai-agent-memory | `mhn-ai-agent-memory/docs/assets/hero.svg` | |
| neck-diagram-studio | `neck-diagram-studio/docs/assets/hero.svg` | |
| zinwa-q25-keyboard | `zinwa-q25-keyboard/docs/assets/hero.svg` | |
| mastodon-agent | `assets/cv-heroes/mastodon-agent.png` | CV highlight; optional on projects broader section |
| iconoclast | Studio site branding or omit hero | Not a GitHub pin |

**Anti-pattern:** Regenerating new SVG banners via `scripts/inline-hero-logo.py` when repo or `cv-heroes` already has art.

---

## Verification commands

```sh
cd ~/Git/public/shahzebqazi.github.io

# Unit tests
python3 -m pip install -r tests/requirements.txt
python3 -m pytest tests/test_unit.py -q

# Live (after deploy to main)
python3 -m pytest tests/test_acceptance.py -q -m "not github_io"

# CV sync
diff <(curl -sL https://sqazi.sh/content/cv.txt) content/cv.txt

# Demo health (example)
for p in lambda-terminal mystic-ai mhn-ai-agent-memory neck-diagram-studio pa2-car-plugin; do
  printf "%s: " "$p"; curl -sI -o /dev/null -w "%{http_code}\n" "https://sqazi.sh/$p/"
done

# github.io redirect (after pages workflow)
curl -sL https://shahzebqazi.github.io/ | head -5
```

---

## Guardrails for the agent

1. **Facts** — Do not invent employers, dates, metrics, or repos. Ask operator if missing.
2. **SWE-only CV** — No mastering-shop lead on public CV; link iconoclastaud.io for audio.
3. **Single deploy path** — Content changes here; infra in `my-servers/moons/sol/`.
4. **No new AI slop art** — Reuse vendored/repo art only.
5. **Minimal diff** — No unrelated refactors; no new markdown files unless this handoff is updated.
6. **Commits** — Only when operator asks; otherwise branch + summary ready to commit.
7. **Project board** — Log tasks on [Project #14](https://github.com/users/shahzebqazi/projects/14).

---

## Suggested PR split

| PR | Scope |
|----|--------|
| 1 | CV dedupe, outcomes, education year, image compress, cv.txt sync |
| 2 | Projects featured reorder + hero art swap + remove uxui slop |
| 3 | SEO meta/canonical/OG in `content.html` shell |
| 4 | (my-servers) S3 prefix sync for demo URLs |

---

## Open questions for operator

Resolved 2026-06-02: (1) TMU **2022**; (2) work auth line **yes** — “Authorized to work in Canada”; (3) mastodon highlight **yes**; (4) uxui **dropped**; (5) SEO titles **Software Engineer + AI Engineer**; (6) mastodon hero **WebP** (`mastodon-agent.webp`, ~66 KB).

---

## References

- AWS cutover / 403 incident: `my-servers/docs/handoff/alerts/2026-06-01-lambda-terminal-down.md`
- DNS: `my-servers/docs/DNS.md`
- Prior audit: `docs/BRANDING_AUDIT_TASKS.md`
- mystic brand pipeline: `mystic-ai/docs/employer/case-brand-pipeline.md`
- Horde hero origin: `my-mac-config/README.md` (private; art vendored in site repo)
