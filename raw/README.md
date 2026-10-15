# `raw/` — your input layer

This is where you drop things into the brain. Claude reads from here but **never modifies**.

## What goes where

- **`raw/transcripts/`** — meeting transcripts. Export from Granola, Otter, Fireflies, Read.ai, Zoom, anything. Plain text (`.txt`, `.md`) or markdown files.
- **`raw/voice/`** — voice memos. Drop `.m4a`, `.mp3`, `.wav` files. Claude transcribes and ingests.
- **`raw/articles/`** — articles you've read and want to remember. Save as `.md`, `.txt`, or `.pdf`.

You can add more folders later (e.g., `raw/books/`, `raw/podcasts/`, `raw/screenshots/`). Just drop the file in and tell Claude where it is.

## How to ingest

Once a file is in `raw/`, in Claude Code say:

> "Ingest this for me."

Claude reads the file, drafts a `source` page in `_outputs/`, shows you the draft, and waits for your approval before moving it to `wiki/sources/`.

## Hard rule

**Claude never modifies anything in `raw/`.** This folder is immutable. If you want to update a transcript or article, edit it yourself.

This rule exists because `raw/` is your source of truth. If the AI could rewrite it, you'd lose the original. The brain's `wiki/` layer is regeneratable; `raw/` is not.
