#!/bin/bash
# UserPromptSubmit hook — force le retrieval grep-first + descente aux feuilles.
# Le stdout est injecté comme contexte à chaque prompt.
cat <<'EOF'
[RETRIEVAL-FIRST — rappel systémique]
Si ce prompt touche un thème du brain (un projet, une personne, un concept, une source, une décision...), NE réponds PAS depuis le contexte auto-chargé, les mémoires, ni le résumé d'un hub. Mécanisme obligatoire :
1. GREP les mots-clés de la requête dans wiki/ → énumère TOUTES les pages candidates (le wiki est l'index, pas domains.md). Vaut pour un sujet neuf sans routing.
2. DESCENDS aux feuilles détaillées (sources, teardowns, syntheses, transcripts), jamais s'arrêter au résumé du hub.
3. Réponds CITÉ depuis le détail.
Question profonde ou multi-pages → dispatch un agent Explore qui balaie le wiki et rend les extraits. Mémoire = pointeur, jamais la donnée.
EOF
