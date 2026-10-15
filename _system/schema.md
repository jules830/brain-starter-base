# Schema — brain-starter v0.1

The brain holds **5 types of pages**. Each lives in `wiki/<type>/` and uses YAML frontmatter + markdown body.

---

## Wikilink form

Always: `[[type-slug]]`. Examples:
- `[[concept-leverage]]`
- `[[source-paul-graham-essay-2026-06-09]]`
- `[[person-jane-smith]]`
- `[[project-q3-product-launch]]`
- `[[synthesis-pricing-takes-2026-06-09]]`

Never: `[[concept:leverage]]` (colon — rejected by Obsidian). Never: `[[leverage]]` (missing type prefix — breaks routing).

### Links must also live in the body

Obsidian's graph view does **not** reliably render links that exist only in YAML frontmatter (`references:`, `reads-from:`, `evidenced-by:`). Every forward link declared in frontmatter MUST therefore also appear inline in the body — at minimum in a trailing `## Connexions` section that bullets each `[[type-slug]]`. Pages whose only links are frontmatter `mentioned-in:` (e.g. most `person` pages) don't need their own `## Connexions`: they're already the *target* of body links from the sources that cite them.

The `recompute-backlinks` skill maintains the inverse `mentioned-in:` field; the `## Connexions` body section mirrors the forward `references:`. Keep both in sync.

---

## The 5 types

### `source`

Anything the user ingested. Lives in `wiki/sources/`.

**Frontmatter:**
```yaml
---
type: source
slug: source-<short-name>-<YYYY-MM-DD>
source-type: article | transcript | voice-memo | book | podcast | other
title: <human-readable title>
created: YYYY-MM-DD
source-url: <optional — link to original>
references:
  - "[[concept-slug]]"
  - "[[person-slug]]"
  - "[[project-slug]]"
publish: false
---
```

**Body sections:**
- `## TL;DR` — 2-3 sentence summary
- `## Key claims` — bulleted list of what matters
- `## Quotes` — verbatim excerpts worth keeping (with location)
- `## Open questions` — what the source raised but didn't answer
- `## Transcript` (only if source is a transcript or voice memo) — the full text

### `concept`

A distilled idea. Lives in `wiki/concepts/`.

**Frontmatter:**
```yaml
---
type: concept
slug: concept-<short-name>
title: <human-readable title>
created: YYYY-MM-DD
evidenced-by:
  - "[[source-slug]]"
publish: false
---
```

**Body sections:**
- `## Definition` — 1-2 sentences
- `## Why it matters`
- `## Connected to` — bulleted `[[concept-slug]]` list of related concepts

`evidenced-by:` is **user-only**. Claude proposes the field, never auto-populates.

### `project`

An active piece of work. Lives in `wiki/projects/`.

**Frontmatter:**
```yaml
---
type: project
slug: project-<short-name>
title: <human-readable title>
created: YYYY-MM-DD
status: active | paused | done
references:
  - "[[person-slug]]"
  - "[[concept-slug]]"
publish: false
---
```

**Body sections:**
- `## Goal`
- `## Current state` — what's happening this week
- `## Decisions made` — log of choices, most recent first
- `## Next moves`

### `person`

Someone the user works with or has talked about. Lives in `wiki/people/`.

**Frontmatter:**
```yaml
---
type: person
slug: person-<firstname-lastname>
title: Firstname Lastname
created: YYYY-MM-DD
role: <their job / context>
references: []
publish: false
---
```

**Body sections:**
- `## Context` — how the user knows them
- `## What they care about`
- `## Recent interactions` — most recent first, each item citing `[[source-slug]]`

### `synthesis`

Your multi-source write-up. Lives in `wiki/syntheses/`.

**Frontmatter:**
```yaml
---
type: synthesis
slug: synthesis-<topic>-<YYYY-MM-DD>
title: <human-readable title>
created: YYYY-MM-DD
composed-on: YYYY-MM-DD
reads-from:
  - "[[source-slug]]"
publish: false
---
```

**Body sections:**
- `## The take` — your synthesis claim, 1 paragraph
- `## Evidence` — bulleted list of `[[source-slug]]` + their contribution
- `## Open questions`

---

## Altitude — hub vs leaf (où vit le texte)

Chaque page a **UNE altitude**. Ne jamais mélanger les deux dans un même fichier.

- **Hub / agrégateur** (`project`, et certaines `synthesis`-hub) = une **carte**. Job : router. Contenu = état (goal, current state, decisions, next moves) + **index de liens annotés** vers ses leaves. Reste **mince**. Un hub ne contient PAS la doctrine ni le détail, il **pointe** vers eux.
- **Leaf / feuille** (`source`, `concept`, `person`, et la plupart des `synthesis`) = un **territoire**. Job : contenir UNE chose à fond. Le texte détaillé vit ici, aussi long que la chose l'exige. Une `source` longue, un `concept` dense, une `person` détaillée = **sain**.

Conséquences :
- **Lier, pas inliner** : si une section d'un hub dépasse ~5 lignes de référence stable (méthode, règle, playbook), ce n'est pas une section, c'est une **leaf** à créer/enrichir puis lier.
- **Zéro duplication** hub↔leaf : une info vit dans UNE seule maison (la leaf dont c'est le job) ; partout ailleurs = un lien.
- **Compaction** : quand un hub gonfle (beaucoup d'ingests sur un thème), passe obligatoire — extraire l'inliné vers ses leaves, ne garder que carte + état + liens.

**Règle dure :** un hub route et reste mince ; une leaf porte le détail. Jamais de doctrine inlinée dans un hub, jamais de duplication hub↔leaf.

---

## Relations & inverse

Forward relations and their inverses:

| Forward | Inverse |
|---|---|
| `references` | `mentioned-in` |
| `evidenced-by` | (none — user-only field) |
| `reads-from` | `mentioned-in` |

The `recompute-backlinks` skill walks the brain and ensures inverses are consistent.

---

## Publish boundary

All pages default to `publish: false`. The user explicitly flips to `true` when they want a page to be considered "public-shareable." Default safe — assume nothing is public unless flagged.

---

## Filename convention

Files live at `wiki/<type>/<type-slug>.md`. The filename matches the `slug:` in frontmatter. Example: `wiki/sources/source-paul-graham-essay-2026-06-09.md`.

---

## Hard rules

1. **Wikilinks use `[[type-slug]]`.** No exceptions.
2. **`evidenced-by:` is user-authored.** Don't auto-fill.
3. **`publish: false` by default.**
4. **All page types live in their typed directory** (`wiki/<type>/`). Don't put a `source` in `wiki/concepts/`.
5. **Slugs are dash-separated, lowercase, no special chars.** `[a-z0-9-]+` only.
