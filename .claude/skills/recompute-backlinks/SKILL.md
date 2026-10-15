---
name: recompute-backlinks
description: Walk all pages in `wiki/`, find every forward relation (`references`, `reads-from`, etc.), and ensure the inverse relation (`mentioned-in`) is correctly populated on the target page. Produces a proposed diff to `_outputs/` first; user approves; then the skill applies. Read-only by default — never auto-modifies `wiki/` without explicit approval. Invoke after bulk ingest sessions, after manual wiki edits, or when wiki-lint flags backlink inconsistencies.
---

# recompute-backlinks

Keeps the brain's link graph consistent. When a `source` page references `[[concept-leverage]]`, the concept page should have `source-<name>` in its `mentioned-in:` field. This skill walks the brain and enforces that.

## When to invoke

The user says any of:
- "Recompute backlinks"
- "Fix the link graph"
- "Update mentioned-in fields"
- "Run backlinks"

Or invoke automatically after bulk ingest sessions (e.g., when 3+ new sources have been ingested in one session).

## Inputs

None. The skill walks the entire `wiki/` directory.

## Pre-flight checks (HALT-don't-bootstrap)

1. **`wiki/` directory exists** and has at least one page.
2. **`_outputs/` directory exists** for the proposed-diff file.
3. **`_system/schema.md` exists** for relation-vocabulary reference.

If any check fails, surface the gap and stop.

## Relation vocabulary

From `_system/schema.md`:

| Forward relation | Inverse |
|---|---|
| `references:` | `mentioned-in:` |
| `reads-from:` | `mentioned-in:` |

`evidenced-by:` is **user-only** — this skill does NOT touch that field.

## Algorithm

### 1. Walk `wiki/`

For each `.md` file under `wiki/<type>/<slug>.md`:
- Parse frontmatter.
- Note the page's `slug`.
- Note all forward-relation fields (`references`, `reads-from`).

### 2. Build the inverse map

For each forward relation `[[target-slug]]` found on a source page:
- Add `[[source-slug]]` to `target-slug`'s implied `mentioned-in:` list.

### 3. Compare implied vs actual

For each page, compare:
- **Implied `mentioned-in:`** — built from step 2
- **Actual `mentioned-in:`** — what's currently in the page's frontmatter

Surface differences as either:
- **Missing inverse** — page's actual `mentioned-in:` is missing an entry that should be there.
- **Stale inverse** — page's actual `mentioned-in:` has an entry that no source page actually references.

### 4. Write the proposed diff

Write to `_outputs/backlink-diff-YYYY-MM-DD.md`:

```markdown
# Backlink diff — YYYY-MM-DD

## Pages with missing inverse relations

### wiki/concepts/concept-leverage.md
- Add to `mentioned-in:`: `[[source-paul-graham-essay-2026-06-09]]`

### wiki/people/person-jane-smith.md
- Add to `mentioned-in:`: `[[source-team-standup-2026-06-09]]`

## Pages with stale inverse relations

### wiki/concepts/concept-fragility.md
- Remove from `mentioned-in:`: `[[source-deleted-old-essay]]` (source no longer references)

## Total changes proposed

- N pages with missing inverses
- M pages with stale inverses
```

### 5. Wait for user approval

Show the user the diff. Ask: "apply this diff to wiki/, or skip specific changes?"

When the user says "apply it" (or equivalent), update each page's frontmatter `mentioned-in:` field to match the implied state.

If the user says "skip <specific change>," exclude those from the apply pass.

## Hard rules

1. **Never modify `evidenced-by:`.** User-only field.
2. **Propose, don't auto-apply.** Diff to `_outputs/` first; wait for explicit user approval.
3. **Don't touch `raw/`.** Read-only across the whole brain.
4. **Preserve any frontmatter fields not in the relation vocabulary.** This skill only touches `mentioned-in:`.

## Skill version

v0.1 — brain-starter starter kit. Trimmed from Yoda's recompute-backlinks (no deal-type relations, no win-drivers / loss-drivers, no supersession backlinks — just the basic `references` ↔ `mentioned-in` and `reads-from` ↔ `mentioned-in` pairs).
