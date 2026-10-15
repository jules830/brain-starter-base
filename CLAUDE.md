# CLAUDE.md — brain-starter (auto-chargé à chaque session)

Ce fichier est lu **automatiquement** par Claude Code à l'ouverture du dossier. Les règles ci-dessous sont **toujours actives et non négociables**. Les règles complètes sont importées en bas (`@_system/...`) — les appliquer.

## Voix — toujours active
- **Zéro em-dash (—) ni en-dash (–)** dans tout texte user-facing ou tout content. Virgules, points, parenthèses à la place.
- Pas de tournures à odeur IA : "Here's the thing", "It's not just X, it's Y", les tricolons, "moreover/furthermore", le ton LinkedIn-inspirational.
- Matcher ta voix : décris-la dans `_system/domains.md` (section *How to treat me*).

## Structure — altitude hub vs leaf (toujours active)
- Un **projet / hub ENGLOBE** des sous-pages, il ne **contient pas** l'info : il pose l'état (goal, current state, decisions, next moves) + un **index de liens annotés**. Il reste **mince**.
- Une **leaf** (`source` / `concept` / `person`) **PORTE** l'info, en détail. C'est là que le texte vit, aussi long qu'il faut. Et **ajouter plus de détail dans les leaves** quand c'est utile.
- **Jamais dupliquer** une info entre un projet et sa sous-page. **Jamais inliner de la doctrine** dans un hub (méthode, règles, playbook → `concept`/`synthesis` liés).
- À l'**ingest** : trier par altitude AVANT d'écrire (détail : `_system/CLAUDE.md` → "Règle d'écriture à l'ingest").

## Lecture & écriture
- **Retrieval-first** : répondre depuis les pages réelles de `wiki/`, citées, jamais de tête.
- **Output-before-write** : drafts dans `_outputs/`, validés, avant `wiki/`. `_system/` gaté pareil.

## Règles complètes importées (à appliquer)
@_system/CLAUDE.md
@_system/domains.md
