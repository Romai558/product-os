# Skill — /pm-commitment-gate

**Décision** : kill / investigate / commit.
**Entrées** : sortie `/pm-prioritize` (candidat + hypothèse initiale) ; artefacts de la boucle discovery ; `evidence-register.md` ; `product-strategy.md` ; `product-facts.md`
**Sortie** : `outputs/specs/[feature]/00-commitment-gate.md`
**Bloque si** : une entrée `evidence-register.md` liée à une hypothèse Value est `critical-gap` ou `contradicted` → `commit` interdit, seule sortie possible `investigate` (ou `kill`)
**Met à jour** : `decision-log.md` (toujours, y compris pour `kill`)

**Le gate entre la boucle discovery et le séquencement strict de delivery.** Transforme la sortie libre et bouclée de la discovery (opportunité, recherche, interviews, reformulations, artefacts sélectionnés) en une décision explicite : **kill**, **investigate**, ou **commit**. Rien n'entre dans `/pm-success-metrics` → `/pm-prd` → `/pm-scope` sans être passé par ce gate.

> C'est ici, pas plus tard, que se fait le tri entre "on a assez appris pour s'engager" et "on doit encore apprendre". Une fois `commit` posé, le séquencement strict démarre — ne plus revenir en arrière sans repasser explicitement par ce gate.

## Déclencheur

- `/pm-commitment-gate [initiative]`
- À la fin d'un tour de boucle discovery, quand la question "on arrête, on creuse encore, ou on s'engage ?" se pose concrètement

## Pré-requis

- Sortie de `/pm-prioritize` (candidat + hypothèse initiale)
- Artefacts produits pendant la boucle discovery (`insights-*.md` — inclut les écarts dit/fait détectés — et selon sélection : `personas-*.md`, `journey-map-*.md`)
- `tools/product-os/context/evidence-register.md` — toutes les entrées liées à l'initiative
- `tools/product-os/context/product-strategy.md` — pour le check de fit stratégique
- `tools/product-os/context/product-facts.md`

## Place dans le pipeline

```
Boucle discovery (interviews, artefacts sélectionnés, reformulations, re-priorisation)
  → /pm-commitment-gate
  → outputs/specs/[feature]/00-commitment-gate.md
  → entrée decision-log.md (kill / investigate / commit)
  ┌─ KILL        → archiver, pas de suite (raison tracée dans decision-log.md)
  ├─ INVESTIGATE → retour à la boucle discovery, next learning step le moins coûteux
  └─ COMMIT      → /pm-success-metrics (séquencement strict démarre ici)
```

## Étapes

### 1. Why now?

Pourquoi cette décision se pose maintenant et pas dans 3 mois — quel signal a déclenché le passage au gate (pas une reformulation du "pourquoi le problème existe", déjà fait en discovery, mais "pourquoi trancher maintenant").

### 2. Evidence strength

Lire `evidence-register.md` pour toutes les entrées liées à l'initiative.

- Lister les entrées par type (si déjà esquissé) ou non typées, avec leur statut (`sufficient` / `weak-but-testable` / `critical-gap` / `contradicted`)
- **Toute entrée `critical-gap` ou `contradicted` liée à une hypothèse de type Value → bloque `commit`.** Le gate ne peut rendre que `investigate` dans ce cas.
- Les `critical-gap`/`contradicted` sur Usability/Feasibility/Viability ne bloquent pas automatiquement le commit — les nommer explicitement dans la recommandation, le PM tranche au cas par cas (une Feasibility non testée peut être acceptable si le risque est cantonné à `/pm-scope`).

**Synthèse de confiance globale — Low / Medium / High.** Pas un score numérique ni un pourcentage (une preuve n'est pas un calcul de précision). Un jugement roulé-up sur trois axes :

- **Qualité** : les entrées sont-elles majoritairement `sufficient`, ou surtout `weak-but-testable` ?
- **Diversité** : les preuves viennent-elles de sources indépendantes (interviews + data + signal marché), ou d'une seule source répétée ?
- **Convergence** : les sources s'accordent-elles, ou y a-t-il un écart dit/fait ou une contradiction non résolue entre elles (cf. `/pm-interview-insights` § Écart dit/fait) ?

**High** = qualité forte + sources diversifiées + convergence claire. **Low** = une seule source, ou des signaux qui se contredisent, ou tout en `weak-but-testable`. **Medium** = entre les deux, à justifier explicitement plutôt que choisi par défaut. Ce verdict est hérité tel quel par `/pm-prd` — jamais recalculé en aval.

### 3. Strategic fit (DHM — Biddle)

Répondre aux 5 sous-questions, aucune ne se substitue aux autres :

- **Objectif produit servi** : quel OKR ou priorité de `product-strategy.md` cette initiative sert-elle réellement (pas par association vague)
- **Avantage différenciant renforcé** (Delight) : en quoi ça rend le produit meilleur pour l'utilisateur d'une façon qu'un concurrent n'offre pas déjà
- **Capacité difficile à copier créée** (Hard-to-copy) : qu'est-ce que ça construit qui ne se réplique pas en 2 semaines par un concurrent
- **Impact économique attendu** (Margin-enhancing) : effet revenu/coût/marge, même en ordre de grandeur
- **Raison de construire plutôt que configurer ou acheter** : a-t-on vérifié qu'aucune solution existante (config produit, outil tiers, service) ne couvre déjà ce besoin

Si une majorité de ces 5 réponses est "aucun/faible/non vérifié" → signal fort vers `investigate` ou `kill`, pas `commit` par défaut.

### 4. Cost of delay

Qu'est-ce que ça coûte concrètement d'attendre encore un cycle de discovery avant de trancher (perte utilisateur continue, fenêtre concurrentielle, coût d'opportunité) — pour éviter de traiter "investigate" comme une option toujours gratuite.

### 5. What happens if we do nothing?

Scénario explicite si on ne fait rien du tout sur ce problème — pas "no-op = statu quo neutre" par défaut : nommer la conséquence réelle (le problème s'aggrave / reste stable / se résout tout seul).

### 6. Cheapest next learning step

**Seulement si la décision penche vers `investigate`** : quelle est l'action la moins coûteuse qui lèverait l'incertitude bloquante identifiée à l'étape 2 (pas "faire toute la discovery à nouveau" — cibler précisément l'entrée `critical-gap`/`contradicted` en cause).

### 7. Décision

**KILL / INVESTIGATE / COMMIT**, justifiée en 2-3 lignes à partir des étapes 1-6.

### 8. Écrire le fichier et l'entrée decision-log

`tools/product-os/outputs/specs/[feature]/00-commitment-gate.md`

Ajouter une entrée à `tools/product-os/context/decision-log.md` (date, contexte, options, choix, justification, signaux de révision — cf. format du fichier).

## Format de sortie

```markdown
# Commitment Gate — [Nom initiative] — [Date]

**Source discovery** : [prioritize / insights / artefacts utilisés]

## Why now?

[Déclencheur du passage au gate]

## Evidence strength

| ID evidence-register | Type | Statut | Bloque commit ? |
|---|---|---|---|
| EV-n | Value/Usability/Feasibility/Viability/non typé | sufficient/weak-but-testable/critical-gap/contradicted | oui si Value + critical-gap/contradicted |

**Confiance globale** : Low / Medium / High
**Justification** : [qualité des entrées / diversité des sources / convergence ou non — pas de %]

## Strategic fit (DHM)

- **Objectif produit servi** : ...
- **Avantage différenciant renforcé** : ...
- **Capacité difficile à copier créée** : ...
- **Impact économique attendu** : ...
- **Construire vs configurer/acheter** : ...

## Cost of delay

[Ce que coûte un cycle d'investigate de plus]

## What happens if we do nothing?

[Scénario explicite, pas un "neutre" par défaut]

## Cheapest next learning step

[Seulement si investigate — action ciblée, pas "refaire la discovery"]

## Décision

**KILL / INVESTIGATE / COMMIT**

Justification : [2-3 lignes]
```

## Règles dures

- **Aucune initiative n'entre en séquencement strict sans être passée par ce gate.**
- **Une entrée `critical-gap` ou `contradicted` sur une hypothèse Value bloque `commit`** — la seule sortie possible est `investigate` (ou `kill` si le PM juge que ça ne vaut plus la peine).
- **`investigate` doit toujours nommer le `cheapest next learning step`** — jamais "à recreuser" sans action concrète.
- **`kill` doit être tracé dans `decision-log.md`** avec la justification, pas juste abandonné en silence — un signal de révision permet de rouvrir plus tard sans repartir de zéro.
- **Le strategic fit n'est pas un tampon automatique** — si la majorité des 5 sous-questions est faible/non vérifiée, ne pas recommander `commit` seulement parce que l'evidence strength est bonne.
- **`what happens if we do nothing` n'est jamais laissé vide** — nommer le scénario, même s'il est "rien de grave à court terme".
- **Confiance globale = Low/Medium/High justifié, jamais un pourcentage** — la justification doit citer qualité/diversité/convergence, pas un chiffre qui simule une précision qu'on n'a pas.
