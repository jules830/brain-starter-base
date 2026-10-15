---
name: wiki-lint
description: Validate the brain's structural integrity. Walks all pages in `wiki/` and surfaces violations — dangling wikilinks, missing required frontmatter fields, schema breakages, slug/filename mismatches, orphaned pages, type/directory mismatches, malformed YAML. Read-only — never auto-fixes; outputs a lint report to `_outputs/lint-report-YYYY-MM-DD.md` for the user to act on. Invoke manually ("lint the brain") or before any major ingest run.
---

# wiki-lint

Sanity check for the brain. Surfaces structural issues without fixing them — the user decides what to repair.

## When to invoke

The user says any of:
- "Lint the brain"
- "Check the wiki for issues"
- "Run a sanity check"
- "Is everything OK?"

Or invoke proactively after large ingest sessions (e.g., 5+ new pages in one session).

## Inputs

None. Walks all of `wiki/`.

## Pre-flight checks (HALT-don't-bootstrap)

1. **`wiki/` directory exists** with at least one page.
2. **`_outputs/` directory exists** for the lint report.
3. **`_system/schema.md` exists** for the schema reference.

If any check fails, surface the gap and stop.

## What gets checked

### 1. Dangling wikilinks

A wikilink `[[type-slug]]` where the target page doesn't exist (`wiki/<type>/<slug>.md` is missing).

Report:
- Source page (where the dangling link is)
- Target slug (what's missing)

### 2. Slug / filename mismatch

The page's `slug:` in frontmatter doesn't match its filename.

Example: `wiki/sources/source-paul-graham.md` with `slug: source-pg-essay`. The filename says one thing; the slug says another. Causes routing issues.

### 3. Type / directory mismatch

A page with `type: concept` living in `wiki/sources/`, or similar misplacement.

### 4. Missing required frontmatter fields

Per `_system/schema.md`, each type has required fields. Surface any page where a required field is missing or empty.

Required-by-type:
- `source`: `type`, `slug`, `source-type`, `title`, `created`
- `concept`: `type`, `slug`, `title`, `created`
- `project`: `type`, `slug`, `title`, `created`, `status`
- `person`: `type`, `slug`, `title`, `created`
- `synthesis`: `type`, `slug`, `title`, `created`, `composed-on`

### 5. Wikilink form violations

Wikilinks not in `[[type-slug]]` form. Examples:
- `[[leverage]]` (missing type prefix)
- `[[concept:leverage]]` (colon — wrong separator)
- `[[concept-Leverage]]` (uppercase in slug)
- `[[concept-leverage|Leverage]]` (alias pipe — flag as recommend-against, not required-fix)

### 6. Orphaned pages

A page that has no inbound `mentioned-in:` AND no outbound `references:`. It's disconnected from the brain.

Surface orphans as low-priority warnings (not always wrong — could be a standalone reference).

### 7. Malformed YAML

Frontmatter that can't be parsed (broken indentation, unquoted strings with special chars, etc.).

### 8. `publish: true` without explicit user action

Any page with `publish: true` in frontmatter. Surface as informational — verify the user intended this.

## Output

A lint report at `_outputs/lint-report-YYYY-MM-DD.md`:

```markdown
# Lint report — YYYY-MM-DD

## Summary

- N total pages scanned
- X errors (must-fix)
- Y warnings (should-fix)
- Z info (review)

## Errors

### Dangling wikilinks (N found)

#### wiki/sources/source-pg-essay-2026-06-09.md
- `[[concept-recruiting-by-hand]]` — target page missing

#### wiki/concepts/concept-leverage.md
- `[[source-archimedes-quote]]` — target page missing

### Slug / filename mismatches (N found)

#### wiki/sources/source-pg-essay-2026-06-09.md
- Filename says `source-pg-essay-2026-06-09`; frontmatter slug says `source-paul-graham-essay`

### Missing required frontmatter (N found)

#### wiki/projects/project-q3-launch.md
- Missing field: `status`

## Warnings

### Wikilink form violations (N found)

#### wiki/sources/source-x.md
- `[[leverage]]` should be `[[concept-leverage]]`

### Orphaned pages (N found)

- `wiki/concepts/concept-isolated-idea.md` — no inbound or outbound links

## Info

### Pages with `publish: true` (N found)

- `wiki/sources/source-my-published-essay.md`
```

## Read-only — never auto-fixes

This skill ONLY produces the report. The user decides what to repair.

For repairs:
- Dangling wikilinks: user either creates the missing page or removes the link.
- Slug/filename mismatch: user fixes one or the other.
- Missing frontmatter: user adds the field.
- Wikilink form violations: user reformats.

If the user asks "fix all of these for me," do the fixes one at a time, showing each change in chat before applying. Do NOT batch auto-fix.

## Hard rules

1. **Never auto-fix.** Report only.
2. **Read-only across `wiki/` and `raw/`.** Write only to `_outputs/`.
3. **Surface, don't lecture.** Each finding gets one line. The user reads the report and acts.

## Skill version

v0.1 — brain-starter starter kit. Trimmed from Yoda's wiki-lint v0.5 (no deal-page hygiene rules, no topic-aggregates discipline, no schema-v0.5 specific checks — just the 8 universal checks above).
