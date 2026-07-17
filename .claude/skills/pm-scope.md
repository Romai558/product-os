# Skill — /pm-scope

**Rôle dans le Product OS**

**Phase :** Delivery (séquencement strict) — étape 2, après le PRD approuvé.
**Question produit :** Quelles unités de valeur livrer, dans quel ordre, avec quels tradeoffs et risques assumés ?
**Décision ou résultat produit :** User stories priorisées + critères d'acceptation Gherkin + pre-mortem, tradeoffs arbitrés par le PM.

**Décision** : quelles unités de valeur livrer, dans quel ordre, avec quels tradeoffs et risques assumés.
**Entrées** : `03-prd.md` (approved) ; `product-facts.md` ; `evidence-register.md`
**Sortie** : `outputs/specs/[feature]/04-scope.md`
**Bloque si** : PRD ≠ `approved`
**Met à jour** : rien directement (tradeoffs arbitrés restent dans le fichier lui-même)

**Étape 2 du workflow delivery.** Transforme un PRD validé par le PM en scope de delivery structuré : user stories, edge cases, dépendances, tradeoffs.

> Input obligatoire = PRD **validé**. Ne pas lancer sur un draft non arbitré.

**Utiliser quand** (`/pm-scope [chemin PRD validé]`, après relecture et arbitrage PM du PRD) :
- Le PRD est `approved` — l'ordre `/pm-commitment-gate` → `/pm-success-metrics` → `/pm-solution-exploration` → `/pm-prd` → `/pm-scope` garantit que l'outcome et l'approche sont déjà posés, pas besoin de re-vérifier séparément.

**Ne pas utiliser quand** :
- Le PRD n'est pas encore `approved` → attendre l'arbitrage PM, ne pas lancer sur un draft.
- On cherche encore à comparer des approches de solution → c'est `/pm-solution-exploration`, en amont.

## Place dans le pipeline

```
03-prd.md (statut approved, outcome chargé)
  → /pm-scope
  → outputs/specs/[feature]/04-scope.md
  → [PM relit — valide les tradeoffs]
  → /pm-prototype
```

## Étapes

### 1. Relire le PRD et le contexte

Charger le PRD validé + `product-facts.md`. Identifier les contraintes qui s'appliquent (stack tech, décisions structurantes, hors scope).

### 2. User stories

Format : **En tant que [persona], je veux [action] pour [bénéfice].**

- Une story = une unité de valeur livrable indépendamment
- Pas de story technique (pas "en tant que dev, je veux une API")
- Ordonner par priorité décroissante (ce sans quoi la feature ne tient pas en premier)

### 2.5 Critères d'acceptation — Gherkin

Pour chaque user story **must-have**, rédiger les critères d'acceptation en Gherkin.

Format :
```
Scenario: [titre du scénario]
  Given [contexte / précondition]
  When [action de l'utilisateur]
  Then [résultat observable attendu]
  And [résultat complémentaire si nécessaire]
```

- Minimum 1 scénario nominal (happy path) par story must-have
- Ajouter les scénarios d'erreur pour les edge cases critiques
- Rester au niveau comportement observable — pas d'implémentation technique
- Ces scénarios deviennent les tests d'acceptance QA

### 3. Edge cases

Pour chaque story principale : lister les cas limites, états vides, erreurs, comportements inattendus. Ce sont les trous que la Tech va trouver en dev — mieux vaut les voir en amont.

### 4. Dépendances

- **Internes** : features existantes impactées, équipes à aligner (CS, Sales, Data)
- **Techniques** : API tierces, migrations de données, contraintes infra
- **Séquençage** : ce qui doit être fait avant pour que cette feature soit possible

### 5. Tradeoffs

Les choix non évidents où plusieurs options existent. Format :
- **Option A** : [description] — avantage : X, risque : Y
- **Option B** : [description] — avantage : X, risque : Y
- **Recommandation agent** : [option] — [justification courte]
- **Décision PM** : [ ] à arbitrer

### 5.5 Pre-mortem (Tigers / Paper Tigers / Elephants)

Imaginer que la feature a échoué. Pourquoi ? Classifier les risques identifiés :

- **Tigers** (risque probable + impact fort) : à adresser immédiatement, blocker potentiel. Action concrète associée.
- **Paper Tigers** (risque qui fait peur mais probabilité faible) : monitorer, ne pas sur-investir en mitigation. Nommer pour ne pas s'en distraire.
- **Elephants** (tout le monde le sait, personne n'en parle) : nommer explicitement. Ce sont souvent les risques les plus dangereux car ils s'accumulent en silence.

Minimum 1 risque par catégorie. Si rien n'émerge dans une catégorie → le nommer ("aucun risque Paper Tiger identifié").

### 6. Écrire le scope

`tools/product-os/outputs/specs/[feature]/04-scope.md`

## Format de sortie

```markdown
# Scope — [Nom feature]

**PRD source** : 03-prd.md
**Date** : YYYY-MM-DD
**Statut** : draft — en attente validation PM

## User Stories

### Must have (sans ça la feature ne tient pas)

- [ ] En tant que [persona], je veux [action] pour [bénéfice]

  ```gherkin
  Scenario: [happy path]
    Given [précondition]
    When [action]
    Then [résultat attendu]

  Scenario: [cas d'erreur]
    Given [précondition]
    When [action qui échoue]
    Then [comportement attendu en erreur]
  ```

### Should have

- [ ] En tant que [persona], je veux [action] pour [bénéfice]

  ```gherkin
  Scenario: [happy path]
    Given [précondition]
    When [action]
    Then [résultat attendu]
  ```

### Nice to have (scope V2)
- [ ] ...

### Won't have (explicitement hors scope)
- [Ce qu'on ne fera pas dans cette itération] — [pourquoi, pour éviter que ça revienne sans arbitrage]

## Edge Cases

| Story | Edge case | Comportement attendu |
|---|---|---|
| [story] | [cas limite] | [ce qu'il doit se passer] |

## Dépendances

### Internes
- ...

### Techniques
- ...

### Séquençage
- [X doit être fait avant Y]

## Tradeoffs à arbitrer (PM)

### [Tradeoff 1 — titre]
- Option A : ... — avantage : ..., risque : ...
- Option B : ... — avantage : ..., risque : ...
- Recommandation : Option [X] car [raison]
- **Décision PM** : [ ]

## Pre-mortem

### Tigers (à traiter maintenant)
- **[Risque]** : [description] — Action : [mitigation concrète]

### Paper Tigers (à surveiller, pas à sur-traiter)
- **[Risque]** : [description] — Pourquoi moins probable qu'il n'y paraît

### Elephants (tout le monde sait, personne ne dit)
- **[Risque]** : [description] — Comment on l'adresse ou on l'accepte explicitement
```

## Règles dures

- **PRD non `approved` = refus d'exécution**, renvoyer vers l'arbitrage PM du PRD. L'outcome est garanti déjà posé par l'ordre du pipeline (`/pm-commitment-gate` → `/pm-success-metrics` → `/pm-prd` → ici) — pas de re-check séparé nécessaire.
- **Hypothèse `weak-but-testable` liée à un tradeoff FEA/VIA** : la noter explicitement dans le tableau des tradeoffs, ne bloque pas l'exécution.
- **Won't have nommé explicitement** — équivalent du W de MoSCoW. Ne jamais laisser du hors-scope implicite : ça revient sans arbitrage au sprint suivant.
- **Pas de story technique** dans les must-have — les choix d'implémentation appartiennent à la Tech.
- **Gherkin obligatoire sur les must-have** — au minimum 1 scénario nominal + 1 scénario d'erreur par story. Les should-have = 1 scénario nominal suffit.
- **Chaque edge case a un comportement attendu défini** — sinon c'est une décision masquée.
- **Les tradeoffs sont nommés explicitement** — pas de choix par défaut silencieux.
- **Les dépendances bloquantes sont en tête** — ne pas enfouir ce qui peut tout bloquer.
- **Pre-mortem obligatoire** — au moins 1 risque par catégorie (Tiger / Paper Tiger / Elephant). Si une catégorie est vide, le dire explicitement.
- **Elephants nommés en premier** lors de la relecture PM — ce sont eux qui créent les surprises en dev.
