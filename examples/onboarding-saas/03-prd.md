# PRD — Activation onboarding équipe

**Date** : 2026-08-05
**Persona principal** : Sam, chef de projet dans une PME de 50 personnes, premier utilisateur à créer le compte pour son équipe
**Outcome / OKR lié** : OKR "Réduire le churn 90 jours"
**Statut** : approved
**Niveau de preuve du problème** : research
**Commitment gate** : 00-commitment-gate.md (commit, 2026-08-03)
**Confiance globale (héritée)** : Medium — cf. 00-commitment-gate.md
**Outcome source** : 01-success-metrics.md
**Approche source** : 02-solution-exploration.md

## Résumé

55% seulement des nouveaux comptes Équipe créent un premier projet et invitent un coéquipier sous 48h — le reste stagne sur un compte vide, sans point de départ clair, jusqu'à l'abandon. L'approche retenue est un wizard interactif qui pré-remplit un premier projet selon le rôle déclaré à l'inscription, avec l'invitation coéquipier intégrée au même flow.

## Problème

**Qui** : Sam (ou équivalent), premier utilisateur d'un compte Équipe qui vient de s'inscrire
**Friction observable** : arrive sur un tableau de bord vide après inscription, ne sait pas par quoi commencer (créer un projet ? inviter d'abord ? configurer les paramètres ?)
**Contexte d'apparition** : immédiatement après la création du compte, avant toute action
**Conséquence** : abandon du compte dans les 7 jours pour 45% des nouveaux comptes Équipe
**Pourquoi maintenant** : User signal (tickets support "je ne sais pas par où commencer" +30% ce trimestre) + Business signal (taux d'activation plafonné à 55% depuis 2 trimestres)

## Preuves disponibles

| Source | Signal observé | Confiance | Statut evidence-register | Limites |
|---|---|---|---|---|
| Analytics produit | Taux d'activation 48h stable à 55% sur 2 trimestres | documented | sufficient | Ne dit pas *pourquoi*, seulement *que* |
| Tickets support (6 mois) | +30% de tickets "je ne sais pas par où commencer" | documented | sufficient | Biais possible : seuls les utilisateurs qui contactent le support sont visibles |
| 6 entretiens utilisateurs | "Je suis arrivé sur un écran vide, j'ai fermé l'onglet et j'ai oublié" (verbatim, 4/6 participants) | verbal | sufficient | Échantillon petit (6), mais convergence forte sur le même thème |

## Outcome (chargé depuis 01-success-metrics.md)

**Comportement à modifier** : créer un premier projet et inviter ≥1 coéquipier sous 48h
**Population** : nouveaux comptes plan Équipe (5-50 sièges), ~340 signups/mois
**Metric de succès** : taux de comptes à 48h — **lien NSM** : prédicteur le plus fort de passage au statut "équipe active hebdomadaire" à J30
**Baseline** : 55% **Cible** : 72% **Fenêtre** : 4 semaines post-ship
**Guardrails** : tickets support onboarding (+10% max), temps médian jusqu'au premier projet (≤10 min)

## Vérification de l'opportunity

**Outcome visé** : augmenter le taux d'activation 48h de 55% à 72%
**Opportunity retenue** : l'absence de point de départ clair sur un compte vide, pas un manque de fonctionnalités
**Alternatives de problème considérées** : "le produit est trop complexe" (écarté — les utilisateurs activés n'expriment pas cette friction) ; "le pricing crée de l'hésitation" (écarté — le problème apparaît après paiement, pas avant)
**Pourquoi cette opportunity** : convergence des 3 sources de preuve sur le même moment précis (l'écran vide initial), pas sur la complexité générale du produit
**Source discovery** : synthèse des 6 entretiens `/pm-interview-insights`, pas d'OST formel construit pour cette initiative

## Contraintes connues

- Le champ `role` est déjà collecté à l'inscription — pas de nouveau champ requis (cf. FEA-1)
- Le design system existant impose des composants de formulaire multi-étapes déjà construits — le wizard doit les réutiliser plutôt qu'en créer de nouveaux
- Pas de budget pour recrutement CS supplémentaire ce trimestre (contrainte qui a pesé sur l'élimination de l'Approche B en solution exploration)

## Hors scope

- Personnalisation des defaults au-delà de 4 rôles principaux (Chef de projet / Développeur / Designer / Autre) — les rôles plus rares seront couverts par un default générique, pas des variantes dédiées, pour ne pas complexifier le premier build
- Onboarding des comptes Solo (1 siège) — hors périmètre, le problème identifié est spécifique à la dynamique d'équipe (inviter quelqu'un)

## Hypothèses critiques restantes

### USA-1 — Usability
**Lien evidence-register** : EV-4
**Énoncé** : un utilisateur qui voit un projet pré-rempli comprend qu'il peut le modifier, il ne le perçoit pas comme figé
**Preuves actuelles** : aucune — hypothèse à tester en usability test avant généralisation
**Confiance** : intuition
**Méthode de validation** : test utilisateur modéré, 5 participants, avant/après wizard
**Critère de décision** : si ≥4/5 participants modifient le projet pré-rempli sans confusion exprimée, hypothèse confirmée
**Statut** : à tester

## Décisions à arbitrer (PM)

- [x] Rollout : progressif (20% des nouveaux comptes) ou 100% direct — tranché en `/pm-scope`, pas encore arbitré à ce stade
- [ ] Faut-il permettre de sauter le wizard entièrement (utilisateur avancé) ? Recommandation agent : oui, avec un lien "Configurer plus tard" visible mais non mis en avant

## Readiness pour `/pm-scope`

- [x] **Statut = `approved`**
- [x] Persona principal identifié
- [x] Outcome chargé depuis 01-success-metrics.md
- [x] Approche chargée depuis 02-solution-exploration.md
- [x] Contraintes critiques connues
- [x] Hypothèses majeures visibles (USA-1)
- [x] Aucune entrée evidence-register liée n'est `contradicted`
- [x] Décisions bloquantes arbitrées par le PM
