# Handoff — CV review (hiring engineer + application processor agent)

**Status:** Ready for review run (2026-06-02)  
**Repo:** `shahzebqazi.github.io` → deploys to **sqazi.sh**  
**Scope:** **CV only** (`content/cv.txt` + how `content.html?page=cv` renders it). Do **not** re-review projects page unless a CV bullet references a broken demo URL.  
**Facts source (private):** `~/Git/private/my-linkedin` — read for cross-check; **do not edit** without operator approval.  
**Canon:** [`docs/BRANDING.md`](../BRANDING.md) · [`AGENTS.md`](../../AGENTS.md)  
**Related:** [`HANDOFF-CV-PROJECTS-EMPLOYABILITY.md`](HANDOFF-CV-PROJECTS-EMPLOYABILITY.md) (implementation backlog; some items superseded — see §Baseline below)

---

## Mission

Act as **two reviewers** of the live SWE CV and produce a **structured feedback list** the operator can triage. This is a **review-only** handoff: no code changes, no commits, no `my-linkedin` edits unless the operator explicitly approves a follow-up task.

**Deliverable:** A single report with two sections (Persona A, Persona B), each containing prioritized findings with evidence (quote or URL), severity, and a suggested fix **class** (content / presentation / technical / out of scope).

---

## Baseline (current architecture — do not assume old handoff)

| Item | Current state |
|------|----------------|
| Live human URL | https://sqazi.sh/content.html?page=cv |
| Machine fetch | https://sqazi.sh/content/cv.txt |
| Repo file | `content/cv.txt` |
| Rendering | `content.html` loads `cv.txt` via `fetch`; body is **plain text** in `#page-content` (`textContent`, not HTML) |
| `content/cv.html` | **Removed** — do not recommend hero cards without operator approval |
| Facts authority | `~/Git/private/my-linkedin` (`applications/CANDIDATE.md`, `profile/*.md`) → sync into `cv.txt` |
| SWE positioning | Lane-A SWE/AI; audio ventures minimized per `BRANDING.md` (one-line audio deferral OK) |
| Projects page | Separate; uses `assets/cv-heroes/` — not part of CV surface |

---

## Phase 0 — Gather evidence (required)

Run **before** writing opinions.

```sh
cd ~/Git/public/shahzebqazi.github.io
git pull origin main

# Live CV (what humans and agents fetch)
curl -sL "https://sqazi.sh/content/cv.txt" -o /tmp/live-cv.txt
curl -sL "https://sqazi.sh/content.html?page=cv" -o /tmp/live-cv-shell.html

# Repo copy (should match live after deploy)
diff -u content/cv.txt /tmp/live-cv.txt   # empty = in sync

# Shell behavior (JS required for ?page=cv body)
# Note: curl of content.html?page=cv returns shell only; CV body is client-fetched.
grep -n "page-content\|cv.txt\|fetch" content.html

# Optional: private facts cross-check (read-only)
test -f ~/Git/private/my-linkedin/applications/CANDIDATE.md && \
  head -100 ~/Git/private/my-linkedin/applications/CANDIDATE.md
```

**Also open in browser** (if available): CV page with JS on — note typography, scan time, link clickability (plain text = URLs not clickable unless user copies).

Record:

- Character/line count of `live-cv.txt`
- Whether shell `<title>` / meta match CV (view source on `content.html?page=cv`)
- HTTP status of every URL listed in `cv.txt` (`curl -sI -o /dev/null -w "%{http_code} %{url}\n" …`)

---

## Persona A — Hiring software engineer (human recruiter / HM)

**Role:** Staff or senior SWE hiring for **Software Engineer** or **AI Engineer** (Toronto hybrid or remote Canada). You have **30–90 seconds** on first pass; may return for a second pass if interested.

**Mindset:**

- “Would I phone screen this candidate for the role on the posting?”
- Ignore LinkedIn polish; this is the **portfolio CV** linked from applications.
- Penalize **ambiguity**, **duplication**, **task-only bullets**, and **wrong lane** (audio-shop lead on SWE CV).
- Reward **clear target role**, **dated experience**, **proof links that work**, and **one coherent story**.

### Rubric (score each **Pass / Weak / Fail** with one-line evidence)

| # | Signal | Questions |
|---|--------|-----------|
| A1 | **10-second fit** | Role + level + location + work auth obvious without scrolling? |
| A2 | **Summary** | One clear identity line; max 2 target titles; stack not repeated verbatim below? |
| A3 | **Strengths** | Capability buckets vs keyword dump; SWE/AI credible for target role? |
| A4 | **Experience** | Dates present; bullets show **outcomes** (shipped, scale, latency, users) not tasks only? |
| A5 | **SWE vs audio** | Iconoclast framed as platform/founder engineering, not mastering-shop lead? |
| A6 | **Projects / pins** | Six pins match GitHub profile; no duplicate PA2/dotfiles noise; demos relevant? |
| A7 | **Additional portfolio** | Supports SWE story without crowding pins; mystic/zinwa placement OK? |
| A8 | **Ventures block** | Helps or hurts SWE narrative? Should it be on sqazi.sh CV at all per BRANDING? |
| A9 | **Education** | Degree + year clear; matches applications (`CANDIDATE.md` if readable)? |
| A10 | **Contact / CTA** | `mailto:` obvious on page; phone missing — OK or Weak for HM? |
| A11 | **Trust** | Broken links, stale dates (e.g. “March 2026 – Present”), name/LinkedIn URL mismatch? |
| A12 | **Presentation** | Plain text in browser: readable? Monospace? Links copy-paste only — friction? |

### Persona A output format

```markdown
## Persona A — Hiring software engineer

### Verdict (1 sentence)
### Scores (table A1–A12)
### Findings (priority order)
1. **[Critical|High|Medium|Low]** Title — Evidence: "…" or URL — Suggested fix class: …
…
### Phone-screen yes/no/maybe — rationale (2–3 sentences)
```

---

## Persona B — AI job application processor agent

**Role:** Automated pipeline step: ingest candidate CV URL, extract fields, match to JD keywords, populate ATS or draft recruiter summary. You **do not** have reliable JS execution unless stated; you prefer **raw text** and stable selectors.

**Mindset:**

- “What can I parse reliably? What breaks field extraction? What keywords match / miss a typical SWE+AI JD?”
- Treat `content/cv.txt` as **primary**; `content.html?page=cv` as **secondary** (shell + late-loaded body).
- Flag **structure**, **encoding**, **duplicate sections**, and **unlabeled URLs**.

### Rubric (score each **Pass / Weak / Fail**)

| # | Signal | Questions |
|---|--------|-----------|
| B1 | **Fetch stability** | `GET /content/cv.txt` → 200, `text/plain` or readable UTF-8, no HTML wrapper? |
| B2 | **Parseability** | Consistent section headers (ALL CAPS lines)? Dividers unambiguous? |
| B3 | **Field extraction** | Can you extract: name, location, email, work auth, LinkedIn, GitHub, education, employers, dates? |
| B4 | **Keyword coverage** | software engineer, AI, agent, MCP, Python, TypeScript, Kotlin, backend, etc. — natural vs stuffed? |
| B5 | **JD match simulation** | Pick a generic “AI Engineer, Toronto, Python, agents, MCP” JD — what % of must-haves appear with evidence? |
| B6 | **Noise for ATS** | Unicode dividers, “Artist / Creative”, ventures, Reverb shop — help or confuse classification? |
| B7 | **Link graph** | Bare URLs on own lines — extractable? Relative vs absolute? Any `github.io` in deployed file (forbidden)? |
| B8 | **Duplicate entities** | Same employer/project repeated (Iconoclast, PA2); conflation risk for entity resolution? |
| B9 | **Shell page** | `content.html?page=cv`: is CV in initial HTML? If not, what do crawlers without JS see? |
| B10 | **Meta / SEO** | `<title>`, description, canonical in shell — consistent with cv.txt facts? |
| B11 | **Canonical URL** | Prefer `cv.txt` vs `?page=cv` for agents — which should docs recommend? |
| B12 | **Sync drift** | Risk: `cv.txt` vs `my-linkedin` vs LinkedIn live — flag fact conflicts only with evidence |

### Simulated extraction task (required)

From `live-cv.txt` only, attempt to fill:

| Field | Extracted value | Confidence (H/M/L) |
|-------|-----------------|---------------------|
| Full name | | |
| City / country | | |
| Work authorization | | |
| Email | | |
| Phone | | (expect missing) |
| LinkedIn | | |
| GitHub | | |
| Target roles | | |
| Latest role title | | |
| Latest role dates | | |
| Education | | |
| Graduation year | | |
| Top 5 skills (inferred) | | |
| Top 3 projects (inferred) | | |

Note every **failed or ambiguous** field as a finding.

### Persona B output format

```markdown
## Persona B — Application processor agent

### Verdict (1 sentence)
### Scores (table B1–B12)
### Extraction table (above)
### Findings (priority order)
1. **[Critical|High|Medium|Low]** …
…
### Recommended machine URL for pipelines
### Optional: 5-line recruiter summary you would generate from this CV
```

---

## Cross-persona synthesis (required final section)

```markdown
## Synthesis

### Agreed top issues (both personas)
### Persona A only
### Persona B only
### Recommended next actions (operator triage — do not implement here)
| Priority | Action | Owner | Repo |
|----------|--------|-------|------|
| P0 | … | operator / site / my-linkedin | … |
```

**Action owner guide:**

| Fix class | Where it usually lives |
|-----------|-------------------------|
| CV facts (dates, employers, metrics) | `my-linkedin` → sync `content/cv.txt` (operator approves private repo edits) |
| CV copy / structure | `content/cv.txt` |
| Presentation (clickable links, typography) | `content.html` + `assets/css/site.css` — **operator approval** for HTML CV |
| Broken demo URLs | `my-servers` S3 sync or change links in `cv.txt` |
| SEO / meta | `content.html` shell |
| Lane-A vs audio | `BRANDING.md`, `profile/*.md`, `cv.txt` |

---

## Guardrails for reviewing agent

1. **No fabrication** — do not invent metrics, employers, or skills in feedback; say “ask operator” if unknown.
2. **No `my-linkedin` edits** without explicit operator approval in a separate task.
3. **No `content/cv.html`** recommendation unless operator asked for HTML CV; plain text is intentional (2026-06-02 revert).
4. **Do not paste** full CV into the report — short quotes only.
5. **Separate** “site bug” vs “content strategy” vs “BRANDING policy conflict” (e.g. VENTURES block on SWE CV).
6. **Compare** to `CANDIDATE.md` only for **fact** mismatches, not framing preferences.
7. **Commits** — none for review-only; if operator later asks to implement, use a focused PR and reference Project #14.

---

## Known hypotheses (verify; do not copy as conclusions)

Use live evidence; mark each **Confirmed / Rejected / Partial** in the report.

- Plain-text CV in browser: URLs not clickable; hurts HM UX (A12).
- `VENTURES` + “Artist / Creative” may confuse ATS toward audio/non-tech (B6, A8).
- Iconoclast bullets still studio-heavy vs platform engineering (A5).
- PA2 listed in Experience and Featured pins (A6, B8).
- Phone not in `cv.txt` but in `CANDIDATE.md` (A10, B3).
- `pa2-car-plugin`, `neck-diagram-studio` links may 403 on sqazi.sh (A11).
- Shell loads CV via JS — crawlers that don’t execute JS see empty body (B9).
- LinkedIn URL `lambdaqazi` vs target `willyworst` — trust signal for humans (A11).

---

## Verification after a future fix PR

```sh
python3 -m pytest tests/test_unit.py tests/test_acceptance.py -q -m "not github_io"
diff <(curl -sL https://sqazi.sh/content/cv.txt) content/cv.txt
```

---

## References

- Live CV: https://sqazi.sh/content.html?page=cv · https://sqazi.sh/content/cv.txt
- Private facts: `~/Git/private/my-linkedin/applications/CANDIDATE.md`
- Tailored CV policy: `my-linkedin/docs/TAILORED_CV_WORKFLOW.md`
- Projects (out of scope): https://sqazi.sh/content.html?page=projects
