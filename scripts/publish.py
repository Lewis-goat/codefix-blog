#!/usr/bin/env python3
"""Nightly publisher: takes the next bank/*.md, renders it as a static post,
regenerates index/RSS/sitemap, and removes the bank file. Deterministic, no deps.

Bank format (strict subset):
---
title: Post title
description: Meta description (<=155 chars)
---
## Heading
Paragraph with [link](https://codefixcoffee.com/...) and **bold**.
- bullet
1. step
"""
import os, re, sys, html, glob, datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BANK = os.path.join(ROOT, "bank")
POSTS = os.path.join(ROOT, "post")
HOST = "https://blog.codefixcoffee.com"

def esc(s): return html.escape(s, quote=False)

def inline(s: str) -> str:
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\((https?://[^)\s]+)\)", r'<a href="\2">\1</a>', s)
    s = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    return s

def render(md: str) -> str:
    out, in_ul, in_ol = [], False, False
    for line in md.splitlines():
        l = line.strip()
        if not l:
            if in_ul: out.append("</ul>"); in_ul = False
            if in_ol: out.append("</ol>"); in_ol = False
            continue
        if l.startswith("### "): out.append(f"<h3>{inline(l[4:])}</h3>"); continue
        if l.startswith("## "):  out.append(f"<h2>{inline(l[3:])}</h2>"); continue
        if l.startswith("- "):
            if not in_ul:
                if in_ol: out.append("</ol>"); in_ol = False
                out.append("<ul>"); in_ul = True
            out.append(f"<li>{inline(l[2:])}</li>"); continue
        m = re.match(r"^(\d+)\.\s+(.*)$", l)
        if m:
            if not in_ol:
                if in_ul: out.append("</ul>"); in_ul = False
                out.append("<ol>"); in_ol = True
            out.append(f"<li>{inline(m.group(2))}</li>"); continue
        out.append(f"<p>{inline(l)}</p>")
    if in_ul: out.append("</ul>")
    if in_ol: out.append("</ol>")
    return "\n".join(out)

def page(title: str, body: str, desc: str, canonical: str) -> str:
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc)}">
<link rel="canonical" href="{canonical}">
<link rel="stylesheet" href="/style.css">
<link rel="alternate" type="application/rss+xml" title="CodeFix Blog" href="/rss.xml">
</head>
<body>
<header class="site"><div class="in"><a class="brand" href="/">☕ CodeFix Blog</a><span><a href="https://codefixcoffee.com">Error-code database →</a></span></div></header>
<main>
{body}
</main>
<footer>CodeFix Blog — repair guides and appliance error-code explainers from <a href="https://codefixcoffee.com">codefixcoffee.com</a>.</footer>
</body></html>"""

def post_meta(path: str):
    src = open(path).read()
    m = re.match(r"^---\ntitle: (.+)\ndescription: (.+)\n---\n(.*)$", src, re.S)
    if not m: raise SystemExit(f"bad frontmatter in {path}")
    return m.group(1).strip(), m.group(2).strip(), m.group(3)

def main():
    bank_files = sorted(glob.glob(os.path.join(BANK, "*.md")))
    if not bank_files:
        print("::notice::bank empty")
        print("::set-output name=empty::true"); print("::set-output name=url::")
        return
    src_path = bank_files[0]
    # numeric prefix (001-) orders the bank but must not appear in the URL
    slug = re.sub(r"^\d+-", "", os.path.splitext(os.path.basename(src_path))[0])
    # publish date: file order defines date; use file mtime date in CI, else today
    date = datetime.date.today().isoformat()
    title, desc, body_md = post_meta(src_path)

    d = os.path.join(POSTS, slug)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.html"), "w") as f:
        f.write(page(title, f'<h1>{esc(title)}</h1>\n<p class="meta">{date}</p>\n{render(body_md)}', desc, f"{HOST}/post/{slug}/"))
    os.remove(src_path)

    # regenerate index + rss + sitemap from all published posts (date = dir mtimes are unreliable; store date file)
    with open(os.path.join(d, "date.txt"), "w") as f: f.write(date)
    entries = []
    for p in sorted(glob.glob(os.path.join(POSTS, "*", "index.html"))):
        s = os.path.dirname(p)
        sl = os.path.basename(s)
        t, de, _ = post_meta_from_html(open(p).read(), sl)
        dt = open(os.path.join(s, "date.txt")).read().strip() if os.path.exists(os.path.join(s, "date.txt")) else date
        entries.append((dt, sl, t, de))
    entries.sort(reverse=True)

    lst = "\n".join(f'<li><a href="/post/{sl}/">{esc(t)}</a><small>{dt} — {esc(de)}</small></li>' for dt, sl, t, de in entries)
    with open(os.path.join(ROOT, "index.html"), "w") as f:
        f.write(page("CodeFix Blog — coffee machine & appliance repair guides",
                     f"<h1>CodeFix Blog</h1>\n<p class=\"meta\">Repair explainers from the <a href=\"https://codefixcoffee.com\">codefixcoffee.com</a> error-code database.</p>\n<ul class=\"postlist\">\n{lst}\n</ul>",
                     "Nightly repair guides and error-code explainers for Jura, De'Longhi, Philips/Saeco, Miele, Nespresso, GE and Samsung appliances.", f"{HOST}/"))

    rss_items = "\n".join(
        f"<item><title>{esc(t)}</title><link>{HOST}/post/{sl}/</link><guid>{HOST}/post/{sl}/</guid><pubDate>{dt}</pubDate><description>{esc(de)}</description></item>"
        for dt, sl, t, de in entries[:20])
    with open(os.path.join(ROOT, "rss.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<rss version="2.0"><channel><title>CodeFix Blog</title><link>{HOST}/</link><description>Appliance repair guides and error-code explainers.</description>\n{rss_items}\n</channel></rss>')

    sm = "\n".join(f"<url><loc>{HOST}/post/{sl}/</loc><lastmod>{dt}</lastmod></url>" for dt, sl, t, de in entries)
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n<url><loc>{HOST}/</loc><lastmod>{date}</lastmod></url>\n{sm}\n</urlset>')

    print(f"published {slug}")
    print(f"::set-output name=title::{title}")
    print(f"::set-output name=url::{HOST}/post/{slug}/")
    print("::set-output name=empty::false")

def post_meta_from_html(doc: str, slug: str):
    t = re.search(r"<title>(.*?)</title>", doc).group(1)
    de = re.search(r'<meta name="description" content="([^"]*)"', doc).group(1)
    return t, de, None

if __name__ == "__main__":
    main()
