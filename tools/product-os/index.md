# Product OS — Index

> Workflow PM complet orchestré par agents. Skills dans `.claude/skills/pm-*.md`.
> Mémoire organisationnelle : `tools/product-os/context/product-facts.md` + `product-strategy.md` + `evidence-register.md` + `decision-log.md` — à remplir avant d'utiliser les agents.
>
> Discovery en boucle (pas de chaîne stricte), artefacts discovery sélectionnés selon l'incertitude à réduire, commitment gate explicite entre discovery et delivery (avec synthèse de confiance Low/Medium/High), metrics posées avant le PRD, `/pm-solution-exploration` entre metrics et PRD (le PRD consolide la solution, il ne la choisit pas), statuts de preuve nuancés, mémoire éclatée en 4 fichiers, Launch Readiness en checklist dédiée, `/pm-sprint-plan` en branche annexe non numérotée, gate solution-encore-valide entre prototype et tickets, post-ship fermant la boucle sur les 4 fichiers mémoire, header standardisé (Décision/Entrées/Sortie/Bloque si/Met à jour) sur chaque skill. Historique des décisions de design : `CHANGELOG.md`.

---

## Ce fichier est la source de vérité

Source canonique opératoire du Product OS pour six choses : le **pipeline détaillé** (§ Pipeline complet et les tableaux par phase), les **statuts de preuve** (§ Statuts de preuve), les **transitions de vocabulaire** entre signal / opportunité / initiative / solution / scope / ticket / release (§ Glossaire), les **familles de décisions** KILL/INVESTIGATE/COMMIT et STOP/ITERATE/SCALE/ROLLBACK (§ Glossaire), la **gouvernance des évolutions** (§ Gouvernance des évolutions) et le **format technique des skills** (§ Header standardisé). Si une information doit être mise à jour, elle se met à jour ici en premier. Le `README.md` est la vue exécutive (proposition de valeur, carte de lecture, portes d'entrée) ; `CHANGELOG.md` garde l'historique des décisions de design déjà prises (append-only, jamais réécrit).

---

## Header standardisé des skills

Chaque fichier `.claude/skills/pm-*.md` ouvre sur 5 champs, avant toute description :

```
**Décision** : la décision produit unique que cette skill tranche ou prépare
**Entrées** : fichiers/contexte nécessaires
**Sortie** : chemin du fichier produit
**Bloque si** : conditions qui empêchent l'exécution ou la progression de statut
**Met à jour** : fichiers mémoire que cette skill écrit ou propose de modifier
```

Test de garde-fou : si une skill ne peut pas se résumer en une phrase "Cette skill décide...", son découpage ou son périmètre doit être challengé avant d'être ajoutée ou modifiée.

### `Ne pas utiliser quand` vs `Bloque si`

Deux sections apparaissent dans plusieurs skills, à ne pas confondre :

- **`Ne pas utiliser quand`** — la skill n'est pas la bonne capacité pour ce besoin. Le problème est un mauvais choix de skill ; la solution est d'en appeler une autre (nommée dans la section).
- **`Bloque si`** (champ du header standardisé) — la skill est la bonne capacité, mais les conditions minimales d'exécution ne sont pas réunies. Le problème est un manque de préparation ; la solution est de satisfaire la condition puis de rappeler la même skill.

---

## Glossaire

Ce glossaire explique les termes utilisés dans les skills et leurs statuts — il ne les traduit pas et ne les uniformise pas artificiellement. Plusieurs désignent des décisions ou des niveaux d'abstraction réellement différents ; les rapprocher sert à les situer les uns par rapport aux autres, pas à les fusionner.

### Trios de décision

| Trio | Où | Sens de chaque valeur |
|---|---|---|
| **KILL / INVESTIGATE / COMMIT** | `/pm-commitment-gate` | `KILL` = archiver, raison tracée dans `decision-log.md`. `INVESTIGATE` = retour **ciblé** à la boucle discovery, avec le "cheapest next learning step" nommé — pas un redémarrage complet. `COMMIT` = entrée dans le séquencement strict de delivery. |
| **STOP / ITERATE / SCALE / ROLLBACK** | `/pm-data-analysis` | `STOP` = la feature reste en l'état, on arrête d'investir dessus sans la retirer. `ITERATE` = résultats mixtes, prochaine hypothèse à formuler. `SCALE` = déployer à 100 % / à plus de segments. `ROLLBACK` = retrait recommandé, résultats négatifs sur métriques primaires ou guardrails. |

Ces deux trios ne sont pas interchangeables : le premier statue sur l'engagement avant toute construction, le second sur la suite à donner une fois des données réelles disponibles.

### Statuts de preuve

Cf. § Statuts de preuve ci-dessous — distincts du niveau de confiance (`documented` / `research` / `verbal` / `intuition`, cf. `CLAUDE.md` § Provenance des claims).

### DHM (Gibson Biddle)

Utilisé dans `/pm-commitment-gate` § Strategic fit, pour ne pas committer sur la seule force de l'evidence :

- **Delight** — l'avantage différenciant que ça renforce pour l'utilisateur
- **Hard-to-copy** — la capacité difficile à répliquer que ça construit
- **Margin-enhancing** — l'impact économique attendu (revenu, coût, marge)

### Frameworks de priorisation (`/pm-prioritize`)

| Framework | Principe | Quand |
|---|---|---|
| **ICE** | Impact × Confidence × Ease (multiplicatif, pas une moyenne) | Défaut, sans donnée d'usage fiable |
| **RICE** | Reach × Impact × Confidence / Effort | Reach fiable et période comparable |
| **Value-Effort** | Grille 2×2, pas de score numérique | Premier tri grossier sur un gros lot de candidats |
| **Scorecard** | Critères pondérés custom | Décision qui dépend de contraintes stratégiques spécifiques |

Arbre de décision complet entre les 4 : `pm-prioritize.md` § Choix du framework. Kano et WSJF sont explicitement exclus (hors scope solo, pas de board à convaincre). **MoSCoW n'est pas un framework de priorisation ici** — c'est le vocabulaire de `/pm-scope` (Must/Should/Nice-to-have/Won't) pour le scope d'une feature déjà choisie, pas le tri entre candidats.

### Transitions de vocabulaire le long du pipeline

Le même référent change de nom selon l'étape — ce n'est pas une incohérence à corriger, mais un changement d'altitude qui reflète l'avancement réel de la décision :

| Terme | Où il apparaît | Ce qu'il désigne |
|---|---|---|
| **Signal** | Entrée de `/pm-market-analysis` | Le déclencheur brut (retour client, move concurrent) — pas encore qualifié |
| **Opportunité** | Sortie de `/pm-market-analysis`, `/pm-prioritize` | Un signal qualifié, formulé en problème/outcome, candidat à la boucle discovery |
| **Initiative** | À partir de `/pm-commitment-gate` | Une opportunité qui a passé le commitment gate — même objet, après engagement |
| **Approche / Solution** | `/pm-solution-exploration`, `/pm-prd` | Une façon précise de répondre à l'initiative, comparée à d'autres avant d'être retenue |
| **Scope** | `/pm-scope` | Le découpage de l'approche retenue en unités de valeur livrables (user stories) |
| **Ticket** | `/pm-tickets` | Une unité de travail assignable à la Tech, dérivée du scope |
| **Release** | `/pm-release` | L'événement de mise en production, avec sa communication |
| **`[feature]`** (token de chemin) | `outputs/specs/[feature]/...` | Historique — cf. § Le token `[feature]` : désigne le slug de l'initiative, pas une feature déjà décidée |

---

## Gouvernance des évolutions

**Product OS est en baseline v1** — pas figée, mais toute proposition de modification future doit suivre une séquence stricte, jamais l'inverse :

1. **Observation** — ce qui a été vu en usage réel
2. **Problème identifié** — pourquoi c'est un problème, pas juste une préférence esthétique
3. **Hypothèse d'amélioration** — ce qui pourrait le résoudre
4. **Évolution de l'architecture** — seulement à ce stade

Objectif : éviter de concevoir des solutions à des problèmes qui n'existent pas encore. Product OS évolue comme n'importe quel produit — à partir de retours d'usage réels, pas de raffinements théoriques.

**En pratique** : une évolution proposée qui ne peut pas citer une Observation concrète (quelle skill a été utilisée sur quelle initiative, ce qui a coincé ou ce qui a été rarement utile) n'est pas prête à être discutée en termes d'architecture — elle doit d'abord être reformulée en Observation/Problème.

---

## Discovery — boucle, pas une chaîne

> **Le séquencement strict commence après `/pm-commitment-gate`, pas ici.** Dans la boucle discovery, les activités ci-dessous s'enchaînent librement — retour en arrière, re-priorisation, reformulation du problème sont normaux, pas des anomalies.

| Skill | Commande | Entrée | Sortie | Obligatoire ? |
|---|---|---|---|---|
| Market Analysis | `/pm-market-analysis` | Signal marché / retour client | `outputs/discovery/market-[sujet]-YYYY-MM-DD.md` | Oui — première étape |
| Prioritize | `/pm-prioritize` | Plusieurs opportunités candidates | `outputs/discovery/prioritize-YYYY-MM-DD.md` — choisit l'opportunité qui entre dans la boucle discovery + recommande un artefact discovery initial ; rappelable pendant la boucle | Oui, rappelable |
| Interview Insights | `/pm-interview-insights` | Transcript user interview | `outputs/interviews/insights-YYYY-MM-DD-[participant].md` — inclut la détection d'écart dit/fait à chaque entretien | Oui si des entretiens sont disponibles, répétable |
| UX Personas | `/pm-ux-personas` | Insights structurés | `outputs/discovery/personas-[segment]-YYYY-MM-DD.md` | **Conditionnel** — cf. § Sélection d'artefact |
| Journey Mapping | `/pm-journey-mapping` | Persona + scénario | `outputs/discovery/journey-map-[persona]-[scenario]-YYYY-MM-DD.md` | **Conditionnel** — cf. § Sélection d'artefact |

## Sélection d'artefact discovery

Persona et journey map ne sont pas enchaînés par défaut. Avant de lancer l'un d'eux, identifier **quelle incertitude précise** on cherche à réduire — chaque artefact n'a de valeur que s'il répond à une incertitude qu'aucun autre artefact déjà produit n'a déjà résolue :

| Incertitude à réduire | Artefact | Statut |
|---|---|---|
| "Qui" — segments hétérogènes pas encore caractérisés | Persona (`/pm-ux-personas`) | Construit |
| "Pourquoi" — motivation/objectif sous-jacent, pas le profil | JTBD | À construire |
| Écart entre ce qui est dit et ce qui est fait | Capturé dans `/pm-interview-insights` § Écart dit/fait, à chaque entretien | Construit |
| "Où" dans un parcours multi-étapes la friction apparaît | Journey Map (`/pm-journey-mapping`) | Construit |
| Expérience traversant plusieurs équipes/systèmes (front-stage/back-stage) | Service Blueprint | À construire |
| Workflow professionnel interne multi-outils (contexte B2B/ops) | Workflow Map | À construire |
| Aucune incertitude réelle restante sur qui/pourquoi/où | Aucun artefact | — |

**Pas de skill de sélection dédiée** — arbitrage jugé trop léger pour justifier une skill séparée. La recommandation initiale est faite par `/pm-prioritize` (champ "Artefact discovery recommandé"), révisable pendant la boucle selon ce que les entretiens révèlent.

JTBD, Service Blueprint et Workflow Map n'ont pas encore de skill dédiée. Construction différée, pas dans le périmètre actuel.

**Règle dure** : ne jamais lancer un artefact discovery "parce que c'est l'étape suivante" — toujours nommer l'incertitude qu'il doit réduire avant de le lancer.

---

## Commitment Gate

| Skill | Commande | Entrée | Sortie |
|---|---|---|---|
| Commitment Gate | `/pm-commitment-gate` | Sortie de la boucle discovery (prioritize + artefacts + evidence-register) | `outputs/specs/[feature]/00-commitment-gate.md` — décision **kill / investigate / commit** + synthèse de confiance Low/Medium/High |

**C'est le seul point de passage entre la boucle discovery et le séquencement strict.** Kill = archivé (raison tracée). Investigate = retour à la boucle, avec le "cheapest next learning step" nommé. Commit = entrée dans `/pm-success-metrics`, confiance globale héritée sans recalcul en aval.

## Delivery — séquencement strict à partir d'ici

| Skill | Commande | Entrée | Sortie |
|---|---|---|---|
| Success Metrics | `/pm-success-metrics` | `00-commitment-gate.md` (commit) | `outputs/specs/[feature]/01-success-metrics.md` — outcome complet (comportement, population, baseline, cible, fenêtre, métrique, guardrails) |
| Solution Exploration | `/pm-solution-exploration` | `01-success-metrics.md` (outcome fixé) | `outputs/specs/[feature]/02-solution-exploration.md` — divergence (approches candidates) → élimination progressive → convergence (approche recommandée + raison d'écarter les autres) |
| PRD | `/pm-prd` | `02-solution-exploration.md` (approche retenue) | `outputs/specs/[feature]/03-prd.md` — charge l'outcome, l'approche et la confiance globale, ne les redéfinit pas. Statuts : `draft`/`ready-for-review`/`approved`/`rejected`/`superseded` |
| Scope | `/pm-scope` | `03-prd.md` statut `approved` | `outputs/specs/[feature]/04-scope.md` |
| Prototype | `/pm-prototype` | `04-scope.md` validé PM | `outputs/specs/[feature]/05-prototype.md` + écrans construits dans `pencils/[cible]-ds.pen` — vérifie aussi si les hypothèses VAL/USA du PRD tiennent toujours |
| Tickets | `/pm-tickets` | `05-prototype.md` / `04-scope.md` validés | `outputs/specs/[feature]/06-tickets.md` + Linear MCP — bloque si une hypothèse a été signalée `contradicted` par le prototype |

### Solution Exploration — pourquoi entre metrics et PRD

Le PRD ne doit pas **découvrir** la solution, seulement **formaliser** celle déjà retenue. Une "direction de solution" optionnelle et légère dans le PRD, jamais comparée à des alternatives, laisse un vrai trou : aucune skill ne compare sérieusement plusieurs approches pour atteindre l'outcome avant la rédaction du PRD.

**Altitudes différentes pour les 4 risques Cagan** : Value s'évalue au niveau du **problème** (l'utilisateur veut-il que ça change ? — déjà tranché en discovery/commitment gate). Usability, Feasibility et Viability sont des propriétés d'une **solution précise** — elles ne peuvent pas être évaluées sérieusement tant qu'aucune solution concrète n'existe. `/pm-solution-exploration` est le foyer propre de ces 3 hypothèses ; `/pm-prd` les hérite, il ne les génère plus.

**Pas de nombre fixe d'approches à comparer** — la diversité des approches prime sur leur quantité. Structure en 3 mouvements : **divergence** (générer les approches réellement distinctes), **élimination progressive** (écarter une à une avec raison précise, jamais "moins bonne" sans cause nommée), **convergence** (recommander l'approche au meilleur rapport risque/impact, pas la moins risquée dans l'absolu ni la moins chère).

## Branche annexe — Sprint Planning

| Skill | Commande | Entrée | Sortie |
|---|---|---|---|
| Sprint Plan | `/pm-sprint-plan` | `06-tickets.md` validés | `outputs/specs/[feature]/sprint-plan-YYYY-MM-DD.md` — **non numéroté**, hors du séquencement principal |

Optionnel par nature (squad qui s'auto-organise vs PM qui anime les rituels) — sorti de la chaîne numérotée pour ne pas laisser un trou de numérotation dans les usages solo. `/pm-release` reprend directement après `06-tickets.md`, que cette skill ait tourné ou non.

## Post-ship

| Skill | Commande | Entrée | Sortie |
|---|---|---|---|
| Release | `/pm-release` | `06-tickets.md` | `outputs/specs/[feature]/07-release.md` — passe `launch-readiness-checklist.md` (gate avant ship) + release notes/stakeholder map (après ship) |
| Data Analysis | `/pm-data-analysis` | Données post-ship / A/B test, `01-success-metrics.md` | `outputs/specs/[feature]/08-data-analysis.md` — adoption/activation/rétention par segment, feedback qualitatif, impact économique, décision STOP/ITERATE/SCALE/ROLLBACK, MAJ des 4 fichiers mémoire |

---

## Pipeline complet

```
Signal / besoin
  ↓ /pm-market-analysis    → opportunités candidates (+ "que se passe-t-il si on ne fait rien")
  ↓ /pm-prioritize         → Top 1 + hypothèse initiale + artefact discovery recommandé (rappelable)
  │
  │  ┌─── BOUCLE DISCOVERY (pas d'ordre imposé, va-et-vient libre) ───┐
  │  │  /pm-interview-insights (écart dit/fait à chaque entretien)     │
  │  │  ⇄ artefact sélectionné (persona / JTBD / journey-map /        │
  │  │  service blueprint / workflow map / aucun) ⇄ reformulation      │
  │  │  du problème ⇄ /pm-prioritize (re-scoring si besoin)            │
  │  └─────────────────────────────────────────────────────────────┘
  │
  ↓ /pm-commitment-gate    → KILL | INVESTIGATE (retour boucle) | COMMIT
  │                          + confiance globale Low/Medium/High (qualité/diversité/convergence)
  ═══════════════ séquencement strict à partir d'ici ═══════════════
  ↓ /pm-success-metrics       → outcome complet (comportement, population,
  │                              baseline, cible, fenêtre, métrique, guardrails)
  ↓ /pm-solution-exploration  → divergence (approches candidates, pas de nombre imposé)
  │                              → élimination progressive (raison précise par approche écartée)
  │                              → convergence (approche recommandée, risque acceptable)
  │                              → hypothèses USA/FEA/VIA-n typées PAR approche
  ↓ /pm-prd                   → problème consolidé + preuves + hypothèses VAL (discovery)
  │                              + USA/FEA/VIA (solution exploration) restantes
  │                              charge l'outcome + l'approche + la confiance (ne les redéfinit pas)
  │                             (PM valide — bloqué si évidence contradicted)
  ↓ /pm-scope            → user stories + pre-mortem (PM valide)
  ↓ /pm-prototype        → specs visuelles DS + vérif hypothèses VAL/USA post-construction (PM valide)
  ↓ /pm-tickets          → tickets Linear MCP (bloque si hypothèse contradicted depuis le prototype)
  ↓ [branche annexe : /pm-sprint-plan, si squad/Shape Up hybride]
  ↓
  ↓ /pm-release        → launch-readiness-checklist.md (gate avant ship) + release notes (après ship)
  ↓ /pm-data-analysis  → vérifie l'outcome de /pm-success-metrics
  │                       → STOP / ITERATE / SCALE / ROLLBACK
  │                       → MAJ systématique : decision-log.md · product-facts.md
  │                          · evidence-register.md · product-strategy.md
```

**Cycle des hypothèses** — germées dès `/pm-prioritize` (première entrée `evidence-register.md`), testées pendant la boucle discovery (y compris l'écart dit/fait de `/pm-interview-insights`) — c'est la couche **Value**. Criblées au commitment gate (tout `critical-gap`/`contradicted` sur une hypothèse Value bloque `commit`). Une fois committé, `/pm-solution-exploration` type les hypothèses **Usability/Feasibility/Viability** par approche candidate — elles n'existent pas avant qu'une solution concrète soit proposée. `/pm-prd` consolide les deux couches sous forme typée **VAL-n / USA-n / FEA-n / VIA-n** — seulement celles encore ouvertes après le commit et le choix d'approche. Re-vérifiées une dernière fois après construction du prototype avant que `/pm-tickets` ne s'exécute.

**OST (Opportunity-Solution Tree, Torres)** : outil de discovery, pas de rédaction PRD. La couche "solution" de l'OST vit désormais dans `/pm-solution-exploration`, pas dans `/pm-prd` qui charge son résultat s'il existe ailleurs, sinon fait une vérification légère.

---

## Statuts de preuve

Remplace le blocage binaire classique "assez de preuves / pas assez". Chaque preuve ou hypothèse dans `evidence-register.md` porte un statut, distinct de son niveau de confiance (`documented/research/verbal/intuition`) :

| Statut | Sens | Effet |
|---|---|---|
| `sufficient` | Preuve solide | Aucun blocage |
| `weak-but-testable` | Incertitude acceptable | Continue avec hypothèse explicite, ne bloque rien |
| `critical-gap` | Risque critique non testé | Bloque le **commitment** (Value, `/pm-commitment-gate`) ou bloque la **convergence** vers une approche (Feasibility/Viability, `/pm-solution-exploration` — retour au commitment gate si aucune approche ne passe) |
| `contradicted` | Preuve infirmée après coup | Bloque `/pm-prd` → `ready-for-review` ; ou, si détecté après construction du prototype, bloque `/pm-tickets` |

Au-dessus du statut par entrée, `/pm-commitment-gate` produit une **synthèse de confiance globale** (Low/Medium/High, jamais un pourcentage) basée sur la qualité, la diversité et la convergence des preuves liées à l'initiative — héritée telle quelle par `/pm-prd`, jamais recalculée en aval.

Détail des règles par skill : § Règles dures de chaque fichier `.claude/skills/pm-*.md`.

---

## Multi-cibles (entreprises, produits, side projects)

**Pattern séquentiel, pas de système multi-workspace.** Une seule cible active à la fois — `product-facts.md`, `product-strategy.md`, `evidence-register.md`, `decision-log.md` et `design-system.md` sont réinitialisés à chaque changement de cible, l'historique de la cible précédente reste accessible via `git log` (pas de duplication de fichiers actifs).

- `product-facts.md` répond à *"comment fonctionne ce produit ?"* (faits stables)
- `product-strategy.md` répond à *"où va ce produit ?"* (OKRs, NSM, positionnement)
- `evidence-register.md` trace toute preuve/hypothèse sur tout le cycle de vie
- `decision-log.md` trace le raisonnement derrière chaque décision PM (git garde les diffs, pas le pourquoi)

**Snapshot au changement de cible** — `context/_archive/[cible]/` reçoit une copie de `product-facts.md`, `product-strategy.md`, `decision-log.md`, `design-system.md`, **plus un `manifest.md`**. **`standards/` n'est jamais concerné** — `ui-checklist.md` et `launch-readiness-checklist.md` vivent hors de `context/` précisément pour qu'aucune procédure d'archivage par cible ne puisse les inclure par erreur :

```markdown
# Manifest — [cible] — archivé le YYYY-MM-DD

**Artefacts valides** : [liste des fichiers de ce snapshot encore fiables]
**Initiative active au moment de l'archivage** : [nom ou "aucune"]
**Décisions ouvertes** : [décisions non tranchées au moment du switch]
**État de la cible** : [pourquoi elle a été fermée — rejetée / en pause / gagnée / autre]
```

Rationale de ce choix d'architecture (alternative évaluée, critères de réévaluation future) : `CHANGELOG.md`.

---

## Le token `[feature]` dans les chemins de sortie

`[feature]` dans `outputs/specs/[feature]/...` désigne le **slug stable de l'initiative, du problème ou de l'outcome traité** — pas une feature ou une solution déjà décidée. Référencé dans les 9 skills numérotées (`/pm-commitment-gate`, `/pm-success-metrics`, `/pm-solution-exploration`, `/pm-prd`, `/pm-scope`, `/pm-prototype`, `/pm-tickets`, `/pm-release`, `/pm-data-analysis`). `/pm-sprint-plan` utilise le même dossier `[feature]/` mais un fichier non numéroté (branche annexe, cf. § Sprint Planning). Origine du nom et raison de sa conservation : `CHANGELOG.md`.

---

## Structure des fichiers

```
tools/product-os/
  index.md                  ← ce fichier
  context/                  ← uniquement le réinitialisable par cible (voir § Multi-cibles)
    product-facts.md              ← faits stables du produit (cible active, réinitialisé)
    product-strategy.md           ← OKRs, NSM, positionnement (cible active, réinitialisé)
    evidence-register.md          ← preuves/hypothèses, tout le cycle de vie (cible active, réinitialisé)
    decision-log.md               ← raisonnement des décisions PM, append-only (cible active, réinitialisé)
    design-system.md              ← DS de la cible active (Mode A rempli / Mode B vide)
    _archive/
      [cible]/               ← snapshot d'une cible fermée + manifest.md
  standards/                ← générique, jamais réinitialisé, jamais archivé par cible
    ui-checklist.md                ← quality gate /pm-prototype
    launch-readiness-checklist.md  ← quality gate /pm-release
  pencils/
    [cible]-ds.pen           ← DS Pencil (tokens + composants) + écrans, un par cible
  outputs/
    interviews/             ← insights user interviews (cible active)
    discovery/               ← personas, journey maps, market analysis, prioritize
    specs/
      [feature]/
        00-commitment-gate.md
        01-success-metrics.md
        02-solution-exploration.md
        03-prd.md
        04-scope.md
        05-prototype.md
        06-tickets.md
        sprint-plan-YYYY-MM-DD.md   ← non numéroté, branche annexe
        07-release.md
        08-data-analysis.md

.claude/skills/             ← agents (hidden, chargés par Claude Code)
  pm-market-analysis.md
  pm-prioritize.md
  pm-interview-insights.md
  pm-ux-personas.md
  pm-journey-mapping.md
  pm-commitment-gate.md
  pm-success-metrics.md
  pm-solution-exploration.md
  pm-prd.md
  pm-scope.md
  pm-prototype.md
  pm-tickets.md
  pm-sprint-plan.md
  pm-release.md
  pm-data-analysis.md
```
