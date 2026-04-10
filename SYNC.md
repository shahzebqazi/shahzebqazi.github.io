# Keeping Everything in Sync

Three things share your bio and need to stay consistent:

| Surface | Repo | What renders |
|---|---|---|
| **GitHub profile** | `shahzebqazi/shahzebqazi` | `README.md` → shown on github.com/shahzebqazi |
| **GitHub Pages / sqazi.sh** | `shahzebqazi/shahzebqazi.github.io` | `index.html` → served at shahzebqazi.github.io and sqazi.sh |
| **Dynamic content** | same repo, `/content/*.txt` | fetched by `content.html?page=` |

---

## When you update your bio

1. Edit the `<main>` section in `index.html`.
2. Copy the same text (plain, no HTML) into `README.md` in the `shahzebqazi/shahzebqazi` repo.
3. Push both repos.

## When you add a project, paper, blog post, or update your CV

1. Edit the relevant file in `/content/` (e.g. `content/projects.html` for the Projects page, or `content/papers.txt`, etc.).
2. Push `shahzebqazi.github.io`. No changes needed in the profile repo — those pages are only on the website.

## When you update links

1. Edit `links.html`.
2. If you want the same links on your GitHub profile, add them to the bottom of `README.md`.
3. Push both repos.

---

## Custom domain setup (sqazi.sh)

The `CNAME` file in this repo tells GitHub Pages to serve from `sqazi.sh`.
You still need to configure DNS with your registrar:

### Option A — Apex domain (sqazi.sh)

Add these A records pointing to GitHub's servers:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

### Option B — www subdomain (www.sqazi.sh)

Add a CNAME record:

```
www  CNAME  shahzebqazi.github.io.
```

### Option C — Both (recommended)

Add all four A records for the apex AND the www CNAME. GitHub will handle the redirect.

After DNS propagates (up to 24h), go to the repo Settings → Pages and check "Enforce HTTPS."

---

## Quick reference

```sh
# push website changes
cd "sqazi website."
git add -A && git commit -m "update" && git push

# push profile README changes (clone once, then reuse)
cd ~/shahzebqazi
git add -A && git commit -m "sync bio" && git push
```
