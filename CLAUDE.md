# Claude — Product OS

Ce dépôt est un ensemble de skills Claude Code (`.claude/skills/pm-*.md`) formant un workflow PM complet. Point d'entrée pour comprendre le système : [`tools/product-os/index.md`](tools/product-os/index.md).

## Provenance des claims

Convention utilisée dans toutes les skills et fichiers `tools/product-os/context/` pour qualifier une information :

- `documented` — décision ou donnée actée, sourcée
- `research` — étude ou source vérifiée
- `verbal` — rapporté à l'oral, non sourcé
- `intuition` — hypothèse de l'utilisateur du système

Ne jamais inventer une information manquante : marquer `[à documenter]` plutôt que de deviner.

## Règles générales

- Les agents préparent, l'humain valide et tranche — aucune skill ne pose un statut d'approbation finale (`approved`, `rejected`, etc.) elle-même.
- Toute évolution du pipeline suit la séquence Observation → Problème → Hypothèse → Évolution (cf. `tools/product-os/index.md` § Gouvernance).
