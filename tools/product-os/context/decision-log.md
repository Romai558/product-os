# Decision Log — [Cible]

**Cible actuelle** : [à renseigner]
**Actif depuis** : [à renseigner]
**État du contexte** : vide — aucune décision enregistrée

## Rôle

Append-only. Git garde l'historique des *changements* de fichiers, pas le *raisonnement* derrière une décision PM. Ce fichier capture ce raisonnement au moment où il est pris, pour pouvoir le retrouver sans reconstituer une conversation ou un diff.

Une entrée par décision PM réelle, notamment :
- `/pm-commitment-gate` : kill / investigate / commit
- `/pm-solution-exploration` : override PM d'une recommandation
- `/pm-prd` : approved / rejected / superseded
- `/pm-scope` : tradeoff arbitré
- `/pm-data-analysis` : stop / iterate / scale / rollback

**Ne jamais éditer ou supprimer une entrée existante** — si une décision est révisée, ajouter une nouvelle entrée qui référence l'ancienne par date, ne pas réécrire l'historique.

## Format d'entrée

```markdown
### YYYY-MM-DD — [Initiative] — [Skill source]

**Contexte** : [pourquoi cette décision se pose maintenant]
**Options considérées** : [liste courte des alternatives réelles]
**Choix** : [décision prise]
**Justification** : [pourquoi celle-ci plutôt que les autres]
**Signaux de révision** : [ce qui, si observé plus tard, remettrait cette décision en cause]
```

---

## Journal

*(Vide — aucune décision enregistrée depuis la création de ce fichier)*
