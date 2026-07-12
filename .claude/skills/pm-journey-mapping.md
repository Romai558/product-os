# Skill — /pm-journey-mapping

**Décision** : quel point de friction précis du parcours utilisateur est le point d'entrée prioritaire pour l'intervention produit.
**Entrées** : `outputs/interviews/insights-*.md` et/ou `outputs/discovery/personas-*.md` ; `product-facts.md`
**Sortie** : `outputs/discovery/journey-map-[persona]-[scenario]-YYYY-MM-DD.md`
**Bloque si** : rien — se déclenche seulement si la sélection d'artefact discovery le recommande
**Met à jour** : rien directement (alimente `/pm-commitment-gate` puis `/pm-prd`)

**Artefact discovery conditionnel — pas une étape obligatoire.** Déclenché seulement si la logique de sélection d'artefact (`tools/product-os/index.md` § Sélection d'artefact discovery) identifie que l'incertitude à réduire porte sur un parcours multi-étapes (où, dans un flow, la friction apparaît) — pas sur "qui" (persona) ni sur un écart dit/fait isolé (couvert dans `/pm-interview-insights`). Documente comment un utilisateur traverse une expérience pour atteindre un objectif : phases, actions, émotions, points de friction et opportunités.

> "L'objectif c'est l'alignement, pas la perfection. La conversation pendant le mapping vaut souvent autant que l'artefact."
> Si l'expérience traverse plusieurs équipes/systèmes (front-stage/back-stage), préférer service blueprint (à construire). Si c'est un workflow professionnel multi-outils, préférer workflow map (à construire).

## Déclencheur

- `/pm-journey-mapping [persona] [scénario]`
- Dans la boucle discovery, après `/pm-interview-insights` ou `/pm-ux-personas` — **seulement si cet artefact a été sélectionné**

## Pré-requis

- `outputs/interviews/insights-*.md`
- `outputs/discovery/personas-*.md` si disponible
- `tools/product-os/context/product-facts.md` — features existantes à positionner sur le journey

## Place dans le pipeline

```
/pm-interview-insights (et /pm-ux-personas si fait), dans la boucle discovery
  → [sélection d'artefact recommande "journey map"]
  → /pm-journey-mapping
  → outputs/discovery/journey-map-[persona]-[scenario]-YYYY-MM-DD.md
  → retour à la boucle discovery (re-priorisation si besoin) → /pm-commitment-gate
  → si commit : alimente /pm-success-metrics puis /pm-prd (problème situé sur le journey)
```

## Étapes

### 1. Définir le cadre

- **Actor** : persona précise (issue de `pm-ux-personas`)
- **Scénario** : situation concrète et objectif de l'utilisateur (ex: "Chef de chantier qui saisit les heures de son équipe en fin de journée")
- **Périmètre** : début et fin du journey (ne pas mapper tout le produit)

### 2. Identifier les phases

4 à 6 phases max qui organisent l'expérience. Nommer du point de vue utilisateur, pas du produit (ex: "Je vérifie les heures", pas "Module pointage").

### 3. Pour chaque phase

- **Actions** : ce que l'utilisateur fait concrètement
- **Pensées** : ce qu'il se dit (verbatims si dispo)
- **Émotions** : courbe émotionnelle (frustration / neutre / satisfaction)
- **Points de friction** : ce qui bloque, ralentit, génère de l'erreur
- **Points de délice** : ce qui fonctionne bien (à ne pas casser)

### 4. Identifier les opportunités

Pour chaque friction : quelle opportunité produit ça ouvre ? Formuler en "Comment pourrait-on..." (HMW — How Might We).

### 5. Distinguer du story mapping

Le journey map = perspective utilisateur (expérience). Le story map = perspective produit (features). Ne pas confondre. Si on veut passer au story mapping → lancer `/pm-story-mapping` (à construire). <!-- lint-ok: référence prospective, /pm-story-mapping n'existe pas encore, construction différée (cf. tools/product-os/index.md) -->

### 6. Écrire le journey

`tools/product-os/outputs/discovery/journey-map-[persona]-[scenario]-YYYY-MM-DD.md`

### 7. Extraire pour la suite

Identifier le moment de friction le plus critique → c'est le point d'entrée recommandé pour `/pm-commitment-gate`, puis (si commit) pour `/pm-prd`.

## Format de sortie

```markdown
# Journey Map — [Persona] — [Scénario] — [Date]

**Actor** : [persona]
**Scénario** : [situation + objectif]
**Périmètre** : de [début] à [fin]
**Sources** : [fichiers utilisés]

---

## Phase 1 — [Nom]

| | Contenu |
|---|---|
| **Actions** | ... |
| **Pensées** | > "[verbatim si dispo]" |
| **Émotion** | 😤 frustration / 😐 neutre / 😊 satisfaction |
| **Frictions** | ... |
| **Délices** | ... |
| **Opportunité** | Comment pourrait-on... |

## Phase 2 — [Nom]
...

---

## Courbe émotionnelle

[Phase 1] 😐 → [Phase 2] 😤 → [Phase 3] 😤 → [Phase 4] 😊

## Top 3 frictions (par criticité)

1. **[Friction]** — phase [X] — opportunité : ...
2. ...

## Point d'entrée recommandé pour le commitment gate

[La friction la plus critique à adresser en priorité, avec justification]
```

## Règles dures

- **Non obligatoire** — ne se lance que si la sélection d'artefact discovery le recommande.
- **4-6 phases max** — au-delà, c'est du bruit ou un scope trop large.
- **Nommer les phases du point de vue utilisateur**, pas du produit.
- **Chaque opportunité est liée à une friction précise** — pas d'opportunité flottante.
- **Ne pas mapper tout le produit** — un journey = un scénario précis.
- **Le journey map ≠ story map** — ne pas glisser vers les features pendant l'exercice.
