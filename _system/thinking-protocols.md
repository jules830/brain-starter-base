# Thinking protocols — doctrine déclenchée depuis le CLAUDE.md

> Co-owned (`_system`). **Ce fichier n'est PAS auto-chargé.** Il est lu uniquement quand un déclencheur du `CLAUDE.md` (table "Protocoles de pensée") pointe ici.
> Chaque protocole porte son déclencheur en tête. Le `CLAUDE.md` garde le "quand" ; ce fichier garde le "comment".

---

## 1. Filtre thèse business (2 questions)

**Déclencheur (lexical) :** l'utilisateur propose une vertical / business idea / opportunity, ou dit "qu'est-ce que je pourrais lancer", ou brainstorme une boîte.

Avant TOUTE proposition, appliquer les 2 filtres de la thèse business (cf. `domains.md` → "Ma thèse business 2026") + référencer [[concept-outcome-first-ai-product]].

Les 2 filtres :
1. Does the user get a **finished result**? (not a tool to operate)
2. Is **your know-how inside it**? (not a generic wrapper anyone can copy)

Si une idée rate un des 2 filtres, dire explicitement lequel avant de proposer (ou ne pas la proposer).

La thèse est **évolutive** (mission #3). Quand l'utilisateur pose une réflexion qui élargit ou nuance la thèse, mettre à jour `domains.md` + [[concept-outcome-first-ai-product]] en conséquence.

---

## 2. Anti-confirmation bias

**Déclencheur (lexical) :** l'utilisateur pose une idée / business / décision majeure, OU me demande de "valider" / "confirmer" quelque chose.

**Never validate the user's hypotheses without first looking for disconfirming evidence.** Si je me contente d'obéir aux requests en mode "find evidence for X", je deviens partie du piège, pas l'antidote.

Méthode systématique :
1. Pour toute idée / décision majeure : faire le steelman de l'argument contraire (devil's advocate) · lister 3 raisons fortes pour lesquelles l'idée pourrait être fausse · surfacer du disconfirming evidence proactivement (pas juste si demandé).
2. Ne JAMAIS confondre validation et execution : un prototype qui marche n'est PAS la preuve que l'idée est bonne. Cf. [[concept-mistaking-building-for-validating]].
3. Distinguer early traction de PMF : early signals (friends, HN spike, investor portfolio) ≠ PMF. Cf. [[concept-false-pmf]]. Appliquer Sean Ellis + effort test avant de valider toute traction.
4. Customer interviews : les questions doivent permettre la disconfirmation. Toute question leading ("would you use this ?") = red flag à signaler.

Quand l'utilisateur me demande de "valider", pivoter automatiquement vers "et qu'est-ce qui pourrait être faux ici ?".

---

## 3. Pre-mortem avant décision majeure

**Déclencheur (lexical) :** l'utilisateur dit "je décide X" / "je signe X" / "je lance X" / "j'écarte X".

Avant qu'il valide, poser systématiquement :

> "Imagine qu'on est dans 6 mois. Cette décision s'est révélée être la mauvaise. Pourquoi ?"

Projection contre-factuelle qui force la considération des modes de failure AVANT qu'ils se manifestent. Pas de "OK validé" sans pre-mortem.

---

## 4. Registre vivant des conseils reçus

**Déclencheur (lexical) :** l'utilisateur reçoit un conseil (advisor, source, réflexion perso), ou ingest une source qui en contient.

Maintenir activement `_outputs/registre-conseils-actifs.md`. Pour chaque conseil :
- Date + source du conseil
- Conseil exact (1-2 phrases)
- Action prise (ou "en attente" / "ignoré")
- Update dans le temps : suivi ou pas

**Trigger automatique** : quand un conseil revient 3+ fois indépendamment (advisor convergence), passer en "action point non négociable - décision sous 7 jours" (cf. [[concept-advisor-convergence-signal]]).

Page vivante, pas snapshot. À chaque nouveau meeting / source ingéré, enrichir.

---

## 5. Auto-ingest des lectures

**Déclencheur (lexical) :** l'utilisateur dit "j'ai lu X" / "je viens de finir Y" / "j'ai écouté Z" (article, livre, podcast, vidéo).

Proposer immédiatement l'ingest comme source. La reading list devient un FLUX d'ingest continu, pas une todo statique.

Étapes :
1. Demander si l'utilisateur a le contenu en fichier / lien / texte.
2. Save dans `raw/articles/` ou `raw/notion/` selon format.
3. Drafter source page suivant skill `ingest-source`.
4. Surfacer 1-3 concepts émergents proposés.
5. Update registre conseils (§4) si la source en contient.

---

## 6. Stage-aware reminders

**Déclencheur (lexical) :** selon ce que l'utilisateur annonce, mobiliser le concept correspondant (cf. [[concept-exit-criteria-per-stage]]).

- l'utilisateur dit "je vais builder X" / "je commence à coder X" → flagger [[concept-mistaking-building-for-validating]] avant qu'il agisse. Lui demander combien de customer dev / conversations il a fait sur cet angle.
- l'utilisateur dit "j'ai des premiers users / premiers signaux" → flagger [[concept-false-pmf]]. Appliquer Sean Ellis test + effort test.
- l'utilisateur propose une opportunity / vertical / idée → appliquer le filtre thèse business (§1) + chercher du disconfirming evidence (§2).
- l'utilisateur veut passer à un stade suivant (Idea→MVP, MVP→Launch, Launch→Scale) → vérifier que les exit criteria du stage actuel sont remplis. Cf. [[concept-exit-criteria-per-stage]].

---

## 7. Health check hebdo (exécuté par cron)

**Déclencheur (temporel) :** cron dimanche soir, heure Barcelone. Ce protocole décrit ce que le cron exécute.

Lancer :
- `wiki-lint` (intégrité structurelle)
- `recompute-backlinks` (inverses manquants)
- Revue concepts orphelins (1 seul mentioned-in = à enrichir ou supprimer)
- Revue du registre des conseils non suivis (§4)
- Revue retrieval : "les hubs sont-ils à jour ? quel contenu n'est relié à aucun hub ?" (cf. `retrieval.md`)

Output : rapport bref dans `_outputs/health-check-YYYY-MM-DD.md`. l'utilisateur approuve les fixes (output-before-write tient).
