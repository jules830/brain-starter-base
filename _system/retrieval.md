# Retrieval protocol — sortir la bonne info au bon moment

> Le brain n'a de valeur que si la donnée RESSORT au bon moment. L'ingest est résolu ; ce doc règle le **retrieval**. Co-owned (`_system`) : Claude propose, l'utilisateur valide.

## Le principe

Le vault Obsidian = toute la donnée, reliée par wikilinks. **Les liens SONT le moteur de retrieval** : depuis un bon point d'entrée, on traverse les liens et on atteint tout le thème. Le job de Claude = (1) trouver le bon point d'entrée **vite et obligatoirement**, (2) traverser les liens, (3) répondre cité. Le meilleur point d'entrée = le **hub** du thème.

La data devient morte quand : il n'y a pas de point d'entrée évident, OU rien n'oblige Claude à y passer (il répond de tête).

## Les 3 couches

### 1. Routing — GREP-FIRST (le wiki est l'index, pas `domains.md`)

**La règle générale, topic-agnostic** : sur toute question de fond, avant de répondre, **grep les mots-clés de la requête dans `wiki/`** pour énumérer TOUTES les pages candidates (hub + feuilles + pages non liées). Ça marche pour n'importe quel sujet, **y compris un sujet neuf sans ligne de routing** — c'est ça qui évite le patch par-sujet.

`domains.md` "Hubs vivants" (thème → hub → mots-déclencheurs) reste un **raccourci utile** pour matcher vite, mais **n'est PAS le point de vérité** : il est partiel et par-sujet. Le point de vérité, c'est le wiki lui-même, atteint par grep. Ne jamais s'arrêter à la carte.

### 2. Hubs — le point d'entrée vivant
Un hub par thème vivant. **Forme obligatoire** :
- **🧭 marqueur + état live daté en haut** : la réponse synthétisée à "où on en est sur X", à jour. C'est CE qui ressort dès qu'on charge le hub (pas besoin de tout lire).
- **Index annoté des sources** : chaque `[[source/concept/person]]` avec 1 ligne "ce qu'il contient" → Claude sait quoi ouvrir sans tout ouvrir.
- **Questions ouvertes / next moves.**

Un hub n'est pas une archive : c'est **la réponse synthétisée + la piste de preuves** sous la main.

### 3. Enforcement — DESCENTE AUX FEUILLES, non-optionnel
Règle dure (gravée dans `_system/CLAUDE.md`, "Retrieval-first") : après le grep, **descendre aux pages DÉTAILLÉES** (sources, teardowns, syntheses, transcripts), **jamais répondre depuis le résumé du hub, le contexte chargé, ni une mémoire.** Le hub = la carte ; la réponse vit dans les feuilles qu'il pointe. **Mémoire = pointeur, jamais donnée.**

**Pour une question profonde ou multi-pages : dispatch un agent Explore** qui balaie le wiki (grep + suit les liens) et rend l'ensemble des pages pertinentes + les extraits. Ça rend l'exhaustivité **mécanique**, pas dépendante de la discipline de Claude. 

## Discipline anti-data-morte (le "vivant")

- **Tout ingest sous un thème MET À JOUR son hub** : re-dater la ligne d'état live + ajouter la nouvelle source à l'index annoté. Sinon le hub rote et ment (pire que pas de hub).
- **Toute source linke SON hub** (lien retour) → la traversée marche dans les deux sens.
- **Annoter les liens, toujours** (un lien nu force à tout ouvrir = friction de retrieval).
- **Health check hebdo** : "les hubs sont-ils à jour ? quel contenu n'est relié à aucun hub ?".

## Hubs actuels

- [[project-exemple]] — 🧭 ton premier hub (à remplacer). Un hub par grand sujet de ta vie / ton travail.

## Enforcement dur — ACTIVÉ (2026-07-04)

Hook `UserPromptSubmit` **actif** (`.claude/hooks/retrieval-first.sh`, câblé dans `settings.local.json`) : injecte à chaque prompt le rappel *"grep wiki/ + descends aux feuilles détaillées, ne réponds pas depuis le résumé du hub ni la mémoire ; question profonde → dispatch Explore."* Rend le réflexe impossible à oublier. Coût : un peu de bruit par tour, assumé.
