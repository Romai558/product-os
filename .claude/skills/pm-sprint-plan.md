# Skill — /pm-sprint-plan

**Rôle dans le Product OS**

**Phase :** Branche annexe (optionnelle) — après les tickets, avant le build, seulement en contexte squad/Shape Up hybride.
**Question produit :** Comment les tickets validés se répartissent-ils dans le temps, compte tenu de la capacité de l'équipe ?
**Décision ou résultat produit :** Un découpage en sprints (objectif, tickets, dépendances, risques par sprint).

**Décision** : comment les tickets validés se répartissent dans le temps (sprints) compte tenu de la capacité de l'équipe.
**Entrées** : `06-tickets.md` (validés) ; `product-facts.md` ; capacité de l'équipe pour le cycle
**Sortie** : `outputs/specs/[feature]/sprint-plan-YYYY-MM-DD.md` (non numéroté — branche annexe, pas dans le séquencement principal)
**Bloque si** : rien — optionnel, activé seulement en contexte squad/Shape Up hybride
**Met à jour** : rien directement

**Branche annexe du workflow delivery — pas dans le séquencement numéroté principal.** Optionnel par nature (squad qui s'auto-organise vs PM qui anime les rituels) : le forcer dans la chaîne `00`-`08` laisserait un trou de numérotation dans la majorité des usages solo. Prend les tickets shippés et les découpe en sprints exécutables. Anime la cérémonie de sprint planning : priorisation, séquençage, dépendances, capacité équipe.

Utilisé dans un contexte **Shape Up hybride** (6 semaines de build redécoupées en sprints de 2 semaines). En Shape Up pur (équipe qui s'auto-organise), ce skill est optionnel — vérifier avec le Tech Lead.

**Utiliser quand** (`/pm-sprint-plan [chemin tickets]`, après validation des tickets, avant le kick-off du build) :
- Le PM anime les rituels, ou le contexte est Shape Up hybride (6 semaines de build redécoupées en sprints de 2 semaines) — y compris en début de cycle pour caler les 3 sprints.

**Ne pas utiliser quand** :
- La squad s'auto-organise en Shape Up pur → optionnel, vérifier avec le Tech Lead avant de l'imposer.

## Place dans le pipeline

```
06-tickets.md (validés)
  → [branche annexe, si contexte squad/Shape Up hybride]
  → /pm-sprint-plan
  → outputs/specs/[feature]/sprint-plan-YYYY-MM-DD.md (non numéroté)
  → [PM anime le sprint planning avec la squad]
  → Build démarre
  → /pm-release reprend directement après 06-tickets.md, que ce skill ait tourné ou non
```

## Étapes

### 1. Charger les tickets

Lire `06-tickets.md`. Identifier :
- Les must-have (bloquants pour le ship)
- Les should-have (inclus si capacité)
- Les dépendances techniques (ticket B ne peut pas démarrer avant ticket A)
- Les tickets qui nécessitent la run team ou une autre squad

### 2. Évaluer la capacité

Demander au PM (si pas dans le contexte) :
- Nombre de devs disponibles sur le cycle
- Jours off prévus
- Autres charges connues (bugs run team, dette tech, réunions)
- Durée des sprints (2 semaines par défaut Shape Up)

### 3. Séquencer les sprints

Découper le build en sprints. Pour chaque sprint :
- **Objectif sprint** : ce qui doit être livré/démo-able à la fin
- **Tickets inclus** : liste avec estimation rough (S/M/L)
- **Dépendances** : ce qui doit être fait avant pour que ce sprint soit possible
- **Risques** : ce qui peut faire déraper ce sprint

Règles de séquençage :
- Must-have en priorité, sprints 1 et 2
- Should-have en sprint 3 (cool down buffer)
- Les tickets à fort risque technique en sprint 1 — fail fast
- Les tickets avec dépendances externes (run team, autre squad) planifiés tôt

### 4. Identifier les points de synchronisation

- Quels tickets nécessitent un sync avec le Designer en cours de sprint ?
- Quels tickets nécessitent une décision PM en cours de build ?
- Où sont les points de démo intermédiaires ?

### 5. Préparer l'animation du sprint planning

Le PM anime la cérémonie avec la squad. Préparer :
- **L'objectif du cycle** : pourquoi on build ça, quel impact attendu
- **La découpe en sprints** : à présenter et ajuster avec la squad
- **Les questions ouvertes** : ce que la squad doit trancher (choix d'implémentation, estimation)
- **Les règles du jeu** : qui fait quoi si un ticket déborde

### 6. Écrire le sprint plan

`tools/product-os/outputs/specs/[feature]/sprint-plan-YYYY-MM-DD.md`

## Format de sortie

```markdown
# Sprint Plan — [Nom feature / Cycle]

**Cycle** : [date début] → [date fin] (6 semaines build)
**Squad** : [noms ou rôles]
**Capacité** : [X devs × Y jours effectifs]
**Tickets source** : 06-tickets.md

---

## Objectif du cycle

[Pourquoi on build ça — lien avec OKR et PRD]

---

## Sprint 1 — [Dates] — Fondations

**Objectif** : [Ce qui doit être livrable/démo-able]
**Focus** : Tickets à fort risque technique — fail fast

| Ticket | Taille | Dépendances | Assigné |
|---|---|---|---|
| [Titre] | S/M/L | [aucune / ticket X] | [dev] |

**Risques** : [ce qui peut faire déraper]
**Sync PM** : [quand / sur quoi]

---

## Sprint 2 — [Dates] — Core

**Objectif** : [Ce qui doit être livrable/démo-able]

| Ticket | Taille | Dépendances | Assigné |
|---|---|---|---|

**Risques** : ...
**Sync PM** : ...

---

## Sprint 3 — [Dates] — Finalisation + Buffer

**Objectif** : [Ship-ready]
**Focus** : Should-have + polish + buffer débordements sprints 1-2

| Ticket | Taille | Dépendances | Assigné |
|---|---|---|---|

**Risques** : ...

---

## Questions ouvertes pour le sprint planning

- [ ] [Question d'implémentation à trancher avec la squad]
- [ ] [Estimation à affiner ensemble]

## Points de synchronisation

- **Sprint 1, J+5** : démo intermédiaire — valider direction technique
- **Sprint 2, J+3** : sync Designer sur [écran X]
- **Fin Sprint 2** : go/no-go sur les should-have Sprint 3
```

## Règles dures

- **Fail fast en sprint 1** — les tickets les plus risqués techniquement en premier. Mieux vaut savoir tôt que ça bloque.
- **Buffer en sprint 3** — ne jamais remplir le sprint 3 à 100% de capacité. C'est le filet de sécurité des débordements.
- **L'objectif sprint est démo-able** — à la fin de chaque sprint, la squad doit pouvoir montrer quelque chose qui tourne.
- **La squad estime, le PM séquence** — ne pas imposer les tailles S/M/L. Les proposer, laisser la squad corriger.
- **Les dépendances bloquantes en tête** — si ticket B attend ticket A, A est en sprint 1 par défaut.
