#!/usr/bin/env node
/**
 * Regenerate projects.html from content/projects.html and papers/cv/blog from
 * content/*.txt. Run after editing those sources:
 *   node scripts/generate-content-pages.mjs
 */
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const root = path.join(__dirname, "..");
const contentDir = path.join(root, "content");
const site = "https://sqazi.sh";

const textPages = [
  {
    slug: "papers",
    title: "Papers",
    description:
      "Public writing and citations — papers and references on sqazi.sh.",
  },
  {
    slug: "cv",
    title: "CV",
    description:
      "CV and professional overview — software, Haskell, and contact on sqazi.sh.",
  },
  {
    slug: "blog",
    title: "Blog",
    description: "Blog — long-form posts and notes on sqazi.sh.",
  },
];

const projectsMeta = {
  slug: "projects",
  title: "Projects",
  description:
    "GitHub Pages portfolio — programming, AI, music, Linux, and games.",
};

function escapeHtml(s) {
  return s
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;");
}

function navHtml() {
  return `<nav>
<a href="index.html">Home</a> /
<a href="links.html">Links</a> /
<a href="projects.html">Projects</a> /
<a href="papers.html">Papers</a> /
<a href="cv.html">CV</a> /
<a href="blog.html">Blog</a>
</nav>`;
}

function shellHtml({ title, description, canonicalPath, mainInner }) {
  const canonical = `${site}/${canonicalPath}`;
  const ogTitle = `${title} — sqazi.sh`;
  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapeHtml(ogTitle)}</title>
<meta name="description" content="${escapeHtml(description)}">
<link rel="canonical" href="${canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="${canonical}">
<meta property="og:title" content="${escapeHtml(ogTitle)}">
<meta property="og:description" content="${escapeHtml(description)}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${escapeHtml(ogTitle)}">
<meta name="twitter:description" content="${escapeHtml(description)}">
</head>
<body>

<header>
<p><strong><a href="index.html">sqazi</a></strong></p>
</header>

${navHtml()}

<hr>

<main>
${mainInner}
</main>

<hr>

<footer>
<p>sqazi.sh</p>
</footer>

</body>
</html>
`;
}

function buildProjectsPage() {
  const fragmentPath = path.join(contentDir, "projects.html");
  const raw = fs.readFileSync(fragmentPath, "utf8");
  const styleMatch = raw.match(
    /<style id="projects-inline-style">[\s\S]*?<\/style>/
  );
  if (!styleMatch) {
    throw new Error("content/projects.html: expected <style id=\"projects-inline-style\">");
  }
  const divStart = raw.indexOf('<div class="projects-page">');
  if (divStart === -1) {
    throw new Error("content/projects.html: expected <div class=\"projects-page\">");
  }
  const divEnd = raw.lastIndexOf("</div>");
  const bodyInner = raw.slice(divStart, divEnd + 6);

  const p = projectsMeta;
  const canonicalPath = "projects.html";
  const ogTitle = `${p.title} — sqazi.sh`;
  const canonical = `${site}/${canonicalPath}`;

  return `<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>${escapeHtml(ogTitle)}</title>
<meta name="description" content="${escapeHtml(p.description)}">
<link rel="canonical" href="${canonical}">
<meta property="og:type" content="website">
<meta property="og:url" content="${canonical}">
<meta property="og:title" content="${escapeHtml(ogTitle)}">
<meta property="og:description" content="${escapeHtml(p.description)}">
<meta name="twitter:card" content="summary">
<meta name="twitter:title" content="${escapeHtml(ogTitle)}">
<meta name="twitter:description" content="${escapeHtml(p.description)}">
${styleMatch[0]}
</head>
<body>

<header>
<p><strong><a href="index.html">sqazi</a></strong></p>
</header>

${navHtml()}

<hr>

<main>
<h1>${escapeHtml(p.title)}</h1>
${bodyInner}
</main>

<hr>

<footer>
<p>sqazi.sh</p>
</footer>

</body>
</html>
`;
}

fs.writeFileSync(path.join(root, "projects.html"), buildProjectsPage(), "utf8");
console.log("Wrote projects.html");

for (const p of textPages) {
  const txtPath = path.join(contentDir, `${p.slug}.txt`);
  const bodyText = fs.readFileSync(txtPath, "utf8");
  const mainInner = `<h1>${escapeHtml(p.title)}</h1>
<pre id="page-content" aria-live="polite">${escapeHtml(bodyText)}</pre>`;
  const html = shellHtml({
    title: p.title,
    description: p.description,
    canonicalPath: `${p.slug}.html`,
    mainInner,
  });
  const outPath = path.join(root, `${p.slug}.html`);
  fs.writeFileSync(outPath, html, "utf8");
  console.log("Wrote", path.relative(root, outPath));
}
