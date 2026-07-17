# Skill — /pm-prioritize

**Rôle dans le Product OS**

**Phase :** Discovery (boucle) — entre `/pm-market-analysis` et la boucle discovery complète, rappelable pendant la boucle.
**Question produit :** Parmi plusieurs opportunités candidates, laquelle mérite d'entrer en boucle discovery en premier ?
**Décision ou résultat produit :** Le Top 1 (et éventuellement un candidat en parallèle) + hypothèse de problème initiale + artefact discovery recommandé.

**Décision** : quelle opportunité entre dans la boucle discovery en premier (et laquelle attend).
**Entrées** : ≥2 opportunités candidates (sorties `/pm-market-analysis` ou décrites à la volée) ; `product-facts.md` ; `product-strategy.md` ; `evidence-register.md`
**Sortie** : `outputs/discovery/prioritize-YYYY-MM-DD.md`
**Bloque si** : rien — mais refuse de conclure sans recommandation explicite
**Met à jour** : `evidence-register.md` (première entrée `weak-but-testable` pour le Top 1)

**Entre Discovery légère et boucle Discovery.** Scorer plusieurs opportunités candidates (issues de `/pm-market-analysis` ou saisies à la main) pour choisir celle qui entre dans la **boucle discovery** (interviews, artefact sélectionné selon l'incertitude à réduire, reformulation du problème — dans l'ordre qui a du sens, pas une chaîne figée) — **la boucle discovery sert à valider le problème, le segment et les solutions possibles, pas à confirmer une solution déjà choisie.**

> `/pm-prioritize` peut être **rappelé plusieurs fois** pendant la boucle discovery si un entretien ou une reformulation du problème change le classement (nouvelle opportunité candidate, hypothèse initiale invalidée, priorité relative qui bascule). Ce n'est pas une étape à usage unique.

Quatre frameworks au choix, pas plus — Kano (nécessite des surveys utilisateurs, c'est de la discovery pas du tri) et WSJF (pensé scaled agile, sert à convaincre un board) ne collent à aucun cas d'usage réel du Product OS solo, restent exclus. MoSCoW n'est pas ici : `/pm-scope` classe déjà les user stories en Must/Should/Nice-to-have + Won't, ça couvre MoSCoW au bon niveau (scope d'une feature déjà choisie, pas tri entre opportunités candidates). Décision actée le 2026-07-10, étendue le 2026-07-11 (ICE reste le défaut sans donnée, Value-Effort et Scorecard ajoutés comme alternatives à RICE). Source : conversation Romain.

**Utiliser quand** (`/pm-prioritize [liste d'opportunités ou dossier outputs/discovery/]`) :
- Plusieurs signaux/opportunités sont candidats et il faut trancher lequel approfondir en premier.
- Un entretien ou une reformulation en boucle discovery change le classement — rappelable, pas à usage unique.

**Ne pas utiliser quand** :
- Une seule opportunité existe déjà et fait consensus → passer directement en boucle discovery, pas besoin de scorer un candidat seul.
- La question porte sur le scope d'une feature déjà choisie (Must/Should/Won't) → c'est `/pm-scope` qui couvre ce tri-là, pas celui-ci (entre opportunités candidates).

## Place dans le pipeline

```
Plusieurs opportunités (sorties /pm-market-analysis)
  → /pm-prioritize
  → outputs/discovery/prioritize-YYYY-MM-DD.md
  → sélectionne l'opportunité qui entre dans la BOUCLE DISCOVERY
    (pas d'ordre imposé — /pm-interview-insights, artefact sélectionné selon
    l'incertitude à réduire, reformulation du problème, re-priorisation si besoin)
    afin de valider le problème, le segment et les solutions possibles
  → boucle jusqu'à /pm-commitment-gate (kill / investigate / commit)
```

**Le séquencement strict commence après `/pm-commitment-gate`, pas ici.** Tant qu'on est dans la boucle discovery, `/pm-prioritize` peut être relancé, un candidat peut être reformulé, une opportunité secondaire peut remonter — rien de tout ça n'est une anomalie.

## Choix du framework

Arbre de décision — ne pas laisser l'agent interpréter, appliquer dans l'ordre :

1. **Plus de 8-10 candidats** → `value-effort` d'abord, pour un premier tri grossier, puis rescorer les survivants avec un framework plus fin.
2. **Pas de donnée d'usage fiable** → `ice`.
3. **Reach fiable et période comparable** → `rice`.
4. **Décision qui dépend de contraintes stratégiques spécifiques** (alignement, risque légal, dette technique) → `scorecard`.
5. **Doute entre ICE et RICE** → `ice` (le défaut le moins susceptible de faire du data washing).
6. **Doute entre ICE et Scorecard** → `scorecard` seulement si les critères additionnels peuvent changer matériellement le classement, sinon rester sur `ice`.

Description des 4 frameworks :

- `--framework=ice` (défaut) : Impact / Confidence / Ease, 1-10 chacun. Pas besoin de donnée d'usage réelle.
- `--framework=rice` : ajoute Reach (nb clients/sessions concernés). **Aucun MCP analytics (Amplitude/Mixpanel/PostHog) n'est branché aujourd'hui** — le Reach est une saisie manuelle de Romain, pas une donnée auto-tirée. Si Reach est une estimation à vue de nez, rester sur ICE plutôt que d'habiller le pif en calcul.
- `--framework=value-effort` : positionnement sur une grille 2×2 (Valeur haute/basse × Effort haut/bas), pas de score numérique. Le plus rapide, pour trier grossièrement un gros lot de candidats avant de scorer finement les survivants avec ICE/RICE/Scorecard.
- `--framework=scorecard` : critères pondérés custom (pas figés à Impact/Confidence/Ease). Utile quand la décision dépend de critères propres au contexte (ex : alignement stratégique, risque légal, dette technique) que ICE/RICE ne capturent pas. Poids définis par Romain au lancement, somme = 100%.

**Jamais comparer directement deux scores issus de frameworks différents** — un score ICE de 7,4 et un score RICE de 280 ne sont pas sur la même échelle. Un changement de framework entre deux runs de `/pm-prioritize` invalide toute comparaison directe des scores.

## Étapes

### 1. Lister les candidats

- Une ligne par opportunité : nom, source (signal/market-analysis), segment concerné
- **Formuler chaque candidat comme un problème ou un résultat souhaité, jamais comme une solution prédéfinie.** Ex : "réduire l'abandon pendant l'onboarding", pas "ajouter un chatbot d'onboarding". Si un candidat arrive formulé comme une solution, le reformuler en problème avant de scorer — sinon la discovery complète en aval ne fait que confirmer un choix déjà fait.

### 2. Scorer

**ICE** — pour chaque candidat :
- Impact (1-10) : effet business/utilisateur si résolu
- Confidence (1-10) : niveau de certitude sur l'impact réel
- Ease (1-10) : facilité de mise en œuvre (10 = trivial)
- Score = (Impact × Confidence × Ease) / 100 — **multiplicatif, pas moyenne**. Une moyenne laisse un Confidence très faible se faire compenser par Impact et Ease (ex : 10/2/10 → moyenne 7,3, alors qu'une confiance de 2 devrait plomber le score). Le produit pénalise réellement le maillon faible : 10×2×10=200 vs 8×8×7=448, le second candidat remonte à raison.

**RICE** — pour chaque candidat :
- Reach (nombre) : clients/sessions concernés sur la période — **flaguer si estimation non sourcée**
- Impact (0.25 / 0.5 / 1 / 2 / 3) : échelle RICE standard
- Confidence (%) : 50 / 80 / 100
- Effort (personne-mois)
- Score = (Reach × Impact × Confidence) / Effort

**Value vs Effort** — pour chaque candidat :
- Valeur : haute / basse (jugement rapide, pas de chiffre)
- Effort : haut / bas (jugement rapide, pas de chiffre)
- Position dans le quadrant (Quick Win / Grand Projet / Combler le temps / Money Pit) — pas de score numérique, juste un tri visuel

**Scorecard** — pour chaque candidat :
- Définir 3-5 critères pondérés au lancement (somme des poids = 100%), ex : impact business (40%), alignement stratégique (25%), faible risque (20%), faible effort (15%)
- **Tous les critères orientés dans le même sens : 10 = situation la plus favorable.** Nommer les critères en conséquence ("faible risque", "faible effort"), jamais "risque" ou "effort" seuls — sinon un score élevé sur un critère défavorable s'additionne positivement par erreur.
- Noter chaque critère 1-10 par candidat
- Score = Σ (note × poids)

### 2.5 Qualité des preuves (tous frameworks)

Distincte du Confidence d'ICE : Confidence mesure la croyance dans l'impact, Qualité des preuves mesure sur quoi cette croyance repose.

- **Haute** : analytics fiables, recherches utilisateurs convergentes, signal répété
- **Moyenne** : quelques interviews ou données partielles
- **Faible** : intuition, anecdote isolée, estimation interne

Noter la source principale de chaque candidat (interview, market-analysis, data, intuition PM) à côté de ce niveau.

### 3. Trier et flaguer

- Classement par score décroissant (au sein d'un même framework — jamais entre frameworks différents)
- Flag explicite sur tout score construit avec une preuve à qualité faible (Reach deviné, Confidence < 80%, poids Scorecard arbitraires)
- **Si l'écart entre les deux premiers scores est inférieur à 10%** : ne pas déclarer de vainqueur automatique. Identifier l'hypothèse ou la donnée manquante qui permettrait de les départager, puis recommander la validation la moins coûteuse pour la lever. Le score identifie l'incertitude à réduire, il ne remplace pas le jugement.

### 4. Recommandation

- **Top 1** entre dans la boucle discovery par défaut.
- Un second candidat ne rentre en parallèle que si sa discovery est légère, indépendante du premier, et compatible avec la capacité disponible — sinon ça crée du WIP au moment précis où l'outil est censé aider à trancher.
- **Hypothèse de problème initiale** pour le Top 1 : une phrase courte de ce qu'on croit vrai sur ce problème avant même de commencer la discovery — pas encore typée VAL/USA/FEA/VIA (ça viendra dans `/pm-prd` une fois affinée), juste ce qui doit être testé en priorité dans la boucle discovery. L'ajouter comme première entrée `weak-but-testable` dans `evidence-register.md`.
- **Artefact discovery recommandé pour le Top 1** : à ce stade, quelle incertitude domine (qui / pourquoi / contradiction dit-fait / où dans le parcours / aucune) et quel artefact de la grille `tools/product-os/index.md` § Sélection d'artefact discovery semble le plus pertinent pour la réduire — reste une recommandation initiale, révisable pendant la boucle si les entretiens pointent ailleurs. Rend la sélection traçable plutôt qu'un jugement implicite à chaque fois.
- Ce qui reste : à monitorer / à reconsidérer au prochain cycle

### 5. Écrire l'analyse

`tools/product-os/outputs/discovery/prioritize-YYYY-MM-DD.md`

## Format de sortie

```markdown
# Prioritization — [Date]

**Framework** : ICE | RICE | Value-Effort | Scorecard
**Candidats évalués** : [N]

## Scores

| Opportunité (formulée en problème) | Source principale | Qualité des preuves | Critères (selon framework) | Score / Position |
|---|---|---|---|---|
| [Nom] | [interview/data/market-analysis/intuition] | haute / moyenne / faible | [détail selon framework choisi] | [score ou quadrant] |

## Recommandation

- **Prioritaire (Top 1)** : [Nom] — entre dans la boucle discovery pour valider problème/segment/solutions
- **Hypothèse de problème initiale** : [phrase courte à tester en discovery]
- **Artefact discovery recommandé** : [persona / JTBD / journey map / service blueprint / workflow map / aucun] — incertitude à réduire : [qui / pourquoi / dit-fait / où / aucune]
- **Parallèle possible si capacité** : [Nom] — seulement si discovery légère et indépendante du Top 1
- **Écart <10% avec le suivant ?** [oui/non — si oui, hypothèse manquante à lever avant de trancher : ...]
- **À monitorer** : [Nom(s)]
- **Reconsidérer prochain cycle** : [Nom(s)]
```

## Règles dures

- **Pas de Kano ni WSJF dans cette skill** — hors scope du Product OS solo, cf. décision 2026-07-10.
- **Pas de MoSCoW ici** — c'est `/pm-scope` qui le couvre (Must/Should/Nice-to-have/Won't), niveau scope d'une feature choisie, pas tri entre candidats.
- **Candidats formulés en problème/outcome, jamais en solution** — reformuler avant de scorer si besoin.
- **ICE est multiplicatif, pas une moyenne** — un Confidence faible doit plomber le score, pas être dilué.
- **RICE sans donnée Reach réelle = flag obligatoire**, ne jamais présenter un score RICE comme objectif s'il repose sur une estimation à vue de nez.
- **Scorecard : critères tous orientés 10=favorable, poids fixés avant de voir les scores** — ne jamais ajuster les poids après coup pour faire remonter un candidat favori, ne jamais noter un critère dans le mauvais sens.
- **Jamais comparer des scores entre frameworks différents** — un ICE et un RICE ne sont pas sur la même échelle.
- **Écart <10% entre les deux premiers = pas de vainqueur automatique** — nommer l'incertitude à lever plutôt que trancher artificiellement.
- **Top 1 dans la boucle discovery par défaut** — un second candidat en parallèle seulement si léger, indépendant et compatible capacité. Ne pas créer du WIP au moment de trancher.
- **`/pm-prioritize` n'est pas à usage unique** — rappelable pendant la boucle discovery si une reformulation ou un entretien change le classement.
- **Toujours conclure par une recommandation explicite** (comme `/pm-market-analysis`) — pas de tableau de scores sans tranche.
