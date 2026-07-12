# Skill — /pm-tickets

**Décision** : comment le travail se découpe en unités assignables à la Tech.
**Entrées** : `04-scope.md` (tradeoffs arbitrés) ; `03-prd.md` ; `05-prototype.md` ; `product-facts.md`
**Sortie** : `outputs/specs/[feature]/06-tickets.md` + tickets Linear MCP
**Bloque si** : un tradeoff du scope reste `[ ] à arbitrer` ; une entrée `evidence-register.md` liée à l'initiative est passée `contradicted` depuis la construction du prototype
**Met à jour** : rien directement (Linear MCP)

**Étape 3 du workflow delivery.** Transforme un scope validé par le PM en tickets d'exécution prêts pour la Tech : contexte, attendu, critères d'acceptance, estimation rough.

Intégration Linear via MCP : les tickets sont créés directement dans le projet Linear sans copier-coller. La PRD et les insights Notion sont référencés en lien.

> Les tickets sont le contrat PM → Tech. Chaque ticket doit être autoportant — la Tech ne doit pas avoir à demander le PRD pour comprendre ce qu'elle build.

## Déclencheur

- `/pm-tickets [chemin scope validé]`
- Après relecture et arbitrage PM du scope (`04-scope.md`)

## Pré-requis

- `outputs/specs/[feature]/04-scope.md` — validé par le PM (tradeoffs arbitrés)
- `outputs/specs/[feature]/03-prd.md` — pour le contexte business
- `outputs/specs/[feature]/05-prototype.md` — vérification post-construction des hypothèses (§ ci-dessous)
- `tools/product-os/context/product-facts.md` — stack tech et conventions

**Gate solution encore valide** : si `05-prototype.md` signale une hypothèse VAL/USA passée `contradicted` dans `evidence-register.md`, refuser de s'exécuter — retour à `/pm-prd` (ou `/pm-commitment-gate` si la remise en cause est profonde) avant de reprendre le ticketing. Ne jamais transformer un prototype en tickets si la solution qu'il documente ne répond plus au problème validé.

## Place dans le pipeline

```
04-scope.md (validé PM)
  → /pm-tickets
  → outputs/specs/[feature]/06-tickets.md
  → [PM relit — valide les critères d'acceptance]
  → MCP Linear : création directe des tickets dans le projet
  → MCP Notion : lien vers PRD + insights dans chaque ticket
```

## Étapes

### 1. Charger le scope, le PRD et le prototype

Lire `04-scope.md` + `03-prd.md` + `05-prototype.md`. Vérifier que tous les tradeoffs sont arbitrés (aucune case `[ ] à arbitrer` restante) et qu'aucune hypothèse VAL/USA n'a été signalée `contradicted` par le prototype. Si l'un ou l'autre bloque, stopper et le signaler.

### 2. Décomposer en tickets

Un ticket = une unité de travail livrable et testable indépendamment.
- Commencer par les tickets bloquants (dépendances)
- Séparer front / back / data si la stack le justifie
- Ne pas créer de tickets de "refacto" dans ce workflow — c'est un sujet séparé

### 3. Pour chaque ticket

- **Titre** : verbe d'action + objet (ex: "Afficher le statut ETA dans la fiche commande")
- **Contexte** : pourquoi on fait ça (1 phrase, lien au PRD)
- **Attendu fonctionnel** : ce que l'utilisateur voit / fait / obtient
- **Critères d'acceptance** : format Given / When / Then (min 2, max 5)
- **Hors scope de ce ticket** : ce qu'on ne fait pas ici
- **Estimation rough** : S (< 1j) / M (1-3j) / L (3-5j) / XL (> 5j, à découper)

### 4. Ordre de séquençage

Numéroter les tickets dans l'ordre de dev recommandé, en respectant les dépendances identifiées dans le scope.

### 5. Écrire les tickets

`tools/product-os/outputs/specs/[feature]/06-tickets.md`

### 6. Pousser dans Linear via MCP

Pour chaque ticket, appeler le MCP Linear pour créer le ticket dans le projet correspondant :
- Titre + description formatés
- Lien vers le PRD Notion en description
- Label feature + estimation
- Assignation si connue

Demander confirmation à Romain avant de créer dans Linear (irréversible sans accès admin).

## Format de sortie

```markdown
# Tickets — [Nom feature]

**Scope source** : 04-scope.md
**Date** : YYYY-MM-DD
**Estimation totale** : [S+M+L sommés]

---

## [01] [Titre du ticket]

**Contexte** : [Pourquoi — lien au PRD en 1 phrase]
**Taille** : S / M / L / XL

### Attendu fonctionnel
[Ce que l'utilisateur voit ou fait]

### Critères d'acceptance
- Given [contexte], When [action], Then [résultat attendu]
- Given ..., When ..., Then ...

### Hors scope de ce ticket
- ...

---

## [02] [Titre du ticket]
...
```

## Règles dures

- **Aucun ticket sans critères d'acceptance** — "ça marche" n'est pas un critère.
- **Stopper si des tradeoffs ne sont pas arbitrés** dans le scope — ne pas inventer une décision.
- **Stopper si une hypothèse VAL/USA est `contradicted`** depuis la construction du prototype — retour PRD/commitment gate obligatoire, jamais de ticketing sur une solution invalidée.
- **XL = à découper obligatoirement** — un ticket XL est un scope, pas un ticket.
- **Le contexte business est obligatoire** — la Tech doit comprendre le pourquoi, pas juste le quoi.
- **Anti-fabrication** : si le scope est ambigu sur un point, noter `[AMBIGU — à clarifier avec PM]` plutôt que supposer.
