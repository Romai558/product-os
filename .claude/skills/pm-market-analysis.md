# Skill — /pm-market-analysis

**Rôle dans le Product OS**

**Phase :** Discovery (boucle) — première étape recommandée.
**Question produit :** Ce signal (retour client, feature request, move concurrent) constitue-t-il une vraie opportunité marché à creuser ?
**Décision ou résultat produit :** Recommandation go / no-go / à monitorer sur l'opportunité.

**Décision** : go / no-go / à monitorer sur une opportunité candidate issue d'un signal marché.
**Entrées** : signal de départ (retour client, feature request, move concurrent) ; `product-facts.md` ; `product-strategy.md`
**Sortie** : `outputs/discovery/market-[sujet]-YYYY-MM-DD.md`
**Bloque si** : rien — jamais bloquant, mais doit toujours conclure par une recommandation explicite
**Met à jour** : rien directement (alimente `/pm-prioritize` et `/pm-prd`)

**Couche Discovery — étape 1.** Analyse une opportunité marché depuis un signal produit : concurrents, segments, sizing, positionnement. Alimente la business opportunity dans `/pm-prd`.

Calibré pour le quotidien PM (30-60 min), pas pour un rapport investisseur. Pour un deep-dive marché complet sur une nouvelle opportunité greenfield → utiliser BMAD market research.

Sources : inspiré de phuryn/pm-skills (competitor-analysis + market-segments + market-sizing) + structure BMAD légère.

**Utiliser quand** (`/pm-market-analysis [signal ou sujet]`) :
- Un signal remonte (retour CS/Sales, insight discovery, move concurrent) et on veut savoir si c'est une vraie opportunité marché.

**Ne pas utiliser quand** :
- Plusieurs opportunités candidates existent déjà et il faut choisir laquelle approfondir en premier → c'est `/pm-prioritize`.
- On veut un deep-dive marché exhaustif type investisseur (TAM/SAM/SOM complet) → hors périmètre, cette skill reste calibrée 30-60 min (utiliser BMAD market research à la place).

## Place dans le pipeline

```
Signal marché / retour client
  → /pm-market-analysis
  → outputs/discovery/market-[sujet]-YYYY-MM-DD.md
  → alimente /pm-prd (business opportunity + positionnement)
```

## Étapes

### 1. Cadrer le signal

- Quel est le déclencheur exact (verbatim client, move concurrent, tendance marché) ?
- Est-ce un signal isolé ou un pattern qui revient ?
- À quel segment de clients ça touche ?

### 2. Analyse concurrentielle (light)

Top 3-5 concurrents directs sur ce sujet spécifique :
- Comment ils l'adressent (ou ne l'adressent pas)
- Leurs forces et faiblesses sur ce point précis
- Gaps identifiés

Pas une analyse concurrentielle complète — rester focalisé sur le sujet du signal.

### 3. Segments concernés

- Quels segments clients sont touchés par ce signal ?
- Lequel est le plus impacté / le plus stratégique ?
- Quel JTBD (job-to-be-done) est derrière ce signal ?

### 4. Sizing de l'opportunité (light)

- Combien de clients actuels sont concernés ?
- Quel impact business si on résout ça (rétention, conversion, expansion) ?
- Estimation rough : opportunité mineure / significative / structurante

Ne pas faire de TAM/SAM/SOM complet sauf si nécessaire pour une décision d'investissement.

### 5. Positionnement

- Comment ce sujet renforce (ou affaiblit) notre positionnement actuel ?
- Y a-t-il un angle de différenciation à saisir vs les concurrents ?

### 6. Synthèse — business opportunity

Format compatible avec `/pm-prd` :
- Pourquoi on s'attaque à ce sujet
- Ce qui se passe si on ne fait rien (scénario explicite, pas "statu quo neutre" par défaut)
- Pour qui
- Quelle proposition de valeur
- Quel impact business attendu
- Recommandation : go / no-go / à monitorer

### 7. Écrire l'analyse

`tools/product-os/outputs/discovery/market-[sujet]-YYYY-MM-DD.md`

## Format de sortie

```markdown
# Market Analysis — [Sujet] — [Date]

**Signal déclencheur** : [verbatim ou observation]
**Segment principal** : [persona concerné]

## Concurrents — comment ils adressent ce sujet

| Concurrent | Approche | Force | Gap |
|---|---|---|---|
| [Nom] | [Ce qu'ils font] | [Point fort] | [Ce qui manque] |

## Segments concernés

- **[Segment 1]** : [JTBD] — criticité : bloquant / important / secondaire
- **[Segment 2]** : ...

## Sizing rough

- Clients actuels concernés : [X% ou nombre]
- Impact business estimé : [rétention / conversion / expansion]
- Taille opportunité : mineure / significative / structurante

## Positionnement

- Lien avec notre positionnement actuel : renforce / neutre / tension
- Angle de différenciation possible : ...

## Business Opportunity — synthèse pour /pm-prd

- **Pourquoi ce sujet maintenant** : ...
- **Ce qui se passe si on ne fait rien** : ...
- **Pour qui** : [segment prioritaire]
- **Proposition de valeur** : ...
- **Impact business attendu** : ...
- **Recommandation** : go / no-go / monitorer
```

## Règles dures

- **Rester focalisé sur le signal** — pas d'analyse marché générale si la question est précise.
- **Go/no-go explicite** en conclusion — pas de synthèse qui ne conclut pas.
- **"Ce qui se passe si on ne fait rien" toujours mentionné** — pas de "statu quo neutre" par défaut, nommer la conséquence réelle (s'aggrave / stable / se résout seul).
- **Distinguer signal isolé et pattern** — un seul retour client ≠ opportunité marché.
- **Sizing rough suffit** — pas de TAM/SAM/SOM sauf besoin spécifique investisseur.
