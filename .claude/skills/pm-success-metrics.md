# Skill — /pm-success-metrics

**Rôle dans le Product OS**

**Phase :** Delivery (séquencement strict) — première étape, juste après le commitment gate.
**Question produit :** Que veut dire "réussir" concrètement pour cette initiative, avant que la solution ne soit conçue ?
**Décision ou résultat produit :** L'outcome complet (comportement, population, baseline, cible, fenêtre, métrique, guardrails), chargé tel quel par le PRD.

**Décision** : ce que "réussir" veut dire concrètement pour cette initiative (l'outcome complet), avant que la solution ne soit conçue.
**Entrées** : `00-commitment-gate.md` (commit) ; `product-strategy.md` (NSM) ; `evidence-register.md`
**Sortie** : `outputs/specs/[feature]/01-success-metrics.md`
**Bloque si** : commitment gate ≠ `commit` ; NSM au statut "à définir" ; comportement/population non identifiables
**Met à jour** : rien directement — source de vérité chargée par `/pm-prd` et vérifiée par `/pm-data-analysis`

**Entre `/pm-commitment-gate` et `/pm-prd` — première étape du séquencement strict.** Définit l'outcome complet d'une initiative dont le commitment gate a dit `commit`, avant que `/pm-prd` ne rédige le problème consolidé. Le PRD **charge** cet outcome, il ne le redéfinit pas — inverse de l'ancien ordre où le PRD posait des métriques directionnelles avant que success-metrics ne vienne les affiner.

> Pourquoi avant le PRD : un problème qu'on s'engage à traiter sans savoir ce que "ça marche" veut dire concrètement (comportement visé, population, baseline, cible, fenêtre) invite à écrire un PRD qui rationalise une solution déjà choisie plutôt qu'un outcome mesurable. Poser l'outcome en premier force la discipline inverse.

**Utiliser quand** (`/pm-success-metrics [initiative committée]`) :
- Juste après que `/pm-commitment-gate` a rendu la décision `commit` — avant tout PRD. Si le commitment gate n'a pas rendu `commit`, refuser de s'exécuter : renvoyer vers la boucle discovery (`investigate`) ou vers l'archivage (`kill`).

**Ne pas utiliser quand** :
- On cherche déjà à comparer des approches de solution → c'est `/pm-solution-exploration`, qui vient après et charge cet outcome, pas l'inverse.

## Exemple

[`examples/onboarding-saas/01-success-metrics.md`](../../examples/onboarding-saas/01-success-metrics.md) : outcome posé pour l'activation onboarding (55% → 72% en 4 semaines), chargé tel quel ensuite par `02-solution-exploration.md` et `03-prd.md` sans être redéfini.

## Place dans le pipeline

```
00-commitment-gate.md (décision commit)
  → /pm-success-metrics
  → outputs/specs/[feature]/01-success-metrics.md
  → /pm-solution-exploration (compare les approches pour atteindre cet outcome)
  → /pm-prd (charge l'outcome et l'approche retenue, ne les redéfinit pas)
  → ... → /pm-tickets
  → (post-ship) /pm-data-analysis vérifie l'objectif posé ici
```

## Étapes

### 1. Charger la North Star Metric

Lire `product-strategy.md § North Star Metric`.

- **Si `Statut = à définir`** : s'arrêter. Demander à Romain de poser la NSM au niveau produit (pas au niveau feature — une NSM se définit une fois, pas à chaque `/pm-success-metrics`). Ne jamais improviser une NSM de substitution pour continuer.
- **Si NSM posée** : la charger comme référence pour l'étape 3.

### 2. Comportement à modifier et population

- **Comportement** : l'action précise que l'utilisateur devrait faire différemment (pas "utiliser plus la feature" — un verbe d'action observable)
- **Population concernée** : quel segment exact, avec sa taille si connue (depuis `product-facts.md` ou `evidence-register.md`)

Ces deux champs distinguent l'outcome recherché d'une métrique orpheline — sans eux, une métrique de succès flotte sans référent concret.

### 3. Metric de succès de l'initiative

- Une métrique observable, spécifique à cette initiative
- Pas une métrique orpheline : doit se relier explicitement à la NSM ou à une des sous-métriques associées (comment cette initiative la fait bouger ?)
- Si aucun lien plausible avec la NSM n'existe, le nommer explicitement — ça questionne la légitimité de l'initiative elle-même

### 4. Baseline

- Valeur actuelle de la métrique de succès, si connue
- **Si la valeur exacte est inconnue** : ne pas bloquer — écrire une estimation explicite marquée comme hypothèse (`confidence: verbal/intuition`), à mesurer réellement à J0. C'est une incertitude acceptable, pas un manque d'information obligatoire.

### 5. Metrics garde-fou

- Contre-indicateurs à surveiller : ce que cette initiative pourrait dégrader en optimisant sa propre métrique
- Minimum 1 garde-fou — si aucun n'émerge, le dire explicitement plutôt que sauter l'étape

### 6. Objectif SMART et fenêtre de mesure

- Cible chiffrée sur la metric de succès
- Fenêtre de mesure explicite (ex : 4 semaines après ship)
- Spécifique, Mesurable, Atteignable, Relié (à la NSM), Temporel

### 7. Source de mesure

- Où et comment cette métrique sera effectivement mesurée
- **Flag si aucun MCP analytics n'est branché** (même principe que Reach dans `/pm-prioritize`) : l'objectif reste posé, mais la mesure sera manuelle tant que la donnée n'est pas câblée — c'est une information souhaitable absente, pas un blocage

### 8. Écrire l'analyse

`tools/product-os/outputs/specs/[feature]/01-success-metrics.md`

## Format de sortie

```markdown
# Success Metrics — [Nom initiative] — [Date]

**Commitment gate source** : 00-commitment-gate.md (commit)
**North Star Metric produit** : [chargée depuis product-strategy.md]

## Outcome

- **Comportement à modifier** : [verbe d'action observable]
- **Population concernée** : [segment précis] — [taille si connue]

## Metric de succès

- **Métrique** : [nom + définition précise]
- **Lien avec la NSM** : [comment cette initiative la fait bouger — ou "aucun lien identifié" si c'est le cas]

## Baseline

- **Valeur** : [chiffre connu] ou [estimation — hypothèse explicite, confidence: verbal/intuition, à mesurer à J0]

## Metrics garde-fou

- **[Contre-indicateur]** : [ce qui pourrait se dégrader] — seuil d'alerte : [valeur]

## Objectif SMART

- **Cible** : [valeur chiffrée]
- **Fenêtre de mesure** : [date ou délai post-ship]
- **Mesuré via** : [source de donnée] — [flag si mesure manuelle par défaut de MCP branché]

## Statut

- [ ] Objectif validé par le PM
- [ ] Repris par /pm-solution-exploration (compare les approches pour l'atteindre)
- [ ] Repris par /pm-prd (charge l'outcome sans le redéfinir)
- [ ] Repris par /pm-data-analysis en post-ship
```

## Règles dures

- **Commitment gate ≠ `commit` = refus d'exécution**, renvoyer vers la boucle discovery ou l'archivage selon la décision.
- **Jamais improviser de NSM au niveau feature** — si `product-strategy.md` n'en a pas, s'arrêter et le signaler. Bloquant.
- **Comportement et population obligatoires** — information structurelle, pas une preuve à collecter : sans eux, bloquer.
- **Baseline valeur inconnue = incertitude acceptable** — continuer avec une estimation marquée comme hypothèse, ne jamais bloquer sur ce point seul.
- **Toute metric de succès se relie à la NSM ou nomme explicitement l'absence de lien.**
- **Au moins 1 metric garde-fou obligatoire**, même si c'est pour dire qu'aucune n'a été identifiée.
- **Objectif chiffré et fenêtre de mesure explicite** — pas de "on verra si ça s'améliore".
- **Source de mesure non câblée = warning, jamais bloquant** — l'objectif reste posé, la mesure sera manuelle en attendant.
- **Ce fichier est input direct de `/pm-data-analysis`** — pas de reformulation entre les deux, le post-ship vérifie exactement ce qui est posé ici.
