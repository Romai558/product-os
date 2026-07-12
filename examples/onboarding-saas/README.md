# Exemple — Activation onboarding équipe (fictif)

Cas synthétique, anonymisé, pour montrer à quoi ressemble un passage réel dans le pipeline — pas un tutoriel exhaustif. Produit fictif : **TaskFlow**, un outil de gestion de projet B2B.

## Le contexte (minimal)

- **Produit** : TaskFlow, plan Équipe (5-50 sièges), ~340 nouveaux comptes/mois
- **Signal initial** : le taux d'activation à 48h (créer un projet + inviter un coéquipier) stagne à 55% depuis 2 trimestres, tickets support "je ne sais pas par où commencer" en hausse de 30%

## Le parcours (4 fichiers, dans l'ordre)

| # | Fichier | Ce qu'il décide |
|---|---|---|
| 1 | [`00-commitment-gate.md`](00-commitment-gate.md) | Le problème mérite-t-il l'engagement ? → **COMMIT** |
| 2 | [`01-success-metrics.md`](01-success-metrics.md) | Que veut dire "réussir" concrètement ? → outcome chiffré (55% → 72% en 4 semaines) |
| 3 | [`02-solution-exploration.md`](02-solution-exploration.md) | Quelle approche, parmi 3 comparées, atteint cet outcome au meilleur rapport risque/impact ? → wizard interactif avec defaults par rôle |
| 4 | [`03-prd.md`](03-prd.md) | Le dossier (problème + outcome + approche + hypothèses restantes) est-il prêt pour l'arbitrage final ? → **approved** |

## Ce que ça montre sur les handoffs

Chaque fichier **charge** ce que le précédent a déjà tranché, il ne le redéfinit jamais :

- `02-solution-exploration.md` reprend l'outcome de `01-success-metrics.md` tel quel (mêmes chiffres : 55%, 72%, 4 semaines) pour comparer les approches contre cet objectif précis — pas contre un objectif vague.
- `03-prd.md` reprend à la fois l'outcome (`01`) et l'approche retenue (`02`) dans ses propres sections dédiées, sans les rediscuter — son travail est de consolider, pas de re-choisir.
- L'hypothèse `USA-1` (est-ce que l'utilisateur comprend qu'il peut modifier le projet pré-rempli) est **typée dans `02-solution-exploration.md`** — c'est une propriété de l'approche retenue, pas du problème — puis **héritée telle quelle** dans `03-prd.md`, pas reformulée.

## Ce qui différencie ça d'une collection de prompts

- Chaque fichier a un statut explicite (`commit`, `approved`...) qui **bloque ou débloque** le fichier suivant — `/pm-scope` refuserait de s'exécuter tant que `03-prd.md` n'est pas `approved`.
- Les 3 approches explorées en `02` ne sont pas juste listées : deux sont **éliminées avec une raison précise, tracée** — reproductible par n'importe qui relit le fichier plus tard, sans reconstituer la conversation qui a mené au choix.
- La confiance globale (`Medium`, posée au commitment gate) est **héritée sans recalcul** jusqu'au PRD — elle ne varie pas selon qui relit le fichier ou quand.

## Pour aller plus loin

Pipeline complet, les 15 skills, la logique de blocage : [`tools/product-os/index.md`](../../tools/product-os/index.md).
