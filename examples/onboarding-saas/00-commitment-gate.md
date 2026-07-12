# Commitment Gate — Activation onboarding équipe — 2026-08-03

**Source discovery** : `/pm-prioritize` (Top 1) + 6 entretiens `/pm-interview-insights` + `evidence-register.md`

## Why now?

Taux d'activation équipe stable à 55% depuis 2 trimestres malgré deux tentatives de correctifs UI mineurs. Tickets support liés à "je ne sais pas par où commencer" en hausse de 30% sur le dernier trimestre — signal business + user convergent, pas un bruit isolé.

## Evidence strength

| ID evidence-register | Type | Statut | Bloque commit ? |
|---|---|---|---|
| EV-1 | Value | sufficient | non |
| EV-2 | Value | sufficient | non |
| EV-3 | Usability | weak-but-testable | non |

**Confiance globale** : Medium
**Justification** : deux sources indépendantes convergentes (analytics produit + tickets support) sur la Value ; aucune contradiction relevée en entretien. Pas High : la cause précise de la confusion (EV-3) reste une hypothèse, pas encore observée en usage réel.

## Strategic fit (DHM)

- **Objectif produit servi** : OKR "Réduire le churn 90 jours" — l'activation équipe est le prédicteur le plus fort de rétention identifié dans `product-strategy.md`.
- **Avantage différenciant renforcé** : un onboarding qui configure un vrai premier projet (pas un tour guidé passif) — aucun concurrent direct ne le fait aujourd'hui.
- **Capacité difficile à copier créée** : logique de defaults intelligents basée sur le rôle déclaré à l'inscription — accumule de la donnée d'usage propriétaire à chaque cohorte.
- **Impact économique attendu** : +5 à 8 points d'activation ≈ réduction churn 90 jours estimée à 2-3% du MRR nouveaux comptes (ordre de grandeur, à confirmer post-ship).
- **Construire vs configurer/acheter** : évalué — les outils de product tours tiers (type Appcues) couvrent le "montrer l'interface", pas "aider à configurer un vrai premier workspace utile". Écart jugé suffisant pour justifier un build interne léger plutôt qu'un achat.

## Cost of delay

Chaque mois sans correctif ajoute une cohorte de nouveaux comptes à l'historique de churn 90 jours — coût cumulatif, pas un retard neutre.

## What happens if we do nothing?

Le taux d'activation reste plafonné à ~55%, le churn 90 jours continue d'absorber une partie significative de l'acquisition payante. Pas d'aggravation brutale attendue, mais un plafond qui ne se lève pas seul.

## Cheapest next learning step

*(Non applicable — décision commit)*

## Décision

**COMMIT**

Justification : deux signaux convergents (business + user), fit stratégique fort sur 4 des 5 critères DHM, coût de l'inaction cumulatif et non négligeable. La seule incertitude réelle (EV-3, cause précise de la confusion) est de nature Usability — évaluable une fois une approche concrète proposée, pas bloquante pour committer au niveau du problème.
