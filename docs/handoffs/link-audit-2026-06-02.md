# Link audit — 2026-06-02

**Repo:** `shahzebqazi.github.io` · **Probe:** `curl -sI -L` · **LinkedIn:** treat `999` as skip  
**Deploy trio** (`index.html`, `content/projects.html`, `content/cv.txt`): all **href targets 200** after copy fix (2026-06-02).

Companion handoff: [`HANDOFF-LINK-COVERAGE.md`](HANDOFF-LINK-COVERAGE.md)

## Summary

| Class | Count | Notes |
|-------|-------|-------|
| URLs in inventory files | 114 row refs, 41 unique | |
| Non-200 in deploy **hrefs** | 0 | sqazi demo prefixes still 403 if probed directly (infra) |

## Inventory

| source_file | line | url | HTTP | intended target | fix_owner |
|-------------|------|-----|------|-----------------|-----------|
| `content/cv.txt` | 3 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `content/cv.txt` | 3 | `https://github.com/shahzebqazi` | 200 | source repo / docs | external |
| `content/cv.txt` | 3 | `https://www.linkedin.com/in/lambdaqazi` | 999 (skip) | LinkedIn profile | external |
| `content/cv.txt` | 30 | `https://github.com/shahzebqazi/PowerAmpache2PluginTemplate` | 200 | source repo / docs | external |
| `content/cv.txt` | 36 | `https://www.iconoclastaud.io/` | 200 | studio site | external |
| `content/cv.txt` | 46 | `https://github.com/shahzebqazi/lambda-terminal` | 200 | source repo / docs | external |
| `content/cv.txt` | 49 | `https://github.com/shahzebqazi/benchmark-euterpea` | 200 | source repo / docs | external |
| `content/cv.txt` | 52 | `https://github.com/shahzebqazi/cursor-agents` | 200 | source repo / docs | external |
| `content/cv.txt` | 55 | `https://github.com/shahzebqazi/mhn-ai-agent-memory` | 200 | source repo / docs | external |
| `content/cv.txt` | 58 | `https://github.com/shahzebqazi/dotfiles` | 200 | source repo / docs | external |
| `content/cv.txt` | 65 | `https://github.com/shahzebqazi/neck-diagram-studio` | 200 | source repo / docs | external |
| `content/cv.txt` | 68 | `https://github.com/shahzebqazi/mystic-ai` | 200 | source repo / docs | external |
| `content/cv.txt` | 68 | `https://github.com/shahzebqazi/mystic-ai#readme` | 200 | source repo / docs | external |
| `content/cv.txt` | 71 | `https://github.com/shahzebqazi/zinwa-q25-keyboard` | 200 | source repo / docs | external |
| `content/cv.txt` | 83 | `https://github.com/shahzebqazi` | 200 | source repo / docs | external |
| `content/cv.txt` | 83 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `content/projects.html` | 2 | `content.html?page=cv` | — | on-site page | site |
| `content/projects.html` | 2 | `https://github.com/shahzebqazi` | 200 | source repo / docs | external |
| `content/projects.html` | 8 | `https://github.com/shahzebqazi/lambda-terminal` | 200 | source repo / docs | external |
| `content/projects.html` | 12 | `https://github.com/shahzebqazi/lambda-terminal` | 200 | source repo / docs | external |
| `content/projects.html` | 13 | `https://github.com/shahzebqazi/lambda-terminal/tree/main/docs/review` | 200 | source repo / docs | external |
| `content/projects.html` | 18 | `https://github.com/shahzebqazi/benchmark-euterpea` | 200 | source repo / docs | external |
| `content/projects.html` | 22 | `https://github.com/shahzebqazi/benchmark-euterpea` | 200 | source repo / docs | external |
| `content/projects.html` | 23 | `https://github.com/shahzebqazi/benchmark-euterpea/blob/main/README.md#public-report` | 200 | source repo / docs | external |
| `content/projects.html` | 28 | `https://github.com/shahzebqazi/cursor-agents` | 200 | source repo / docs | external |
| `content/projects.html` | 32 | `https://github.com/shahzebqazi/cursor-agents` | 200 | source repo / docs | external |
| `content/projects.html` | 38 | `https://github.com/shahzebqazi/mhn-ai-agent-memory` | 200 | source repo / docs | external |
| `content/projects.html` | 42 | `https://github.com/shahzebqazi/mhn-ai-agent-memory` | 200 | source repo / docs | external |
| `content/projects.html` | 43 | `https://github.com/shahzebqazi/mhn-ai-agent-memory#demo` | 200 | source repo / docs | external |
| `content/projects.html` | 48 | `https://github.com/shahzebqazi/dotfiles` | 200 | source repo / docs | external |
| `content/projects.html` | 52 | `https://github.com/shahzebqazi/dotfiles` | 200 | source repo / docs | external |
| `content/projects.html` | 58 | `https://github.com/shahzebqazi/PowerAmpache2PluginTemplate` | 200 | source repo / docs | external |
| `content/projects.html` | 62 | `https://github.com/shahzebqazi/PowerAmpache2PluginTemplate` | 200 | source repo / docs | external |
| `content/projects.html` | 75 | `https://www.iconoclastaud.io/` | 200 | studio site | external |
| `content/projects.html` | 79 | `https://www.iconoclastaud.io/` | 200 | studio site | external |
| `content/projects.html` | 85 | `https://github.com/shahzebqazi/mystic-ai` | 200 | source repo / docs | external |
| `content/projects.html` | 89 | `https://github.com/shahzebqazi/mystic-ai` | 200 | source repo / docs | external |
| `content/projects.html` | 90 | `https://github.com/shahzebqazi/mystic-ai` | 200 | source repo / docs | external |
| `content/projects.html` | 95 | `https://github.com/shahzebqazi/mastodon-agent` | 200 | source repo / docs | external |
| `content/projects.html` | 99 | `https://github.com/shahzebqazi/mastodon-agent` | 200 | source repo / docs | external |
| `content/projects.html` | 105 | `https://github.com/shahzebqazi/zinwa-q25-keyboard` | 200 | source repo / docs | external |
| `content/projects.html` | 109 | `https://github.com/shahzebqazi/zinwa-q25-keyboard` | 200 | source repo / docs | external |
| `content/projects.html` | 115 | `https://github.com/shahzebqazi/neck-diagram-studio` | 200 | source repo / docs | external |
| `content/projects.html` | 119 | `https://github.com/shahzebqazi/neck-diagram-studio` | 200 | source repo / docs | external |
| `content/projects.html` | 120 | `https://github.com/shahzebqazi/neck-diagram-studio` | 200 | source repo / docs | external |
| `index.html` | 8 | `https://fonts.googleapis.com` | 404 | Google Fonts CDN | external |
| `index.html` | 9 | `https://fonts.gstatic.com` | 404 | Google Fonts CDN | external |
| `index.html` | 10 | `https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600&display=swap` | 200 | Google Fonts CDN | external |
| `index.html` | 26 | `content.html?page=projects` | — | on-site page | site |
| `index.html` | 28 | `content.html?page=cv` | — | on-site page | site |
| `index.html` | 30 | `content.html?page=blog` | — | on-site page | site |
| `index.html` | 42 | `content.html?page=cv` | — | on-site page | site |
| `index.html` | 42 | `content.html?page=projects` | — | on-site page | site |
| `index.html` | 44 | `https://github.com/shahzebqazi/cursor-agents` | 200 | source repo / docs | external |
| `index.html` | 44 | `https://github.com/shahzebqazi/mhn-ai-agent-memory` | 200 | source repo / docs | external |
| `index.html` | 44 | `https://github.com/shahzebqazi/benchmark-euterpea` | 200 | source repo / docs | external |
| `index.html` | 44 | `https://github.com/shahzebqazi/dotfiles` | 200 | source repo / docs | external |
| `index.html` | 46 | `https://github.com/shahzebqazi/lambda-terminal` | 200 | source repo / docs | external |
| `index.html` | 46 | `https://github.com/shahzebqazi/lambda-terminal/tree/main/docs/review` | 200 | source repo / docs | external |
| `index.html` | 46 | `https://github.com/shahzebqazi/neck-diagram-studio` | 200 | source repo / docs | external |
| `index.html` | 46 | `https://github.com/shahzebqazi/PowerAmpache2PluginTemplate` | 200 | source repo / docs | external |
| `index.html` | 46 | `https://github.com/shahzebqazi/zinwa-q25-keyboard` | 200 | source repo / docs | external |
| `index.html` | 48 | `https://www.iconoclastaud.io/` | 200 | studio site | external |
| `index.html` | 50 | `mailto:code@sqazi.sh` | — | contact email | site |
| `index.html` | 50 | `https://social.devilplan.com/@willy` | 200 | external | external |
| `index.html` | 50 | `https://matrix.to/#/@metalmasteringengineer:matrix.org` | 200 | external | external |
| `index.html` | 50 | `https://www.instagram.com/kongposhmosh/` | 200 | external | external |
| `index.html` | 53 | `mailto:code@sqazi.sh?subject=Support` | — | contact email | site |
| `index.html` | 58 | `mailto:code@sqazi.sh` | — | contact email | site |
| `index.html` | 58 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `index.html` | 58 | `content.html?page=cv` | — | on-site page | site |
| `content/blog.txt` | 42 | `https://sqazi.sh/` | 200 | portfolio / CV | external |
| `content/blog.txt` | 42 | `https://sqazi.sh/links.html` | 200 | project demo prefix (S3) | external |
| `docs/BRANDING.md` | 3 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 13 | `content.html?page=cv` | — | on-site page | site |
| `docs/BRANDING.md` | 13 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 14 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 15 | `https://sqazi.sh/` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 16 | `content.html?page=projects` | — | on-site page | site |
| `docs/BRANDING.md` | 16 | `https://sqazi.sh/content.html?page=projects` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 17 | `https://github.com/shahzebqazi` | 200 | source repo / docs | external |
| `docs/BRANDING.md` | 18 | `https://shahzeb.me/` | 200 | link hub | external |
| `docs/BRANDING.md` | 19 | `https://sqazi.sh/links.html` | 200 | project demo prefix (S3) | external |
| `docs/BRANDING.md` | 20 | `https://www.linkedin.com/in/lambdaqazi` | 999 (skip) | LinkedIn profile | external |
| `docs/BRANDING.md` | 34 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 35 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 43 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 44 | `https://shahzebqazi.github.io` | 200 | external | external |
| `docs/BRANDING.md` | 45 | `https://github.com/shahzebqazi` | 200 | source repo / docs | external |
| `docs/BRANDING.md` | 46 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 47 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 49 | `https://shahzeb.me` | 200 | link hub | external |
| `docs/BRANDING.md` | 57 | `https://shahzeb.me/` | 200 | link hub | external |
| `docs/BRANDING.md` | 70 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/BRANDING.md` | 70 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 6 | `https://github.com/users/shahzebqazi/projects/14` | 404 | external | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 24 | `https://sqazi.sh` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 25 | `https://shahzebqazi.github.io` | 200 | external | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 45 | `https://sqazi.sh/` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 45 | `https://github.com/shahzebqazi/my-servers/blob/main/docs/handoff/alerts/2026-06-01-lambda-terminal-down.md` | 404 | source repo / docs | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 65 | `mailto:code@sqazi.sh` | — | contact email | site |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 104 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 138 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 138 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 139 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 183 | `content.html?page=` | — | on-site page | site |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 255 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 263 | `https://shahzebqazi.github.io/` | 200 | external | external |
| `docs/handoffs/HANDOFF-CV-PROJECTS-EMPLOYABILITY.md` | 276 | `https://github.com/users/shahzebqazi/projects/14` | 404 | external | external |
| `docs/BRANDING_AUDIT_TASKS.md` | 8 | `https://sqazi.sh/content/cv.txt` | 200 | portfolio / CV | external |
| `docs/BRANDING_AUDIT_TASKS.md` | 12 | `https://www.linkedin.com/in/lambdaqazi` | 999 (skip) | LinkedIn profile | external |
| `docs/BRANDING_AUDIT_TASKS.md` | 18 | `https://sqazi.sh/content.html?page=cv` | 200 | portfolio / CV | external |
| `docs/BRANDING_AUDIT_TASKS.md` | 28 | `https://sqazi.sh/content.html?page=projects` | 200 | portfolio / CV | external |
| `docs/BRANDING_AUDIT_TASKS.md` | 46 | `https://sqazi.sh/links.html` | 200 | project demo prefix (S3) | external |

## Probe log (unique URLs)

```text
404	https://fonts.googleapis.com
200	https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500&family=IBM+Plex+Sans:wght@400;600&display=swap
404	https://fonts.gstatic.com
200	https://github.com/shahzebqazi
200	https://github.com/shahzebqazi/PowerAmpache2PluginTemplate
200	https://github.com/shahzebqazi/benchmark-euterpea
200	https://github.com/shahzebqazi/benchmark-euterpea/blob/main/README.md#public-report
200	https://github.com/shahzebqazi/cursor-agents
200	https://github.com/shahzebqazi/dotfiles
200	https://github.com/shahzebqazi/lambda-terminal
200	https://github.com/shahzebqazi/lambda-terminal/tree/main/docs/review
200	https://github.com/shahzebqazi/mastodon-agent
200	https://github.com/shahzebqazi/mhn-ai-agent-memory
200	https://github.com/shahzebqazi/mhn-ai-agent-memory#demo
404	https://github.com/shahzebqazi/my-servers/blob/main/docs/handoff/alerts/2026-06-01-lambda-terminal-down.md
200	https://github.com/shahzebqazi/mystic-ai
200	https://github.com/shahzebqazi/mystic-ai#readme
200	https://github.com/shahzebqazi/neck-diagram-studio
200	https://github.com/shahzebqazi/zinwa-q25-keyboard
404	https://github.com/users/shahzebqazi/projects/14
200	https://matrix.to/#/@metalmasteringengineer:matrix.org
200	https://shahzeb.me
200	https://shahzeb.me/
200	https://shahzebqazi.github.io
200	https://shahzebqazi.github.io/
200	https://social.devilplan.com/@willy
200	https://sqazi.sh
200	https://sqazi.sh/
200	https://sqazi.sh/content.html?page=cv
200	https://sqazi.sh/content.html?page=projects
200	https://sqazi.sh/content/cv.txt
200	https://sqazi.sh/links.html
200	https://www.iconoclastaud.io/
200	https://www.instagram.com/kongposhmosh/
999	https://www.linkedin.com/in/lambdaqazi
```

## sqazi.sh demo prefixes (extra probe)

```text
403	https://sqazi.sh/lambda-terminal/
403	https://sqazi.sh/pa2-car-plugin/
403	https://sqazi.sh/iconoclast-vst-ui/
403	https://sqazi.sh/neck-diagram-studio/
403	https://sqazi.sh/mhn-ai-agent-memory/
403	https://sqazi.sh/mystic-ai/
403	https://sqazi.sh/benchmark-euterpea/
```
