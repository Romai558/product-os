# Skill — /pm-solution-exploration

**Décision** : quelle approche est la plus susceptible d'atteindre l'outcome avec un niveau de risque acceptable, et pourquoi les autres sont écartées.
**Entrées** : `01-success-metrics.md` (outcome fixé) ; `evidence-register.md` ; `product-facts.md` (contraintes tech/stack) ; artefacts discovery pertinents si disponibles (`journey-map-*.md`, `personas-*.md`)
**Sortie** : `outputs/specs/[feature]/02-solution-exploration.md`
**Bloque si** : aucune approche candidate ne passe un seuil minimal de faisabilité/viabilité → `critical-gap` sur hypothèse Feasibility/Viability, retour à `/pm-commitment-gate` (pas de PRD écrit sur une base infaisable)
**Met à jour** : `evidence-register.md` (typage `USA-n`/`FEA-n`/`VIA-n` sur l'approche recommandée) ; `decision-log.md` (si le PM override la recommandation)

**Entre `/pm-success-metrics` et `/pm-prd`.** Le PRD ne doit pas découvrir la solution, seulement formaliser celle déjà retenue ici. Explore l'espace des solutions possibles pour l'outcome déjà fixé, les compare sérieusement, élimine progressivement les moins pertinentes, et recommande une approche avec les raisons d'écarter les autres.

> **Value vs Usability/Feasibility/Viability — deux altitudes différentes.** Value (l'utilisateur veut-il que ce problème soit résolu ?) s'évalue au niveau du problème/outcome, déjà fait en amont (discovery, commitment gate). Usability, Feasibility et Viability sont des propriétés d'une solution précise — elles ne peuvent pas être évaluées sérieusement tant qu'aucune solution concrète n'existe. C'est ici, pas dans `/pm-prd`, qu'elles se typent pour de vrai.

## Déclencheur

- `/pm-solution-exploration [initiative committée, outcome fixé]`
- Après `/pm-success-metrics`, avant `/pm-prd`

## Pré-requis

- `outputs/specs/[feature]/01-success-metrics.md` — outcome déjà défini
- `tools/product-os/context/evidence-register.md`
- `tools/product-os/context/product-facts.md` — contraintes tech, stack, décisions structurantes
- Optionnel : artefacts de la boucle discovery (`journey-map-*.md`, `personas-*.md`)

## Place dans le pipeline

```
01-success-metrics.md (outcome fixé)
  → /pm-solution-exploration
  → outputs/specs/[feature]/02-solution-exploration.md
  → [PM valide la recommandation, ou override — override tracé dans decision-log.md]
  → /pm-prd (charge l'approche retenue, ne la redéfinit pas)
```

## Étapes

### 1. Divergence — générer les approches candidates

Générer **autant d'approches réellement distinctes que nécessaire** pour couvrir sérieusement l'espace des solutions — **pas de nombre imposé**. Le critère est la diversité des approches (des façons différentes de résoudre le problème), pas leur quantité : deux variantes cosmétiques de la même idée ne comptent pas comme deux approches.

**Si une exploration honnête ne révèle qu'une seule approche sérieusement envisageable** : le dire explicitement, ne pas fabriquer d'alternatives de façade pour remplir la section.

Pour chaque approche : une description courte de comment elle résout le problème (pas un scope détaillé — ça reste le rôle de `/pm-scope`, une fois l'approche retenue).

### 2. Comparaison — avantages, limites, risques, coûts

Pour chaque approche candidate : avantages, limites, risques principaux, coût/effort estimé (ordre de grandeur — l'estimation précise vient plus tard, dans `/pm-scope`/`/pm-tickets`).

### 3. Challenger les hypothèses de chaque approche

Pour chaque approche, typer les hypothèses `USA-n`/`FEA-n`/`VIA-n` **spécifiques à cette approche** — elles diffèrent par construction d'une approche à l'autre (la faisabilité d'une approche "config produit" n'est pas celle d'une approche "custom build"). Même format riche que dans `/pm-prd` : énoncé, preuves actuelles, confiance, méthode de validation, critère de décision, statut.

### 4. Élimination progressive

Pas un choix en un coup. Éliminer les approches les moins pertinentes une à une, en nommant la **raison précise** ("faisabilité incertaine sur X", "coût disproportionné vs impact attendu", "hypothèse Usability non tenable au vu de Y") — jamais "moins bonne" sans cause nommée. Les approches éliminées restent documentées avec leur raison, elles ne disparaissent pas du fichier : un retour en arrière futur doit pouvoir s'appuyer dessus sans tout refaire.

### 5. Convergence — recommandation

Recommander l'approche qui atteint l'outcome avec le **meilleur rapport risque/impact** compte tenu des contraintes de `product-facts.md` — pas nécessairement la moins risquée dans l'absolu, ni la moins chère. Justifier explicitement pourquoi les approches éliminées ont été écartées (renvoyer à l'étape 4, ne pas répéter).

### 6. Écrire l'analyse et le gate PM

`tools/product-os/outputs/specs/[feature]/02-solution-exploration.md`. Le PM valide la recommandation ou l'override. En cas d'override, la raison est tracée dans `decision-log.md` — comme toute décision PM qui s'écarte d'une recommandation agent ailleurs dans le système.

## Format de sortie

```markdown
# Solution Exploration — [Nom initiative] — [Date]

**Outcome source** : 01-success-metrics.md

## Décision

**Approche recommandée** : [nom court]
**Pourquoi** : [2-3 lignes — la synthèse, le détail complet est plus bas]
**Niveau de risque accepté** : [ce qui reste incertain malgré tout, même sur l'approche retenue]

---

## Approches explorées (divergence)

### Approche A — [nom]

**Comment elle résout le problème** : ...
**Avantages** : ...
**Limites** : ...
**Risques** : ...
**Coût/effort estimé** : [ordre de grandeur]

**Hypothèses spécifiques** :

#### USA-1 — Usability
**Énoncé** : [hypothèse testable propre à cette approche]
**Preuves actuelles** : [même partielles, ou "aucune"]
**Confiance** : documented | research | verbal | intuition
**Méthode de validation** : ...
**Critère de décision** : ...
**Statut** : à tester | partiellement confirmée | confirmée | infirmée

#### FEA-1 — Feasibility
[même structure]

#### VIA-1 — Viability
[même structure]

### Approche B — [nom]
[même structure]

*(Autant d'approches que nécessaire pour couvrir sérieusement l'espace — pas de nombre imposé. Une seule approche sérieuse identifiée → le dire explicitement plutôt que fabriquer des alternatives de façade.)*

---

## Élimination progressive (convergence)

| Approche | Éliminée à quelle étape | Raison précise |
|---|---|---|
| [Approche B] | [ex: étape 3, hypothèse FEA] | [cause nommée, pas "moins bonne"] |

## Approche recommandée — détail complet

[Reprise détaillée de la synthèse en tête de fichier, avec le raisonnement complet]

## Statut

- [ ] Recommandation validée par le PM
- [ ] Override PM (si applicable) — raison tracée dans `decision-log.md`
- [ ] Repris par `/pm-prd` (charge l'approche retenue, ne la redéfinit pas)
```

## Règles dures

- **Pas de nombre fixe d'approches** — la diversité prime sur la quantité. Une seule approche sérieuse identifiée = le dire explicitement, jamais de façade pour remplir la section.
- **Divergence puis élimination progressive puis convergence** — pas un choix en un coup. Chaque approche écartée porte une raison précise, tracée, pas supprimée du fichier.
- **Hypothèses USA/FEA/VIA typées par approche, jamais globalement** — elles diffèrent par construction d'une approche à l'autre.
- **Value reste hors du périmètre de cette skill** — déjà évalué en amont (discovery, commitment gate), au niveau du problème, pas de la solution.
- **La recommandation vise le meilleur rapport risque/impact**, pas la solution la moins risquée dans l'absolu ni la moins chère.
- **Aucune approche ne passant les seuils de faisabilité/viabilité minimaux → retour à `/pm-commitment-gate`**, pas de PRD prématuré sur une base infaisable.
- **Override PM de la recommandation = tracé dans `decision-log.md`.**
- **Ce fichier est input direct de `/pm-prd`** — l'approche retenue n'est jamais redéfinie dans le PRD, seulement chargée et consolidée.
