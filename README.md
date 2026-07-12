# Product OS

Workflow PM complet orchestré par agents Claude Code — 15 skills couvrant discovery, un commitment gate explicite, delivery séquentiel strict, et post-ship. Conçu pour tourner comme méthodologie, pas comme suite de documents.

> **Statut : v1 expérimentale.** Architecture stabilisée après plusieurs passes de conception, actuellement en phase de validation par usage réel — aucune initiative n'a encore traversé le pipeline de bout en bout en conditions réelles. Structuré et cohérent (linté automatiquement), mais pas encore éprouvé à l'usage. À tester, pas à adopter les yeux fermés.

## Exemple

[`examples/onboarding-saas/`](examples/onboarding-saas/) — un cas fictif mais réaliste (activation onboarding d'un SaaS B2B) qui traverse 4 étapes du pipeline (commitment gate → success metrics → solution exploration → PRD) et montre concrètement comment un fichier hérite de ce que le précédent a tranché, sans le redéfinir.

## Pourquoi

La plupart des workflows "PM + IA" traitent la discovery et la delivery de la même façon : une chaîne linéaire de documents. Product OS part d'un principe différent :

- **La discovery est une boucle**, pas une chaîne — valider un problème suppose des allers-retours (entretiens, reformulation, re-priorisation), pas un ordre figé.
- **Un commitment gate explicite** sépare "on explore encore" de "on s'engage" — rien n'entre en delivery sans être passé par une décision kill / investigate / commit, avec un vrai check de fit stratégique (DHM — Delight/Hard-to-copy/Margin-enhancing, Gibson Biddle).
- **Le choix de solution est séparé de sa consolidation** — une skill dédiée (`/pm-solution-exploration`) compare plusieurs approches avant que le PRD ne formalise celle retenue. Le PRD ne découvre jamais la solution, il l'hérite.
- **Les 4 risques Cagan ne sont pas à la même altitude** — Value se juge au niveau du problème (avant qu'une solution existe), Usability/Feasibility/Viability sont des propriétés d'une solution précise.
- **Chaque preuve porte un statut de blocage nuancé** (`sufficient` / `weak-but-testable` / `critical-gap` / `contradicted`), pas un blocage binaire "assez de preuves ou pas".
- **La mémoire est éclatée par fonction** (faits produit / stratégie / registre de preuves / journal de décisions), pas dans un fichier fourre-tout.

Détail complet du pipeline, des skills et de la gouvernance : [`tools/product-os/index.md`](tools/product-os/index.md).

## Démarrage

1. Cloner ce repo (ou copier `.claude/skills/` et `tools/product-os/` dans un projet existant qui utilise Claude Code).
2. Remplir `tools/product-os/context/product-facts.md` et `product-strategy.md` pour ta cible active — les skills produisent des outputs génériques tant que ces fichiers sont vides.
3. Démarrer par `/pm-market-analysis` ou `/pm-prioritize` sur un signal réel.

## Vérifier la cohérence

```bash
python3 tools/product-os/lint-pm-skills.py
```

Vérifie la présence des 5 champs de header standardisé sur chaque skill, les références à des fichiers/skills inexistants, les collisions de numérotation, et la cohérence bidirectionnelle skills ↔ index. Voir [`CONTRIBUTING.md`](CONTRIBUTING.md) pour le mécanisme d'annotation `lint-ok`.

Tourne aussi automatiquement en CI sur chaque push et pull request ([`.github/workflows/lint.yml`](.github/workflows/lint.yml)).

## Gouvernance

Ce système est en **baseline v1**. Toute évolution doit partir d'un usage réel observé, jamais d'un raffinement théorique — détail dans [`tools/product-os/index.md`](tools/product-os/index.md#gouvernance-des-évolutions).

## Origine

Extrait le 2026-07-12 d'un système personnel plus large (un "second brain" orchestré par agents). Inspiré du pattern 3-agents delivery de Marion Jachimski, de la discovery continue de Teresa Torres (Opportunity-Solution Tree), des 4 risques de Marty Cagan (Value/Usability/Feasibility/Viability), du framework DHM de Gibson Biddle, et de [phuryn/pm-skills](https://github.com/phuryn/pm-skills). Historique détaillé des décisions de design : [`CHANGELOG.md`](CHANGELOG.md).

## Licence

MIT — voir [`LICENSE`](LICENSE).
