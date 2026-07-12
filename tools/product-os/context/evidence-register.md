# Evidence Register — [Cible]

**Cible actuelle** : [à renseigner]
**Actif depuis** : [à renseigner]
**État du contexte** : vide — aucune initiative en cours

## Rôle

Registre unique de toute preuve et hypothèse produit, sur tout le cycle de vie d'une initiative (discovery, commitment gate, PRD, scope, post-ship) — pas seulement au moment du PRD. Deux axes distincts par entrée, à ne jamais confondre :

- **Confiance** (`documented / research / verbal / intuition`) — d'où vient la preuve, quel niveau de solidité de source.
- **Statut** (`sufficient / weak-but-testable / critical-gap / contradicted`) — quel comportement de blocage ça déclenche.

## Statuts et effet par skill

| Statut | Sens | Effet |
|---|---|---|
| `sufficient` | Preuve solide, pas d'incertitude bloquante | Aucun blocage |
| `weak-but-testable` | Incertitude acceptable — hypothèse explicite posée | Ne bloque rien, continue avec l'hypothèse nommée |
| `critical-gap` | Risque critique non testé | Bloque le **commitment** (`/pm-commitment-gate` ne peut pas rendre `commit`) — bloque aussi la **convergence** vers une approche dans `/pm-solution-exploration` |
| `contradicted` | Preuve infirmée par une donnée postérieure | Bloque `/pm-prd` → `ready-for-review` ; ou, si détecté après construction du prototype, bloque `/pm-tickets` |

Détail des règles de blocage par skill : voir chaque fichier `.claude/skills/pm-*.md` § Règles dures.

## Format d'entrée

| ID | Initiative | Type | Énoncé | Source | Confiance | Statut | MAJ |
|---|---|---|---|---|---|---|---|
| EV-1 | [slug initiative] | VAL / USA / FEA / VIA / non typé (discovery) | [hypothèse ou preuve, une phrase testable] | [interview / market-analysis / data / intuition PM] | documented / research / verbal / intuition | sufficient / weak-but-testable / critical-gap / contradicted | YYYY-MM-DD |

- **ID** : `EV-n`, séquentiel, jamais réutilisé même si une entrée devient obsolète.
- **Type** : laissé "non typé" tant qu'on est en discovery — VAL se type au niveau du problème (discovery/commitment gate), USA/FEA/VIA se typent par approche dans `/pm-solution-exploration`, jamais avant qu'une solution concrète existe.
- **Statut mis à jour dans le temps** : une entrée `weak-but-testable` peut devenir `contradicted` (nouvel entretien qui infirme) ou `sufficient` (preuve confirmée) — mettre à jour la ligne, ne pas dupliquer.

## Qui écrit ici

- `/pm-interview-insights`, `/pm-market-analysis` et les artefacts discovery sélectionnés (persona/JTBD/etc.) : ajoutent des entrées au fil de la discovery.
- `/pm-prioritize` : référence la Qualité des preuves déjà notée ici pour les candidats scorés.
- `/pm-commitment-gate` : lit les entrées liées à l'initiative pour évaluer *Evidence strength* — bloque `commit` si une entrée Value est `critical-gap` ou `contradicted`.
- `/pm-solution-exploration` : type les hypothèses USA/FEA/VIA par approche candidate.
- `/pm-prd` : formalise les hypothèses encore ouvertes ; vérifie qu'aucune entrée liée n'est passée à `contradicted`.
- `/pm-scope` : peut ajouter des entrées `weak-but-testable` sur des tradeoffs FEA/VIA découverts en scoping.
- `/pm-data-analysis` : clôture une entrée (`sufficient` confirmé ou `contradicted` infirmé) une fois les données post-ship disponibles.

---

## Registre

*(Vide — aucune initiative n'a encore traversé la discovery)*

| ID | Initiative | Type | Énoncé | Source | Confiance | Statut | MAJ |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |
