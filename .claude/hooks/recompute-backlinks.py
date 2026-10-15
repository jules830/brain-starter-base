#!/usr/bin/env python3
"""Additive-only backlink recompute — wired as a Stop hook.

Walks wiki/ and ensures every forward relation (references / reads-from) has its
inverse (mentioned-in) on the target page. ADDITIVE ONLY: it adds missing
inverses silently; it NEVER removes anything. Entries that look stale (a
mentioned-in with no matching forward ref) are FLAGGED to _outputs/ for a human
to decide — because a "stale" link is often a real body mention the source just
didn't list in references.

Reads the Stop-hook JSON on stdin and ignores it. Exits 0 always so it never
blocks the turn from ending.
"""
import os, re, sys, glob, json

# Drain stdin (Stop hook payload) so we don't break the pipe; we don't need it.
try:
    sys.stdin.read()
except Exception:
    pass

ROOT = os.environ.get("CLAUDE_PROJECT_DIR") or os.path.dirname(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
)
WIKI = os.path.join(ROOT, "wiki")
OUTPUTS = os.path.join(ROOT, "_outputs")
FORWARD_FIELDS = ("references", "reads-from")

if not os.path.isdir(WIKI):
    sys.exit(0)

files = [f for f in glob.glob(os.path.join(WIKI, "**", "*.md"), recursive=True)
         if os.path.basename(f) != "README.md"]

def split_fm(path):
    txt = open(path).read()
    parts = txt.split("---\n")
    if len(parts) < 3:
        return None, None, txt
    return parts[1], "---\n".join(parts[2:]), txt

slug_path, forward, actual_mi = {}, {}, {}
for f in files:
    fm, _body, _ = split_fm(f)
    if fm is None:
        continue
    m = re.search(r"^slug:\s*(\S+)", fm, re.M)
    if not m:
        continue
    slug = m.group(1).strip()
    slug_path[slug] = f
    fwd, mi, cur = [], set(), None
    for line in fm.splitlines():
        h = re.match(r"^([\w-]+):", line)
        if h:
            cur = h.group(1)
        lk = re.search(r"\[\[([^\]]+)\]\]", line)
        if lk and cur:
            tgt = lk.group(1).strip()
            if cur in FORWARD_FIELDS:
                fwd.append(tgt)
            elif cur == "mentioned-in":
                mi.add(tgt)
    forward[slug] = fwd
    actual_mi[slug] = mi

implied = {s: set() for s in slug_path}
for src, tgts in forward.items():
    for t in tgts:
        implied.setdefault(t, set()).add(src)

added, stale = {}, {}
for slug, path in slug_path.items():
    miss = implied.get(slug, set()) - actual_mi.get(slug, set())
    extra = actual_mi.get(slug, set()) - implied.get(slug, set())
    if miss:
        added[slug] = sorted(miss)
    if extra:
        stale[slug] = sorted(extra)

# Apply additive fixes.
for slug, new in added.items():
    path = slug_path[slug]
    fm, body, _ = split_fm(path)
    lines = fm.splitlines()
    mi_idx = next((i for i, l in enumerate(lines) if re.match(r"^mentioned-in:", l)), None)
    add_lines = [f'  - "[[{e}]]"' for e in new]
    if mi_idx is not None:
        j = mi_idx + 1
        while j < len(lines) and lines[j].startswith("  -"):
            j += 1
        lines[j:j] = add_lines
    else:
        pub = next((i for i, l in enumerate(lines) if re.match(r"^publish:", l)), None)
        block = ["mentioned-in:"] + add_lines
        if pub is not None:
            lines[pub:pub] = block
        else:
            lines += block
    open(path, "w").write("---\n" + "\n".join(lines) + "\n---\n" + body)

# Flag stale (never remove). Write a report only if any exist.
if stale and os.path.isdir(OUTPUTS):
    report = os.path.join(OUTPUTS, "backlink-stale-flags.md")
    with open(report, "w") as fh:
        fh.write("# Backlink stale flags (NOT auto-removed)\n\n")
        fh.write("These `mentioned-in:` entries have no matching forward ref. "
                 "Often the source mentions the target in its body but didn't list "
                 "it in `references:`. Decide per case: add the forward ref, or remove "
                 "the backlink.\n\n")
        for slug in sorted(stale):
            fh.write(f"## {os.path.relpath(slug_path[slug], ROOT)}\n")
            for s in stale[slug]:
                fh.write(f"- `[[{s}]]` — no page lists this as a forward ref\n")
            fh.write("\n")

if added:
    n = sum(len(v) for v in added.values())
    print(f"[backlinks] added {n} missing inverse link(s) across {len(added)} page(s)")
if stale:
    print(f"[backlinks] flagged {len(stale)} page(s) with possible stale links -> _outputs/backlink-stale-flags.md")

sys.exit(0)
