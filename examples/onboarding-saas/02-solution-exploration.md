# Solution Exploration — Activation onboarding équipe — 2026-08-03

**Outcome source** : 01-success-metrics.md

## Décision

**Approche recommandée** : Wizard interactif avec defaults intelligents basés sur le rôle déclaré
**Pourquoi** : seule approche qui adresse directement la confusion identifiée en entretien ("je ne savais pas quoi remplir en premier") sans coût disproportionné ni dépendance humaine non scalable.
**Niveau de risque accepté** : l'hypothèse Usability (le wizard réduit réellement la confusion, pas seulement le temps passé) reste `weak-but-testable` — à confirmer via test utilisateur avant généralisation à 100%.

---

## Approches explorées (divergence)

### Approche A — Wizard interactif avec defaults intelligents

**Comment elle résout le problème** : à l'inscription, propose un premier projet pré-rempli selon le rôle déclaré (ex: "Chef de projet" → projet "Sprint équipe" avec colonnes standard), avec une invitation coéquipier intégrée à la même étape.
**Avantages** : scalable, ne dépend d'aucune ressource humaine, mesurable immédiatement
**Limites** : nécessite de définir des defaults pertinents par rôle — risque de defaults mal calibrés pour les rôles moins fréquents
**Risques** : si les defaults sont perçus comme rigides, risque de frustration plutôt que d'aide
**Coût/effort estimé** : M — logique de defaults + 3 écrans, pas de nouvelle intégration tierce

**Hypothèses spécifiques** :

#### USA-1 — Usability
**Énoncé** : un utilisateur qui voit un projet pré-rempli comprend qu'il peut le modifier, il ne le perçoit pas comme figé
**Preuves actuelles** : aucune — hypothèse à tester en usability test avant généralisation
**Confiance** : intuition
**Méthode de validation** : test utilisateur modéré, 5 participants, avant/après wizard
**Critère de décision** : si ≥4/5 participants modifient le projet pré-rempli sans confusion exprimée, hypothèse confirmée
**Statut** : à tester

#### FEA-1 — Feasibility
**Énoncé** : les defaults par rôle peuvent être construits avec les données de rôle déjà collectées à l'inscription (pas de nouveau champ requis)
**Preuves actuelles** : vérifié avec l'équipe technique — le champ `role` existe déjà en base
**Confiance** : documented
**Méthode de validation** : déjà validé en amont
**Critère de décision** : n/a, déjà confirmée
**Statut** : confirmée

### Approche B — Appel d'onboarding assisté par un humain

**Comment elle résout le problème** : un membre de l'équipe CS propose un appel de 15 min aux nouveaux comptes Équipe pour configurer le premier projet ensemble.
**Avantages** : taux de succès individuel probablement très élevé, feedback qualitatif riche
**Limites** : ne scale pas au-delà de quelques dizaines de comptes/mois sans recrutement CS
**Risques** : dépendance à la disponibilité de l'équipe CS, coût récurrent croissant avec le volume
**Coût/effort estimé** : L récurrent (coût humain, pas juste un coût de build ponctuel)

**Hypothèses spécifiques** :

#### VIA-1 — Viability
**Énoncé** : le coût CS par compte reste inférieur à la valeur vie client additionnelle générée par l'activation
**Preuves actuelles** : aucun calcul fait à ce stade
**Confiance** : intuition
**Méthode de validation** : calcul de coût CS chargé vs LTV incrémental avant tout pilote
**Critère de décision** : ratio coût/LTV incrémental > 20% = viabilité douteuse au volume actuel
**Statut** : à tester

### Approche C — Empty states enrichis (tooltips + bandeau d'aide contextuel)

**Comment elle résout le problème** : ajoute des indices visuels et un bandeau explicatif sur les écrans vides existants, sans changer le flow d'inscription.
**Avantages** : coût le plus faible, aucun changement de flow
**Limites** : reste une aide passive — n'adresse pas directement "je ne sais pas par où commencer", seulement "je ne comprends pas cet écran vide"
**Risques** : risque élevé de ne pas bouger la métrique, déjà partiellement tenté (2 correctifs UI mineurs cités au commitment gate, sans effet observé)
**Coût/effort estimé** : S

---

## Élimination progressive (convergence)

| Approche | Éliminée à quelle étape | Raison précise |
|---|---|---|
| Approche C | Comparaison (étape 2) | Aide passive — déjà tentée sous une forme proche (2 correctifs UI mineurs), sans effet mesuré sur le taux d'activation cité au commitment gate. Ne traite pas la cause identifiée en entretien (absence de point de départ, pas manque d'indices visuels). |
| Approche B | Hypothèse Viability (étape 3) | Coût CS récurrent croissant avec le volume, pas de calcul de viabilité favorable établi, dépendance à une ressource humaine non scalable pour un problème qui touche 340 comptes/mois. |

## Approche recommandée — détail complet

Wizard interactif avec defaults intelligents (Approche A). Meilleur rapport risque/impact : coût de build ponctuel modéré (M), scalable sans dépendance humaine, feasibility déjà confirmée (le champ `role` existe), seule inconnue réelle (USA-1) est testable rapidement via usability test avant généralisation — pas un pari all-in sans filet.

## Statut

- [x] Recommandation validée par le PM
- [ ] Override PM (si applicable) — raison tracée dans decision-log.md
- [x] Repris par /pm-prd (charge l'approche retenue, ne la redéfinit pas)
