# `wiki/` — what your AI writes

This is where Claude stores your brain's structured knowledge.

You read this. You ask Claude questions about it. You curate (delete what's wrong, edit what needs improvement, ask Claude to merge duplicates).

**Claude writes here, but only after you approve a draft.** New content goes to `_outputs/` first as a draft. You read the draft, approve, then it moves to `wiki/`.

## Folders

- **`sources/`** — pages about things you ingested (articles, meetings, voice memos, books).
- **`projects/`** — pages about active work you're doing.
- **`concepts/`** — pages about distilled ideas, one per concept.
- **`people/`** — pages about people you work with or have talked about.
- **`syntheses/`** — Claude's multi-source write-ups citing your sources.
- **`decisions/`** — (optional, empty for now) pages about discrete decisions you've made.

## Schema

Each page type has a strict frontmatter + body shape. See `_system/schema.md` for the spec.

Filenames match the `slug:` in frontmatter. Example: `wiki/sources/source-paul-graham-essay-2026-06-09.md`.

## Wikilinks

Pages cite each other using `[[type-slug]]` form. Example: a source page might reference `[[concept-leverage]]` and `[[person-paul-graham]]`. Obsidian renders these as clickable links so you can navigate.

Open the graph view in Obsidian (left sidebar — looks like a constellation) to see your brain take shape.
