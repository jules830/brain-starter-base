# `_outputs/` — drafts before commit

This is where Claude puts drafts of new pages before they land in `wiki/`.

When you ingest a source, Claude writes the draft here first. You read it, decide if it's good, and tell Claude to commit it to `wiki/` (or ask Claude to revise it first).

This is the "output-before-write" discipline — you stay in control of what goes into your brain.

## Workflow

1. You drop a file in `raw/`.
2. Claude reads it, drafts a `wiki/sources/` page, writes the draft to `_outputs/<draft-name>.md`.
3. You read the draft. Approve, edit, or ask Claude to revise.
4. When you say "looks good, commit it," Claude moves the file from `_outputs/` to `wiki/sources/`.

## You can also use it for

- Anything Claude generates that isn't ready for `wiki/` — proposals, analysis files, summaries.
- Scratch space for Claude to think through something before writing the final.

## What to expect

Files in `_outputs/` accumulate. You can delete drafts that didn't end up in `wiki/`. Don't worry about clutter — it's the drafts folder.
