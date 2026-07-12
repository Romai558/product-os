# Success Metrics — Activation onboarding équipe — 2026-08-03

**Commitment gate source** : 00-commitment-gate.md (commit)
**North Star Metric produit** : Équipes actives hebdomadaires (≥3 membres avec ≥1 action sur un projet partagé/semaine)

## Outcome

- **Comportement à modifier** : créer un premier projet et y inviter au moins un coéquipier dans les 48h suivant l'inscription
- **Population concernée** : nouveaux comptes plan Équipe (5-50 sièges) — environ 340 signups/mois

## Metric de succès

- **Métrique** : taux de comptes ayant créé un projet + invité ≥1 coéquipier sous 48h
- **Lien avec la NSM** : ce comportement est le prédicteur le plus fort observé de passage au statut "équipe active hebdomadaire" à J30

## Baseline

- **Valeur** : 55% (mesuré, dernier trimestre)

## Metrics garde-fou

- **Volume de tickets support "onboarding"** : ne doit pas augmenter de plus de 10% — un wizard mal calibré pourrait créer plus de confusion qu'il n'en résout
- **Temps médian jusqu'au premier projet créé** : ne doit pas dépasser 10 minutes — un onboarding plus "guidé" ne doit pas devenir plus long

## Objectif SMART

- **Cible** : 72% (contre 55% baseline)
- **Fenêtre de mesure** : 4 semaines après ship, cohortes complètes uniquement
- **Mesuré via** : événements produit déjà instrumentés (`project_created`, `teammate_invited`) — pas de nouvelle instrumentation nécessaire

## Statut

- [x] Objectif validé par le PM
- [x] Repris par /pm-solution-exploration (compare les approches pour l'atteindre)
- [x] Repris par /pm-prd (charge l'outcome sans le redéfinir)
- [ ] Repris par /pm-data-analysis en post-ship
