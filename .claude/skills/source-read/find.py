"""Search several saved source files at once and print only matching lines.

usage: .venv/bin/python .claude/skills/source-read/find.py '<regex>' <file> [<file> ...]
Case-insensitive. Prints at most MAX_HITS matches per file, each with one line
of context before and after, so a whole file never lands in the context window.
"""
import re
import sys

MAX_HITS = 15
CONTEXT = 1


def main(pattern, files):
    rx = re.compile(pattern, re.IGNORECASE)
    for path in files:
        try:
            lines = open(path, encoding="utf-8", errors="replace").read().splitlines()
        except OSError as e:
            print(f"=== {path}: {e.strerror}")
            continue
        hits = [i for i, line in enumerate(lines) if rx.search(line)]
        print(f"=== {path} ({len(hits)} matches, {len(lines)} lines)")
        shown = set()
        for i in hits[:MAX_HITS]:
            for j in range(max(0, i - CONTEXT), min(len(lines), i + CONTEXT + 1)):
                if j not in shown and lines[j].strip():
                    shown.add(j)
                    print(f"{j + 1}: {lines[j][:300]}")
        if len(hits) > MAX_HITS:
            print(f"... {len(hits) - MAX_HITS} more; narrow the pattern or Read with offset")
    return 0


if __name__ == "__main__":
    if len(sys.argv) < 3:
        sys.exit("usage: find.py '<regex>' <file> [<file> ...]")
    sys.exit(main(sys.argv[1], sys.argv[2:]))
