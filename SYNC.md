# Keeping Everything in Sync

Three things share your bio and need to stay consistent:

| Surface | Repo | What renders |
|---|---|---|
| **GitHub profile** | `shahzebqazi/shahzebqazi` | `README.md` → shown on github.com/shahzebqazi |
| **GitHub Pages / sqazi.sh** | `shahzebqazi/shahzebqazi.github.io` | `index.html` → served at shahzebqazi.github.io and sqazi.sh |
| **Dynamic content** | same repo, `/content/` | Projects: `content/projects.html`; Papers, CV, Blog: `content/*.txt` — fetched by `content.html?page=` |

---

## When you update your bio

1. Edit the `<main>` section in `index.html`.
2. Copy the same text (plain, no HTML) into `README.md` in the `shahzebqazi/shahzebqazi` repo.
3. Push both repos.

## When you add a project, paper, blog post, or update your CV

1. Edit the relevant file in `/content/` (e.g. `content/projects.html` for the Projects page, or `content/papers.txt`, etc.).
2. Push `shahzebqazi.github.io`. No changes needed in the profile repo — those pages are only on the website.

## When you update links

1. Edit `links/index.html` (served at `/links/` on every domain that points at this site, e.g. `https://sqazi.sh/links/` and `https://shahzeb.me/links/`).
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

## Custom domain setup (shahzeb.me on DigitalOcean)

The same GitHub Pages site can serve **multiple** custom domains. Add `shahzeb.me` in the repo **Settings → Pages → Custom domain** (in addition to `sqazi.sh` if it is already listed). The `CNAME` file in this repo can only list one primary hostname; extra domains are configured in the GitHub UI.

In the [DigitalOcean control panel](https://cloud.digitalocean.com/), open **Networking → Domains**, select `shahzeb.me`, and add the same DNS GitHub expects for a user site apex:

**Apex (shahzeb.me)** — four **A** records, hostname `@`, each pointing to one of:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Optional **www** — one **CNAME** record: hostname `www`, value `shahzebqazi.github.io.` (trailing dot optional depending on the UI).

After propagation, enable **Enforce HTTPS** for `shahzeb.me` in GitHub Pages settings if offered. The links page is then available at `https://shahzeb.me/links/` (same files as `https://sqazi.sh/links/`).

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
