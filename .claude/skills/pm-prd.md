# Skill — /pm-prd

**Rôle dans le Product OS**

**Phase :** Delivery (séquencement strict) — étape de consolidation, après commitment gate + success-metrics + solution-exploration.
**Question produit :** Le dossier (problème, outcome, approche retenue, hypothèses restantes) est-il prêt pour l'arbitrage final du PM ?
**Décision ou résultat produit :** Un PRD au statut `draft` → `ready-for-review`, que le PM fait passer à `approved` / `rejected` / `superseded`.

**Décision** : le dossier (problème, outcome, approche retenue, hypothèses restantes) est-il prêt pour l'arbitrage final du PM.
**Entrées** : `00-commitment-gate.md` (commit) ; `01-success-metrics.md` (outcome) ; `02-solution-exploration.md` (approche retenue, validée PM) ; `product-facts.md` ; `product-strategy.md` ; `evidence-register.md`
**Sortie** : `outputs/specs/[feature]/03-prd.md`
**Bloque si** : une entrée `evidence-register.md` liée à l'initiative est `contradicted` → bloque le passage à `ready-for-review` (reste `draft`)
**Met à jour** : `evidence-register.md` (formalise les hypothèses encore ouvertes) ; `decision-log.md` (si retour au commitment gate)

**Étape de consolidation, après le séquencement strict a déjà tranché l'essentiel.** Le PRD ne choisit ni l'outcome (`/pm-success-metrics`) ni l'approche (`/pm-solution-exploration`) — il les **charge et les consolide** en un document arbitrable par le PM. Ne découvre jamais la solution : elle est déjà retenue avant que cette skill ne s'exécute.

Le PRD décrit le problème, charge l'outcome posé par `/pm-success-metrics` et l'approche retenue par `/pm-solution-exploration` (il ne les redéfinit pas), documente les preuves disponibles, les contraintes et les hypothèses critiques restantes.

> **Les agents préparent. Le PM valide et tranche.** Ne jamais passer à `/pm-scope` sans relecture et arbitrage explicite du PM.

**Utiliser quand** (`/pm-prd [initiative committée, approche retenue]`, après `/pm-commitment-gate` + `/pm-success-metrics` + `/pm-solution-exploration`, jamais avant) :
- L'outcome et l'approche sont déjà posés, et il faut consolider le dossier complet pour l'arbitrage PM.

**Ne pas utiliser quand** :
- L'outcome n'est pas encore fixé → `/pm-success-metrics` d'abord.
- Plusieurs approches n'ont pas encore été comparées → `/pm-solution-exploration` d'abord, le PRD ne doit jamais découvrir la solution.
- On veut découper en user stories / edge cases → c'est `/pm-scope`, qui vient après un PRD `approved`.

## Pré-requis

**Le gate de preuve a déjà eu lieu au commitment gate. Le choix de solution a déjà eu lieu à `/pm-solution-exploration`.** `/pm-prd` ne re-bloque pas sur "preuve insuffisante" ni ne rediscute l'approche — seule exception : si une entrée `evidence-register.md` liée à l'initiative passe à `contradicted` pendant la rédaction du PRD (découverte tardive), voir § Statuts plus bas.

## Exemple

[`examples/onboarding-saas/03-prd.md`](../../examples/onboarding-saas/03-prd.md) : PRD `approved` consolidant l'outcome (55%→72%) et l'approche (wizard interactif) déjà tranchés en amont, sans les rediscuter.

## Place dans le pipeline

```
00-commitment-gate.md (commit) → 01-success-metrics.md (outcome) → 02-solution-exploration.md (approche retenue)
  → /pm-prd
  → outputs/specs/[feature]/03-prd.md
  → [PM relit et arbitre]
  → /pm-scope
```

## Cycle des hypothèses (discovery → solution exploration → PRD)

Les hypothèses ne naissent pas dans `/pm-prd` — elles y sont **consolidées**, et depuis deux sources distinctes selon leur nature :

```
Dès /pm-prioritize :
  Problem Statement initial (= le candidat formulé en problème/outcome)
  + hypothèse(s) de problème initiales (première entrée evidence-register.md)
Pendant la boucle discovery (/pm-interview-insights, artefacts sélectionnés, reformulations) :
  hypothèses de VALUE testées, précisées, confirmées ou infirmées — evidence-register.md mis à jour
Au commitment gate :
  toute hypothèse Value encore critical-gap ou contradicted bloque le commit
Dans /pm-solution-exploration (une fois committé, une approche choisie) :
  hypothèses de USABILITY/FEASIBILITY/VIABILITY typées PAR APPROCHE
  (elles n'existent pas avant qu'une solution concrète soit proposée)
Dans /pm-prd (consolidation finale) :
  Problem Statement consolidé (Value, hérité de la discovery)
  + approche retenue (Usability/Feasibility/Viability, héritées de /pm-solution-exploration)
  + preuves confirmées
  + hypothèses critiques restantes (VAL/USA/FEA/VIA-n, typées) — formalisation,
    pas génération : le gros du travail est déjà fait en amont
```

**Value s'évalue au niveau du problème** (l'utilisateur veut-il que ça change ?), **Usability/Feasibility/Viability au niveau de la solution retenue** (peut-on construire et faire fonctionner cette approche précise ?) — deux altitudes différentes, deux origines différentes dans le pipeline. `/pm-prd` ne les invente pas, il les rassemble.

Si aucune hypothèse initiale n'existe en entrée (brief direct, pas de passage par `/pm-prioritize`), les formuler à l'étape 3 plutôt que de sauter l'exercice.

## Étapes

### 1. Charger le contexte

Lire `product-facts.md` et `product-strategy.md`. Identifier :
- Le persona principal concerné
- Les features existantes liées
- Les décisions structurantes et contraintes connues
- Les OKRs ou outcomes liés

Charger aussi la **confiance globale** posée par `00-commitment-gate.md` (Low/Medium/High + justification) — héritée telle quelle, jamais recalculée ici.

### 2. Vérifier l'état des preuves dans le registre

Lire `evidence-register.md` pour les entrées liées à cette initiative.

**Ne jamais transformer directement une demande de solution en problème validé.**

Exemple :
- Demande : "Ajouter un chatbot dans l'onboarding"
- Problème à vérifier : "Les utilisateurs abandonnent l'onboarding parce qu'ils ne comprennent pas les prochaines étapes"

Si une entrée liée est passée à `contradicted` depuis le commit : voir § Statuts. Si une entrée est `critical-gap` (nouvelle, pas bloquée en amont) : la lister explicitement en étape 11, avec un arbitrage PM requis — ça n'empêche pas d'écrire le PRD.

### 3. Formuler le problème

- Quel utilisateur est concerné (persona précis)
- Quelle friction concrète et observable il rencontre (pas interprétée)
- Dans quel contexte elle apparaît
- Quelles conséquences elle produit
- Pourquoi maintenant — catégoriser le signal :
  - **User signal** : fréquence, sévérité, répétition, abandon, friction
  - **Business signal** : revenu, conversion, churn, coût, marge
  - **Strategic signal** : priorité explicitement décidée
  - **Constraint signal** : réglementation, date butoir, risque, dépendance

Un simple rattachement à un OKR ne suffit pas seul — nommer le type de signal.

### 4. Vérifier l'opportunity (pas d'OST complet ici)

L'Opportunity-Solution Tree (Torres, 4 niveaux) est un outil de **discovery**, pas de rédaction de PRD. Si un OST a déjà été fait ailleurs, charger son résultat. Sinon, faire uniquement une vérification légère :

- Outcome visé
- Opportunity retenue
- Alternatives de problème considérées
- Raison du choix
- Source éventuelle (fichier OST ou résultats de discovery)

**Ne pas construire un OST complet dans `/pm-prd`** — la comparaison de solutions a déjà eu lieu dans `/pm-solution-exploration`. Si l'agent doit encore comparer des opportunities de problème à ce stade, le travail est encore en discovery (retour à la boucle, pas de PRD prématuré).

### 5. Documenter les preuves

Pour chaque preuve : source, signal observé, niveau de confiance, statut (`sufficient`/`weak-but-testable` — les `critical-gap`/`contradicted` non résolus sont traités à l'étape 2). Réutiliser la taxonomie déjà définie dans le wiki (`CLAUDE.md` § Provenance) : `documented / research / verbal / intuition`.

### 6. Charger l'outcome (pas le redéfinir)

Lire `01-success-metrics.md`. Reprendre tel quel :
- Comportement à modifier
- Population concernée
- Metric de succès + lien NSM
- Baseline, cible, fenêtre de mesure
- Guardrails

**Ne jamais redéfinir ces valeurs dans le PRD** — si elles semblent fausses ou obsolètes, renvoyer à `/pm-success-metrics` pour révision, ne pas corriger en silence dans le PRD.

### 7. Charger l'approche retenue (pas la redéfinir)

Lire `02-solution-exploration.md`. Reprendre tel quel :
- Approche recommandée + pourquoi
- Niveau de risque accepté
- Raison d'écarter les alternatives (résumé, pas le détail complet — renvoyer au fichier source)

**Ne jamais rediscuter le choix d'approche dans le PRD** — si l'approche semble fausse ou obsolète (nouvelle contrainte découverte, hypothèse USA/FEA/VIA contredite), renvoyer à `/pm-solution-exploration` pour révision, ne pas trancher en silence dans le PRD.

### 8. Identifier les contraintes connues

Réglementaires, business, techniques, données disponibles, opérationnelles, design system, dépendances, décisions structurantes.

### 9. Définir le hors-scope

Ce qui ne sera pas traité dans cette itération, et pourquoi. Ne pas y placer artificiellement un élément indispensable juste pour réduire la taille apparente du projet.

### 10. Consolider les hypothèses critiques restantes — numérotées et typées

Format **TYPE-n** (type fixe, numéro séquentiel par type) :

- **VAL-n — Value** : héritée de la discovery/du commitment gate — l'utilisateur veut-il réellement cette amélioration ?
- **USA-n — Usability** : héritée de `/pm-solution-exploration` — l'utilisateur peut-il comprendre et utiliser l'approche retenue ?
- **FEA-n — Feasibility** : héritée de `/pm-solution-exploration` — peut-on la construire dans les contraintes existantes ?
- **VIA-n — Viability** : héritée de `/pm-solution-exploration` — compatible business, légal, opérations ?

Ne garder que les hypothèses encore ouvertes — celles déjà confirmées passent dans "Preuves disponibles" (étape 5), pas ici. Pour chaque hypothèse restante, préciser : ID `evidence-register.md` lié, énoncé testable, preuves actuelles (même partielles), niveau de confiance, méthode de validation, critère de décision, statut. **Ce n'est pas un exercice de génération** — USA/FEA/VIA sont déjà typées dans `02-solution-exploration.md`, cette étape les reprend et vérifie qu'aucune n'a été oubliée. Une hypothèse réellement nouvelle qui émerge en consolidant peut être ajoutée ici, mais l'essentiel du travail est déjà fait en amont.

### 11. Lister les arbitrages PM

Décisions manquantes, tradeoffs, risques, choix bloquants, y compris tout `critical-gap` découvert en cours de rédaction (étape 2). L'agent prépare les options, le PM tranche.

### 12. Écrire le PRD

`tools/product-os/outputs/specs/[feature]/03-prd.md`

Statut initial : `draft`.

### Transitions de statut — droits agent vs PM

| Statut | Qui le pose | Depuis |
|---|---|---|
| `draft` | Agent | Création initiale |
| `ready-for-review` | Agent | Une fois `draft` complet et aucune entrée `evidence-register.md` liée n'est `contradicted` — signale au PM que c'est prêt à relire |
| `approved` | **PM uniquement** | `ready-for-review` — jamais posé par l'agent |
| `rejected` | **PM uniquement** | `ready-for-review` — le PM tranche que le sujet ne mérite pas delivery |
| `superseded` | **PM uniquement** | N'importe quel statut — un nouveau PRD remplace celui-ci |

**L'agent ne pose jamais `approved`, `rejected` ou `superseded`** — ce sont des arbitrages PM, pas des sorties d'agent.

## Statuts de preuve — effet sur ce PRD

- **`sufficient` / `weak-but-testable`** : hypothèse ouverte normale, listée en étape 10, ne bloque rien.
- **`critical-gap` découvert pendant la rédaction** (pas intercepté au commitment gate ou à la solution exploration) : listé comme hypothèse critique + arbitrage PM obligatoire (étape 11) — n'empêche **pas** d'écrire ou de faire passer le PRD en `ready-for-review`.
- **`contradicted`** : bloque le passage à `ready-for-review`. Le PRD reste `draft`. Action requise : retour à `/pm-commitment-gate` (si la remise en cause touche le problème) ou `/pm-solution-exploration` (si elle touche l'approche) pour re-décision, entrée `decision-log.md` créée pour tracer la re-décision.

## Format de sortie

```markdown
# PRD — [Nom du problème ou outcome]

**Date** : YYYY-MM-DD
**Persona principal** : [profil]
**Outcome / OKR lié** : [outcome ou KR]
**Statut** : draft | ready-for-review | approved | rejected | superseded
**Niveau de preuve du problème** : documented | research | verbal | intuition
**Commitment gate** : 00-commitment-gate.md (commit, [date])
**Confiance globale (héritée)** : Low / Medium / High — cf. 00-commitment-gate.md
**Outcome source** : 01-success-metrics.md
**Approche source** : 02-solution-exploration.md

## Résumé

[3-5 lignes : le problème, pour qui, pourquoi maintenant, résultat recherché, approche retenue]

## Problème

**Qui** : [persona précis]
**Friction observable** : [comportement, difficulté ou perte concrète]
**Contexte d'apparition** : [quand, dans quel parcours]
**Conséquence** : [impact utilisateur ou business]
**Pourquoi maintenant** : [user / business / strategic / constraint signal]

## Preuves disponibles

| Source | Signal observé | Confiance | Statut evidence-register | Limites |
|---|---|---|---|---|
| [source] | [signal] | documented/research/verbal/intuition | sufficient/weak-but-testable | [limite éventuelle] |

## Outcome (chargé depuis 01-success-metrics.md)

**Comportement à modifier** : ...
**Population** : ...
**Metric de succès** : ... — **lien NSM** : ...
**Baseline** : ... **Cible** : ... **Fenêtre** : ...
**Guardrails** : ...

## Approche retenue (chargée depuis 02-solution-exploration.md)

**Approche** : [nom court]
**Pourquoi** : [résumé — détail complet dans 02-solution-exploration.md]
**Niveau de risque accepté** : ...
**Alternatives écartées** : [renvoi au tableau d'élimination de 02-solution-exploration.md, pas répété ici]

## Vérification de l'opportunity

**Outcome visé** : [outcome]
**Opportunity retenue** : [besoin ou douleur]
**Alternatives de problème considérées** : [autres lectures possibles du problème — pas les alternatives de solution, déjà dans 02-solution-exploration.md]
**Pourquoi cette opportunity** : [preuves ou raisonnement]
**Source discovery** : [fichier OST ou résultats de discovery si existant]

## Contraintes connues

- [contrainte réglementaire, technique, business ou opérationnelle]
- [dépendance connue]
- [décision structurante]

## Hors scope

- [élément exclu] — [raison]

## Hypothèses critiques restantes

### VAL-1 — Value
**Lien evidence-register** : EV-n
**Énoncé** : [hypothèse testable]
**Preuves actuelles** : [même partielles, ou "aucune"]
**Confiance** : documented | research | verbal | intuition
**Méthode de validation** : [comment on teste]
**Critère de décision** : [ce qui ferait basculer confirmée/infirmée]
**Statut** : à tester | partiellement confirmée | confirmée | infirmée

### USA-1 — Usability
[même structure — héritée de 02-solution-exploration.md]

### FEA-1 — Feasibility
[même structure — héritée de 02-solution-exploration.md]

### VIA-1 — Viability
[même structure — héritée de 02-solution-exploration.md]

## Décisions à arbitrer (PM)

- [ ] [question ouverte]
- [ ] [tradeoff]
- [ ] [critical-gap découvert en cours de rédaction, si applicable]

## Readiness pour `/pm-scope`

- [ ] **Statut = `approved`**
- [ ] Persona principal identifié
- [ ] Outcome chargé depuis 01-success-metrics.md
- [ ] Approche chargée depuis 02-solution-exploration.md
- [ ] Contraintes critiques connues
- [ ] Hypothèses majeures visibles (VAL/USA/FEA/VIA-n)
- [ ] Aucune entrée evidence-register liée n'est `contradicted`
- [ ] Décisions bloquantes arbitrées par le PM
```

## Règles dures

- **Le gate de preuve a lieu au commitment gate, le choix de solution a lieu à `/pm-solution-exploration` — pas ici.** `/pm-prd` ne bloque plus sur "preuve insuffisante" en bloc et ne rediscute jamais l'approche retenue. Seul `contradicted` bloque, et seulement le passage à `ready-for-review`.
- **Ne jamais transformer directement une demande de solution en problème validé.**
- **Un problème ou outcome cohérent = un PRD** — ne jamais regrouper plusieurs problèmes indépendants dans le même document.
- **Pas d'OST complet ni de comparaison de solutions dans `/pm-prd`** — la première est un outil de discovery, la seconde le rôle de `/pm-solution-exploration`.
- **L'outcome est chargé depuis `01-success-metrics.md`, l'approche depuis `02-solution-exploration.md`, jamais redéfinis ici** — toute correction va dans la skill source, pas dans le PRD.
- **La confiance globale est héritée du commitment gate, jamais recalculée** — si elle semble obsolète, retourner à `/pm-commitment-gate`, ne pas la réévaluer en silence dans le PRD.
- **Toute preuve doit porter un niveau de confiance** — réutiliser `documented/research/verbal/intuition`.
- **Hypothèses typées avec identifiant séquentiel par type (VAL-n/USA-n/FEA-n/VIA-n), liées à un ID `evidence-register.md`** — Value hérité de la discovery, Usability/Feasibility/Viability hérités de `/pm-solution-exploration`. `/pm-prd` consolide, ne génère pas de nouvelles hypothèses USA/FEA/VIA sauf découverte tardive réelle.
- **Pas de user stories, acceptance criteria ou découpage technique** — appartient à `/pm-scope`.
- **Ne pas placer artificiellement hors scope un élément indispensable** juste pour réduire la taille apparente du projet.
- **Lister explicitement les décisions manquantes** — le PM arbitre, pas l'agent.
- **Une entrée `contradicted` bloque `ready-for-review`** et déclenche un retour à `/pm-commitment-gate` ou `/pm-solution-exploration` selon ce qu'elle remet en cause, tracé dans `decision-log.md`.
- **Jamais de passage à `/pm-scope` sans validation PM explicite** (statut `approved`).
