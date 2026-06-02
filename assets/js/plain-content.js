/**
 * Render plain .txt content with clickable links (CV, blog, papers).
 * cv.txt stays plain for machines; the browser view linkifies URLs.
 */
(function (global) {
  var GITHUB_REPO_ANCHOR = {
    "lambda-terminal": "project-lambda-terminal",
    "benchmark-euterpea": "project-benchmark-euterpea",
    "cursor-agents": "project-cursor-agents",
    "mhn-ai-agent-memory": "project-mhn-ai-agent-memory",
    dotfiles: "project-dotfiles",
    PowerAmpache2PluginTemplate: "project-power-ampache-2",
    "neck-diagram-studio": "project-neck-diagram-studio",
    "mystic-ai": "project-mystic-ai",
    "zinwa-q25-keyboard": "project-zinwa-q25-keyboard",
  };

  var URL_RE = /https?:\/\/[^\s<>"']+/g;
  var EMAIL_RE = /\bcode@sqazi\.sh\b/g;

  function trimUrlTrailingPunct(url) {
    return url.replace(/[.,;:)·]+$/g, "");
  }

  function hrefForUrl(url, opts) {
    if (!opts || !opts.linkGithubReposToProjects) return url;
    var m = url.match(
      /^https:\/\/github\.com\/shahzebqazi\/([^/#?]+)(?:[#?].*)?$/i
    );
    if (!m) return url;
    var anchor = GITHUB_REPO_ANCHOR[m[1]];
    if (!anchor) return url;
    return "content.html?page=projects#" + anchor;
  }

  function isExternal(href) {
    return /^https?:\/\//i.test(href) && href.indexOf(location.origin) !== 0;
  }

  function appendLink(parent, url, opts) {
    var href = hrefForUrl(url, opts);
    var a = document.createElement("a");
    a.href = href;
    a.textContent = url;
    if (isExternal(href)) {
      a.target = "_blank";
      a.rel = "noopener noreferrer";
    }
    parent.appendChild(a);
  }

  function appendSegment(parent, text, opts) {
    var last = 0;
    var combined = [];
    var m;

    EMAIL_RE.lastIndex = 0;
    while ((m = EMAIL_RE.exec(text)) !== null) {
      combined.push({ index: m.index, end: m.index + m[0].length, kind: "email" });
    }
    URL_RE.lastIndex = 0;
    while ((m = URL_RE.exec(text)) !== null) {
      combined.push({ index: m.index, end: m.index + m[0].length, kind: "url", raw: m[0] });
    }

    combined.sort(function (a, b) {
      return a.index - b.index;
    });

    if (combined.length === 0) {
      parent.appendChild(document.createTextNode(text));
      return;
    }

    for (var i = 0; i < combined.length; i++) {
      var hit = combined[i];
      if (hit.index < last) continue;
      if (hit.index > last) {
        parent.appendChild(document.createTextNode(text.slice(last, hit.index)));
      }
      if (hit.kind === "email") {
        var mail = document.createElement("a");
        mail.href = "mailto:code@sqazi.sh";
        mail.textContent = "code@sqazi.sh";
        parent.appendChild(mail);
      } else {
        var raw = hit.raw;
        var url = trimUrlTrailingPunct(raw);
        var trailing = raw.slice(url.length);
        appendLink(parent, url, opts);
        if (trailing) parent.appendChild(document.createTextNode(trailing));
      }
      last = hit.end;
    }

    if (last < text.length) {
      parent.appendChild(document.createTextNode(text.slice(last)));
    }
  }

  function renderInto(el, text, opts) {
    el.textContent = "";
    el.className = "page-content--plain";
    appendSegment(el, text, opts || {});
  }

  global.PlainContent = { renderInto: renderInto };
})(typeof window !== "undefined" ? window : globalThis);
