# Changelog

Historique des décisions de design. Append-only — une entrée passée ne se réécrit jamais ; une décision révisée ajoute une nouvelle entrée qui référence l'ancienne.

## 2026-07-12 — Baseline v1

### Refonte du pipeline (1re passe)

- Discovery transformée en boucle libre (`/pm-market-analysis` → `/pm-prioritize` → boucle `/pm-interview-insights` ⇄ artefact sélectionné ⇄ reformulation ⇄ re-priorisation) — le séquencement strict démarre après le commitment gate, pas avant.
- Artefacts discovery (persona, empathy map, journey map) rendus conditionnels — déclenchés seulement si une grille de sélection identifie l'incertitude qu'ils réduisent, plus jamais enchaînés par défaut.
- Nouvelle skill `/pm-commitment-gate` : seul point de passage entre la boucle discovery et le séquencement strict, décision kill/investigate/commit sur 6 critères (Why now / Evidence strength / Strategic fit DHM / Cost of delay / What happens if we do nothing / Cheapest next learning step).
- `/pm-success-metrics` déplacée avant le PRD — l'outcome complet se pose avant que le problème ne soit consolidé.
- Statut binaire "preuve suffisante ou pas" remplacé par 4 statuts nuancés (`sufficient` / `weak-but-testable` / `critical-gap` / `contradicted`).
- Mémoire éclatée en 4 fichiers : `product-facts.md`, `product-strategy.md`, `evidence-register.md`, `decision-log.md`.
- Post-ship renforcé : Launch Readiness avant ship, adoption/activation/rétention par segment, impact économique, décision STOP/ITERATE/SCALE/ROLLBACK, mise à jour systématique des 4 fichiers mémoire.

### Audit ciblé (2e passe)

- Empathy map fusionnée dans `/pm-interview-insights` (champ obligatoire "écart dit/fait" à chaque entretien, pas optionnel dans une skill conditionnelle — sinon le signal disparaît silencieusement).
- Launch Readiness extraite en checklist dédiée (`standards/launch-readiness-checklist.md`) plutôt que gardée inline ou promue en skill séparée.
- `/pm-sprint-plan` sortie du séquencement numéroté (branche annexe, sortie non numérotée) — optionnel par nature, ne devrait pas créer un trou de numérotation dans les usages solo.
- Gate "solution encore valide" entre `/pm-prototype` et `/pm-tickets`, réutilisant le statut `contradicted` de l'evidence-register plutôt qu'une nouvelle skill de design review.
- Synthèse de confiance globale Low/Medium/High (qualité/diversité/convergence des preuves, jamais un pourcentage) ajoutée au commitment gate.
- Header standardisé (Décision/Entrées/Sortie/Bloque si/Met à jour) sur toutes les skills, avec test de garde-fou "cette skill décide...".

### Solution Exploration (3e passe)

- Nouvelle skill `/pm-solution-exploration`, insérée entre `/pm-success-metrics` et `/pm-prd` : divergence (approches candidates, pas de nombre imposé) → élimination progressive (raison précise par approche écartée) → convergence (approche au meilleur rapport risque/impact).
- Séparation d'altitude pour les 4 risques Cagan : Value au niveau du problème (discovery/commitment gate), Usability/Feasibility/Viability au niveau de la solution retenue, typées par approche dans la nouvelle skill.
- `/pm-prd` repositionné en skill de consolidation ("le dossier est-il prêt pour l'arbitrage") plutôt que de décision de solution — charge l'outcome et l'approche sans les redéfinir.
- Renumérotation : `00-commitment-gate` → `01-success-metrics` → `02-solution-exploration` → `03-prd` → `04-scope` → `05-prototype` → `06-tickets` → `07-release` → `08-data-analysis`.

### Audit maintenabilité

- Séparation `context/` (réinitialisable par cible) / `standards/` (générique, jamais réinitialisé) — `ui-checklist.md` et `launch-readiness-checklist.md` déplacés hors de `context/`.
- Linter `tools/product-os/lint-pm-skills.py` : vérifie les headers standardisés, les références à des fichiers/skills inexistants, les collisions de numérotation, la cohérence bidirectionnelle skills ↔ index.
- Mécanisme d'annotation `<!-- lint-ok: raison -->` pour les exceptions volontaires (références historiques ou prospectives) — local et explicite, pas une allowlist cachée dans le script.

### Extraction

- Extrait dans un dépôt séparé, avec `context/` réinitialisé en templates génériques.

## Règle de gouvernance actée

Toute évolution future doit suivre : **Observation → Problème identifié → Hypothèse d'amélioration → Évolution de l'architecture**, jamais l'inverse. Détail : `tools/product-os/index.md` § Gouvernance des évolutions.
