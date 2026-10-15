---
name: ingest-source
description: Ingest a raw source (article, transcript, voice memo, pasted text, URL) into the brain. Reads the raw file, drafts a `source` page to `_outputs/`, proposes new concept stubs + person stubs the source surfaces, and waits for user approval before any file moves to `wiki/`. Honors output-before-write, immutable `raw/`, and `publish: false` defaults. Invoke whenever the user says "ingest this," "add this to my brain," "process this for me," or drops a file in `raw/` and asks for it to be handled.
---

# ingest-source

The workhorse skill. Turns raw input (article, transcript, voice memo, URL, pasted text) into a structured `wiki/sources/<source-slug>.md` page.

## When to invoke

The user says any of:
- "Ingest this for me"
- "Add this to my brain"
- "Process this file"
- "Turn this into a source"
- Or drops a file in `raw/` and says "handle this"

If the user pastes text directly into chat instead of dropping a file, ingest the pasted text. Save the pasted text to `raw/<topic>/<topic>-<YYYY-MM-DD>.md` first so it has a stable file reference, then proceed.

## Inputs

ONE of:
1. **File path** in `raw/` — e.g., `raw/articles/paul-graham-essay-2026-06-09.md`. Default case.
2. **Pasted text** in chat. Save to `raw/articles/<topic>-<YYYY-MM-DD>.md` first.
3. **URL** — fetch the content, save to `raw/articles/<short-name>-<YYYY-MM-DD>.md`, then proceed.
4. **Voice memo** — `.m4a`, `.mp3`, `.wav` in `raw/voice/`. Transcribe first (use whatever transcription tool the user has available; if none, tell the user this version can't transcribe and ask them to provide a text version).

## Pre-flight checks (HALT-don't-bootstrap)

Before drafting:

1. **The raw file exists** at the path the user gave (or you stored). If not, tell the user the path is wrong and stop.
2. **`_system/schema.md` exists.** If missing, tell the user the brain isn't initialized and point them at `START-HERE.md`.
3. **`_system/domains.md` is customized.** If it still says "the AI fills this in" (default stub), tell the user they need to complete the `STARTER-PROMPT.md` customization first.
4. **`_outputs/` directory exists** for the draft destination.
5. **`wiki/sources/` directory exists** for the eventual destination.

If any check fails, surface the gap and stop. Do NOT silently create folders.

## Outputs

ALL outputs go to `_outputs/` first. NOTHING lands in `wiki/` until the user explicitly approves.

You produce:

1. **The draft source page** at `_outputs/source-<short-name>-<YYYY-MM-DD>.md` — full frontmatter + body per `_system/schema.md` §`source` type.
2. **An "ingest summary"** message in chat surfacing:
   - The draft source-page slug + path
   - 1-3 concept stubs the source surfaces (proposed, not auto-written — ask the user if they want each minted)
   - 1-3 person stubs the source surfaces (same — proposed, not auto-written)
   - Open questions or things that were unclear in the source
   - The user's next action: review the draft and tell you to commit (or revise).

## Algorithm

### 1. Read the raw file

Read it fully. If it's a transcript, get the speakers right (use the user's `_system/domains.md` to identify which speaker is the user).

### 2. Classify the source-type

Pick one: `article | transcript | voice-memo | book | podcast | other`. This goes in frontmatter.

### 3. Draft the frontmatter

Required fields per schema:
- `type: source`
- `slug: source-<short-name>-<YYYY-MM-DD>` — short-name is 2-4 dash-separated words capturing what it's about
- `source-type:` — the classification from step 2
- `title:` — human-readable title
- `created: <today's date>` (YYYY-MM-DD)
- `source-url:` — only if applicable
- `references:` — list of `[[concept-slug]]` / `[[person-slug]]` / `[[project-slug]]` the source mentions that ALREADY EXIST in `wiki/`. Do NOT invent new slugs here; only reference pages that exist. New stub proposals go to the chat output, not the frontmatter.
- `publish: false` — always default false.

### 4. Draft the body

Sections (in order):

- `## TL;DR` — 2-3 sentences. What is this source about? Plain English, no jargon.
- `## Key claims` — bulleted list of what the source argues / shows / asserts. One bullet per claim.
- `## Quotes` — verbatim excerpts worth keeping. Each quote on its own line with `>` markdown blockquote, followed by a location reference if applicable (page number, timestamp, paragraph).
- `## Open questions` — what the source raised but didn't answer. Stuff the user might want to think about later.
- `## Transcript` — ONLY if source-type is `transcript` or `voice-memo`. Include the full text.
- `## Connexions` — bulleted `[[type-slug]]` list mirroring every forward link in the `references:` frontmatter. **Required whenever `references:` is non-empty.** Obsidian's graph does not reliably render frontmatter-only links, so each forward reference MUST also appear inline in the body here, otherwise the page shows up disconnected in the graph. Weave the same `[[...]]` into the prose above where it reads naturally too, but this section is the guaranteed minimum.

### 5. Identify concept + person stubs

Walk the source for:
- **Concepts** mentioned that don't exist as `wiki/concepts/concept-*.md` yet. Examples: a framework name, a coined term, a non-obvious idea. For each, propose a stub to the user.
- **People** mentioned that don't exist as `wiki/people/person-*.md` yet. For each, propose a stub.

**Don't auto-mint these.** Propose them in the ingest summary. Ask the user which to mint.

### 6. Check for supersession

Briefly check if this source updates or replaces an existing source. If it does (e.g., a v2 of an article, a follow-up meeting on the same topic), surface it in the ingest summary so the user can mark the old source `superseded-by:` this one.

### 7. Write the draft

Write to `_outputs/source-<short-name>-<YYYY-MM-DD>.md`.

### 8. Surface the ingest summary

In chat, return a short structured summary:

```
## Ingested: <title>

**Draft:** `_outputs/source-<short-name>-<YYYY-MM-DD>.md`

**Concept stubs surfaced** (not yet minted):
- `[[concept-slug-1]]` — <short description>
- `[[concept-slug-2]]` — <short description>

**Person stubs surfaced** (not yet minted):
- `[[person-firstname-lastname]]` — <role / context>

**Supersession check:** <none / or pointer to which existing source>

**Your next move:**
- Read the draft in `_outputs/`.
- If it looks good, say "commit it" and I'll move it to `wiki/sources/`.
- If you want changes, tell me what to fix.
- For the concept and person stubs, tell me which ones to mint (or say "skip them" if you don't want any yet).
```

### 9. Wait for user approval

Do NOT move the file to `wiki/sources/` until the user explicitly approves.

When the user says "commit it" (or equivalent), move the file from `_outputs/` to `wiki/sources/<source-slug>.md`.

For concept and person stubs the user approves: draft them to `_outputs/` first, show the user the draft, then commit on approval. Same output-before-write rule.

## Hard rules

1. **Never modify `raw/`.** Read-only.
2. **Output before write.** Drafts go to `_outputs/` first. Wait for explicit approval before moving to `wiki/`.
3. **Don't auto-mint concepts or people.** Propose them; let the user pick.
4. **Don't auto-fill `evidenced-by:`.** That field is user-only.
5. **`publish: false` by default.**
6. **Wikilinks use `[[type-slug]]`.** Always.
7. **Every frontmatter forward link also appears inline in the body** (in `## Connexions` at minimum). Frontmatter-only links render unreliably in Obsidian's graph.
8. **Filenames match the `slug:` in frontmatter.** No date suffix on `project-` / `concept-` / `person-` slugs.
8. **Keep the ingest summary short.** First-time users get scared by walls of text.

## Example invocation

**User:** "Ingest the article I just dropped in `raw/articles/`."

**Claude (this skill):**
1. Lists `raw/articles/`, finds the most recent file.
2. Reads it.
3. Drafts `_outputs/source-do-things-that-dont-scale-2026-06-09.md` with TL;DR + key claims + quotes + open questions.
4. Surfaces 2 concept stubs (`concept-recruiting-by-hand`, `concept-fragility-as-feature`) and 1 person stub (`person-paul-graham`).
5. Returns ingest summary in chat.
6. Waits for user to say "commit it."

## Skill version

v0.1 — brain-starter starter kit. Trimmed from Yoda's full v0.5 ingest-source (no sales-deal binding, no HubSpot integration, no topic hubs, no patterns, no decisions — just sources, concepts, people, projects, syntheses).
