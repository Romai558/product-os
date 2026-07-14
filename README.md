# Product OS

**An agentic product management system for Claude Code.**

Product OS transforme un signal produit en décision, puis en exécution traçable :

**Discovery → Commitment → Solution Exploration → Delivery → Post-ship**

Ce n'est pas une collection de prompts. C'est un système de 15 skills spécialisées, reliées par des handoffs explicites, une mémoire produit persistante et des quality gates qui empêchent d'avancer lorsque les preuves sont insuffisantes.

## Ce que le système optimise

Product OS est conçu pour aider un PM à mieux répondre à quatre questions :

1. Ce problème mérite-t-il réellement notre attention ?
2. Avons-nous assez de preuves pour nous engager ?
3. Quelle solution maximise l'impact avec un niveau de risque acceptable ?
4. Les résultats post-ship justifient-ils de continuer, itérer, scaler ou rollback ?

L'objectif n'est pas de produire plus de documents. L'objectif est de rendre les décisions produit plus explicites, plus cohérentes et plus faciles à réviser.

## Principes d'architecture

### La discovery est une boucle, pas une chaîne

Les artefacts discovery ne sont pas obligatoires ni exécutés dans un ordre fixe. Interviews, personas, journey maps et priorisation sont utilisés uniquement lorsqu'ils réduisent une incertitude réelle.

### L'engagement est une décision explicite

Avant toute delivery, `/pm-commitment-gate` impose une décision :

- **KILL**
- **INVESTIGATE**
- **COMMIT**

Le gate vérifie notamment la qualité des preuves, le niveau de confiance et le fit stratégique.

### Le Problem Space et le Solution Space sont séparés

Le système distingue :

- **Value risk** : le problème mérite-t-il d'être résolu ?
- **Usability, Feasibility, Viability risks** : cette solution précise est-elle utilisable, faisable et viable ?

`/pm-solution-exploration` compare plusieurs approches avant que le PRD ne formalise la solution retenue.

### Le PRD ne découvre pas la solution

Le PRD consolide :

- le problème validé ;
- l'outcome attendu ;
- les métriques de succès ;
- l'approche retenue ;
- les arbitrages ;
- les hypothèses restantes.

Il hérite des décisions prises en amont au lieu de les recréer.

### Les preuves ont des statuts opérationnels

Chaque preuve est qualifiée avec l'un des statuts suivants :

- `sufficient`
- `weak-but-testable`
- `critical-gap`
- `contradicted`

Le système distingue ainsi une incertitude acceptable d'un manque critique qui doit bloquer la progression.

### La mémoire est structurée par fonction

Le contexte produit est séparé en quatre sources :

- `product-facts.md`
- `product-strategy.md`
- `evidence-register.md`
- `decision-log.md`

Les agents chargent ces fichiers avant d'agir et ne devinent jamais une information manquante.

## Pipeline

```
DISCOVERY LOOP
/pm-market-analysis
/pm-prioritize
/pm-interview-insights
/pm-ux-personas
/pm-journey-mapping
        ↓
COMMITMENT GATE
/pm-commitment-gate
KILL | INVESTIGATE | COMMIT
        ↓
DELIVERY
/pm-success-metrics
/pm-solution-exploration
/pm-prd
/pm-scope
/pm-prototype
/pm-tickets
        ↓
POST-SHIP
/pm-release
/pm-data-analysis
STOP | ITERATE | SCALE | ROLLBACK
```

`/pm-sprint-plan` existe comme branche optionnelle pour les contextes squad ou Shape Up hybride.

## Exemple

[`examples/onboarding-saas/`](examples/onboarding-saas/) — un cas fictif mais réaliste (activation onboarding d'un SaaS B2B) qui traverse 4 étapes du pipeline (commitment gate → success metrics → solution exploration → PRD) et montre concrètement comment un fichier hérite de ce que le précédent a tranché, sans le redéfinir.

## Pourquoi Product OS

La plupart des workflows "PM + IA" automatisent la rédaction de documents.

Product OS cherche plutôt à orchestrer un raisonnement produit complet :

- décider avant d'exécuter ;
- séparer faits, hypothèses et intuitions ;
- conserver le raisonnement derrière les décisions ;
- réutiliser les apprentissages entre agents ;
- bloquer les handoffs lorsque les preuves ne sont pas suffisantes ;
- fermer la boucle après le lancement.

Chaque skill possède une responsabilité unique et commence par cinq champs standardisés :

- **Décision**
- **Entrées**
- **Sortie**
- **Bloque si**
- **Met à jour**

## Démarrage

### 1. Cloner le repository

```bash
git clone https://github.com/Romai558/product-os.git
cd product-os
```

Il est aussi possible de copier uniquement :

```
.claude/skills/
tools/product-os/
```

dans un projet Claude Code existant.

### 2. Initialiser le contexte produit

Compléter :

```
tools/product-os/context/product-facts.md
tools/product-os/context/product-strategy.md
```

Toute information inconnue doit rester marquée `[à documenter]`.

### 3. Lancer une première initiative

À partir d'un signal réel :

```
/pm-market-analysis
```

ou :

```
/pm-prioritize
```

Le détail complet du pipeline et des règles se trouve dans [`tools/product-os/index.md`](tools/product-os/index.md).

## Vérifier la cohérence

```bash
python3 tools/product-os/lint-pm-skills.py
```

Le linter vérifie notamment :

- la présence des headers standardisés ;
- les références vers des skills ou fichiers inexistants ;
- les collisions de numérotation ;
- la cohérence entre les skills et l'index.

Tourne aussi automatiquement en CI sur chaque push et pull request ([`.github/workflows/lint.yml`](.github/workflows/lint.yml)).

Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) pour les conventions de contribution.

## Statut

**v1 expérimentale** — architecture stabilisée, actuellement en validation par usage réel.

Les évolutions du système doivent suivre cette séquence :

**Observation → Problème → Hypothèse → Évolution**

Aucune nouvelle skill ou modification du pipeline ne doit être ajoutée uniquement parce qu'elle rend l'architecture plus élégante.

## Influences

Product OS s'appuie notamment sur :

- **Teresa Torres** — Continuous Discovery et Opportunity-Solution Trees
- **Marty Cagan** — Value, Usability, Feasibility, Viability risks
- **Gibson Biddle** — DHM : Delight, Hard-to-copy, Margin-enhancing
- **[phuryn/pm-skills](https://github.com/phuryn/pm-skills)** — plusieurs patterns opérationnels PM

L'historique des décisions d'architecture est disponible dans [`CHANGELOG.md`](CHANGELOG.md).

## Licence

MIT — voir [`LICENSE`](LICENSE).
