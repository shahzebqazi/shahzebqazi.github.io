# Handoff — link coverage (sqazi.sh portfolio)

**Status:** Copy fixes on `main` (`fdae1c4`) · S3 demo prefixes still **403** — infra: [`my-servers` alert](https://github.com/shahzebqazi/my-servers/blob/main/docs/handoff/alerts/2026-06-02-sqazi-demo-prefixes-403.md) + `moons/sol/scripts/sync-project-prefixes.sh`  
**Audit artifact:** [`link-audit-2026-06-02.md`](link-audit-2026-06-02.md)  
**Related:** [`HANDOFF-CV-PROJECTS-EMPLOYABILITY.md`](HANDOFF-CV-PROJECTS-EMPLOYABILITY.md) Phase 4 · [`my-servers` lambda-terminal alert](https://github.com/shahzebqazi/my-servers/blob/main/docs/handoff/alerts/2026-06-01-lambda-terminal-down.md)

---

## Goal

**100% working links** in user-facing deploy set: `index.html`, `content/projects.html`, `content/cv.txt`, `content.html` shell + `assets/js/plain-content.js`, and CV browser view. Docs/README tracked for sync; not deployed to S3.

---

## Policy (canonical)

| Surface | Rule |
|---------|------|
| **Deployed HTML / `content/*`** | Prefer `https://sqazi.sh/<project>/` for live demos **when prefix returns 200**. Until then: **GitHub repo**, **tree/blob paths**, or **README anchors** — never `403`/`404` hrefs. |
| **`shahzebqazi.github.io` in deployed copy** | **Avoid** per [`AGENTS.md`](../../AGENTS.md). Per-repo Pages may exist; link from **GitHub README** (e.g. benchmark `#public-report`) or restore via S3 mirror. |
| **`content/cv.txt`** | GitHub + sqazi CV URLs only; no `sqazi.sh/<demo>/` (cleaned 2026-06-02). |
| **Phone** | Must not appear on public site. |
| **Infra** | `my-servers` moon Sol: `aws s3 sync` project build output → `s3://…/<prefix>/` + CloudFront subpath index function. |

---

## Resolutions applied (2026-06-02)

| Was (broken) | Now (deployed) | Strategy | Owner |
|--------------|----------------|----------|-------|
| `sqazi.sh/lambda-terminal/` (403) | `github.com/.../lambda-terminal/tree/main/docs/review` | **B** copy | site ✓ |
| `github.com/.../benchmark-euterpea/tree/main/report` (404) | `.../benchmark-euterpea/blob/main/README.md#public-report` | **B** copy | site ✓ |
| `sqazi.sh/iconoclast-vst-ui/` (403) | `iconoclastaud.io` studio hub + VST mockups link; demo prefix renamed **`vst-ui/`** | **C** remove old prefix | site ✓ |
| `sqazi.sh/neck-diagram-studio/`, `pa2-car-plugin/` on home (403) | GitHub repo links only | **B** copy | site ✓ |
| `sqazi.sh/mhn-ai-agent-memory/` in README | `github.com/.../mhn-ai-agent-memory` | **B** copy | site ✓ |
| All `sqazi.sh/<demo>/` prefixes | Still **403** | **A** infra | **my-servers** |

**Operator decision (optional):** After S3 sync, revert demo links to `https://sqazi.sh/<prefix>/` and re-run probe. For benchmark interactive report, either mirror to `sqazi.sh/benchmark-euterpea/` or add a **documented** `github.io` exception in `AGENTS.md` (not done — README anchor used instead).

---

## S3 sync checklist (Phase 4 — `my-servers`)

Sync source → S3 prefix (re-probe until 200):

| Prefix | Likely source on disk | GitHub Pages fallback (200 today) |
|--------|----------------------|-----------------------------------|
| `lambda-terminal/` | `~/Git/public/lambda-terminal/docs/review` | `shahzebqazi.github.io/lambda-terminal/` |
| `benchmark-euterpea/` | `~/Git/public/benchmark-euterpea/docs/site/dist` | `shahzebqazi.github.io/benchmark-euterpea/` |
| `pa2-car-plugin/` | PowerAmpache2 Pages artifact path (confirm in repo) | `shahzebqazi.github.io/pa2-car-plugin/` |
| `neck-diagram-studio/` | `~/Git/public/neck-diagram-studio/frontend/out` | `shahzebqazi.github.io/neck-diagram-studio/` |
| `mhn-ai-agent-memory/` | repo `docs/` or Pages path | `shahzebqazi.github.io/mhn-ai-agent-memory/` |
| `mystic-ai/` | mystic-ai Pages path | `shahzebqazi.github.io/mystic-ai/` |
| `vst-ui/` | `~/Git/private/Iconoclast/iconoclast` @ branch **`iconoclast-vst-ui`** (static `index.html` at repo root) | — |
| ~~`iconoclast-vst-ui/`~~ | **Obsolete** — merged into `iconoclast`; standalone repo deleted | — |

Example (lambda-terminal, from incident doc):

```sh
BUCKET=sqazi-sh-sol-prod-700890257515  # confirm via terraform output
SRC=~/Git/public/lambda-terminal/docs/review
aws s3 sync "${SRC}/" "s3://${BUCKET}/lambda-terminal/" --delete
aws cloudfront create-invalidation --distribution-id <ID> --paths "/lambda-terminal/*"
```

**Note:** lambda-terminal was synced 2026-06-01 then **403 again** on 2026-06-02 — verify bucket objects and OAC before re-audit.

---

## CV ↔ projects anchors

`assets/js/plain-content.js` `GITHUB_REPO_ANCHOR` must match every `id="project-*"` on featured/broader cards linked from `cv.txt`:

| Repo slug | Card `id` |
|-----------|-----------|
| `lambda-terminal` | `project-lambda-terminal` |
| `benchmark-euterpea` | `project-benchmark-euterpea` |
| `cursor-agents` | `project-cursor-agents` |
| `mhn-ai-agent-memory` | `project-mhn-ai-agent-memory` |
| `dotfiles` | `project-dotfiles` |
| `PowerAmpache2PluginTemplate` | `project-power-ampache-2` |
| `neck-diagram-studio` | `project-neck-diagram-studio` |
| `mystic-ai` | `project-mystic-ai` |
| `zinwa-q25-keyboard` | `project-zinwa-q25-keyboard` |

---

## Verification (repeat after deploy / S3 sync)

```sh
cd ~/Git/public/shahzebqazi.github.io
python3 -m pytest tests/test_unit.py tests/test_links.py -q -m "not github_io"

diff <(curl -sL https://sqazi.sh/content/cv.txt) content/cv.txt

for p in lambda-terminal pa2-car-plugin vst-ui neck-diagram-studio mhn-ai-agent-memory mystic-ai benchmark-euterpea; do
  printf "sqazi.sh/%s: " "$p"
  curl -sI -o /dev/null -w "%{http_code}\n" -L "https://sqazi.sh/$p/"
done

rg -n 'shahzebqazi\.github\.io' index.html content.html content/ assets/js/plain-content.js \
  && echo "FAIL: github.io in deployed paths" || echo "OK"

rg -n 'sqazi\.sh/[a-z]' index.html content/projects.html content/cv.txt
```

---

## For the next agent

1. Do **not** re-extract URLs from scratch — refresh [`link-audit-YYYY-MM-DD.md`](link-audit-2026-06-02.md) only when copy or infra changes.
2. If operator approves S3 work, run sync in `my-servers` then flip hrefs back to `sqazi.sh/<prefix>/` where 200.
3. **iconoclast-vst-ui** — resolved 2026-06-02: merged into **`shahzebqazi/iconoclast`** branch `iconoclast-vst-ui`; standalone repo deleted; S3 prefix **`vst-ui/`** (sync from private checkout — see `my-servers` alert).
4. Site copy + handoffs committed 2026-06-02; re-probe after S3 sync before restoring `sqazi.sh/<prefix>/` hrefs.
