# Launch Readiness Checklist — Quality Gate `/pm-release`

> Générique, pas réinitialisée par cible (même statut que `ui-checklist.md`). Gate à passer **avant** le ship, pas une checklist rétroactive après coup.
> Chaque item exige une réponse explicite, pas une case cochée sans preuve. Item non résolu = go/no-go tracé dans `decision-log.md`, pas ignoré en silence.

---

## Instrumentation

- [ ] Les événements/métriques nécessaires à `01-success-metrics.md` (metric de succès + guardrails) sont effectivement câblés, pas juste "prévus"
- [ ] Si partiel ou absent : lister précisément ce qui manque — le ship peut avancer, mais la mesure sera aveugle tant que ce n'est pas corrigé

## Rollout

- [ ] Mode choisi et justifié : progressif (%, cohorte, feature flag) ou 100% direct
- [ ] Le choix reflète le niveau de risque identifié dans le pre-mortem du scope (`03-scope.md` § Tigers/Paper Tigers/Elephants)

## Critères de rollback

- [ ] Seuils précis définis sur les guardrail metrics de `01-success-metrics.md`
- [ ] Agréés **avant** le ship — jamais improvisés après un incident

## Go / No-go

- [ ] Décision explicite, pas un ship par défaut faute d'objection
- [ ] Si le go n'est pas trivial (ex : lancement malgré un guardrail incomplet) : tracé dans `decision-log.md`

---

## Scoring

- ✅ **Prêt** : les 4 sections répondues, aucune sans réponse explicite
- 🟡 **Prêt sous réserve** : instrumentation ou rollback partiels, mais nommés et acceptés explicitement (go/no-go tracé)
- 🔴 **Pas prêt** : un des 4 items sans réponse du tout, ou rollback non défini

`/pm-release` ne poursuit pas vers les release notes tant que le scoring n'est pas au moins 🟡.
