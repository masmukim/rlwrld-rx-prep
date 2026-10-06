"""Save a web page or PDF as plain text so agents can Grep the original wording.

usage: .venv/bin/python .claude/skills/source-read/fetch.py <url> <out.txt>
Prints only a short status line; read the file with Grep/Read afterwards.
"""
import datetime
import io
import logging
import os
import re
import sys
import urllib.request
from html.parser import HTMLParser

UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"
SKIP = {"script", "style", "noscript", "svg", "nav", "footer", "header", "form"}
BLOCK = {"p", "div", "br", "li", "tr", "h1", "h2", "h3", "h4", "h5", "h6", "section", "article", "table", "pre", "blockquote"}


class Text(HTMLParser):
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP:
            self.skip += 1
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_endtag(self, tag):
        if tag in SKIP and self.skip:
            self.skip -= 1
        elif tag in BLOCK:
            self.out.append("\n")

    def handle_data(self, data):
        if not self.skip:
            self.out.append(data)


def to_text(body, ctype):
    if "pdf" in ctype or body[:5] == b"%PDF-":
        from pypdf import PdfReader  # installed in .venv
        logging.getLogger("pypdf").setLevel(logging.ERROR)  # font warnings only add noise
        return "\n".join(p.extract_text() or "" for p in PdfReader(io.BytesIO(body)).pages)
    charset = re.search(r"charset=([\w-]+)", ctype)
    html = body.decode(charset.group(1) if charset else "utf-8", errors="replace")
    p = Text()
    p.feed(html)
    text = "".join(p.out)
    return re.sub(r"\n\s*\n+", "\n\n", re.sub(r"[ \t]+", " ", text)).strip()


def main(url, out):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept-Language": "ko,en;q=0.9,ja;q=0.8"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            body, ctype = r.read(), r.headers.get("Content-Type", "")
    except Exception as e:  # 403, DNS, timeout: report and let the agent fall back
        print(f"FAIL {url} {e}")
        return 1
    try:
        text = to_text(body, ctype)
    except Exception as e:  # encrypted or broken PDF, bad encoding
        print(f"FAIL {url} could not extract text: {type(e).__name__}")
        return 1
    if len(text) < 500:
        print(f"FAIL {url} only {len(text)} chars (JS-rendered or blocked page)")
        return 1
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(f"URL: {url}\nFETCHED: {datetime.date.today()}\n\n{text}\n")
    print(f"OK {out} {text.count(chr(10)) + 1} lines {len(text)} chars")
    return 0


if __name__ == "__main__":
    sys.exit(main(*sys.argv[1:3]))
