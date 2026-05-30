# Keeping Everything in Sync

**Branding map:** [`docs/BRANDING.md`](docs/BRANDING.md) — sqazi.sh is the **canonical CV** (`content/cv.txt`); shahzeb.me is the link hub; LinkedIn/tailored CVs derive from the reference CV.

Three things share your bio and need to stay consistent:

| Surface | Repo | What renders |
|---|---|---|
| **GitHub profile** | `shahzebqazi/shahzebqazi` | `README.md` → shown on github.com/shahzebqazi |
| **sqazi.sh (AWS)** | `shahzebqazi/my-website` (private) | `index.html` → S3 + CloudFront at sqazi.sh |
| **Dynamic content** | same repo, `/content/` | Projects: `content/projects.html`; Papers, CV, Blog: `content/*.txt` — fetched by `content.html?page=` |

---

## When you update your bio

1. Edit the `<main>` section in `index.html`.
2. Copy the same text (plain, no HTML) into `README.md` in the `shahzebqazi/shahzebqazi` repo.
3. Push both repos.

**Lane-A drift (2026-05-28):** Profile `shahzebqazi/README.md` is **SWE-first** (canonical 8, Catppuccin badges) per `docs/BRANDING.md`. Until P0-3 lands, `index.html` may still be audio-forward — align home lede to README/CV, then re-sync both surfaces.

## When you add a project, paper, blog post, or update your CV

1. Edit the relevant file in `/content/` (e.g. `content/projects.html` for the Projects page, or `content/papers.txt`, etc.).
2. Push `my-website` (merge to `main` deploys via GitHub Actions). No changes needed in the profile repo — those pages are only on the website.

## When you update links

Outbound links live in a **separate** repository (its own GitHub Pages site). Edit that repo’s HTML; keep **`links.html`** in this repo only if the redirect target URL changes (see below).

1. Edit the links site in its repository (not `my-website`).
2. If you want the same links on your GitHub profile, add them to the bottom of `README.md` in `shahzebqazi/shahzebqazi`.
3. Push the links repo and the profile repo as needed.

**Redirect in this repo:** `links.html` sends visitors to **`https://shahzeb.me/`** (repo `shahzebqazi/links`). Adjust the `meta refresh`, `link rel="canonical"`, and body link if the link-hub domain changes.

---

## Custom domain (sqazi.sh on AWS)

DNS and TLS are managed in **`my-servers`** ([`moons/sol/`](https://github.com/shahzebqazi/my-servers/tree/main/moons/sol)) — S3, CloudFront, ACM; `sqazi.sh` DNS usually stays on DigitalOcean.

See **[`docs/AWS_MIGRATION.md`](docs/AWS_MIGRATION.md)** for setup, cutover from GitHub Pages, and registrar nameserver changes.

---

## Quick reference

```sh
# push website changes (deploys to AWS on main)
cd ~/Git/Personal/shahzebqazi.github.io   # or my-website after rename
git add -A && git commit -m "update" && git push

# push profile README changes (clone once, then reuse)
cd ~/shahzebqazi
git add -A && git commit -m "sync bio" && git push
```
